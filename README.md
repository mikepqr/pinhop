# Pinhop

Timehop for Pinboard.

Get pinboard posts from a previous month or day as a pinboard-style web page.

## Installation

Copy [pinhop](pinhop) into your path.

Requires requests (e.g. `pip install --user requests`). Uses `tqdm` if
installed (optional).

## Usage

```
usage: pinhop [-h] [--token TOKEN] [-o OUT] [--date DATE] [--open] [y]

Get pinboard posts from a previous month or day. By default, writes posts from
this month one year ago to pinhop.html.

positional arguments:
  y                  years ago this month

optional arguments:
  -h, --help         show this help message and exit
  --token TOKEN      Pinboard API token (see
                     https://pinboard.in/settings/password). Required if
                     PINBOARD_TOKEN environment variable not set.
  -o OUT, --out OUT  output file
  --date DATE        Get posts for particular month (YYYY-MM format) or day
                     (YYYY-MM-DD) (overrides y)
  --open             Load in browser when finished (macOS only)
```
