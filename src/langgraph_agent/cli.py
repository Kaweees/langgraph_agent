import asyncio

import typer

from .agent import runner

app = typer.Typer()


@app.command()
def run():
    _response = asyncio.run(
        runner.run_debug("Write a blog post about the benefits of multi-agent systems for software developers")
    )


def entrypoint():
    app()
