import os
from statistics import mode
import sys
import time
from datetime import datetime, timedelta
from app import schemas
from models.init import create_all
from pyspark.sql import SparkSession
from pyspark.sql import *
from pyspark.sql.types import *
from pyspark.sql.functions import *
import json

#time now 
now = datetime.utcnow()
# how old files can be read, for the moment its 24 hours 
howold = 24*3600
# my_dict is used map dat directory name with table name so as to write data into correct table.
my_dict = {'1': 'users', '2': 'ads', '3': 'ads_transaction', '4':'referrals'}
#engine = create_all()
#print("engine", engine)

## this function return if  your file is timedelta times old 
def is_file_older_than (file, delta): 
    cutoff = now - delta
    mtime = datetime.utcfromtimestamp(os.path.getmtime(file))
    if mtime < cutoff:
        return True
    return False
## this function reads all the files from the folders and insert the data.
def insert_data():
  engine = create_all()
  print("engine", engine) 

  staging_path = "./data/"
  filesSet = set()
  spark = SparkSession.builder.appName("insertData").config("spark.jars", "/Users/ishani/spark-2.4.4-bin-hadoop2.7/jars/postgresql-42.3.3.jar").getOrCreate()

  print("hello2")
  dictionary_df = {}

  for fdir in os.listdir(staging_path):
    print("dir", staging_path+fdir)
    for fname in os.listdir(staging_path+fdir):
      filePath = staging_path+fdir+"/"+fname

      ti_c = os.path.getctime(filePath)

      check_older = is_file_older_than(filePath, timedelta(hours=1))
      print("check", check_older)
      schema = getattr(schemas, my_dict.get(fdir))

      dictionary_df[fname] = spark.read.options(header='True', delimiter=',').schema(schema).csv(filePath)
      dictionary_df[fname].show()
      if my_dict.get(fdir) == "users":   
        dictionary_df[fname] = dictionary_df[fname].drop('index')

      dictionary_df[fname].write.format("jdbc").option("url", "jdbc:postgresql://localhost:5432/testgdc").option("driver","org.postgresql.Driver").option("dbtable",my_dict.get(fdir)).option("user", "postgres").option("password","password").option("stringtype","unspecified").mode('append').save()

  spark.close()
if __name__ == "__main__":
    insert_data()