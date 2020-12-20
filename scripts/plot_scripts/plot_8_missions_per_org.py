#Creates a bar plot to picture which Organisations were in the top with the most launches

missions_by_org = data.groupby('Organisation')['Rocket_Status'].agg(['count'])\
.reset_index().sort_values(by='count',ascending=False).to_numpy()

#Dictionary of color per country
colorMapSubset = data[['Country','Color']].drop_duplicates().reset_index(drop=True)
colorMapSubset = dict(zip(colorMapSubset.Country, colorMapSubset.Color))
 
fig = make_subplots(rows=1, cols=2)

trace1 = go.Bar(x=missions_by_org[:50,0],
                y=missions_by_org[:50,1],
                marker_line=dict(color='#000000', width=1))

sb2 = px.sunburst(data, path=['Organisation'],color='Country',color_discrete_map=colorMapSubset)._data

trace2 = go.Sunburst(labels=sb2[0]['labels'],
                     parents=sb2[0]['parents'],
                     values=sb2[0]['values'],
                     domain={'x': [0.75, .98], 'y': [0.05, 1]},
                     marker=sb2[0]['marker'],marker_line=dict(color='#000000', width=.9))

layout = go.Layout(height = 600,
                   width = 1300,
                   autosize = False,
                   title=dict(text='Number of spatial missions by organisation',x=0.5,y=0.9,font=dict(family="Roboto",size=30,color='#000000')))

fig = go.Figure(data = [trace1, trace2], layout = layout)
fig.update_xaxes(tickangle=270, tickfont=dict(family='Roboto', color='black', size=20),tickmode='linear')
fig.update_yaxes(tickfont=dict(family='Roboto', color='black', size=20))
fig.show()

fig.write_image("images/plots/fig8_missions_per_org.pdf")
fig.write_image("images/plots/fig8_missions_per_org.eps")

#Useful links for a foreing reader to understand plotly's sintaxes
#https://stackoverflow.com/questions/61241172/plotly-how-to-create-sunburst-subplot-using-graph-objects
#https://stackoverflow.com/questions/64377918/plotly-how-to-generate-side-by-side-px-sunburst-plots