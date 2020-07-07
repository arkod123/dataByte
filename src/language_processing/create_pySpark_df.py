# -*- coding: utf-8 -*-
"""
Created on Tue Jul  7 07:00:47 2020

In this module we will read the IMDB data set and read it in a spark dataframe
and save it back for future use
@author: arko.das
"""

# import packages
 
from pyspark.sql.types import *
from pyspark.sql.dataframe import *
from pyspark.context import SparkContext
from pyspark.sql.session import SparkSession

# Initate spark main funtion
try:
    sc = SparkContext('local')
except:
    sc = SparkContext.getOrCreate()
    spark = SparkSession(sc)

# define spark schema
schema = StructType([
        StructField("ID", IntegerType(), nullable=False),
        StructField("Rating", IntegerType()),
        StructField("comments", StringType()),
        StructField("comment_category", StringType())
        ])

training_df = spark.createDataFrame(sc.emptyRDD(), schema)
test_df = spark.createDataFrame(sc.emptyRDD(), schema)

training_df.printSchema()






