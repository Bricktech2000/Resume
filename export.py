import base64
import time
import os
import re


def make_text_renderer(format_strong, format_emphasis, format_code, format_html, len_patched=len, width=96, small_width=90):
  from marko.renderer import Renderer

  def fill(string, target_width, justify=False):
    from textwrap import fill
    right_float_delta = (width - small_width) if '|||' in string else 0
    patched_len_delta = len(string) - len_patched(string)
    target_width = target_width + right_float_delta + patched_len_delta

    def _justify(text):
      lines = text.split('\n')
      return '\n'.join(list(map(lambda line: line.replace(' ', '  ', target_width - len_patched(line)), lines[:-1])) + [lines[-1]])

    return _justify(fill(string, target_width)) if justify else fill(string, target_width)

  class TextRenderer(Renderer):
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

        from selenium import webdriver
        from selenium.webdriver.common.by import By

        options = webdriver.ChromeOptions()
        options.add_argument('--headless')
        driver = webdriver.Chrome(options=options)
        driver.get(
            f'https://patorjk.com/software/taag/#p=display&f=Stick%20Letters&t={"".join(formatless(child) for child in element.children)}')
        time.sleep(0.25)
        ascii_art = driver.find_element(By.ID, 'taag_output_text').text
        driver.quit()
        return f'{ascii_art}'

      if element.level == 2:
        return f'{self.format_html("&ndash;&ndash;") + (" " + self.render_children(element).upper() + " ").ljust(self.width, self.format_html("&ndash;"))}\n'

      if element.level == 3:
        def strong_safe(element):
          # mildly hacky
          from marko.inline import Link
          if isinstance(element, Link):
            return f'{self.format_strong(self.render_children(element))} <{element.dest}>'
          return self.format_strong(self.render(element))

        return f'{fill("".join(strong_safe(child) for child in element.children), self.small_width)}'
      raise NotImplementedError

    def render_list_item(self, element):
      newline = '\n'
      return f'{self.format_html("&bull;")} {(newline + "  ").join(fill(self.render_children(element), self.small_width, justify=True).split(newline))}\n'

    def render_blank_line(self, _):
      return f'\n'

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
      return f'{fill(self.format_code("[" + self.format_html(element.children) + "]"), self.small_width)}'

    def render_emphasis(self, element):
      newline = '\n'
      return f'|||{(newline + "|||").join(fill(self.format_emphasis(self.render_children(element)), self.small_width).split(newline))}'

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


def md_process(md):
  return md.encode('utf-8')


def utf8_txt_process(md):
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
      lambda element: element.replace('&nbsp;', ' ').replace('&bull;', '•').replace('&mdash;', '—').replace('&dollar;', '$').replace('&ndash;', '—'))

  return Markdown(parser=Parser, renderer=Utf8TxtRenderer)(md)


def ascii_txt_process(md):
  from marko.parser import Parser
  from marko import Markdown

  AsciiTxtRenderer = make_text_renderer(
      str.upper, lambda emphasis: emphasis, lambda code: code,
      lambda element: element.replace('&nbsp;', ' ').replace('&bull;', '-').replace('&mdash;', '--').replace('&dollar;', '$').replace('&ndash;', '-'))

  # raise exception if not valid ASCII
  return Markdown(parser=Parser, renderer=AsciiTxtRenderer)(md).decode('utf-8').encode('ascii')


def term_txt_process(md):
  from marko.parser import Parser
  from marko import Markdown

  TermTxtRenderer = make_text_renderer(
      lambda strong: '\033[1m' + strong + '\033[0m',
      lambda emphasis: '\033[3m' + emphasis + '\033[0m',
      lambda code: '\033[3m' + code + '\033[0m',
      lambda element: element.replace('&nbsp;', ' ').replace('&bull;', '•').replace(
          '&mdash;', '—').replace('&dollar;', '$').replace('&ndash;', '—'),
      lambda string: len(re.sub(r'\033[^m]*m', '', string)))

  return Markdown(parser=Parser, renderer=TermTxtRenderer)(md)


def html_process(md):
  from marko.ext.gfm import gfm
  with open('template.html', 'r') as f:
    template = f.read()
    return template.replace('{{export}}',
                            '<section>' +
                            gfm(md)
                            .replace('&amp;', '&')
                            .replace('<hr />', '</section><section>')
                            + '</section>').encode('utf-8')


def pdf_process(md):
  with open('temp.html', 'wb') as f:
    f.write(html_process(md))

  from selenium import webdriver

  options = webdriver.ChromeOptions()
  settings2 = {
      'landscape': False,
      'displayHeaderFooter': False,
      'paperWidth': 210 / 25.4,  # why imperial?
      'paperHeight': 297 / 25.4,
      'marginTop': 0,
      'marginBottom': 0,
      'marginLeft': 0,
      'marginRight': 0,
  }
  options.add_argument('--headless')
  driver = webdriver.Chrome(options=options)
  driver.get(f'file://{os.path.realpath("temp.html")}')
  time.sleep(0.25)
  pdf = base64.b64decode(driver.execute_cdp_cmd('Page.printToPDF', settings2)['data'])
  driver.quit()
  os.remove('temp.html')

  return pdf


def compose(*fns):
  from functools import reduce
  return reduce(lambda g, f: lambda *args: f(g(*args)), fns)


def preprocess(md):
  import subprocess

  md = md

  commit_hash = subprocess.check_output(['git', 'rev-parse', 'HEAD']).decode('utf-8').strip()[0:15]
  day, month, year = time.strftime('%d %b %Y').split()
  md = md.replace('{{COMMIT_HASH}}', commit_hash).replace('{{DAY}}', day).replace(
      '{{MONTH}}', month).replace('{{YEAR}}', year)

  md = re.sub(r'<\?(.|\n)*?\?>(\n\n)?', r'', md)

  return md


def export(extension, process):
  print(f'exporting `{extension}` file...')
  with open(f'resume.md', 'r') as f:
    md = f.read()
    with open(f'export/resume{extension}', 'wb') as f:
      f.write(process(md))


export('.html', compose(preprocess, html_process))
export('.ascii.txt', compose(preprocess, ascii_txt_process))
export('.utf-8.txt', compose(preprocess, utf8_txt_process))
export('.term.txt', compose(preprocess, term_txt_process))
export('.pdf', compose(preprocess, pdf_process))
export('.md', compose(preprocess, md_process))
print('done.')
