from tools.base import Tool
from core.memory import memory


class MemoryTool(Tool):

    name = "memory"

    description = (
        "Store information, search memory, "
        "recall all memories and forget memories."
    )

    def run(self, action=None, **kwargs):

        if action is None:
            return {
                "error": "Memory tool requires an action."
            }

        if action == "remember":

            memory_data = kwargs.get("memory")

            if memory_data is None:
                return {
                    "error": "Missing memory."
                }

            memory.remember(memory_data)

            return {
                "success": True
            }

        elif action == "search":

            keyword = kwargs.get("keyword")

            if not keyword:
                return {
                    "error": "Missing keyword."
                }

            return memory.search(keyword)

        elif action == "recall":

            return memory.recall()

        elif action == "forget":

            category = kwargs.get("category")
            key = kwargs.get("key")

            if not category or not key:
                return {
                    "error": "Missing category or key."
                }

            memory.forget(category, key)

            return {
                "success": True
            }

        return {
            "error": f"Unknown action: {action}"
        }