import json
import pygal
from pygal_maps_world.i18n import COUNTRIES
from pygal_maps_world.maps import World
from pygal.style import RotateStyle
from pygal.style import LightColorizedStyle

def get_country_code(country_name):
	for code, name in COUNTRIES.items():
			if name == country_name:
				return code
	return None 
	
with open('D:\party_power.json') as f:
	power_data = json.load(f)
	
cc_power = {}
for power_dict in power_data:
	if power_dict['year'] == '2007' and power_dict['party_string'] == 'REP':
		power_index = float(power_dict['diflogrile'])
		country_name = power_dict['country_name']
		code = get_country_code(country_name)
		if code:
			cc_power[code] = power_index
		else:
			print('ERROR - ' + country_name)
		
		
		
cc_power1,cc_power2,cc_power3,cc_power4,cc_power5,cc_power6,cc_power7 = \
 {},{},{},{},{},{},{}

for cc,num in cc_power.items():
	if num < 0.25:
		cc_power1[cc] = num
	elif num < 0.5:
		cc_power2[cc] = num
	elif num < 0.75:
		cc_power3[cc] = num
	elif num < 1.0:
		cc_power4[cc] = num
	elif num < 1.5:
		cc_power5[cc] = num
	elif num < 2.0:
		cc_power6[cc] = num
	else:
		cc_power7[cc] = num
print(len(cc_power1),len(cc_power2),len(cc_power3),len(cc_power4),\
len(cc_power5),len(cc_power6),len(cc_power7))


wm_style = pygal.style.RotateStyle('#336699',\
 base_style=pygal.style.LightColorizedStyle)
wm = pygal.maps.world.World(style=wm_style)
wm.title = "Republicans 2007"
wm.add('None',{})
wm.add('0-0.25', cc_power1)
wm.add('0.25-0.5', cc_power2)
wm.add('0.5-0.75', cc_power3)
wm.add('0.75-1.0', cc_power4)
wm.add('1.0-1.5', cc_power5)
wm.add('1.5-2.0', cc_power6)
wm.add('>2.0', cc_power7)
wm.render_to_file('Republicans 2007.svg')	
