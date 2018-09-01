# Pinhop

Timehop for Pinboard.

## Installation

Requires Python 3.6+ (f-strings) and requests (e.g. `pip install --user
requests`). Uses `tqdm` if installed.

Copy [pinhop](pinhop) into your path.

## Usage

```
usage: pinhop [-h] [--token TOKEN] [-o OUT] [--month MONTH] [--open] yearsago

Get pinboard posts from a previous month. By default, writes posts from this
month one year ago to pinhop.html.

positional arguments:
  yearsago           years ago this month

optional arguments:
  -h, --help         show this help message and exit
  --token TOKEN      Pinboard API token (see
                     https://pinboard.in/settings/password). Required if
                     PINBOARD_TOKEN environment variable not set.
  -o OUT, --out OUT  output file
  --month MONTH      Get posts for particular month in YYYY-MM format
                     (overrides -y)
  --open             Load in browser when finished (macOS only)
```
