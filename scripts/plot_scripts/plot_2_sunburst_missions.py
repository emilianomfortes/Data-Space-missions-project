# This script creats a sunburst chart to provide general information about the data
data = pd.read_csv('data/missions_formatted.csv')

#Dictionary of color per country
colorMapSubset = data[['Country','Color']].drop_duplicates().reset_index(drop=True)
colorMapSubset = dict(zip(colorMapSubset.Country, colorMapSubset.Color))

fig = px.sunburst(data, path=['Country', 'Organisation', 'Mission_Status'],color='Country',color_discrete_map=colorMapSubset,height=700)

#Legend
for i, m in enumerate(data['Country'].unique()):
    fig.add_annotation(dict(font=dict(color=data['Color'].unique()[i],size=14),
                                        x=0.8,
                                        y=1-(i/data['Country'].nunique()),
                                        showarrow=False,
                                        text=data['Country'].unique()[i].upper(),
                                        textangle=0,
                                        xanchor='left',
                                        xref="paper",
                                        yref="paper"))
fig.show()

fig.write_image("images/plots/fig2_sunburst.pdf")
fig.write_image("images/plots/fig2_sunburst.eps")
