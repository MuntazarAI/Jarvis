from pprint import pprint

from execution.orchestrator import engineering_orchestrator

result = engineering_orchestrator.prepare(".")

pprint(result)