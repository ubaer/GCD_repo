import glob
all_files = glob.glob('Gutenberg Small/*.*')

def file_contents(file_name):
    f = open(file_name, encoding='utf8')
    try:
        return f.read()
    finally:
        f.close()
        return ""  # If we don't return anything here we have the risk of not returning anything if the codec does not work with some text which follows by the program crashing.

datasource = dict((file_name, file_contents(file_name)) for file_name in all_files)

results = []

#sort results from high to low
results = sorted(results.items(), key=lambda x: x[1], reverse=True)
#print results
i = open('outfile','w')
i.write(str(results))
i.close()
