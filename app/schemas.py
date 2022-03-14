from xmlrpc.client import DateTime, _datetime_type
from pyspark.sql.types import *
users = StructType([
    StructField("index", IntegerType(), True),
    StructField("id", IntegerType(), True),
    StructField("age", IntegerType(), True),
    StructField("birthdate", StringType(), True),
    StructField("city", StringType(), True),
    StructField("created_at", TimestampType(), True),
    StructField("sex", StringType(), True),
    StructField("lat", DoubleType(), True),
    StructField("long", DoubleType(), True),
    StructField("password", StringType(), True),
    StructField("utm_source", StringType(), True),
    StructField("utm_medium", StringType(), True),
    StructField("utm_campaign", StringType(), True),
    StructField("firstname", StringType(), True),
    StructField("lastname", StringType(), True),
    StructField("useragent", StringType(), True),
    StructField("misc", StringType(), True),
    ])

ads = StructType([
  StructField("index", IntegerType(), True),
  StructField("owner_id", IntegerType(), True),
  StructField("title", StringType(), True),
  StructField("category", StringType(), True),
  StructField("price", DoubleType(), True),
  StructField("city", StringType(), True),
  StructField("created_at", TimestampType(), True),
  StructField("deleted_at", TimestampType(), True),
  StructField("id", IntegerType(), True),
])

referrals = StructType([
  StructField("id", IntegerType(), True),
  StructField("referrer_user_id", IntegerType(), True),
  StructField("referree_user_id", IntegerType(), True),
  StructField("created_at", TimestampType(), True),
  StructField("deleted_at", TimestampType(), True),
])

ads_transaction = StructType([
  StructField("id", IntegerType(), True),
  StructField("ad_ownerid", IntegerType(), True),
  StructField("buyer_user_id", IntegerType(), True),
  StructField("ad_id", IntegerType(), True),
  StructField("sold_price", DoubleType(), True),
  StructField("created_at", TimestampType(), True),
])