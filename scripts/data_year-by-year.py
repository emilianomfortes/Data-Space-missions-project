## -- Create an empty Year-by-year dataframe and add the years column -- ##
yby = pd.DataFrame()
yby['Year'] = data['Year'].sort_values().unique()


## -- Number of missions -- ##
yby['Missions'] = data.drop_duplicates(subset=['Organisation', 'Date'], keep='last').value_counts(subset=['Year']).reset_index().sort_values(by='Year').reset_index().iloc[:,2]

# - Mission status (outcome) - #
yby['Mission: Success'] = data.drop_duplicates(subset=['Organisation', 'Date'], keep='last')['Mission_Status'].eq('Success').astype(int).groupby(data['Year']).sum().to_numpy()
yby['Mission: Failure'] = data.drop_duplicates(subset=['Organisation', 'Date'], keep='last')['Mission_Status'].eq('Failure').astype(int).groupby(data['Year']).sum().to_numpy()
yby['Mission: Partial Failure'] = data.drop_duplicates(subset=['Organisation', 'Date'], keep='last')['Mission_Status'].eq('Partial Failure').astype(int).groupby(data['Year']).sum().to_numpy()
yby['Mission: Prelaunch Failure'] = data.drop_duplicates(subset=['Organisation', 'Date'], keep='last')['Mission_Status'].eq('Prelaunch Failure').astype(int).groupby(data['Year']).sum().to_numpy()
yby['Mission: Non Success'] = yby['Mission: Failure']+yby['Mission: Partial Failure']+yby['Mission: Prelaunch Failure']


## -- Rocket status -- ##
yby['Status: Active'] = data.drop_duplicates(subset=['Organisation', 'Date'], keep='last')['Rocket_Status'].eq('Active').astype(int).groupby(data['Year']).sum().to_numpy()
yby['Status: Retired'] = data.drop_duplicates(subset=['Organisation', 'Date'], keep='last')['Rocket_Status'].eq('Retired').astype(int).groupby(data['Year']).sum().to_numpy()



## -- Top organisation columns -- ##

# USEFUL LINKS BELOW
#https://stackoverflow.com/questions/38933071/group-by-two-columns-and-count-the-occurrences-of-each-combination-in-pandas
#https://stackoverflow.com/questions/15705630/get-the-rows-which-have-the-max-count-in-groups-using-groupby

aux = data.groupby(['Year','Organisation','Country']).size().reset_index()
idx = aux.groupby(['Year'])[0].transform(max) == aux[0]
#print(aux[idx].head(10))
yby['Top_organisation'] = aux[idx].reset_index()['Organisation']
yby['Top_organisation_country'] = aux[idx].reset_index()['Country']
yby['Top_organisation_count'] = yby['Top_organisation'] + ' ('+aux[idx].reset_index()[0].astype(str)+')'

#Create a Year-on-Year Chart Showing the Country Doing the Most Number of Launches

aux = data.groupby(['Year','Country'])[['Year','Country']].size().reset_index()
idx = aux.groupby(['Year'])[0].transform(max) == aux[0]
aux[idx]
yby['Top_country'] = aux[idx].reset_index()['Country']
yby['Top_country_count'] = yby['Top_country'] + ' ('+aux[idx].reset_index()[0].astype(str)+')'
yby = yby.merge(country_colors,how="left",left_on="Top_country",right_on="Country")
yby = yby.drop(columns="Country")
yby.to_csv('data/data_yby.csv',index=False)
yby.info()