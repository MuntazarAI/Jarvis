from typing import Dict, Callable
import time
import asyncio
import inspect

class CircuitBreaker:
    def __init__(self, failure_threshold: int = 5, timeout: int = 60):
        self.failure_threshold = failure_threshold
        self.timeout = timeout
        self.failure_count = 0
        self.last_failure_time = None
        self.is_open = False
    
    async def call(self, func: Callable, *args, **kwargs):
        """Execute function with circuit breaker protection"""
        if self.is_open:
            if time.time() - self.last_failure_time > self.timeout:
                self.is_open = False
                self.failure_count = 0
            else:
                return {"status": "circuit_open"}
        
        try:
            if inspect.iscoroutinefunction(func):
                result = await func(*args, **kwargs)
            else:
                result = func(*args, **kwargs)
            self.failure_count = 0
            return {"status": "success", "result": result}
        except Exception as e:
            self.failure_count += 1
            self.last_failure_time = time.time()
            if self.failure_count >= self.failure_threshold:
                self.is_open = True
            return {"status": "failed", "error": str(e)}

class HealthCheck:
    def __init__(self):
        self.checks = {}
        self.results = []
    
    def register_check(self, name: str, check_func: Callable):
        """Register health check"""
        self.checks[name] = check_func
    
    async def run_checks(self) -> Dict:
        """Run all health checks"""
        results = {}
        for name, check_func in self.checks.items():
            try:
                if inspect.iscoroutinefunction(check_func):
                    result = await check_func()
                else:
                    result = check_func()
                results[name] = {"status": "healthy", "result": result}
            except Exception as e:
                results[name] = {"status": "unhealthy", "error": str(e)}
        self.results.append({"timestamp": time.time(), "checks": results})
        return results
    
    def get_health_status(self) -> Dict:
        if not self.results:
            return {"status": "unknown"}
        last_check = self.results[-1]
        all_healthy = all(c["status"] == "healthy" for c in last_check["checks"].values())
        return {"status": "healthy" if all_healthy else "unhealthy"}

_circuit_breaker = None

def get_circuit_breaker():
    global _circuit_breaker
    if _circuit_breaker is None:
        _circuit_breaker = CircuitBreaker()
    return _circuit_breaker
