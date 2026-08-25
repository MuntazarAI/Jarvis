"""SecurityManager - Zero-trust validation"""
from typing import Dict, List, Any
from datetime import datetime, timezone
from enum import Enum
import logging

logger = logging.getLogger(__name__)

class ThreatLevel(Enum):
    LOW = "low"
    MEDIUM = "medium"
    HIGH = "high"
    CRITICAL = "critical"

class SecurityDecision(Enum):
    APPROVED = "approved"
    DENIED = "denied"

class SecurityManager:
    def __init__(self):
        self.threat_level = ThreatLevel.LOW
        self.blocked_count = 0
        self.approved_count = 0
        self.security_events: List[Dict[str, Any]] = []
        logger.info("SecurityManager initialized")
    
    async def validate_request(self, task: str, user_id: str, agent_type: str, context: Dict[str, Any] = None) -> tuple:
        if not task or not isinstance(task, str) or len(task.strip()) == 0:
            self.blocked_count += 1
            return SecurityDecision.DENIED, "Empty task", {}
        if self._check_injection_patterns(task):
            self.threat_level = ThreatLevel.HIGH
            self.blocked_count += 1
            return SecurityDecision.DENIED, "Injection detected", {}
        self.approved_count += 1
        return SecurityDecision.APPROVED, "Approved", {}
    
    def _check_injection_patterns(self, task: str) -> bool:
        patterns = ["'; DROP", "OR 1=1", "__import__", "eval("]
        return any(p.lower() in task.lower() for p in patterns)
    
    def get_security_stats(self) -> Dict[str, Any]:
        total = self.blocked_count + self.approved_count
        return {"threat_level": self.threat_level.value, "blocked": self.blocked_count, "approved": self.approved_count, "total": total}

_security_manager = None

def get_security_manager() -> SecurityManager:
    global _security_manager
    if _security_manager is None:
        _security_manager = SecurityManager()
    return _security_manager
