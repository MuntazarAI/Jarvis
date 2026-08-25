import pytest
from jarvis.core.batch.processor import BatchProcessor

@pytest.mark.asyncio
async def test_batch_process():
    processor = BatchProcessor()
    batch = processor.create_batch("b1", [1, 2, 3])
    results = await processor.process_batch("b1", lambda x: x * 2)
    assert len(results) == 3
