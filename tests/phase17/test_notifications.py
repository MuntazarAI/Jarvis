import pytest
from jarvis.core.notifications.notifier import get_notification_manager

def test_notify():
    nm = get_notification_manager()
    result = nm.notify("test message", "email")
    assert result

def test_invalid_channel():
    nm = get_notification_manager()
    result = nm.notify("msg", "invalid")
    assert not result

def test_get_notifications():
    nm = get_notification_manager()
    nm.notify("msg1", "sms")
    notifs = nm.get_notifications()
    assert len(notifs) > 0
