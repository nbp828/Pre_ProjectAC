from elasticsearch import Elasticsearch


class Searcher:

    def __init__(self):
        self.es = Elasticsearch()

    def search(self, query_body):
        response = self.es.search(index="test-research", body=query_body)
        print("Got %d Hits:" % response['hits']['total']['value'])
        return response

# res = es.search(index="test-index", body={"query": {"match_all": {}}})
# response = es.search(index="sw", body={"query": {"prefix": {"name": "lu"}}})

# response = es.search(index="test-index", body={"query": {"match": {'title': 'multilingual'}}})
# response = es.search(index="test-research", body=
# {"query":{"query_string": {"fields": ["title","abstract"],"query": "multilingual lexical"}}})
# res = es.search(index="sw", body={"query": {"match": {'name':'Darth Maul'}}})
# query_body = {"query":{"query_string": {"fields": ["title","abstract"],"query": "multilingual lexical"}}}

# query_body = {"query": {"match": {'title':'multilingual lexical', 'abstract': 'multilingual lexical'}}}


s = Searcher()
query_body = {"query":
                  {"query_string":
                       {"fields": ["title", "abstract", "introduction"]
                           , "query": "multilingual lexical"
                        }
                   }
              }

response = s.search(query_body)
for hit in response['hits']['hits']:
    print(hit["_id"])
    print(hit["_score"])
    print(hit["_source"]['title'])