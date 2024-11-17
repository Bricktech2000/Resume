# Resume

_Resume exporter from Markdown to various formats_

## Overview

Resume markup is located in [resume.md](resume.md). The Markdown source code is then exported to [various formats](export/) automatically using [export.py](export.py).

## Requirements

```bash
apt-get install -y chromium-browser chromium-chromedriver figlet
pip install marko selenium
```

## Export

```bash
python3 export.py
```
