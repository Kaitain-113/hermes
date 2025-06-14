from hermes.media_utils import  get_text_from_image

from hermes.services import (
    notifier,
    copy_content_to_clipboard,
    create_file
)


def handle_text_to_clipboard():
    text = get_text_from_image()
    if copy_content_to_clipboard(text):
        notifier("Text processed", "Image text is available on clipboard")
        return
    
    notifier("Error", "Unable to copy text to clipboard")


def handle_text_to_console():
    text = get_text_from_image()
    print("|" + "< IMAGE TEXT >".center(60, "=") + "|\n")
    print(text)
    print("=-=" * 20)


def handle_text_to_file(file_path: str):
    text = get_text_from_image()
    if create_file(file_path, text):
        notifier("Text processed", "Image text is available on clipboard")
        return
    
    notifier("Error", "Unable to copy text to clipboard")
