#!/usr/bin/env python
# -*- coding: utf-8 -*-

# anchor extraction from html document
import urllib2
import urlparse
import re
import csv
import time




import os
mergedListFileName='pages_temp.txt'
if os.path.exists(mergedListFileName):
    os.remove(mergedListFileName)
f = open(mergedListFileName, 'w')
#names=['Культурное_наследие_России/Москва/Центральный_округ/Арбат','Культурное_наследие_России/Москва/Центральный_округ/Басманный_район_(часть_1)','Культурное_наследие_России/Москва/Центральный_округ/Басманный_район_(часть_2)']

names=['Культурное_наследие_России/Москва/Центральный_округ/Арбат']


names.append('Культурное_наследие_России/Москва/Центральный_округ/Басманный_район_(часть_1)')
names.append('Культурное_наследие_России/Москва/Центральный_округ/Басманный_район_(часть_2)')
names.append('Культурное_наследие_России/Москва/Центральный_округ/Басманный_район_(часть_3)')
names.append('Культурное_наследие_России/Москва/Центральный_округ/Замоскворечье')
names.append('Культурное_наследие_России/Москва/Центральный_округ/Красносельский_район')
names.append('Культурное_наследие_России/Москва/Центральный_округ/Мещанский район')
names.append('Культурное_наследие_России/Москва/Центральный_округ/Пресненский_район_(часть_1)')
names.append('Культурное_наследие_России/Москва/Центральный_округ/Пресненский_район_(часть_2)')
names.append('Культурное_наследие_России/Москва/Центральный_округ/Таганский_район_(часть_1)')
names.append('Культурное_наследие_России/Москва/Центральный_округ/Таганский_район_(часть_2)')
names.append('Культурное_наследие_России/Москва/Центральный_округ/Тверской_район_(часть_1)')
names.append('Культурное_наследие_России/Москва/Центральный_округ/Тверской_район_(часть_2)')
names.append('Культурное_наследие_России/Москва/Центральный_округ/Кремль_и_Красная_площадь')
names.append('Культурное_наследие_России/Москва/Центральный_округ/Хамовнический_район_(часть_1)')
names.append('Культурное_наследие_России/Москва/Центральный_округ/Хамовнический_район_(часть_2)')
names.append('Культурное_наследие_России/Москва/Центральный_округ/Якиманка_(часть_1)')
names.append('Культурное_наследие_России/Москва/Центральный_округ/Якиманка_(часть_2)')

names.append('Культурное_наследие_России/Москва/Восточный_округ')
names.append('Культурное_наследие_России/Москва/Западный_округ')
names.append('Культурное_наследие_России/Москва/Северный_округ')
names.append('Культурное_наследие_России/Москва/Северный_округ/Посёлок_Сокол')
names.append('Культурное_наследие_России/Москва/Северо-восточный_округ')
names.append('Культурное_наследие_России/Москва/Северо-западный_округ')
names.append('Культурное_наследие_России/Москва/Юго-восточный_округ')
names.append('Культурное_наследие_России/Москва/Юго-западный_округ')
names.append('Культурное_наследие_России/Москва/Южный_округ')
names.append('Культурное_наследие_России/Москва/Северный_округ')



names.append('Культурное_наследие_России/Московская_область/Подольск')
names.append('Культурное_наследие_России/Московская_область/Подольский_район')
names.append('Культурное_наследие_России/Московская_область/Орехово-Зуево')
names.append('Культурное_наследие_России/Московская_область/Орехово-Зуевский_район')
names.append('Культурное_наследие_России/Московская_область/Щёлковский_район')
names.append('Культурное_наследие_России/Московская_область/Ногинск')
names.append('Культурное_наследие_России/Московская_область/Ногинский_район')
names.append('Культурное_наследие_России/Московская_область/Балашиха')
names.append('Культурное_наследие_России/Московская_область/Одинцовский_район')





for page in names:
	print page
	html=urllib2.urlopen('https://ru.wikivoyage.org/wiki/'+page+'?action=raw').read()
	f.write(html)
f.close()



pageName2='Москва/Южный_округ'
pageName='Культурное_наследие_России/'+pageName2

from time import gmtime, strftime

csvFileName='ZadrotContest_'+'_'+strftime("%Y-%m-%d-%H-%M-%S", gmtime())
writer = csv.writer(open(csvFileName+'.csv', 'w'))
writer.writerow(['lat','lon','photographed','name','address'])


#html=urllib2.urlopen('https://ru.wikivoyage.org/wiki/'+pageName+'?action=raw').read()
with open (mergedListFileName, "r") as myfile:
    html=myfile.read()

#print data1



p = re.compile(ur'{{monument (.+?)}}', re.MULTILINE | re.DOTALL)
test_str = html#.decode('utf-8')

for monument in re.findall(p, test_str):
	monumentdata = {}

	monumentdata['lat'] ='0'
	monumentdata['lon'] ='0'


	value=re.search('name=(.+?)\|',monument)
	if value:
		monumentdata['name'] = value.group(1).strip()


	pAddress = re.compile(ur'address=(.+?)\|', re.MULTILINE | re.DOTALL)
	value = re.search(pAddress, monument)
	if value:
		monumentdata['address'] = value.group(1).strip()


	pLat = re.compile(ur'lat=(.+?)\|', re.MULTILINE | re.DOTALL)
	value = re.search(pLat, monument)
	if value:
		monumentdata['lat'] = value.group(1).strip()

	pLon = re.compile(ur'long=(.+?)\|', re.MULTILINE | re.DOTALL)
	value = re.search(pLon, monument)
	if value:
		monumentdata['lon'] = value.group(1).strip()


	pImage = re.compile(ur'image=(.+?)\|', re.MULTILINE | re.DOTALL)
	value = re.search(pImage, monument)
	if value:
		monumentdata['image'] = value.group(1).strip()


	pCommonscat = re.compile(ur'commonscat=(.+?)\|', re.MULTILINE | re.DOTALL)
	value = re.search(pCommonscat, monument)
	if value:
		monumentdata['commonscat'] = value.group(1).strip()


	if monumentdata['image'] or monumentdata['commonscat']:
		monumentdata['photographed']=1
	else:
		monumentdata['photographed']=0

	#print monumentdata['name']
	#print monumentdata['address']
	#print monumentdata['lat']
	#print monumentdata['lon']
	#print monumentdata['image']
	#print monumentdata['commonscat']
	#print monumentdata['photographed']


	row=monumentdata['lat'],monumentdata['lon'],monumentdata['photographed'],monumentdata['name'],monumentdata['address']
	if monumentdata['photographed']==0: 
		print monumentdata['name'],' ',monumentdata['address']	
		writer.writerow(row)


#print html

quit()

