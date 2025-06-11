import typer
import pytesseract
from uuid import uuid4
from PIL import Image, ImageGrab
from services import notifier

app = typer.Typer()

def get_image_from_clipboard() -> str:
    image = ImageGrab.grabclipboard()

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


@app.command()
def get_text_from_image():
    image = get_image_from_clipboard()
    if image is None:
        raise Exception("No image found in clipboard")
    
    img_text = extract_text_from_image(image)
    if img_text is None:
        raise Exception("No text found in image")
        
    notifier("Hermes", "Image text is available on clipboard")
    
    print(img_text)


if __name__ == "__main__":
    app()
