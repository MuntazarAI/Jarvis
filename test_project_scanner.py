from pprint import pprint

from analysis.project_scanner import project_scanner

project = project_scanner.scan(".")

pprint(project)