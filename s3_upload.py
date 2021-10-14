import boto3
s3 = boto3.resource('s3')
filename="list"
bucketname="muzokahraman"
res=s3.meta.client.upload_file(filename, bucketname, filename)
print(res)

