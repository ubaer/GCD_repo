from operator import add

from pyspark import SparkContext, SparkConf

conf = SparkConf().setAppName('').setMaster('local').set("spark.executor.memory", "8g")
sc = SparkContext(conf=conf)
folder = 'wordcount/*'


def word_count(topAmount):
    count = sc.textFile(folder) \
        .map(lambda x: x.replace(',', ' ').replace('.', ' ').replace('-', ' ').replace('\"', ' ').lower()) \
        .flatMap(lambda x: x.split()) \
        .map(lambda x: (x, 1)) \
        .reduceByKey(add) \
        .map(lambda x: (x[1], x[0])) \
        .sortByKey(False)
    return count.take(topAmount)


print(word_count(20))
