import typer

from hermes.handlers import get_text_from_image

app = typer.Typer()


@app.command()
def text_to_clipboard():
    get_text_from_image("clipboard")


@app.command()
def text_to_console():
    get_text_from_image("console")


if __name__ == "__main__":
    app()
