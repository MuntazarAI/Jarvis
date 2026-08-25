import pytest
from jarvis.core.agents.speech_recognition_agent import SpeechRecognitionAgent
from jarvis.core.agents.vision_processing_agent import VisionProcessingAgent
from jarvis.core.agents.intent_classification_agent import IntentClassificationAgent
from jarvis.core.agents.anomaly_detection_agent import AnomalyDetectionAgent
from jarvis.core.agents.prediction_agent import PredictionAgent

@pytest.mark.asyncio
async def test_speech():
    agent = SpeechRecognitionAgent()
    result = await agent.execute("test")
    assert result.success

@pytest.mark.asyncio
async def test_vision():
    agent = VisionProcessingAgent()
    result = await agent.execute("test")
    assert result.success

@pytest.mark.asyncio
async def test_intent():
    agent = IntentClassificationAgent()
    result = await agent.execute("test")
    assert result.success

@pytest.mark.asyncio
async def test_anomaly():
    agent = AnomalyDetectionAgent()
    result = await agent.execute("test")
    assert result.success

@pytest.mark.asyncio
async def test_prediction():
    agent = PredictionAgent()
    result = await agent.execute("test")
    assert result.success
