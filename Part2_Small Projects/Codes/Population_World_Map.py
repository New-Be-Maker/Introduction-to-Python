import json
import pygal
from pygal_maps_world.i18n import COUNTRIES
from pygal_maps_world.maps import World
from pygal.style import RotateStyle
from pygal.style import LightColorizedStyle
"""
the json file Country Code is different from pygal_maps_world.maps.
We need to adapt them. this function is for Line 25-33.
"""
def get_country_code(country_name):
	for code, name in COUNTRIES.items():
			if name == country_name:
				return code
	return None #Why indent like this? why not else?[I tried, report bug]
"""
1.check json file, which contains a lot of dictionaries as elment.
2.each dictionary has 4 keys.
3.jason.load is to tranfer json into a format Python can use.
"""
with open('D:\population_data.json') as f:
	pop_data = json.load(f)
	
#This dictionary is for later usage.
cc_population = {}	
for pop_dict in pop_data:
	if pop_dict['Year'] == '2010':
		country_name = pop_dict['Country Name']
		population = int(float(pop_dict['Value']))
		code = get_country_code(country_name)
		if code:
			cc_population[code] = population
		else:
			print('ERROR - ' + country_name)
			
cc_pop1,cc_pop2,cc_pop3 = {},{},{}

for cc,pop in cc_population.items():
	if pop < 10000000:
		cc_pop1[cc] = pop
	elif pop < 1000000000:
		cc_pop2[cc] = pop
	else:
		cc_pop3[cc] = pop
print(len(cc_pop1),len(cc_pop2),len(cc_pop3))

#Draw graphy. Codes from Pygal. 

wm_style = pygal.style.RotateStyle('#3399AA',\
 base_style=pygal.style.LightColorizedStyle)
wm = pygal.maps.world.World(style=wm_style)
wm.title = "World Population in 2010,by Country"

wm.add('0-10m', cc_pop1)
wm.add('10-1bn', cc_pop2)
wm.add('>1bn', cc_pop3)
wm.render_to_file('world_population.svg')				

		
		
	    
		
	
