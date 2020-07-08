# -*- coding: utf-8 -*-
"""
Created on Tue Jul  7 07:00:47 2020

In this module we will read the IMDB data set and read it in a spark dataframe
and save it back for future use
@author: arko.das
"""

# import packages
import os
# spark packages
from pyspark.sql.types import *
from pyspark.sql.dataframe import *
from pyspark.context import SparkContext
from pyspark.sql.session import SparkSession


# Initate spark main funtion
try:
    sc = SparkContext('local')
    spark = SparkSession(sc)
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

# function to append data to empty 
def addElemToDF(input_data_path, input_df, comment_category = ""):
    total_file = len(os.listdir(input_data_path))
    i = 0
    for elem in os.listdir(input_data_path):
        reviewer_id = int(elem.split("_")[0])
        rating = int(elem.split("_")[1].split(".")[0])
        with open(os.path.join(input_data_path, elem), "r", encoding="utf8") as fo:
            for line in fo:
                line = line.strip("\n")
        input_df = input_df.unionAll(spark.createDataFrame([(reviewer_id, rating, line, comment_category)],schema))
        i = i + 1
        print(i, " out of ", total_file, " processed")
    return input_df


# get the training file location
train_pos_file_path = r"C:\Users\arko.das\PycharmProjects\dataByte\data\aclImdb\train\pos"
train_neg_file_path = r"C:\Users\arko.das\PycharmProjects\dataByte\data\aclImdb\train\neg"
test_pos_file_path = r"C:\Users\arko.das\PycharmProjects\dataByte\data\aclImdb\test\pos"
test_neg_file_path = r"C:\Users\arko.das\PycharmProjects\dataByte\data\aclImdb\test\neg"


training_df = addElemToDF(train_pos_file_path, training_df, comment_category = "positive")
#training_df = addElemToDF(train_neg_file_path, training_df, comment_category = "negative")
training_df.show()






