from jarvis.core.agents.base_agent import BaseAgent, AgentType, AgentResult
import time

class VisionAgent(BaseAgent):
    def __init__(self):
        super().__init__(AgentType.VISION)
    
    async def execute(self, task: str, context=None) -> AgentResult:
        start = time.time()
        res = AgentResult(True, AgentType.VISION, f"Vision: {task[:20]}", "", (time.time() - start) * 1000)
        await self._track_result(res)
        return res
