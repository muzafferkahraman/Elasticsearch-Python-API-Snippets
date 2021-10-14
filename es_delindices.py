from elasticsearch import Elasticsearch as ES
import json
es=ES(['124.252.253.240:9200'])
s="index='nuage_vport_qos-2021-02-15', ignore=[400, 404]"
es.indices.delete(s)

