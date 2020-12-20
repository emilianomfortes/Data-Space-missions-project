#Creates a scatter plot to see the distribution over time of missions from the top 10 Organisations

#Dictionary of color per country
colorMapSubset = data[['Country','Color']].drop_duplicates().reset_index(drop=True)
colorMapSubset = dict(zip(colorMapSubset.Country, colorMapSubset.Color))

#Top 10 organisations with the most launches
top_org = data.groupby('Organisation')['Mission_Status'].apply(lambda x: np.sum(len(x))).sort_values(ascending=False).iloc[:10].reset_index()['Organisation'].to_numpy()
chart = []
for org in top_org:
    chart.append(data[data['Organisation']==org][['Organisation','Year','Mission_Status']])
top_org_missions = pd.DataFrame()
for c in chart:
    top_org_missions = top_org_missions.append(c,ignore_index=True)
top_org_launches = top_org_missions.groupby(['Organisation','Year'])['Mission_Status'].apply(lambda x: np.sum(len(x))).reset_index()

#Figure
fig = px.line(top_org_launches, x="Year", y="Mission_Status", color='Organisation')
fig.update_layout(height=600, width=1300, autosize=False,title=dict(text='Year-by-year mission distribution of the top 10 organisations',x=0.5,y=0.95,font=dict(family="Roboto",size=30,color='#000000')),
                 yaxis_title="Number of missions", xaxis_title="Year",font=dict(family="Roboto",size=20,color="black"))
fig.update_xaxes(tickangle=0, tickfont=dict(family='Roboto', color='black', size=20))
fig.update_yaxes(tickfont=dict(family='Roboto', color='black', size=20))
fig.show()

fig.write_image("images/plots/fig10_organisations_yby.pdf")
fig.write_image("images/plots/fig10_organisations_yby.eps")