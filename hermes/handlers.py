from hermes.media_utils import (
    extract_text_from_image,
    get_image_from_clipboard
)
from hermes.services import notifier, copy_to_clipboard


def get_text_from_image(output: str):
    image = get_image_from_clipboard()
    if image is None:
        raise Exception("No image found in clipboard")
    
    img_text = extract_text_from_image(image)
    if img_text is None:
        raise Exception("No text found in image")
    
    match output:
        case "clipboard":
            if copy_to_clipboard(img_text):
                notifier("Text processed", "Image text is available on clipboard")
            else:
                notifier("Error", "Unable to copy text to clipboard")

        case "console":
            print("|" + "< IMAGE TEXT >".center(60, "=") + "|\n")
            print(img_text)
            print("=-=" * 20)
