from pyspark import SparkContext, SparkConf
from pyspark.sql.context import SQLContext

from task1 import task1
from task2 import task2
from task3 import task3

def main():
    conf = SparkConf().setAppName("TDT4305 Assignment 1").setMaster("local")
    sc = SparkContext(conf=conf)
    sqlContext = SQLContext(sc)
    # Task 1
    posts, comments, users, badges = task1(sc)

    # Task 2
    task2(posts, comments, users, badges)

    # Task 3
    task3(posts, comments, users, sqlContext, sc)


if __name__ == "__main__":
    main()

