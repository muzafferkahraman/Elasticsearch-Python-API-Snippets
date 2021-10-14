from elasticsearch import Elasticsearch as ES
f=open("/root/list","r")
es=ES(['124.252.253.124:9200'])
for s in f:
   s=s.rstrip("\n")
   print(s)   
   es.indices.delete(index=s, ignore=[400, 404])

