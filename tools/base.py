from abc import ABC, abstractmethod


class Tool(ABC):
    """
    Base class for every Jarvis tool.
    """

    name = ""
    description = ""

    @abstractmethod
    def run(self, **kwargs):
        """
        Every tool implements this.
        """
        pass

    def execute(self, arguments):
        """
        Execute a tool using a dictionary of arguments.
        """

        if arguments is None:
            arguments = {}

        return self.run(**arguments)

    def schema(self):
        return {
            "name": self.name,
            "description": self.description
        }