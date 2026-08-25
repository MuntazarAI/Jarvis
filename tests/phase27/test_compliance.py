import pytest
from jarvis.core.compliance.auditor import ComplianceAuditor

def test_add_rule():
    auditor = ComplianceAuditor()
    auditor.add_rule("rule1", "security", lambda: True)
    assert "rule1" in auditor.rules

def test_run_audit():
    auditor = ComplianceAuditor()
    auditor.add_rule("r1", "type", lambda: True)
    results = auditor.run_audit()
    assert results["r1"]["status"] == "pass"

def test_audit_history():
    auditor = ComplianceAuditor()
    auditor.add_rule("r2", "type", lambda: True)
    auditor.run_audit()
    history = auditor.get_audit_history()
    assert len(history) > 0
