import boto3
s3 = boto3.resource('s3')
filename="list"
bucketname="muzokahraman"
res=s3.Object(bucketname, filename).delete()
print(res)

