# This script creates a chloropet chart to provide general information about the data and the countries involved

#Read sample dataset with countries iso codes for a chloropeth plot
df = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/2014_world_gdp_with_codes.csv')[['COUNTRY','CODE']]

#Minor tweaks 
df['COUNTRY'] = df['COUNTRY'].map(lambda x: x.lower())
df['MISSIONS'] = np.zeros(len(df),dtype=int)
df['FAILED MISSIONS'] = np.zeros(len(df),dtype=int)
df = df.replace({'united states':'usa'})
df = df.replace({'russia':'russian federation'})

data = pd.read_csv('data/missions_formatted.csv')

countries_with_missions = data['Country'].unique()

for countr in countries_with_missions:
    df.loc[df['COUNTRY']==countr,'MISSIONS'] = data[data['Country']==countr].groupby('Country')['Mission_Status'].apply(lambda x: np.sum(len(x)))[0]
    if countr != 'kenya': #Kenya does not have failed missions
        df.loc[df['COUNTRY']==countr,'FAILED MISSIONS'] = data[(data['Country']==countr) & (data['Mission_Status']!='Success')].groupby('Country')['Mission_Status'].apply(lambda x: np.sum(len(x)))[0]

import plotly.express as px
df = df[(df['MISSIONS']>0) & (df['FAILED MISSIONS']>0)]


#https://plotly.com/python/choropleth-maps/
fig = px.choropleth(df, locations="CODE",
                    color="MISSIONS", # lifeExp is a column of gapminder
                    hover_name="COUNTRY", # column to add to hover information
                    color_continuous_scale=px.colors.sequential.Teal,
                    height=700)


fig.update_layout(title=dict(text='Number of missions per Country',x=0.5,y=.95,font=dict(family="Roboto",size=30,color='#000000')),
    geo=dict(
        showframe=False,
        showcoastlines=False,
        projection_type='equirectangular'
    ))
fig.show()

fig.write_image("images/plots/fig1_chloropeth.pdf")
fig.write_image("images/plots/fig1_chloropeth.eps")
