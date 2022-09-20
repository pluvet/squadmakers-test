from elasticsearch import Elasticsearch, exceptions
from source.infraestructure.env import ES_HOST_URL

es = Elasticsearch(hosts=[ES_HOST_URL])
