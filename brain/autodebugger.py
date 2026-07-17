from tools.registry import registry


class AutoDebugger:

    def debug(self, python_result):

        if python_result.get("success", True):
            return {
                "success": True,
                "message": "No errors detected."
            }

        stderr = python_result.get("stderr", "")

        error_tool = registry.get("error_analyzer")
        reader = registry.get("code_reader")
        analyzer = registry.get("code_analyzer")

        error = error_tool.execute({
            "traceback": stderr
        })

        frame = error.get("last_frame")

        if not frame:
            return {
                "success": False,
                "error": "Could not locate failing file."
            }

        source = reader.execute({
            "path": frame["path"]
        })

        analysis = analyzer.execute({
            "path": frame["path"]
        })

        return {
            "success": True,
            "error": error,
            "source": source,
            "analysis": analysis
        }


autodebugger = AutoDebugger()