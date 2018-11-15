#coding:utf-8
import random
from collections import Counter
from operator import itemgetter


class count:
    def __init__(self,count):
        #self.item = item
        self.count = count
        self.i = 0

    def show(item):
        return item.count

    def add(item):
        item.i = item.i + 1
        return item.i


def get_items(array):
    item = []
    for i in range(len(array)):
        item.append(array[i][1])
    return item

name_file = open('./voc.names')
html_file = open('./dummy.html','w')
line = name_file.readline()
names = []
results = []

html_file.write('<!DOCTYPE html><html><head><meta charset="UTF-8"><script language="JavaScript" type="text/javascript">function Checkvalues(){var str="<h4>Result</h4>";for (var i=0; i<document.contactform.item.length; i++){if (document.contactform.item[i].checked) {str += document.contactform.item[i].value;str += "<br>";}}document.write(str);}</script></head><title>Dummy result</title><body>This is a test page.<form name="contactform" action="#" method="GET"><ul>')


while line:
	names.append(line.strip())
	line = name_file.readline()

for i in range(random.randrange(30,40)):    #
    results.append([random.randrange(1,13),names[random.randrange(len(names))]])

#print(results)

results_sort_direc = sorted(results)
print(results_sort_direc)

counter = Counter(get_items(results))

for word, cnt in counter.most_common():
    #print(word, cnt)
    exec("%s = count(%d)" % (word , cnt))

    #name = count(word,cnt)
#print(name.show())

for i in range(1,13):
    head = False
    for direc, item in results_sort_direc:
        if i == direc and head == False:
            html_file.write('<li><h4>' + str(direc) +'時方向</h4><input type="checkbox" name="item" value=' + item + '>' + item)
            head = True
            if(eval(item).show()>1):
                html_file.write(' (' + str(eval(item).add()) + ' of ' + str(eval(item).show()) + ')')
            html_file.write('<br>')
            #print(item,eval(item).show())
        elif i == direc :
            html_file.write('<input type="checkbox" name="item" value=' + item + '>' + item)
            if(eval(item).show()>1):
                html_file.write(' (' + str(eval(item).add()) + ' of ' + str(eval(item).show()) + ')')
            html_file.write('<br>')
            #print(item,eval(item).show())
    if head == True:
        html_file.write('</li>')


html_file.write('</ul><input type="button" value="submit" onclick="Checkvalues();"></form></body></html>')

name_file.close
html_file.close

print("Done")
