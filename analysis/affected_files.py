from analysis.dependency_graph import dependency_graph


class AffectedFiles:
    """
    Finds every file that is directly or indirectly affected
    by a change in another file.
    """

    def __init__(self):
        self.graph = {}

    def build(self, root="."):
        self.graph = dependency_graph.build(root)
        return self.graph

    def affected_by(self, filename):

        if not self.graph:
            return []

        affected = set()
        queue = [filename]

        while queue:

            current = queue.pop(0)

            if current in affected:
                continue

            affected.add(current)

            info = self.graph.get(current)

            if not info:
                continue

            for file in info.get("used_by", []):

                if file not in affected:
                    queue.append(file)

        affected.discard(filename)

        return sorted(affected)


affected_files = AffectedFiles()