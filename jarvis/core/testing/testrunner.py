from typing import Callable, Dict

class TestCase:
    def __init__(self, name: str, test_func: Callable):
        self.name = name
        self.test_func = test_func
        self.passed = False
        self.error = None

class TestRunner:
    __test__ = False  # Prevent pytest from treating this production class as a test container.
    def __init__(self):
        self.tests = []
        self.results = []
    
    def add_test(self, name: str, test_func: Callable):
        self.tests.append(TestCase(name, test_func))
    
    def run_tests(self) -> Dict:
        for test in self.tests:
            try:
                test.test_func()
                test.passed = True
            except Exception as e:
                test.error = str(e)
            self.results.append({
                "name": test.name,
                "passed": test.passed,
                "error": test.error
            })
        return self.get_summary()
    
    def get_summary(self) -> Dict:
        passed = sum(1 for r in self.results if r["passed"])
        total = len(self.results)
        return {
            "total": total,
            "passed": passed,
            "failed": total - passed,
            "success_rate": (passed / total * 100) if total > 0 else 0
        }

_runner = None

def get_test_runner():
    global _runner
    if _runner is None:
        _runner = TestRunner()
    return _runner
