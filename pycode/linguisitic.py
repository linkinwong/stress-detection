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
#direc = '/home/nico/Desktop/Transcriptions/Female_Lamusia/'
direc = '/home/nico/Desktop/Transcriptions/Male_Shabab_Perry/'
for i in range(1,9): #number of people 8
        for j in range(1,13): #number of questions 12
		print i
		print j
                os.chdir(direc+str(i)+'/')
		f = open(str(j)+'.tdf', 'r')
		lines =f.readlines()
		last_line = lines[-1]
		transcription = last_line.split("\t")[7]
		doubleDashFree = transcription.replace('--',' -- ')
		a = doubleDashFree.replace('  ',' ')
		#file = open("/home/nico/Linguisitic/Female/EngFemale"+num3_0str(i)+num2_0str(j)+'.dataOri', "w")
		file = open("/home/nico/Linguisitic/Male/EngMale"+num3_0str(i)+num2_0str(j)+'.dataOri', "w")
                file.write(a)
		file.close()
		commanFree = doubleDashFree.replace(',',' ,')
		periodFree = commanFree.replace('.',' .')
		questionFree = periodFree.replace('?',' ?')
		a = questionFree.replace('  ',' ')
		b = a.replace(' ','\n')
		#file = open("/home/nico/Linguisitic/Female/EngFemale"+num3_0str(i)+num2_0str(j)+'.data', "w")
		file = open("/home/nico/Linguisitic/Male/EngMale"+num3_0str(i)+num2_0str(j)+'.data', "w")
                file.write(b)
		file.close()
		#create a dictionary
		d = b.split("\n")
		dic = {}
		for word in d:
			if dic.has_key(word):
				dic[word] = dic[word]+1
			else:
				dic[word] = 1
		sorted_dic = sorted(dic.iteritems(), key=operator.itemgetter(1))
	#	fileDic = open("/home/nico/Linguisitic/Female/EngFemale"+num3_0str(i)+num2_0str(j)+'.dic', "w")
		fileDic = open("/home/nico/Linguisitic/Male/EngMale"+num3_0str(i)+num2_0str(j)+'.dic', "w")
		for x in range(1,len(sorted_dic)):
#		for item in sorted_dic:
#			fileDic.write(str(item[1])+'\t'+ item[0]+'\n')
			fileDic.write(str(sorted_dic[len(sorted_dic)-x][1])+'\t'+ sorted_dic[len(sorted_dic)-x][0]+'\n')
		fileDic.close()

#		for item in sorted_dic.iteritems():
#			fileDic.write(str(item[1])+'\t'+ item[0]+'\n')
#		fileDic.close()

		
#for key in dic.iterkeys():
#	if dic1.has_key(key):
#		dic[key] = dic[key] + dic1[key]

#for key in dic1.iterkeys():
#	if not dic.has_key(key):
#		dic[key] = dic1[key]


		#os.system('./SMILExtract -C ../config/change384.conf -I ../../'+direc +sDir+'/' + listName[k]+  ' -O CanMale1-12-384_'+split +'s.arff')

