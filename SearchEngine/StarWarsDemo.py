import requests
import json
from elasticsearch import Elasticsearch

es = Elasticsearch([{'host': 'localhost', 'port': 9200}])

# r = requests.get('http://localhost:9200')
# i = 1
# while r.status_code == 200:
#     r = requests.get('http://swapi.co/api/people/' + str(i))
#     es.index(index='sw', doc_type='people', id=i, body=json.loads(r.content))
#     i = i + 1
#
#
# r = requests.get('http://localhost:9200')
# i = 18
# while r.status_code == 200:
#    r = requests.get('http://swapi.co/api/people/'+ str(i))
#    es.index(index='sw', doc_type='people', id=i, body=json.loads(r.content))
#    i=i+1


res = es.search(index="sw", body={"query": {"match": {'name':'Darth Maul'}}})
print("Got %d Hits:" % res['hits']['total']['value'])
for hit in res['hits']['hits']:
    print(hit["_id"])
    print(hit["_source"])
    # print("%(timestamp)s %(author)s: %(text)s" % hit["_source"])
