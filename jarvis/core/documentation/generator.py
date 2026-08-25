from typing import Dict

class DocumentationGenerator:
    def __init__(self):
        self.docs = {}
        self.sections = {}
    
    def add_doc(self, doc_id: str, title: str, content: str):
        self.docs[doc_id] = {
            "title": title,
            "content": content,
            "sections": []
        }
    
    def add_section(self, doc_id: str, section_name: str, section_content: str):
        if doc_id in self.docs:
            self.docs[doc_id]["sections"].append({
                "name": section_name,
                "content": section_content
            })
    
    def generate_markdown(self, doc_id: str) -> str:
        if doc_id not in self.docs:
            return ""
        doc = self.docs[doc_id]
        md = f"# {doc['title']}\n\n{doc['content']}\n\n"
        for section in doc["sections"]:
            md += f"## {section['name']}\n{section['content']}\n\n"
        return md
    
    def get_toc(self) -> list:
        return [{"id": k, "title": v["title"]} for k, v in self.docs.items()]

_generator = None

def get_documentation_generator():
    global _generator
    if _generator is None:
        _generator = DocumentationGenerator()
    return _generator
