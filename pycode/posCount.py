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
for i in range(6,13): #number of people 8
        for j in range(1,13): #number of questions 12
		print i
		print j
		dirc = '/home/nico/Linguisitic/Female/'
		name = 'EngFemale'+num3_0str(i)+num2_0str(j)
                os.chdir(dirc)
		f = open(name +'.pos', 'r')
		lines =f.readlines()
		x=[]
		for a in lines:
	     		x.append(a.strip())
		dic = {}
		for word in x:
			if dic.has_key(word):
				dic[word] = dic[word]+1
			else:
				dic[word] = 1
		sorted_dic = sorted(dic.iteritems(), key=operator.itemgetter(1))
		fileDic = open("/home/nico/Linguisitic/Female/" + name +'.dicPos', "w")
		for x in range(1,len(sorted_dic)):
			fileDic.write(str(sorted_dic[len(sorted_dic)-x][1])+'\t'+ sorted_dic[len(sorted_dic)-x][0]+'\n')
		fileDic.close()
		f.close()

		

for i in range(1,9): #number of people 8
        for j in range(1,13): #number of questions 12
		print i
		print j
		dirc = '/home/nico/Linguisitic/Male/'
		name = 'EngMale'+num3_0str(i)+num2_0str(j)
                os.chdir(dirc)
		f = open(name +'.pos', 'r')
		lines =f.readlines()
		x=[]
		for a in lines:
	     		x.append(a.strip())
		dic = {}
		for word in x:
			if dic.has_key(word):
				dic[word] = dic[word]+1
			else:
				dic[word] = 1
		sorted_dic = sorted(dic.iteritems(), key=operator.itemgetter(1))
		fileDic = open("/home/nico/Linguisitic/Male/" + name +'.dicPos', "w")
		for x in range(1,len(sorted_dic)):
			fileDic.write(str(sorted_dic[len(sorted_dic)-x][1])+'\t'+ sorted_dic[len(sorted_dic)-x][0]+'\n')
		fileDic.close()
		f.close()



