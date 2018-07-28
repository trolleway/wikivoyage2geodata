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




names.append('Культурное наследие России/Москва/Центральный округ/Кремль')
names.append('Культурное наследие России/Москва/Центральный округ/Красная площадь и Китай-город')
names.append('Культурное наследие России/Москва/Центральный округ/Полукольцо центральных площадей')
names.append('Культурное наследие России/Москва/Центральный округ/От Пречистенской наб. до Воздвиженки')
names.append('Культурное наследие России/Москва/Центральный округ/От Воздвиженки до Тверской')
names.append('Культурное наследие России/Москва/Центральный округ/От Тверской до Бол. Лубянки')
names.append('Культурное наследие России/Москва/Центральный округ/От Бол. Лубянки до Маросейки и Покровки')
names.append('Культурное наследие России/Москва/Центральный округ/От Маросейки и Покровки до Москворецкой наб.')
names.append('Культурное наследие России/Москва/Центральный округ/Бульварное кольцо')
names.append('Культурное наследие России/Москва/Центральный округ/Остров')
names.append('Культурное наследие России/Москва/Центральный округ/От Пятницкой до Озерковской наб.')
names.append('Культурное наследие России/Москва/Центральный округ/От Бол. Полянки до Пятницкой')
names.append('Культурное наследие России/Москва/Центральный округ/От Крымской и Якиманской наб. до Бол. Полянки')
names.append('Культурное наследие России/Москва/Центральный округ/От Пречистенской наб. до Пречистенки')
names.append('Культурное наследие России/Москва/Центральный округ/От Пречистенки до Нового Арбата')
names.append('Культурное наследие России/Москва/Центральный округ/От Нового Арбата до Мал. Никитской')
names.append('Культурное наследие России/Москва/Центральный округ/От Мал. Никитской до Тверской')
names.append('Культурное наследие России/Москва/Центральный округ/Тверская и 1-я Тверская-Ямская')
names.append('Культурное наследие России/Москва/Центральный округ/От Тверской до Цветного бульв.')
names.append('Культурное наследие России/Москва/Центральный округ/От Цветного бульв. до просп. Сахарова')
names.append('Культурное наследие России/Москва/Центральный округ/От просп. Сахарова до Покровки')
names.append('Культурное наследие России/Москва/Центральный округ/От Покровки до Серебрянической наб.')
names.append('Культурное наследие России/Москва/Центральный округ/От Берниковской наб. до Котельнической и Гончарной наб.')
names.append('Культурное наследие России/Москва/Центральный округ/Садовое кольцо')
names.append('Культурное наследие России/Москва/Центральный округ/За Садовым кольцом от Пушкинской до Шлюзовой наб.')
names.append('Культурное наследие России/Москва/Центральный округ/От Садов. кольца до Фрунзенск., Лужнецк., Новодев., Саввинск., Ростов. и Смолен. наб.')
names.append('Культурное наследие России/Москва/Центральный округ/Новодевичий монастырь')
names.append('Культурное наследие России/Москва/Центральный округ/Новодевичье кладбище (до 1946)')
names.append('Культурное наследие России/Москва/Центральный округ/Новодевичье кладбище (после 1946)')
names.append('Культурное наследие России/Москва/Центральный округ/За Садовым кольцом от Краснопресненской наб. до 1-й Тверской-Ямской')
names.append('Культурное наследие России/Москва/Центральный округ/Ваганьковское кладбище')
names.append('Культурное наследие России/Москва/Центральный округ/За Садовым кольцом от 1-й Тверской-Ямской до просп. Мира')
names.append('Культурное наследие России/Москва/Центральный округ/За Садовым кольцом от просп. Мира до Стар. Басманной и Спартаковской ул.')
names.append('Культурное наследие России/Москва/Центральный округ/За Садовым кольцом от Стар. Басманной и Спартаковской ул. до Яузы')
names.append('Культурное наследие России/Москва/Центральный округ/За Садовым кольцом от Яузы до набережной Москвы-реки')

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
	else:
		monumentdata['name'] = 'NULL'


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
	if monumentdata['photographed']==0 or monumentdata['photographed']==1: 
		print monumentdata['name'],' ',monumentdata['address']	
		writer.writerow(row)

#generate vrt

txt='''<OGRVRTDataSource>
    <OGRVRTLayer name="'''+csvFileName+'''">
        <LayerSRS>WGS84</LayerSRS>
        <SrcDataSource>'''+csvFileName+'''.csv</SrcDataSource>
        <GeometryType>wkbPoint</GeometryType>
        <GeometryField encoding="PointFromColumns" x="Lon" y="Lat"/>
    </OGRVRTLayer>
</OGRVRTDataSource>'''
text_file = open(csvFileName+".vrt", "w")
text_file.write(txt)
text_file.close()

#convert to geojson using ogr2ogr

command='ogr2ogr -f "GeoJSON" '+csvFileName+'.geojson '+csvFileName+'.vrt'
print command
os.system(command)
