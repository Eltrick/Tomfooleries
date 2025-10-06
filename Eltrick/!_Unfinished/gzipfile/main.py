import gzip

with open('ill logic lut compressed 4.txt', 'r') as file:
    data = file.read()
    with open('data.bin', 'wb') as output:
        output.write(gzip.compress(data.encode('utf-8')))