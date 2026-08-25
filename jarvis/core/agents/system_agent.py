from jarvis.core.agents.base_agent import BaseAgent, AgentType, AgentResult
import time

class SystemAgent(BaseAgent):
    def __init__(self):
        super().__init__(AgentType.SYSTEM)
    
    async def execute(self, task: str, context=None) -> AgentResult:
        if any(x in task.lower() for x in ["rm -rf", "dd if="]):
            return AgentResult(False, AgentType.SYSTEM, error="Blocked")
        start = time.time()
        res = AgentResult(True, AgentType.SYSTEM, f"System: {task[:20]}", "", (time.time() - start) * 1000)
        await self._track_result(res)
        return res
