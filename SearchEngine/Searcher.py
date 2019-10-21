from elasticsearch import Elasticsearch


class Searcher:

    def __init__(self):
        self.es = Elasticsearch()

    def search(self, query_body):
        response = self.es.search(index="test-research", body=query_body)
        print("Got %d Hits:" % response['hits']['total']['value'])
        return response


# s = Searcher()
# query_body = {"query":
#                   {"query_string":
#                        {"fields": ["title", "abstract", "introduction"]
#                            , "query": "multilingual lexical"
#                         }
#                    }
#               }
#
# response = s.search(query_body)
# for hit in response['hits']['hits']:
#     print(hit["_id"])
#     print(hit["_score"])
#     print(hit["_source"]['title'])