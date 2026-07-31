from pprint import pprint

from analysis.project_scanner import project_scanner

if __name__ == "__main__":
    project = project_scanner.scan(".")

    pprint(project)
