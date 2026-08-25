class AdaptationEngine:
    def __init__(self):
        self.perf = {}
        self.history = []
    
    async def learn_from_result(self, agent_name: str, result, feedback=None):
        if agent_name not in self.perf:
            self.perf[agent_name] = {"total": 0, "success": 0}
        self.perf[agent_name]["total"] += 1
        if result.success:
            self.perf[agent_name]["success"] += 1
        self.history.append({"agent": agent_name})
    
    def get_performance_stats(self, agent_name=None):
        return self.perf.get(agent_name, {}) if agent_name else self.perf
    
    def get_learning_insights(self):
        return {"total_learned": len(self.history)}

_engine = None
def get_adaptation_engine():
    global _engine
    if _engine is None:
        _engine = AdaptationEngine()
    return _engine
