from analysis.dependency_graph import dependency_graph

graph = dependency_graph.build(".")

print("=" * 80)
print("DEPENDENCY GRAPH SUMMARY")
print("=" * 80)

print(f"\nTotal files: {len(graph)}")

print("\nFirst 10 files:\n")

for filename in sorted(graph)[:10]:

    info = graph[filename]

    print(f"{filename}")

    print(f"  Imports   : {len(info['imports'])}")

    print(f"  Classes   : {len(info['classes'])}")

    print(f"  Functions : {len(info['functions'])}")

    print(f"  Used by   : {len(info['used_by'])}")

    print()

print("=" * 80)