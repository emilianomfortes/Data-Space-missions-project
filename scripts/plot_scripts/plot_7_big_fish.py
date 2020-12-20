#Creates sunburst charts to picture which Organisations and which countries played the biggest roles during the space missions

#Dictionary of color per country
colorMapSubset = data[['Country','Color']].drop_duplicates().reset_index(drop=True)
colorMapSubset = dict(zip(colorMapSubset.Country, colorMapSubset.Color))

fig = go.Figure()
fig = make_subplots(rows=1,cols=2,subplot_titles=("Top organisation", "Top country"))

#Dictionary of data for the sunburst plot of the Top organizations
sb1 = px.sunburst(yby, path=['Year','Top_organisation_count'],color='Top_organisation_country',color_discrete_map=colorMapSubset)._data

#Dictionary of data for the sunburst plot of the Top countries
sb2 = px.sunburst(yby, path=['Year','Top_country_count'],color='Top_country',color_discrete_map=colorMapSubset)._data

fig.add_trace(go.Sunburst(
    branchvalues='total',
    labels=sb1[0]['labels'],
    parents=sb1[0]['parents'],
    values=sb1[0]['values'],
    ids=sb1[0]['ids'],
    marker=sb1[0]['marker'],
    domain=dict(column=0)))

fig.add_trace(go.Sunburst(
    branchvalues='total',
    labels=sb2[0]['labels'],
    parents=sb2[0]['parents'],
    values=sb2[0]['values'],
    ids=sb2[0]['ids'],
    marker=sb2[0]['marker'],
    domain=dict(column=1),maxdepth=2))

fig.add_annotation(x=0.01, y=1,
            showarrow=False,
            text="Top organisation",
            font_size=20)

fig.add_annotation(x=0.61, y=1,
            showarrow=False,
            text="Top country",
            font_size=20)

#Legend

for i, m in enumerate(data['Country'].unique()):
    fig.add_annotation(dict(font=dict(color=data['Color'].unique()[i],size=14),
                                        x=0.45,
                                        y=.9-(i/data['Country'].nunique()),
                                        showarrow=False,
                                        text=data['Country'].unique()[i].upper(),
                                        textangle=0,
                                        xanchor='left',
                                        xref="paper",
                                        yref="paper"))


fig.update_layout(
    grid= dict(columns=2, rows=1),
    #autosize = False,
    margin = dict(t=0, l=0, r=0, b=0)
)

fig.show()

fig.write_image("images/plots/fig7_big_fish.pdf")
fig.write_image("images/plots/fig7_big_fish.eps")
