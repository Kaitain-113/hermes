import typer
from hermes.handlers import (
    handle_text_to_clipboard,
    handle_text_to_console,
    handle_text_to_file
)

app = typer.Typer()

@app.command()
def text_to_clipboard():
    handle_text_to_clipboard()


@app.command()
def text_to_console():
    handle_text_to_console()


@app.command()
def text_to_file(file_path: str):
    handle_text_to_file(file_path)


if __name__ == "__main__":
    app()
