
import csv
z = 0
p = 0
my_list1 = []
my_list2 = []
fname = 'file.txt'
ryadky = []
fd = open(fname, 'r', encoding='utf8')
ryadky=fd.readlines()
fd.close()
for elem in ryadky:
    z=z+len(elem)
    p=p+elem.count(" ")
    slova=elem.split(" ")
    my_list1.append(slova)
print('p=', p)
print('sym=', z)
L1=len(my_list1)
L2=0
words_all=0
words_uniq=0
for i in range(L1):
    elem=my_list2
    words_all=words_all+1
    if elem in my_list2:
        continue
    else:
        my_list2.append(elem)
#print(my_list2)
L1=len(my_list2)
for i in range (L1):
    elem=my_list2[i]
    zriz=elem[-2:]
    if zriz=="\n":
        my_list2[i]=elem[0:-2]
        #print(zriz)
words_uniq=len(my_list2)
print(my_list2)
print('all_words=', words_all)
print('unique words=',words_uniq)
