from typing import Dict

class Notification:
    def __init__(self, msg: str, channel: str):
        self.message = msg
        self.channel = channel
        self.sent = False
    
    def mark_sent(self):
        self.sent = True

class NotificationManager:
    def __init__(self):
        self.notifications = []
        self.channels = {"email", "sms", "push", "webhook"}
    
    def notify(self, message: str, channel: str) -> bool:
        if channel not in self.channels:
            return False
        notif = Notification(message, channel)
        notif.mark_sent()
        self.notifications.append(notif)
        return True
    
    def get_notifications(self) -> list:
        return self.notifications.copy()
    
    def clear(self):
        self.notifications.clear()

_manager = None

def get_notification_manager():
    global _manager
    if _manager is None:
        _manager = NotificationManager()
    return _manager
