from elasticsearch import Elasticsearch as ES 
import json
es=ES(['124.252.253.124:9200'])
res=es.snapshot.get(repository='backup', snapshot='muzo2')
snapshot=res["snapshots"][0]["snapshot"]
indices=res["snapshots"][0]["indices"]
print(snapshot)
print("----------------------------")
for indice in indices:
 print(indice)






