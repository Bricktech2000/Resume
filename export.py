def export(extension, process):
  print(f'exporting `{extension}` file...')
  with open(f'resume.md', 'r') as f:
    md = f.read()
    with open(f'export/resume.{extension}', 'wb') as f:
      f.write(process(md))


def md_process(md):
  return md.encode('utf-8')


def txt_process(md):
  from marko.renderer import Renderer
  from marko.parser import Parser
  from marko import Markdown
  from textwrap import fill

  width = 100
  small_width = 94
  newline = '\n'

  class TextRenderer(Renderer):
    def render_code_block(self, element):
      raise NotImplementedError

    def render_heading(self, element):
      if element.level == 1:
        from selenium import webdriver
        from selenium.webdriver.common.by import By
        import time
        options = webdriver.ChromeOptions()
        options.add_argument('--headless')
        driver = webdriver.Chrome(options=options)
        driver.get(
            f'https://patorjk.com/software/taag/#p=display&f=Stick%20Letters&t={self.render_children(element).upper()}')
        time.sleep(0.25)
        ascii_art = driver.find_element(By.ID, 'taag_output_text').text
        driver.quit()
        return f'{ascii_art}'
      if element.level == 2:
        return f'{self.parse_html("&mdash;&mdash;") + (" " + self.render_children(element).upper() + " ").ljust(width, self.parse_html("&mdash;"))}\n'
      if element.level == 3:
        return f'{fill(self.render_children(element).upper(), small_width)}'
      raise NotImplementedError

    def render_list_item(self, element):
      return f'{self.parse_html("&bull;")} {(newline + "  ").join(fill(self.render_children(element), small_width).split(newline))}\n'

    def render_blank_line(self, element):
      return f'\n'

    def render_quote(self, element):
      return f'| {"| ".join([self.render(child) for child in element.children])}'

    def render_fenced_code(self, element):
      raise NotImplementedError

    def render_thematic_break(self, element):
      return f'\n{" " * (width // 2 - 3) + self.parse_html("&bull;&nbsp;&bull;&nbsp;&bull;")}\n'

    def render_html_block(self, element):
      return f''

    def render_link_ref_def(self, element):
      raise NotImplementedError

    def render_setext_heading(self, element):
      raise NotImplementedError

    def render_paragraph(self, element):
      return f'{fill(self.render_children(element), small_width)}\n'

    def render_line_break(self, element):
      return f'\n'

    def render_literal(self, element):
      return f'{element.children}'

    def render_inline_html(self, element):
      return f''

    def render_code_span(self, element):
      return f'[{fill(self.parse_html(element.children), small_width)}]'

    def render_emphasis(self, element):
      newline = '\n'
      return f'|||{(newline + "|||").join(fill(self.render_children(element), small_width).split(newline))}'

    def render_strong_emphasis(self, element):
      return f'{fill(self.render_children(element).upper(), small_width)}'

    def render_link(self, element):
      return f'{self.render_children(element)} <{element.dest}>'

    def render_image(self, element):
      raise NotImplementedError

    def render_autolink(self, element):
      raise NotImplementedError

    def render_raw_text(self, element):
      return f'{self.parse_html(element.children)}'

    def parse_html(self, element):
      return element.replace("&nbsp;", " ").replace("&bull;", "•").replace("&mdash;", "—")

  markdown = Markdown(parser=Parser, renderer=TextRenderer)
  return '\n'.join(map(
      lambda line: line.replace('|||', ' ' * (width - len(line) + 5)),
      markdown.convert(md).split('\n')
  )).encode('utf-8')


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
  import base64
  import json
  import time
  import os

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
  pdf = base64.b64decode(driver.execute_cdp_cmd("Page.printToPDF", settings2)['data'])
  driver.quit()
  os.remove('temp.html')

  return pdf


export('html', html_process)
export('txt', txt_process)
export('pdf', pdf_process)
export('md', md_process)
print('done.')
