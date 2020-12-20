# This script creates a year by year plot of the money spent on missions by all countries


#Filter only the data on which we actually have information for the prices
money_year = data[data['Price']>0].groupby('Year')['Price'].apply(lambda x: np.mean(x)).reset_index()
#Money by organisation
money_org = data.groupby('Organisation')['Price'].apply(lambda x: np.sum(x))
money_org = money_org[money_org>0].reset_index()


#Figure
trace1 = go.Bar(x=money_year['Year'], y=money_year['Price'], marker_color='#85bb65',marker_line=dict(color='#000000', width=1))

sb2 = px.sunburst(money_org, path=['Organisation'], values='Price',labels='Organisation')._data
trace2 = go.Sunburst(labels=sb2[0]['labels'], parents=sb2[0]['parents'], values=sb2[0]['values'], domain={'x': [0.75, .98], 'y': [0.05, 1]},marker_line=dict(color='#000000', width=1))

layout = go.Layout(height = 600,width = 1300, autosize = False, yaxis_title="Money spent (million us)", xaxis_title="Year",
                   title=dict(text='Money spent by year (a lot of information is missing)',x=0.5,y=0.9,font=dict(family="Roboto",size=30,color='#000000')),
                   font=dict(family="Roboto",size=20,color="black"))


fig = go.Figure(data = [trace1, trace2], layout = layout)
fig.add_annotation(text="Money spent by organisation", xref="paper", yref="paper", x=0.98, y=0.95, showarrow=False)
fig.update_xaxes(tickangle=270, tickfont=dict(family='Roboto', color='black', size=20),tickmode='linear')
fig.update_yaxes(tickfont=dict(family='Roboto', color='black', size=20))
fig.show()

fig.write_image("images/plots/fig6_money_by_year.pdf")
fig.write_image("images/plots/fig6_money_by_year.eps")
