import pytest
from jarvis.core.neural.models import get_model

@pytest.mark.asyncio
async def test_intent_model():
    model = get_model("intent")
    result = await model.infer("search")
    assert "intent" in result

@pytest.mark.asyncio
async def test_anomaly_model():
    model = get_model("anomaly")
    result = await model.infer({"cpu": 0.5})
    assert "is_anomalous" in result

@pytest.mark.asyncio
async def test_prediction_model():
    model = get_model("prediction")
    result = await model.infer([0.1, 0.2])
    assert "prediction" in result
