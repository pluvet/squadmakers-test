import pytest
from elasticsearch import AsyncElasticsearch

@pytest.fixture
async def elasticsearch_database_connection():
    # For this test to work there must exist
    # an elasticsearch db listening on port localhost:9200

    es = AsyncElasticsearch('http://localhost:9200/', verify_certs=True)

    assert await es.ping()