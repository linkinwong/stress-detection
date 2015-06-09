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
dicAll = {}
idfCount = {}
count = 1
for i in range(6,13): #number of people 8(male1-9) (female 6-13)
        for j in range(1,13): #number of questions 12
		print i
		print j
		dirc = '/home/nico/Linguisitic/Female/'
		name = 'EngFemale'+num3_0str(i)+num2_0str(j)
#		dirc = '/home/nico/Linguisitic/Male/'
#		name = 'EngMale'+num3_0str(i)+num2_0str(j)
                os.chdir(dirc)
		f = open(name+'.dicPos', 'r')
		lines =f.readlines()
		x=[]
		for a in lines:
	     		x.append(a.strip())
		dic = {}
		temp = []

		for ii in range(1,len(x)):
			temp = x[ii].split("\t")
			dic[temp[1]]=int(temp[0])
		if count == 1:
			for key in dic.iterkeys():
				dicAll[key]= dic[key]
		else:
			for key in dic.iterkeys():
				if dicAll.has_key(key):
					dicAll[key] = dic[key] + dicAll[key]
				else:
					dicAll[key] = dic[key]
		count = count +1
		f.close()
					
sorted_dic = sorted(dicAll.iteritems(), key=operator.itemgetter(1))
fileDic = open("/home/nico/Linguisitic/Female/EngFemale.posAll", "w")
#fileDic = open("/home/nico/Linguisitic/Male/EngMale.posAll", "w")
for x in range(1,len(sorted_dic)):
	fileDic.write(str(sorted_dic[len(sorted_dic)-x][1])+'\t'+ sorted_dic[len(sorted_dic)-x][0]+'\n')
fileDic.close()


# word count & TFIDF for each answer
for i in range(6,13): #number of people 8
        for j in range(1,13): #number of questions 12
		print i
		print j
		dirc = '/home/nico/Linguisitic/Female/'
		name = 'EngFemale'+num3_0str(i)+num2_0str(j)
#		dirc = '/home/nico/Linguisitic/Male/'
#		name = 'EngMale'+num3_0str(i)+num2_0str(j)
                os.chdir(dirc)
		f = open(name+'.dicPos', 'r')
		lines =f.readlines()
		x=[]
		for a in lines:
	     		x.append(a.strip())
		dic = {}
		temp = []

		for ii in range(1,len(x)):
			temp = x[ii].split("\t")
			dic[temp[1]]=int(temp[0])

		dicOne={}
		for key in dicAll.iterkeys():
			if dic.has_key(key):
				dicOne[key]= dic[key]
			else:
				dicOne[key]= 0
#		fileDic = open("/home/nico/Linguisitic/Male/EngMale"+num3_0str(i)+num2_0str(j)+'.posCount', "w")
		fileDic = open("/home/nico/Linguisitic/Female/EngFemale"+num3_0str(i)+num2_0str(j)+'.posCount', "w")
		for key in dicOne.iterkeys():
			fileDic.write(str(dicOne[key])+'\t'+ key +'\n')
		fileDic.close()




		#os.system('./SMILExtract -C ../config/change384.conf -I ../../'+direc +sDir+'/' + listName[k]+  ' -O CanMale1-12-384_'+split +'s.arff')

