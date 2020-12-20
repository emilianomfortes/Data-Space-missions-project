# This script creates a year by year plot of the percentage of failed missions and how these improved over the years

meann = np.mean(yby['Mission: Non Success'][10:]/yby['Missions'][10:])

fig = go.Figure(data=[
    go.Scatter(x=yby.Year, y=yby['Mission: Non Success']/yby['Missions'],name='Year-on-year percentage of failures',marker_color="red",mode='lines+markers'),
    go.Scatter(x=yby.Year[10:], y=np.zeros(len(yby[10:]))+meann,name=r"Mean saturation value = "+str(np.round(meann,3)*100)+"%",marker_color="red" ),
])

fig.update_layout(height = 600,width = 1300, autosize = False, yaxis_title="Percentage", xaxis_title="Year",yaxis=dict(tickformat=".2%"),
                   title=dict(text='Percentage of failed missions',x=0.5,y=0.91,font=dict(family="Roboto",size=30,color='#000000')),
                   font=dict(family="Roboto",size=20,color="black"))


fig.update_xaxes(tickangle=0, tickfont=dict(family='Roboto', color='black', size=20))
fig.update_yaxes(tickfont=dict(family='Roboto', color='black', size=20))
fig.show()

fig.write_image("images/plots/fig5_percentage_failures.pdf")
fig.write_image("images/plots/fig5_percentage_failures.eps")