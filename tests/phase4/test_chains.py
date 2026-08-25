import pytest
from jarvis.core.automation.automation_chains import Chain, ChainType, ChainManager

@pytest.fixture
def manager():
    return ChainManager()

@pytest.mark.asyncio
async def test_chain_execution(manager):
    def t1():
        return 1
    def t2():
        return 2
    chain = Chain("c1", ChainType.SEQUENTIAL, [t1, t2])
    manager.register_chain(chain)
    results = await chain.execute()
    assert len(results) == 2

@pytest.mark.asyncio
async def test_chain_via_manager(manager):
    def task():
        return "ok"
    chain = Chain("c1", ChainType.SEQUENTIAL, [task])
    manager.register_chain(chain)
    results = await manager.execute_chain("c1")
    assert len(results) == 1

def test_list_chains(manager):
    def t():
        return 1
    chain = Chain("c1", ChainType.SEQUENTIAL, [t])
    manager.register_chain(chain)
    chains = manager.list_chains()
    assert len(chains) == 1
