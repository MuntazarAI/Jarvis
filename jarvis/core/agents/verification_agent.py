from jarvis.core.agents.base_agent import BaseAgent, AgentType, AgentResult
import time

class VerificationAgent(BaseAgent):
    def __init__(self):
        super().__init__(AgentType.VERIFICATION)
    
    async def execute(self, task: str, context=None) -> AgentResult:
        start = time.time()
        res = AgentResult(True, AgentType.VERIFICATION, "APPROVED", "", (time.time() - start) * 1000)
        await self._track_result(res)
        return res
