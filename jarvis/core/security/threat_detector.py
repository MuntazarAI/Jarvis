class ThreatDetector:
    def __init__(self):
        self.patterns = {"sql": ["'; DROP", "OR 1=1"], "cmd": ["; ls", "| nc"]}
    
    async def analyze(self, task):
        risk = 0.0
        threats = []
        for t, p in self.patterns.items():
            for pattern in p:
                if pattern.lower() in task.lower():
                    threats.append(t)
                    risk += 0.6
        return {"risk": min(1.0, risk), "threat": risk > 0.5, "detected": threats}

_td = None
def get_threat_detector():
    global _td
    if _td is None:
        _td = ThreatDetector()
    return _td
