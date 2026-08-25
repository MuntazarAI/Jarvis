import pytest
from jarvis.core.analytics.tracker import get_analytics

def test_track_event():
    analytics = get_analytics()
    analytics.track_event("user_login")
    events = analytics.get_events()
    assert len(events) > 0

def test_counter():
    analytics = get_analytics()
    analytics.increment_counter("page_views", 5)
    count = analytics.get_counter("page_views")
    assert count == 5

def test_summary():
    analytics = get_analytics()
    analytics.track_event("event1")
    analytics.increment_counter("cnt", 3)
    summary = analytics.get_summary()
    assert summary["total_events"] > 0
