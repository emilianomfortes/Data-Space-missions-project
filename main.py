### --- Libraries --- ###
#Essentials
import numpy as np
import random
from datetime import datetime
from iso3166 import countries #iso codes for countries (DID WE USE THIS?)
import pycountry #list of countries, can be used simply with pycountry.countries (https://pypi.org/project/pycountry/)

#Data management
mport pandas as pd
pd.set_option('display.max_colwidth', None)

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
