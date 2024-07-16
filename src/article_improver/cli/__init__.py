# SPDX-FileCopyrightText: 2024-present CodePeacock <mayursinalkar404@gmail.com>
#
# SPDX-License-Identifier: MIT
import click

from article_improver.__about__ import __version__


@click.group(context_settings={"help_option_names": ["-h", "--help"]}, invoke_without_command=True)
@click.version_option(version=__version__, prog_name="article-improver")
def article_improver():
    click.echo("Hello world!")
