import os
import typer
import pytesseract
from uuid import uuid4
from PIL import Image, ImageGrab

app = typer.Typer()


def get_image_from_clipboard() -> str:
    image = ImageGrab.grabclipboard()

    # TO-DO multi operational system
    if isinstance(image, Image.Image):
        image_path = f'/tmp/{uuid4()}.png'
        image.save(image_path)
        return image_path

    return None

def extract_text_from_image(image_path: str) -> str:
    if not image_path:
        return None

    img = Image.open(image_path)

    result = pytesseract.image_to_string(img)
    return result


# TODO: command to setup language
@app.command()
def get_text_from_image():
    image = get_image_from_clipboard()
    if not image:
        raise Exception("No image found in clipboard")
    
    text = extract_text_from_image(image)
    if not text:
        raise Exception("No text found in image")
    
    print(text)


if __name__ == "__main__":
    app()
