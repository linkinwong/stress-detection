def num3_0str(num):
        if num < 10:
                return '00' + str(num)
        elif (num < 100):
                return '0' + str(num)
        else:
                return str(num)

def num2_0str(num):
        if num < 10:
                return '0' + str(num)
        else:
                return str(num)

import os
import sys
import math
import operator
wordAll = []
idfAll = []
count = 0
wordN_Male = 1066
wordN_Female = 987
posN = 39

ccc= posN

#r = 8*12 #male
r = 5*12 #female

temp = []
for ii in range(r):temp.append([0]*ccc)
#for i in range(1,9): #number of people 8(male1-9) (female 6-13)
for i in range(8,13): #number of people 8(male1-9) (female 6-13)
        for j in range(1,13): #number of questions 12
		print i
		print j
		dirc = '/home/nico/Linguisitic/Female/'
		name = 'EngFemale'+num3_0str(i)+num2_0str(j)
#		dirc = '/home/nico/Linguisitic/Male/'
#		name = 'EngMale'+num3_0str(i)+num2_0str(j)
                os.chdir(dirc)
#		f = open(name+'.wordCount', 'r')
#		f = open(name+'.tfidf', 'r')
		f = open(name+'.posCount', 'r')
		lines =f.readlines()
		x=[]
		for a in lines:
	     		x.append(a.strip())
		
		for ii in range(1,len(x)):
			aa = x[ii].split("\t")	
			temp[count][ii-1]= int(aa[0])
		count = count +1
		f.close()

#fileAll = open('/home/nico/Linguisitic/Male/EngMale1-8.wordCount', "w")
#fileAll = open('/home/nico/Linguisitic/Male/EngMale1-8.tfidf', "w")
#fileAll = open('/home/nico/Linguisitic/Male/EngMale1-8.posCount', "w")

#fileAll = open('/home/nico/Linguisitic/Female/EngFemale6-10.wordCount', "w")
#fileAll = open('/home/nico/Linguisitic/Female/EngFemale6-10.tfidf', "w")
fileAll = open('/home/nico/Linguisitic/Female/EngFemale6-10.posCount', "w")
for i in range(0,r):
	for j in range(0,ccc):
		fileAll.write(str(temp[i][j])+'\t')
	fileAll.write('\n')
fileAll.close()

					

