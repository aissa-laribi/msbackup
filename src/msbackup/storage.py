def local(infile, outfile):
    outfile.write(infile)

def s3(client, infile, bucket, file_name):
    client.upload_fileobj(infile, bucket, file_name)