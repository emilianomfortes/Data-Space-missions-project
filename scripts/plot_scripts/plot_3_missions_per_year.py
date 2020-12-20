# This script creates a year by year plot of the number of missions

fig = go.Figure(data=[
    go.Bar(name='Prelaunch Failure', x=yby['Year'], y=yby['Mission: Prelaunch Failure'],marker_color='black',marker_line=dict(color='#000000', width=1)),
    go.Bar(name='Partial Failure', x=yby['Year'], y=yby['Mission: Partial Failure'],marker_color='darkmagenta',marker_line=dict(color='#000000', width=1)),
    go.Bar(name='Failure', x=yby['Year'], y=yby['Mission: Failure'],marker_color='red',marker_line=dict(color='#000000', width=1)),
    go.Bar(name='Success', x=yby['Year'], y=yby['Mission: Success'],marker_color='royalblue',marker_line=dict(color='#000000', width=1)),
])
# Change the bar mode
fig.update_layout(barmode='stack',title=dict(text='Number of missions per year',x=0.5,y=0.93,font=dict(family="Roboto",size=30,color='#000000')),
                  height = 800,width = 1300, autosize = False,yaxis_title="Number of missions", xaxis_title="Year",
                  font=dict(family="Roboto",size=20,color="black"))
fig.update_xaxes(tickangle=0, tickfont=dict(family='Roboto', color='black', size=20))
fig.update_yaxes(tickfont=dict(family='Roboto', color='black', size=20))
fig.show()

fig.write_image("images/plots/fig3_missions_per_year.pdf")
fig.write_image("images/plots/fig3_missions_per_year.eps")