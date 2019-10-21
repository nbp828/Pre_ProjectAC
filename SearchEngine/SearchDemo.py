from datetime import datetime
from elasticsearch import Elasticsearch

# doc_reader = DocumentReader.DocumentReader()
# doc_reader.load_docs()
# docs = doc_reader.documents

es = Elasticsearch()

doc = {
    'author': 'kimchy',
    'text': 'Elasticsearch: cool. bonsai cool.',
    'timestamp': datetime.now(),
}

res = es.index(index="test-index", doc_type='tweet', id="hello", body=doc)
print(res['result'])

res = es.get(index="test-index", doc_type='tweet', id="hello")
print(res['_source'])

es.indices.refresh(index="test-index")

res = es.search(index="test-index", body={"query": {"match_all": {}}})
# res = es.search(index="sw", body={"query": {"match": {'name':'Darth Vader'}}})
print("Got %d Hits:" % res['hits']['total']['value'])
for hit in res['hits']['hits']:
    print(hit["_id"])
    print(hit["_source"])

