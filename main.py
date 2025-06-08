import typer
from PIL import Image, ImageGrab

app = typer.Typer()


def get_image_from_clipboard() -> Image.Image | None:
    image = ImageGrab.grabclipboard()

    if isinstance(image, Image.Image):
        return image

    return None

@app.command()
def get_text_from_image():
    """
    Extract image from clipboard
    """

    image = get_image_from_clipboard()
    image.show()

    print("test")


if __name__ == "__main__":
    app()
