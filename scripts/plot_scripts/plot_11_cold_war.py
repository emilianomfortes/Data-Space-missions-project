#Creates a plot to analyze the cold war

#Auxiliar dataframe to analayze the space race
space_race_by = pd.DataFrame()
space_race_by['Year'] = data[data['Year']<=1991].Year.sort_values(ascending=True).unique()
space_race_by['USA'] = data[(data['Year']<=1991) & (data['Country'] == 'usa')].groupby('Year')['Mission_Status'].agg(['count']).to_numpy()
space_race_by['URSS'] = np.zeros(len(space_race_by),dtype=int)
space_race_by['URSS'] = data[(data['Year']<=1991) & (data['Country'] == 'russian federation')].groupby('Year')['Mission_Status'].agg(['count']).to_numpy()

#Data for the pie chart (basically counts the number of missions done by the usa and the urss)
a = ['USA', 'URSS']
b = [0,0]
b[0] = space_race_by['USA'].astype(int).sum()
b[1] = space_race_by['URSS'].astype(int).sum()

fig = make_subplots(
    rows=1, cols=2,
    column_widths=[0.8, 0.2],
    specs=[[{"type": "bar"}, {"type": "pie"}]])

#SUBPLOT LEFT
fig_data = px.bar(space_race_by, x="Year", y=['USA','URSS'],barmode='group')._data
trace1 = go.Bar(fig_data[0],marker_line=dict(color='#000000', width=1))
trace2 = go.Bar(fig_data[1],marker_line=dict(color='#000000', width=1))
fig.add_trace(trace1, row=1, col=1)
fig.add_trace(trace2, row=1, col=1)

#SUBPLOT RIGHT
trace3 = go.Pie(labels=a, values=b, textinfo='label+percent',insidetextorientation='radial',showlegend=False,marker_line=dict(color='#000000', width=1))
fig.add_trace(trace3, row=1, col=2)

fig.update_layout(height = 600,width = 1700, autosize = False, yaxis_title="Number of missions", xaxis_title="Year",font=dict(family="Roboto",size=20,color="black"),
    title=dict(text='      Number of missions during the cold war                                                                         Percentage of missions',x=0.52,y=0.9,font=dict(family="Roboto",size=30,color='#000000')))
fig.update_xaxes(tickfont=dict(family='Roboto', color='black', size=20))
fig.update_yaxes(tickfont=dict(family='Roboto', color='black', size=20))
fig.show()

fig.write_image("images/plots/fig11_cold_war.pdf")
fig.write_image("images/plots/fig11_cold_war.eps")