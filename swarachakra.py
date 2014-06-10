#!/usr/bin/python

lang = 'telugu'

f = open('telugu.csv', 'r')
t = open('template.txt', 'r')
c = open('chakra.txt', 'r')
o = open('MainLanguage.java', 'w')

lines = f.readlines()
template = t.read()
chakra = c.read()

f.close()
t.close()
c.close()

halantExists = 'true'
halantEnd = '35'

def getShowChakra(v):
	if v == '0':
		return 'false'
	return 'true'

def getShowCustomChakra(v):
	if v == '0' or v == '1' :
		return 'false'
	return 'true'

def getCustomChakraLayout(v):
	if v == '0' or v == '1':
		return ''
	array = v.split(' ')
	text = ''
	for s in array:
		text += '"' + s + '"' + ','
	return text[:-1]

def getShowIcon(v):
	if v == '0':
		return 'false'
	return 'true'

def getIcon(v):
	if v == '0' :
		return ''
	return v

def getChangeLayout(v):
	if v == '0\n':
		return 'false'
	return 'true'

def getLayout(v):
	if v == '0\n':
		return ''
	return v

keys = ''

i = 0

for line in lines:
	array = line.split(',')

	keys += 'KeyAttr myKey' + str(i) + ' = new KeyAttr();' + '\n'
	keys += '	myKey' + str(i) + '.code = ' + array[0] + ';' + '\n'
	keys += '	myKey' + str(i) + '.label = "' + array[1] + '" ;' + '\n'
	keys += '	myKey' + str(i) + '.showChakra = ' + getShowChakra(array[2]) + ' ;' + '\n'
	keys += '	myKey' + str(i) + '.showCustomChakra = ' + getShowCustomChakra(array[2]) + ' ;' + '\n'
	keys += '	myKey' + str(i) + '.customChakraLayout = new String[] {' + getCustomChakraLayout(array[2]) + '} ;' + '\n'
	keys += '	myKey' + str(i) + '.showIcon = ' + getShowIcon(array[3]) + ' ;' + '\n'
	keys += '	myKey' + str(i) + '.icon = "' + getIcon(array[3]) + '";' + '\n'
	keys += '	myKey' + str(i) + '.changeLayout = ' + getChangeLayout(array[4]) + ' ;' '\n'
	keys += '	myKey' + str(i) + '.layout = "' + getLayout(array[4]) + '";' + '\n'
	keys += '	myKey.set(' + str(i) + ', myKey' + str(i) + ');' + '\n' + '\n'

	i = i + 1

output = template.replace('LANGUAGE_NAME', lang)
output = output.replace('ALL_KEYS', keys)
output = output.replace('N_KEYS', str(i))
output = output.replace('DEFAULT_CHAKRA', chakra)
output = output.replace('HALANT_EXISTS', halantExists)
output = output.replace('HALANT_END', halantEnd)

o.write(output)

o.close()
