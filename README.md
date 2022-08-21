## Linsh 🔗
[![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg)](https://www.python.org/)
[![License](https://img.shields.io/badge/License-Apache_2.0-blue.svg)](https://opensource.org/licenses/Apache-2.0)
[![PyPI version](https://img.shields.io/pypi/v/Linsh.svg)](https://pypi.org/project/Linsh/)



Fed up of long links 😩  ??? Use ✨ Linsh ✨, a CLI tool to shorten links right from your terminal.
#### Extra Features

* Copies link to clipboard
* Opens link in your browser

#### **Index**
* [Installation]()
* [Usage]()
* [Config file]()
* [Supported API's]()
* [License]()

#### Installation

* Build 

Download the latest build for windows from releases.

* Pypi

Requirement:
[Python](https://www.python.org/)🐍 

Fire up your terminal and run `pip install linsh`
Go to `\venv\Lib\site-packages\Linsh_Darkhound-org` and rename `__main__.py` as `Linsh.py`.
Make sure its properly installed by running `python Linsh.py -a` or `python Linsh.py --help`

* Cloning

Requirement:
[Python](https://www.python.org/)🐍

Clone the repo or download source as zip from releases and unzip in a new folder. Make a new virtual environment in it, activate and install the requirement by running `pip install -r requirements.txt` . 

Run the app `python linsh.py`[or `python __main__.py`] and start shortening your long urls.


#### Usage
Run `linsh.exe --help` from command line
```
Usage: linsh.exe [OPTIONS] COMMAND [ARGS]...

Options:
  -li, --license
  -a, --about
  -ro, --github_repo
  -?, --darkhound_org
  --version            Show the version and exit.
  --help               Show this message and exit.

Commands:
  bitly
  chilp
  cuttly
  tiny-url

```
* Flags

`-li` / `--license` : Displays a brief license information of Linsh.

`-a` / `--about` : Displays a brief information of what Linsh does.

`-ro` / `--github_repo` : Opens the github repository link in your default browser.

`-?` / `--darkhound_org` : Displays a brief information about the developer.

`--version` : Displays the version

`--help` : Displays available commands and flags

[Note: `<command> --help` will display the flags for the respective commands, eg: `linsh.exe bitly --help` ]

* Commands 

`bitly` : Shorten your urls using [bitly]() api

`chilp` : Shorten your urls using [chilp]() api

`cuttly` : Shorten your urls using [cuttly]() api 

`tiny-url` : Shorten your urls using [tiny-url]() api


* Example usage : 
```

linsh.exe tiny-url -u http://test.com/ -o 

Shortened URL: https://tinyurl.com/test1234
 Link copied to clip board..!!

```

[Note: `-o / --open` will open the link in your browser. ]

#### Config file
For shortening links to bitly and cuttly an api key [or an access token] is necessary. Api keys should be pasted as such in the config.cfg file. An example is shown below
```
[Bitly]
api-key = '20b200gf394849gg55aaea555fsfs'

[Cuttly]
api-key = '112sfsf555aeaa55gg948493fg00d'
```
Get bitly api key from : https://dev.bitly.com/

Get cuttly api key from : https://cutt.ly/cuttly-api

#### Supported API's

Linsh currently supports tiny-url, bitly, cuttly and chilp only . More api's will be added in upcoming relases.

#### License

Linsh is licensed under the [Apache License 2.0]()

























