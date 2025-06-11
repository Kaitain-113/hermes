from hermes.media_utils import (
    extract_text_from_image,
    get_image_from_clipboard
)
from hermes.services import notifier, copy_to_clipboard

def get_text_from_image():
    image = get_image_from_clipboard()
    if image is None:
        raise Exception("No image found in clipboard")
    
    img_text = extract_text_from_image(image)
    if img_text is None:
        raise Exception("No text found in image")
        
    if content_on_clipboard := copy_to_clipboard(img_text):
        notifier("Text processed", "Image text is available on clipboard")
        return
    
    notifier("Error", "Unable to copy text to clipboard")

    