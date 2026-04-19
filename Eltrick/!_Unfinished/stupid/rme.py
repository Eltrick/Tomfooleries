from time import time

start=time()
m=[49,46,36,43,22,45]
r=[14,41,13,37,9,13]

a=0
while a%49!=14 or a%46!=41 or a%36!=13 or a%43!=37 or a%22 !=9 or a%45!=13:
    a += 1
print(a)
print(time()-start)