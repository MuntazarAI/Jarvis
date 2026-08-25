from jarvis.core.transform.transformer import TransformPipeline

def test_transform():
    pipeline = TransformPipeline()
    t = pipeline.create_transformer("t1")
    t.add_step(lambda x: x * 2)
    result = pipeline.apply("t1", 5)
    assert result == 10
