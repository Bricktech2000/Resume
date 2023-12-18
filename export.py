import base64
import time
import os
import re

# external requirements:
# - `marko`
# - Google Chrome
# - `git` in `$PATH`
# - `chromedriver` in `$PATH`
# - an internet connection
# - an _export_ folder


heading_cache = {'Emilien Breton': r'''
 ___                 ___          __   __   ___ ___  __       
|__   |\/| | |    | |__  |\ |    |__) |__) |__   |  /  \ |\ | 
|___  |  | | |___ | |___ | \|    |__) |  \ |___  |  \__/ | \| 
                                                              
'''[1:-1]}


def utf8_replace_html_entities(html):
  return html.replace('&nbsp;', ' ').replace('&ensp;', '  ').replace('&bull;', '•').replace('&mdash;', '—').replace('&dollar;', '$').replace('&ndash;', '—')


def ascii_replace_html_entities(html):
  return html.replace('&nbsp;', ' ').replace('&ensp;', '  ').replace('&bull;', '-').replace('&mdash;', '--').replace('&dollar;', '$').replace('&ndash;', '-')


def make_text_renderer(format_strong, format_emphasis, format_code, format_html, len_patched=len, width=96, small_width=90):
  from marko.renderer import Renderer

  def fill(text, target_width, justify=False):
    right_float_delta = (width - small_width) if '|||' in text else 0
    target_width = target_width + right_float_delta  # allow right float to take full `width`

    def fill(text, target_width, len_patched=len):
      words = text.split()
      lines = []
      for word in words:
        if len(lines) == 0:
          lines.append(word)
        elif len_patched(lines[-1] + ' ' + word) > target_width:
          lines.append(word)
        else:
          lines[-1] += ' ' + word
      return '\n'.join(lines)

    def _justify(text):
      lines = text.split('\n')
      return '\n'.join(list(map(lambda line: line.replace(' ', '  ', target_width - len_patched(line)), lines[:-1])) + [lines[-1]])

    return _justify(fill(text, target_width, len_patched)) if justify else fill(text, target_width, len_patched)

  class TextRenderer(Renderer):
    # rule of thumb for newlines:
    # 1. add newlines at the end of render strings so all elements display on their own line with no blank lines
    # 2. add newlines at the start of render strings to add spacing between elements

    def __init__(self, *args, **kwargs):
      super().__init__(*args, **kwargs)

      self.format_strong = format_strong
      self.format_emphasis = format_emphasis
      self.format_code = format_code
      self.format_html = format_html
      self.width = width
      self.small_width = small_width

    def render_document(self, element):
      # "|||" is used to represent `float: right`
      return '\n'.join(map(
          lambda line: line.replace('|||', ' ' * (self.width - len_patched(line) + 5)),
          self.render_children(element).split('\n')
      )).encode('utf-8')

    def render_code_block(self, _):
      raise NotImplementedError

    def render_heading(self, element):
      if element.level == 1:
        def formatless(element):
          # mildly hacky
          from marko.inline import StrongEmphasis, Emphasis
          if isinstance(element, StrongEmphasis) or isinstance(element, Emphasis):
            return ''.join(map(formatless, element.children))
          return self.render(element)

        formatless_children = "".join(formatless(child) for child in element.children)

        if formatless_children not in heading_cache:
          from selenium import webdriver
          from selenium.webdriver.common.by import By

          options = webdriver.ChromeOptions()
          options.add_argument('--headless')
          driver = webdriver.Chrome(options=options)
          driver.get(
              f'http://patorjk.com/software/taag/#p=display&f=Stick%20Letters&t={formatless_children}')
          time.sleep(0.5)
          heading_cache[formatless_children] = driver.find_element(By.ID, 'taag_output_text').text
          driver.quit()

        return f'{heading_cache[formatless_children]}\n'

      if element.level == 2:
        return f'\n{self.format_html("&ndash;&ndash;") + (" " + self.render_children(element).upper() + " ").ljust(self.width, self.format_html("&ndash;"))}\n'

      if element.level == 3:
        def strong_safe(element):
          # mildly hacky
          from marko.inline import Link
          if isinstance(element, Link):
            return f'{self.format_strong(self.render_children(element))} <{element.dest}>'
          return self.format_strong(self.render(element))

        return f'\n{fill("".join(strong_safe(child) for child in element.children), self.small_width)}\n'
      raise NotImplementedError

    def render_list(self, element):
      def render_list_child(element, bullet):
        newline = '\n'
        return f'{bullet}{(newline + " " * len(bullet)).join(fill(self.render_children(element), self.small_width, justify=True).split(newline))}\n'

      return ''.join(render_list_child(child, '  ' if element.ordered else self.format_html('&bull; ')) for child in element.children)

    def render_list_item(self, _):
      raise NotImplementedError

    def render_blank_line(self, _):
      return f''

    def render_quote(self, element):
      return f'| {"| ".join(self.render(child) for child in element.children)}'

    def render_fenced_code(self, _):
      raise NotImplementedError

    def render_thematic_break(self, _):
      return f'\n{" " * (self.width // 2 - 3) + self.format_html("&bull;&nbsp;&bull;&nbsp;&bull;")}\n'

    def render_html_block(self, _):
      return f''

    def render_link_ref_def(self, _):
      raise NotImplementedError

    def render_setext_heading(self, _):
      raise NotImplementedError

    def render_paragraph(self, element):
      return f'{fill(self.render_children(element), self.small_width)}\n'

    def render_line_break(self, _):
      return f'\n'

    def render_literal(self, element):
      return f'{element.children}'

    def render_inline_html(self, _):
      return f''

    def render_code_span(self, element):
      newline = '\n'
      return f'|||{(newline + "|||").join(fill(self.format_code(self.format_html(element.children)), self.small_width).split(newline))}'

    def render_emphasis(self, element):
      return f'{fill(self.format_emphasis(self.render_children(element)), self.small_width)}'

    def render_strong_emphasis(self, element):
      return f'{fill(self.format_strong(self.render_children(element)), self.small_width)}'

    def render_link(self, element):
      return f'{self.render_children(element)} <{element.dest}>'

    def render_image(self, _):
      raise NotImplementedError

    def render_autolink(self, _):
      raise NotImplementedError

    def render_raw_text(self, element):
      return f'{self.format_html(element.children)}'

  return TextRenderer


def make_html_process(text_primary, text_secondary, background):
  def html_process(source):
    from marko.ext.gfm import gfm

    with open('template.html', 'r') as f:
      template = f.read()
      return template.replace('[EXPORT]',
                              '<section>' +
                              gfm(source)
                              .replace('&amp;', '&')
                              .replace('<hr />', '</section><section>')
                              + '</section>') \
          .replace('[TEXT_PRIMARY]', text_primary).replace('[TEXT_SECONDARY]', text_secondary).replace('[BACKGROUND]', background).encode('utf-8')

  return html_process


def make_pdf_process(html_process):
  def pdf_process(source):
    with open('temp.html', 'wb') as f:
      f.write(html_process(source))

    from selenium import webdriver

    options = webdriver.ChromeOptions()
    settings = {
        'landscape': False,
        'displayHeaderFooter': False,
        'printBackground': True,
        'paperWidth': 210 / 25.4,  # why imperial?
        'paperHeight': 297 / 25.4,
        'marginTop': 0,
        'marginBottom': 0,
        'marginLeft': 0,
        'marginRight': 0,
    }
    # for some reason, `--headless` results in different line breaks
    options.add_argument('--headless')
    driver = webdriver.Chrome(options=options)
    driver.get(f'file://{os.path.realpath("temp.html")}')
    time.sleep(0.5)
    pdf = base64.b64decode(driver.execute_cdp_cmd('Page.printToPDF', settings)['data'])
    driver.quit()
    os.remove('temp.html')

    return pdf

  return pdf_process


def md_process(source):
  return utf8_replace_html_entities(re.sub(r'<!--(.|\n)*?-->(\n\n)?', r'', source)).encode('utf-8')


def dark_html_process(source):
  return make_html_process('#FFFFFF', '#AAAAAA', '#000000')(source)


def light_html_process(source):
  return make_html_process('#000000', '#888888', '#FFFFFF')(source)


def ascii_txt_process(source):
  from marko.parser import Parser
  from marko import Markdown

  AsciiTxtRenderer = make_text_renderer(
      lambda strong: str.upper(strong), lambda emphasis: '[' + emphasis + ']', lambda code: code,
      lambda html: ascii_replace_html_entities(html))

  # raise exception if not valid ASCII
  return Markdown(parser=Parser, renderer=AsciiTxtRenderer)(source).decode('utf-8').encode('ascii')


def utf8_txt_process(source):
  from marko.parser import Parser
  from marko import Markdown

  def make_format(map):
    def format(string):
      return ''.join(map[ord(char)] if ord(char) < len(map) else char for char in string)
    return format

  Utf8TxtRenderer = make_text_renderer(
      make_format(
          '                                 !"#$%&\'()*+,-./𝟬𝟭𝟮𝟯𝟰𝟱𝟲𝟳𝟴𝟵:;<=>?@𝗔𝗕𝗖𝗗𝗘𝗙𝗚𝗛𝗜𝗝𝗞𝗟𝗠𝗡𝗢𝗣𝗤𝗥𝗦𝗧𝗨𝗩𝗪𝗫𝗬𝗭[\\]^_`𝗮𝗯𝗰𝗱𝗲𝗳𝗴𝗵𝗶𝗷𝗸𝗹𝗺𝗻𝗼𝗽𝗾𝗿𝘀𝘁𝘂𝘃𝘄𝘅𝘆𝘇{|}~'),
      make_format(
          '                                 !"#$%&\'()*+,-./0123456789:;<=>?@ᴀʙᴄᴅᴇꜰɢʜɪᴊᴋʟᴍɴᴏᴘQʀꜱᴛᴜᴠᴡxʏᴢ[\\]^_`ᴀʙᴄᴅᴇꜰɢʜɪᴊᴋʟᴍɴᴏᴘQʀꜱᴛᴜᴠᴡxʏᴢ{|}~'),
      make_format(
          '                                 !"#$%&\'()*+,-./0123456789:;<=>?@ᴀʙᴄᴅᴇꜰɢʜɪᴊᴋʟᴍɴᴏᴘQʀꜱᴛᴜᴠᴡxʏᴢ[\\]^_`ᴀʙᴄᴅᴇꜰɢʜɪᴊᴋʟᴍɴᴏᴘQʀꜱᴛᴜᴠᴡxʏᴢ{|}~'),
      lambda html: utf8_replace_html_entities(html))

  return Markdown(parser=Parser, renderer=Utf8TxtRenderer)(source)


def term_txt_process(source):
  from marko.parser import Parser
  from marko import Markdown

  TermTxtRenderer = make_text_renderer(
      lambda strong: '\033[1m' + strong + '\033[0m',
      lambda emphasis: '[' + '\033[3m' + emphasis + '\033[0m' + ']',
      lambda code: '\033[3m' + code + '\033[0m',
      lambda html: utf8_replace_html_entities(html),
      lambda string: len(re.sub(r'\033[^m]*m', '', string)))

  return Markdown(parser=Parser, renderer=TermTxtRenderer)(source)


def dark_pdf_process(source):
  return make_pdf_process(dark_html_process)(source)


def light_pdf_process(source):
  return make_pdf_process(light_html_process)(source)


def compose(*fns):
  from functools import reduce
  return reduce(lambda g, f: lambda *args: f(g(*args)), fns)


def preprocess(source):
  import subprocess

  commit_hash = subprocess.check_output(['git', 'rev-parse', 'HEAD']).decode('utf-8').strip()[0:7].upper()
  day, month, year = time.strftime('%d %b %Y').split()
  source = source.replace('[COMMIT_HASH]', commit_hash).replace('[DAY]', day).replace(
      '[MONTH]', month).replace('[YEAR]', year)

  return source


def export(extension, process):
  print(f'exporting `{extension}` file...')
  with open(f'resume.md', 'r') as f:
    source = f.read()
  processed = process(source)  # blocking
  with open(f'export/resume{extension}', 'wb') as f:
    f.write(processed)


export('.md', compose(preprocess, md_process))
export('.dark.html', compose(preprocess, dark_html_process))
export('.light.html', compose(preprocess, light_html_process))
export('.ascii.txt', compose(preprocess, ascii_txt_process))
export('.utf-8.txt', compose(preprocess, utf8_txt_process))
export('.term.txt', compose(preprocess, term_txt_process))
export('.dark.pdf', compose(preprocess, dark_pdf_process))
export('.light.pdf', compose(preprocess, light_pdf_process))
print('done.')
