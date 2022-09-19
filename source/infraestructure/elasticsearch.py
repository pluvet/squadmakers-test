from elasticsearch import AsyncElasticsearch
from source.infraestructure.env import ES_HOST_URL

es = AsyncElasticsearch(hosts=ES_HOST_URL)

