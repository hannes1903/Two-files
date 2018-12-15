#def main():
 #   f = open("firstfile.txt", "w+")
  #  for i in range(10):
   #     f.write("This is line %d\r\n" % (i + 1))
    #f.close()

import random

f = open ('fileone.txt', 'w')

for i in range(int(input('how many to generate?: '))):
    line = str(random.randint(1, 10)) + "\n"
    f.write(line)
    print(line)

f.close()

f = open ('filetwo.txt', 'w')

for i in range(int(input('how many to generate?: '))):
    line = str(random.randint(1, 10)) + "\n"
    f.write(line)
    print(line)

f.close()

with open('fileone.txt','r') as masterdata:
    with open('filetwo.txt','r') as useddata:
        with open(r'only_in_fileone.txt','w+') as Newdata:
            usedfile = [ x.strip('\n') for x in list(useddata) ] #1
            masterfile = [ x.strip('\n') for x in list(masterdata) ] #2

            for line in masterfile: #3
                if line not in usedfile: #4
                    Newdata.write(line + '\n') #5

with open('fileone.txt','r') as masterdata:
    with open('filetwo.txt','r') as useddata:
        with open(r'in_both_files.txt','w+') as Newdata:
            usedfile = [ x.strip('\n') for x in list(useddata) ] #1
            masterfile = [ x.strip('\n') for x in list(masterdata) ] #2

            for line in masterfile: #3
                if line in usedfile: #4
                    Newdata.write(line + '\n') #5

with open('fileone.txt','r') as masterdata:
    with open('filetwo.txt','r') as useddata:
        with open(r'new_in_filetwo.txt','w+') as Newdata:
            usedfile = [ x.strip('\n') for x in list(useddata) ] #1
            masterfile = [ x.strip('\n') for x in list(masterdata) ] #2

            for line in usedfile: #3
                if line not in masterfile: #4
                    Newdata.write(line + '\n') #5