from pprint import pprint

from execution.orchestrator import engineering_orchestrator

if __name__ == "__main__":
    result = engineering_orchestrator.prepare(".")

    pprint(result)
