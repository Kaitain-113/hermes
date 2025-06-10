from notifypy import Notify

def notifier(title, message):
    notification = Notify()
    notification.icon = "./resources/notification_icon/clipboard.png"
    notification.title = title
    notification.message = message
    notification.send()

