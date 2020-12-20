missions = data.groupby('Country').size().reset_index().rename(columns={0: "Number of missions"})

missions_by_country = data.groupby('Country')['Rocket_Status'].agg(['count'])\
.reset_index().sort_values(by='count',ascending=False).to_numpy()

#Dictionary of color per country
colorMapSubset = data[['Country','Color']].drop_duplicates().reset_index(drop=True)
colorMapSubset = dict(zip(colorMapSubset.Country, colorMapSubset.Color))

mbc = pd.DataFrame(missions_by_country).rename(columns={0:'Country',1:'Missions'})
mbc = mbc.merge(data[['Country','Color']].drop_duplicates().reset_index(drop=True), left_on="Country",right_on="Country")

fig = make_subplots(
    rows=1, cols=2,
    column_widths=[0.8, 0.2],
    specs=[[{"type": "bar"}, {"type": "pie"}]])

#SUBPLOT LEFT
trace1 = go.Bar(x=mbc['Country'],y=mbc['Missions'],
               marker_color=mbc['Color'],marker_line=dict(color='#000000', width=1),
               text=mbc['Missions'],texttemplate='%{text:.2s}', textposition='outside',name='countries',legendgroup='countries',showlegend=False)
fig.add_trace(trace1, row=1, col=1)


#SUBPLOT RIGHT
sb2 = px.sunburst(data.drop_duplicates(subset=['Organisation', 'Date'], keep='last'), path=['Country'],color='Country',color_discrete_map=colorMapSubset)._data
trace2 = go.Pie(labels=sb2[0]['labels'], values=sb2[0]['values'],textposition='inside', textinfo='percent+label',insidetextorientation='radial',name='countries',legendgroup='countries',marker=dict(colors=sb2[0]['marker']['colors'],line=dict(color='#000000', width=1)))
fig.add_trace(trace2, row=1, col=2)

fig.update_layout(height = 800,width = 1400, autosize = False, yaxis_title="Number of missions", xaxis_title="Country",font=dict(family="Roboto",size=20,color="black"),
    title=dict(text='                    Number of missions during the cold war                 Percentage of missions',x=0.2,y=0.93,font=dict(family="Roboto",size=30,color='#000000')))
fig.update_xaxes(tickangle=270,tickfont=dict(family='Roboto', color='black', size=20))
fig.update_yaxes(tickfont=dict(family='Roboto', color='black', size=20))

fig.show()

fig.write_image("images/plots/fig9_missions_per_country.pdf")
fig.write_image("images/plots/fig9_missions_per_country.eps")
