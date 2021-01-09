# _*_ coding: utf-8 _*_

"""
Party power distribution index
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

This exercise is similar to population world map. However, we need to deal with more problems in this
exercise. Some country names are not matched with pygal standard COUNTRIES。


:presenter: by Yifeng
"""

import json
import pygal
from pygal_maps_world.i18n import COUNTRIES
from pygal_maps_world.maps import World
from pygal.style import RotateStyle
from pygal.style import LightColorizedStyle


def get_country_code(country_name):
    """
     Sometimes the country codes or country name in json file are different from them in COUNTRIES(from pygal module)
     So,before we start everything, we need to check them. And adapt them if it is necessary.
     It is better to print COUNTRIES.items() first to check the standard format.
    """

    for country_code, name in COUNTRIES.items():
        if name == country_name:
            return country_code
    return None


with open('party_power.json') as f:
    power_data = json.load(f)

cc_power = {}
for power_dict in power_data:
    if power_dict['year'] == '2007' and power_dict['party_string'] == 'REP':
        power_index = float(power_dict['diflogrile'])
        country_name = power_dict['country_name']
        # why don't we use the countrycode2 in the data file directly?
        # It is 2 characters and align with pygal standard format.
        country_code = get_country_code(country_name)
        if country_code:
            cc_power[country_code] = power_index
        else:
            print('ERROR - ' + country_name)

cc_power1, cc_power2, cc_power3, cc_power4, cc_power5, cc_power6, cc_power7 = \
    {}, {}, {}, {}, {}, {}, {}

for cc, num in cc_power.items():
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
print(len(cc_power1), len(cc_power2), len(cc_power3), len(cc_power4), len(cc_power5), len(cc_power6), len(cc_power7))

wm_style = pygal.style.RotateStyle('#336699', base_style=pygal.style.LightColorizedStyle)
wm = pygal.maps.world.World(style=wm_style)

# To set the contents that we want to show in the graph.
wm.title = "Republicans 2007"
# How to set color for 'None'?
wm.add('None', {})
wm.add('0-0.25', cc_power1)
wm.add('0.25-0.5', cc_power2)
wm.add('0.5-0.75', cc_power3)
wm.add('0.75-1.0', cc_power4)
wm.add('1.0-1.5', cc_power5)
wm.add('1.5-2.0', cc_power6)
wm.add('>2.0', cc_power7)
wm.render_to_file('Republicans 2007.svg')

