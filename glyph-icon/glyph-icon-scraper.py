import requests
import json

#'https://raw.githubusercontent.com/google/material-design-icons/master/font/MaterialIcons-Regular.codepoints'
#'https://raw.githubusercontent.com/FortAwesome/Font-Awesome/master/metadata/icons.json'
MATERIALICONS = 'https://cdn.jsdelivr.net/gh/google/material-design-icons@master/font/MaterialIcons-Regular.codepoints'
FONTAWESOME = 'https://cdn.jsdelivr.net/gh/FortAwesome/Font-Awesome@master/metadata/icons.json'

# scrap material icons

try:
	r = requests.get(MATERIALICONS)
	if r.status_code == 200:
		codepoints = r.text.split('\n')
		output = ''
		for i in codepoints:
			code = i.split(' ')[0]
			if code != '':
				output += '"' + code + '",'
		output = output[:-1] # remove last ','
		with open('materialicons.txt', 'w') as f:
			f.write(output)
except:
	None

# scrap font awesome

try:
	r = requests.get(FONTAWESOME)
	if r.status_code == 200:
		codepoints = json.loads(r.text)
		output = ''
		for i in codepoints:
			if codepoints[i]['free'] == ['solid']: #choose free solid styles
				output += '"fas fa-' + i + '",'
		output = output[:-1] # remove last ','
		with open('fontawesome_free.txt', 'w') as f:
			f.write(output)
		output = ''
		for i in codepoints:
			if codepoints[i]['free'] == ['brands']: #choose free brands styles
				output += '"fab fa-' + i + '",'
		output = output[:-1] # remove last ','
		with open('fontawesome_brands.txt', 'w') as f:
			f.write(output)
except:
	None
