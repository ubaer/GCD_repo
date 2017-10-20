from pyspark import SparkContext, SparkConf

conf = SparkConf().setAppName('').setMaster('local')
sc = SparkContext(conf=conf)
to_find = '10.99.99.186'


def find_string(s):
    return s.find(to_find) >= 0


count = sc.textFile("GCD-Week-6-access_log.txt").filter(find_string).count()

print(count)
