from pprint import pprint

from analysis.affected_files import affected_files

affected_files.build(".")

print()
print("=" * 80)
print("FILES AFFECTED BY core/config.py")
print("=" * 80)

pprint(
    affected_files.affected_by(
        "core/config.py"
    )
)

print()
print("=" * 80)
print("FILES AFFECTED BY tools/registry.py")
print("=" * 80)

pprint(
    affected_files.affected_by(
        "tools/registry.py"
    )
)