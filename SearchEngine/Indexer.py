from elasticsearch import Elasticsearch
from SearchEngine import DocumentReader

doc_reader = DocumentReader.DocumentReader()
doc_reader.load_docs()
docs = doc_reader.documents

es = Elasticsearch()

count = 0
for key in docs:
    body = docs[key]
    es_id = key

    response = es.index(index="test-research", doc_type='research_paper', id=es_id, body=body)
    # print(response['result'])
    count += 1
    if count % 25 == 0:
        print(response['result'])

print(count)
es.indices.refresh(index="test-research")



