import time
from typing import Dict

class ComplianceRule:
    def __init__(self, rule_id: str, rule_type: str, check_func):
        self.rule_id = rule_id
        self.rule_type = rule_type
        self.check_func = check_func
        self.passed = False

class ComplianceAuditor:
    def __init__(self):
        self.rules = {}
        self.audit_log = []
    
    def add_rule(self, rule_id: str, rule_type: str, check_func):
        self.rules[rule_id] = ComplianceRule(rule_id, rule_type, check_func)
    
    def run_audit(self) -> Dict:
        results = {}
        for rule_id, rule in self.rules.items():
            try:
                passed = rule.check_func()
                rule.passed = passed
                results[rule_id] = {"status": "pass" if passed else "fail"}
            except Exception as e:
                results[rule_id] = {"status": "error", "error": str(e)}
        
        self.audit_log.append({"timestamp": time.time(), "results": results})
        return results
    
    def get_audit_history(self) -> list:
        return self.audit_log.copy()

_auditor = None

def get_compliance_auditor():
    global _auditor
    if _auditor is None:
        _auditor = ComplianceAuditor()
    return _auditor
