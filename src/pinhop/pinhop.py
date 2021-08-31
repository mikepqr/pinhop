import calendar
import json
from datetime import datetime as dt
from urllib.parse import urlencode
from urllib.request import urlopen

import typer
from tqdm import tqdm

from pinhop.css import css


def add_auth(params):
    global auth_token
    if not auth_token:
        raise ValueError(
            "Auth token unset. Configure PINBOARD_TOKEN "
            "environment variable or provide --token command line "
            "argument."
        )
    params.update({"auth_token": auth_token, "format": "json"})
    return params


def days_of_month(year, month):
    """
    Return list of YYYY-MM-DD strings for all days in year-month.
    """
    days_in_month = calendar.monthrange(year, month)[1]
    return [
        "{year}-{month:02d}-{day:02d}".format(year=year, month=month, day=day)
        for day in range(1, days_in_month + 1)
    ]


def get_day(day):
    params = add_auth({"dt": day})
    url = "https://api.pinboard.in/v1/posts/get?{}".format(urlencode(params))
    r = urlopen(url)
    return json.loads(r.read())


def get_posts_days(days):
    """
    Returns list of posts for list of days (where each day is a YYYY-MM-DD
    string.
    """
    jsons = [get_day(day) for day in tqdm(days)]
    posts = [post for json in jsons for post in json["posts"]]
    for post in posts:
        post.update({"user": jsons[0]["user"]})
    return posts


def format_extended(extended):
    return "<br />".join(extended.strip().split("\n"))


def format_tags(post):
    tags = post["tags"].split()
    urls = ["https://pinboard.in/u:{}/t:".format(post["user"]) + tag for tag in tags]
    return "&nbsp;".join(
        '<a class="tag" href="{url}">{tag}</a>'.format(url=url, tag=tag)
        for tag, url in zip(tags, urls)
    )


def format_time(isotime):
    return isotime[:10]


def post_html(post):
    data = {
        "extended": format_extended(post["extended"]),
        "tags": format_tags(post),
        "time": format_time(post["time"]),
        "href": post["href"],
        "description": post["description"],
    }
    return """
    <div class="bookmark">
        <div class="display">
            <div class="title">
                <a class="title" href="{href}">{description}</a>
            </div>
            <div class="description">{extended}</div>
            {tags}
            <div><a class="when">{time}</a></div>
        </div>
    </div>
    """.format(
        **data
    )


def posts_html(posts):
    return "\n".join(post_html(post) for post in posts)


def assemble_page(posts, title=""):
    data = {
        "title": " ".join(("Pinhop", title)),
        "posts": posts_html(posts),
        "css": css,
    }
    return """
    <html><head>
    <meta http-equiv="content-type" content="text/html; charset=utf-8" />
    <title>{title}</title>
    <style>
    {css}
    </style>
    </head>
    <body>
    <div id="banner">
    <div id="logo">
        <a id="pinboard_name" href="#">{title}</a>
    </div>
    <div id="top_menu">&nbsp;</div>
    <div style="clear:both"></div>
    </div>
    <div id="content" style="width: 700px; margin: 0;">
        <div id="main_column">
            <div id="bookmarks">
                {posts}
            </div>
        </div>
    </div>
    </body>
    </html>
    """.format(
        **data
    )


def get_posts(yearsago=1, year=None, month=None, day=None):
    """
    Return bookmarks posted this month years ago, or in a specific year and
    month.
    """
    if day:
        assert year is not None
        assert day is not None
        days = ["-".join((str(year), str(month), str(day)))]
    else:
        days = None
    if year is None and month is None:
        today = dt.today()
        year, month = today.year - yearsago, today.month
    if not days:
        days = days_of_month(year, month)
    return get_posts_days(days)


def pinhop(
    yearsago: int = typer.Option(
        1, "--yearsago", "-y", help="Number of years ago this month"
    ),
    cli_token: str = typer.Option(
        None,
        "--token",
        help=(
            "Pinboard API token (see https://pinboard.in/settings/password). "
            "Required if PINBOARD_TOKEN environment variable not set."
        ),
        envvar="PINBOARD_TOKEN",
    ),
    fname: str = typer.Option("pinhop.html", "--out", help="Output file"),
    date: str = typer.Option(
        None,
        help=(
            "Get posts for particular month (YYYY-MM format) or day "
            "(YYYY-MM-DD) (overrides y)"
        ),
    ),
    browse: bool = typer.Option(
        False,
        help="Load output file in browser when finished",
    ),
):
    """
    Get pinboard posts from a previous month or day. By default, writes
    posts from this month one year ago to pinhop.html.
    """

    global auth_token
    auth_token = cli_token

    year, month, day = None, None, None
    if date:
        try:
            date_dt = dt.strptime(date, "%Y-%m")
            year, month, day = date_dt.year, date_dt.month, None
        except ValueError:
            date_dt = dt.strptime(date, "%Y-%m-%d")
            year, month, day = date_dt.year, date_dt.month, date_dt.day
        title = date
    else:
        suffix = "" if yearsago == 1 else "s"
        title = f"{yearsago} year{suffix} ago"

    posts = get_posts(yearsago=yearsago, year=year, month=month, day=day)
    page = assemble_page(posts, title=title)
    with open(fname, "w") as f:
        f.write(page)

    if browse:
        typer.launch(fname)


def main():
    typer.run(pinhop)
