from typing import Dict, Callable

class GraphQLField:
    def __init__(self, name: str, field_type: str, resolver: Callable = None):
        self.name = name
        self.field_type = field_type
        self.resolver = resolver or (lambda obj: None)

class GraphQLType:
    def __init__(self, name: str):
        self.name = name
        self.fields = {}
    
    def add_field(self, name: str, field_type: str, resolver: Callable = None):
        self.fields[name] = GraphQLField(name, field_type, resolver)
    
    def get_fields(self) -> Dict:
        return self.fields.copy()

class GraphQLSchema:
    def __init__(self):
        self.types = {}
        self.root_query = GraphQLType("Query")
    
    def add_type(self, gql_type: GraphQLType):
        self.types[gql_type.name] = gql_type
    
    def add_query_field(self, name: str, field_type: str, resolver: Callable):
        self.root_query.add_field(name, field_type, resolver)
    
    def get_schema_info(self) -> Dict:
        return {"types": list(self.types.keys()), "query_fields": list(self.root_query.fields.keys())}

_schema = None

def get_graphql_schema():
    global _schema
    if _schema is None:
        _schema = GraphQLSchema()
    return _schema
