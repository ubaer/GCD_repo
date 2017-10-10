import glob
import mincemeat
import re
import stopwords
import string
import time
import os
from threading import Timer

def file_contents(file_name):
    f = open(file_name)
    try:
        print('reading:' + file_name)
        return f.read()
    finally:
        f.close()

def mapfn(k, v):
    for w in v.split():
        yield w, 1

def reducefn(k, vs):
    result = 0
    for v in vs:
        result += v
    return result

def start_client():
    os.system('startclients.bat')

start_time = time.time()

all_files = glob.glob('Gutenberg Small/*.*')
datasource = dict((file_name, file_contents(file_name)) for file_name in all_files)

# The reason I filter hyphens here is so I can have a real word count.
# If you filter out words that contain a hyphen in the filter part, you won't get the real word count.
# example:'car.' because it is the last word of the sentence will not be removed but become 'car' and thus gets counted.
for key, value in datasource.items():
    i = re.sub(r'[^\w\s]', '', value)
    datasource[key] = i

#exec(open("mincemeat.py -p", 'supersafe', 'localhost').read())

s = mincemeat.Server()
s.datasource = datasource
s.mapfn = mapfn
s.reducefn = reducefn

t = Timer(0.1, start_client)
t.start()

# changed the password to a supersafe password
results = s.run_server(password="supersafe")

# Dictionary of all the words that have to be filtered
filter_words = {}
filter_words.update(stopwords.allStopWords)
filter_words.update(dict.fromkeys(string.ascii_lowercase, 1)) # We only need lowercase because in the removal phase we compare with lowercase only

# Remove stopwords
results = {key: value for key, value in results.items() if str(key).lower() not in filter_words}
# sort results from high to low
results = sorted(results.items(), key=lambda x: x[1], reverse=True)

i = open('outfile', 'w')
i.write(str(results))
i.close()

print("--- %s seconds ---" % (time.time() - start_time))