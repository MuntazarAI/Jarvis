import pytest
from jarvis.core.documentation.generator import DocumentationGenerator

def test_add_doc():
    gen = DocumentationGenerator()
    gen.add_doc("d1", "Title", "Content")
    assert "d1" in gen.docs

def test_add_section():
    gen = DocumentationGenerator()
    gen.add_doc("d2", "Title", "Content")
    gen.add_section("d2", "Section1", "Content")
    assert len(gen.docs["d2"]["sections"]) > 0

def test_generate_markdown():
    gen = DocumentationGenerator()
    gen.add_doc("d3", "My Doc", "Intro")
    md = gen.generate_markdown("d3")
    assert "My Doc" in md
