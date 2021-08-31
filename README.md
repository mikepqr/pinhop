# Pinhop

Timehop for Pinboard.

Get pinboard posts from a previous month or day as a pinboard-style web page.

## Installation

```
pip install pinhop
```

## Usage

```
Usage: pinhop [OPTIONS]

  Get pinboard posts from a previous month or day. By default, writes posts
  from this month one year ago to pinhop.html.

Options:
  -y, --yearsago INTEGER          Number of years ago this month  [default: 1]
  --token TEXT                    Pinboard API token (see
                                  https://pinboard.in/settings/password).
                                  Required if PINBOARD_TOKEN environment
                                  variable not set.
  --out TEXT                      Output file  [default: pinhop.html]
  --date TEXT                     Get posts for particular month (YYYY-MM
                                  format) or day (YYYY-MM-DD) (overrides y)
  --browse / --no-browse          Load output file in browser when finished
                                  [default: no-browse]
  --install-completion [bash|zsh|fish|powershell|pwsh]
                                  Install completion for the specified shell.
  --show-completion [bash|zsh|fish|powershell|pwsh]
                                  Show completion for the specified shell, to
                                  copy it or customize the installation.
  --help                          Show this message and exit.
```
