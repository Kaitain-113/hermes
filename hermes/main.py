import typer

from hermes.handlers import get_text_from_image

app = typer.Typer()


@app.command()
def textify():
    """
    Get text from image (on clipboard) and put response on clipboard
    """
    get_text_from_image()


if __name__ == "__main__":
    app()
