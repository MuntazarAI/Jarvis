import pytest
from jarvis.core.deployment.deployer import DeploymentManager

def test_deploy():
    dm = DeploymentManager()
    assert dm.deploy("v1.0", {"config": "prod"})

def test_current_version():
    dm = DeploymentManager()
    dm.deploy("v2.0", {})
    assert dm.get_current_version() == "v2.0"

def test_rollback():
    dm = DeploymentManager()
    dm.deploy("v3.0", {})
    assert dm.rollback("v3.0")
    history = dm.get_deployment_history()
    assert history["v3.0"] == "rolled_back"
