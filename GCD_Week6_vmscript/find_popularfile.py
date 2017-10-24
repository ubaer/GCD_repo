from operator import add

from pyspark import SparkContext, SparkConf

conf = SparkConf().setAppName('').setMaster('local').set("spark.executor.memory", "8g")
sc = SparkContext(conf=conf)


def find_get(s):
    second = s[s.index("\"") + 1:].index("\"")
    return s[s.index("\"") + 1:][:second]


logData = sc.textFile("GCD-Week-6-access_log.txt").cache()
filteredData = logData.map(find_get)

counts = filteredData.map(lambda x: (x, 1)).reduceByKey(add)
output = counts.collect()

highest = ('', 0)
for (word, count) in output:
    if (highest[1] < count):
        highest = (word, count)

print(highest)
