#!/usr/bin/env python3

import invoke
import sys
import random
import colorama
import datetime
from termcolor import colored
from dateutil.parser import parse

class Source:
    def __init__(self, title, url, author, license, length):
        self.title = title
        self.url = url
        self.author = author
        self.license = license
        self.length = length

    @property
    def author_name(self):
        return authors[self.author]

    @property
    def start_at(self):
        return random.randint(0, self.length)

    @property
    def delta(self):
        time_delta = datetime.timedelta(seconds=self.start_at)
        return parse(str(time_delta)).strftime("%H:%M:%S")

    @property
    def command(self):
        return f"cvlc --no-video {self.url} --start-time={self.start_at}"

    def __repr__(self):
        return (
            f"{colored(self.title, 'yellow')}\n"
            + f"{colored(self.url, 'magenta')} ({self.delta})\n"
            + f"Author: {self.author}\n"
            + f"        {colored(self.author_name, 'green')}\n"
            + f"{self.license}\n"
        )

authors = {
    "RelaxedMovement": "https://www.youtube.com/c/TheRelaxedMovement",
}
library = [
    Source(
        title="Lofi Chilled Beats - 12 Hours of DMCA Free and Copyright Free Music for Twitch Streamers",
        author="RelaxedMovement",
        url="https://www.youtube.com/watch?v=udGvUx70Q3U",
        license="© Henry Keate t/a TheRelaxedMovement. All Rights Reserved.",
        length=43194
    ),
    Source(
        title="Lofi Jazz - 12 Hours of Copyright Free Music for Creators",
        author="RelaxedMovement",
        url="https://www.youtube.com/watch?v=PlEBqUGYVT8",
        license="© Henry Keate t/a TheRelaxedMovement. All Rights Reserved.",
        length=42942,
    )
]

def main():
    colorama.init()
    selection = library[1] if len(sys.argv) == 2 else random.choice(library)
    print(selection)
    invoke.run(selection.command, hide="both")


if __name__ == "__main__":
    main()
