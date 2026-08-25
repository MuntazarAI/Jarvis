from typing import List, Dict

class KnowledgeGraph:
    def __init__(self):
        self.entities = {}
        self.relationships = []
    
    def add_entity(self, entity_id: str, entity_type: str, properties: Dict = None):
        """Add entity to knowledge graph"""
        self.entities[entity_id] = {
            "id": entity_id,
            "type": entity_type,
            "properties": properties or {}
        }
    
    def add_relationship(self, source_id: str, target_id: str, relationship_type: str, properties: Dict = None):
        """Add relationship between entities"""
        self.relationships.append({
            "source": source_id,
            "target": target_id,
            "type": relationship_type,
            "properties": properties or {}
        })
    
    def get_entity_neighbors(self, entity_id: str) -> List[Dict]:
        """Get neighbors of an entity"""
        neighbors = []
        for rel in self.relationships:
            if rel["source"] == entity_id:
                neighbors.append({"entity": rel["target"], "relationship": rel["type"]})
        return neighbors
    
    def get_graph_stats(self) -> Dict:
        return {
            "entities": len(self.entities),
            "relationships": len(self.relationships)
        }

_graph = None

def get_knowledge_graph():
    global _graph
    if _graph is None:
        _graph = KnowledgeGraph()
    return _graph
