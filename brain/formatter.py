def format_tool_result(tool_result):
    """
    Convert tool results into human-readable text.
    """

    if isinstance(tool_result, list):

        if not tool_result:
            return "I couldn't find anything."

        lines = []

        for item in tool_result:
            lines.append(f"{item['path']} = {item['value']}")

        return "\n".join(lines)

    if isinstance(tool_result, dict):

        if not tool_result:
            return "Done."

        lines = []

        for key, value in tool_result.items():
            lines.append(f"{key}: {value}")

        return "\n".join(lines)

    return str(tool_result)