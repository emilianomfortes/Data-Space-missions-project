### --- Libraries --- ###
#Essentials
import numpy as np
import random
from datetime import datetime
from iso3166 import countries #iso codes for countries (DID WE USE THIS?)
import pycountry #list of countries, can be used simply with pycountry.countries (https://pypi.org/project/pycountry/)

#Data management
import pandas as pd
pd.set_option('display.max_colwidth', None)

#Sometimes Pandas will give a warning raise for valid operations 
#(see https://stackoverflow.com/questions/20625582/how-to-deal-with-settingwithcopywarning-in-pandas)
#The following script provides a simple workaround to disable them when so desired!
class ChainedAssignent:
    def __init__(self, chained=None):
        acceptable = [None, 'warn', 'raise']
        assert chained in acceptable, "chained must be in " + str(acceptable)
        self.swcw = chained

    def __enter__(self):
        self.saved_swcw = pd.options.mode.chained_assignment
        pd.options.mode.chained_assignment = self.swcw 
        return self

    def __exit__(self, *args):
        pd.options.mode.chained_assignment = self.saved_swcw

#Visualization
import matplotlib.pyplot as plt
import plotly.express as px
import plotly.graph_objects as go
import psutil

### --- Changed and leased countries --- ###
#More information regarding this can be seen in the colab notebook. Basically, since the beginning of the space race and up to date, countries have changed names or leased their territory to other country

changed_countries = {'russia':'russian federation',
                     'new mexico':'usa',
                     'yellow sea':'china',
                     'shahrud missile test site':'iran',
                     'pacific missile range facility':'usa',
                     'barents sea':'russian federation',
                     'gran canaria':'usa',
                     'algeria, france':'algeria',
                     'marshall islands, usa':'usa',
                     'french guiana, france':'french guiana',
                     'kiritimati':'republic of kiribati',}

# It is also important to take into consideration which country was in charge of the mission 
leased_countries = {'russia':'russian federation',
                     'new mexico':'usa',
                     'yellow sea':'china',
                     'shahrud missile test site':'iran',
                     'pacific missile range facility':'usa',
                     'barents sea':'russian federation',
                     'gran canaria':'usa',
                     'kiritimati':'republic of kiribati',
                     'marshall islands, usa':'usa',
                     'kazakhstan':'russian federation',
                     'algeria, france':'france',
                     'french guiana, france':'france'}


### --- Data cleansing --- ###

# Remove duplicates, useless columns, change format of columns and reshape information that will be useful. Please watch the notebook for detailed information or open the data_cleanse script

exec(open("scripts/data_cleanse.py").read()) #Saves new dataframe as "data/missions_formatted.csv"
data = pd.read_csv('data/missions_formatted.csv')

### --- Generating Plots --- ###

## -- Chloropet map -- ##

exec(open("scripts/plot_scripts/plot_1_chloropeth_missions.py").read())
exec(open("scripts/plot_scripts/plot_2_sunburst_missions.py").read())
