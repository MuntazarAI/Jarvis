import pytest
from jarvis.core.logging.logger import get_logger

def test_log_message():
    logger = get_logger("test")
    logger.info("test message")
    logs = logger.get_logs()
    assert len(logs) > 0

def test_log_levels():
    logger = get_logger("test2")
    logger.debug("debug")
    logger.info("info")
    logger.error("error")
    assert len(logger.logs) >= 3

def test_get_logs_by_level():
    logger = get_logger("test3")
    logger.error("err")
    errors = logger.get_logs("ERROR")
    assert len(errors) > 0
