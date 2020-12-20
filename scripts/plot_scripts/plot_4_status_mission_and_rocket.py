# This script creates a bar chart with the status of the missions (success/fail) and how many active rockets remain on space

success_fail = data.drop_duplicates(subset=['Organisation', 'Date'], keep='last').groupby('Mission_Status')['Rocket_Status'].agg(['count'])\
.reset_index().sort_values(by='count',ascending=False).to_numpy()
status = data.drop_duplicates(subset=['Organisation', 'Date'], keep='last').groupby('Rocket_Status')['Rocket_Status'].agg(['count'])\
.reset_index().sort_values(by='count',ascending=False).to_numpy()


#Figure

trace1 = go.Bar(x=success_fail[:,0], y=success_fail[:,1],showlegend=False,marker_color=['royalblue','red','darkmagenta','black'],marker_line=dict(color='#000000', width=1))#, marker_color='#85bb65')

sb2 = px.sunburst(data, path=['Rocket_Status'])._data
trace2 = go.Pie(labels=sb2[0]['labels'], values=sb2[0]['values'], textinfo='label+percent',insidetextorientation='radial',showlegend=False, domain={'x': [0.7, .98], 'y': [0.3, 0.9]},
                marker_colors=['royalblue','#839deb'],marker_line=dict(color='#000000', width=1))

layout = go.Layout(height = 600,width = 1300, autosize = False, yaxis_title="Number of missions", xaxis_title="Mission status",
                   title=dict(text='Mission-status distribution',x=0.5,y=0.91,font=dict(family="Roboto",size=30,color='#000000')),
                   font=dict(family="Roboto",size=20,color="black"))


fig = go.Figure(data = [trace1, trace2], layout = layout)
fig.add_annotation(text="Rocket status", xref="paper", yref="paper", x=0.9, y=0.97, showarrow=False)
fig.update_xaxes(tickangle=0, tickfont=dict(family='Roboto', color='black', size=20),tickmode='linear')
fig.update_yaxes(tickfont=dict(family='Roboto', color='black', size=20))
fig.show()

fig.write_image("images/plots/fig4_status_mission_and_rocket.pdf")
fig.write_image("images/plots/fig4_status_mission_and_rocket.eps")