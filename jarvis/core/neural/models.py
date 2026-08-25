class NeuralModelBase:
    def __init__(self, name: str):
        self.name = name
    
    async def infer(self, data):
        return await self._forward(data)
    
    async def _forward(self, data):
        raise NotImplementedError

class IntentClassificationModel(NeuralModelBase):
    def __init__(self):
        super().__init__("intent")
    
    async def _forward(self, text):
        return {"intent": "execute"}

class AnomalyDetectionModel(NeuralModelBase):
    def __init__(self):
        super().__init__("anomaly")
    
    async def _forward(self, metrics):
        return {"is_anomalous": False}

class PredictionModel(NeuralModelBase):
    def __init__(self):
        super().__init__("prediction")
    
    async def _forward(self, historical):
        return {"prediction": 0.5}

_models = {}
def get_model(name: str):
    if name not in _models:
        if name == "intent":
            _models[name] = IntentClassificationModel()
        elif name == "anomaly":
            _models[name] = AnomalyDetectionModel()
        elif name == "prediction":
            _models[name] = PredictionModel()
    return _models[name]
