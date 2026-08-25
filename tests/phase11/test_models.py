import pytest
from jarvis.core.models.classifier import NeuralClassifier, RegressorModel

def test_classifier_train():
    clf = NeuralClassifier("test_clf")
    clf.train([1, 2, 3], ["a", "b", "a"])
    assert clf.is_trained

def test_classifier_predict():
    clf = NeuralClassifier("test_clf")
    clf.train([1, 2, 3], ["cat", "dog"])
    result = clf.predict(1)
    assert "prediction" in result

def test_regressor():
    reg = RegressorModel("test_reg")
    reg.train([1, 2, 3], [1.0, 2.0, 3.0])
    result = reg.predict(2)
    assert "prediction" in result
