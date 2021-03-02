import RPi.GPIO as IO
import time
import pymongo
from pymongo import MongoClient
cluster = MongoClient("mongodb://m001-student:m001-student@sandbox-shard-00-00-4hc82.mongodb.net:27017,sandbox-shard-00-01-4hc82.mongodb.net:27017,sandbox-shard-00-02-4hc82.mongodb.net:27017/test?ssl=true&replicaSet=Sandbox-shard-0&authSource=admin&retryWrites=true&w=majority")
db = cluster["integra"]
collection = db["posts"]
IO.setwarnings(False)
IO.setmode(IO.BCM)
x = 0 
IO.setup(2,IO.OUT) #GPIO 2 -> Red LED as output
IO.setup(3,IO.OUT) #GPIO 3 -> Green LED as output
IO.setup(14,IO.IN) #GPIO 14 -> IR sensor as input
try:
    while 1:
        if(IO.input(14)==True): #object is far away
            IO.output(2,True) #Red led ON
            IO.output(3,False) # Green led OFF
        if(IO.input(14)==False): #object is near
            IO.output(3,True) #Green led ON
            IO.output(2,False) # Red led OFF
            x = (x + 1)
            print (x)
            time.sleep(1)
            post = { "Cantidad": str(x)}
            collection.insert_one(post)
except Exception as e:
    print(e)