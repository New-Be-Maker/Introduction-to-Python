# _*_ coding: utf-8 _*_

"""
Population world map
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

This exercise is from internet. Pygal is the module used in this exercise.
We will also have a better understanding of json file when we finish this exercise.

:Declaration: data and some code are open source from internet
:presenter: by Yifeng
"""

import json
import pygal
from pygal_maps_world.i18n import COUNTRIES
from pygal_maps_world.maps import World
from pygal.style import RotateStyle
from pygal.style import LightColorizedStyle

"""
 this function is for Line 25-33.
"""


def get_country_code(country_name):  # A solution?
    """
    Sometimes the country codes or country name in json file are different from them in COUNTRIES(from pygal module)
    So,before we start everything, we need to check them. And adapt them if it is necessary.
    It is better to print COUNTRIES.items() first to check the standard format.
    """
    for country_code, name in COUNTRIES.items():
        if name == country_name:
            return country_code
    # Still need to think about this.
    return None


with open('population_data.json') as f:
    pop_data = json.load(f)

# This dictionary is for later usage.
cc_population = {}
for pop_dict in pop_data:
    """
    Here the logic is that we want filter 'Year' and select what data will be used in the end.
    1.we want to use the value of population.
    2.we want to have the standard country codes that matches pygal requirement.
    """
    if pop_dict['Year'] == '2010':
        country_name = pop_dict['Country Name']
        population = int(float(pop_dict['Value']))
        country_code = get_country_code(country_name)
        if country_code:
            cc_population[country_code] = population
        else:
            print('ERROR - ' + country_name)

cc_pop1, cc_pop2, cc_pop3 = {}, {}, {}

for cc, pop in cc_population.items():
    if pop < 10000000:
        cc_pop1[cc] = pop
    elif pop < 1000000000:
        cc_pop2[cc] = pop
    else:
        cc_pop3[cc] = pop
print(len(cc_pop1), len(cc_pop2), len(cc_pop3))

# Set graph format and preferences
wm_style = pygal.style.RotateStyle('#336699', base_style=pygal.style.LightColorizedStyle)
world = World(style=wm_style)
wm = pygal.maps.world.World(style=wm_style)

# To set contents shown on the graph.
wm.title = "World Population in 2010,by Country"
wm.add('0-10m', cc_pop1)
wm.add('10-1bn', cc_pop2)
wm.add('>1bn', cc_pop3)
wm.render_to_file('world_population.svg')
		
	    
		
	
