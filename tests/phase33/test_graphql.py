import pytest
from jarvis.core.graphql.resolver import GraphQLSchema, GraphQLType

def test_add_type():
    schema = GraphQLSchema()
    gql_type = GraphQLType("User")
    schema.add_type(gql_type)
    assert "User" in schema.types

def test_add_query_field():
    schema = GraphQLSchema()
    schema.add_query_field("getUser", "User", lambda: {})
    fields = schema.root_query.get_fields()
    assert "getUser" in fields

def test_schema_info():
    schema = GraphQLSchema()
    schema.add_query_field("field1", "Type", lambda: {})
    info = schema.get_schema_info()
    assert len(info["query_fields"]) > 0
