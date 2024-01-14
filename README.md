# Resume

_Current resume as a software engineer_

## Overview

Resume markup is located in [resume.md](resume.md). The markdown source code is then exported to [various formats](export/) automatically using [export.py](export.py).

## Requirements

```bash
wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb
sudo dpkg -i google-chrome-stable_current_amd64.deb
apt-get install -y chromium-chromedriver figlet
pip install marko selenium
```

## Export

```bash
time python3 export.py
```
