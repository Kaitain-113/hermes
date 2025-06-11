from notifypy import Notify
import pyperclip

def notifier(title: str, message: str) -> None:
    notification = Notify()
    notification.icon = "hermes/resources/notification_icon/clipboard.png"
    notification.title = title
    notification.message = message
    notification.send()

def copy_to_clipboard(text: str) -> bool:
    pyperclip.copy(text)
    return True
