import pytest
from jarvis.core.testing.testrunner import TestRunner

def test_add_test():
    runner = TestRunner()
    runner.add_test("test1", lambda: None)
    assert len(runner.tests) > 0

def test_run_tests():
    runner = TestRunner()
    runner.add_test("t1", lambda: True)
    runner.add_test("t2", lambda: None)
    summary = runner.run_tests()
    assert summary["total"] == 2

def test_test_summary():
    runner = TestRunner()
    runner.add_test("pass", lambda: None)
    summary = runner.run_tests()
    assert summary["passed"] > 0
