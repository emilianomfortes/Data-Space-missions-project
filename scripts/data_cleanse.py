## -- Only read the columns we care about -- ##
data = pd.read_csv('data/mission_launches.csv', usecols=['Organisation','Location','Date','Rocket_Status','Price','Mission_Status'])
data = pd.DataFrame(data)


## -- Convert Date column to datatime type -- ##
data['Date'] = pd.to_datetime(data['Date'],utc=True)
print('Converted "Date" column into datetime format')

## -- Add column with Year and another one with the Year & Month of each mission -- ##
data['Year'] = data['Date'].map(lambda x: x.year)
data['Year/Month'] = data['Date'].map(lambda x: datetime(x.year, x.month, 1))
print('Added "Year" and "Year/Month" columns')

## -- Convert strings to lower cases -- ##
data['Location'] = data['Location'].map(lambda x: x.lower())


## -- Add the country column that indicates who led the mission. Also, update locations which have changed -- ##
data['Country'] = data['Location'].replace(leased_countries, regex=True)
data['Location'] = data['Location'].replace(changed_countries, regex=True)

countrylist = np.array(list(pycountry.countries))
countrieslist = []
for i in range(len(countrylist)):
    countrieslist.append(countrylist[i].name.lower())
countrieslist.append('usa')
countrieslist.append('iran')
countrieslist.append('north korea')
countrieslist.append('south korea')
#print(data['Location_Country'].unique())
#print(data['Country'].unique())

## -- data.Location.map(lambda x: x.split()) -- ##
data['Location_Country'] = data.Location.map(lambda x: [word for word in countrieslist if word in x])
data['Country'] = data.Country.map(lambda x: [word for word in countrieslist if word in x])

data['Location_Country'] = data['Location_Country'].map(lambda x: ' '.join(x))
data['Country'] = data['Country'].map(lambda x: ' '.join(x))
print('Added "Country" and "Location_Country" columns')

## -- Change Rocket StatusActive/StatusRetired to simply Active/Retired -- ##
data['Rocket_Status'] = pd.Series(np.where(data.Rocket_Status.values == 'StatusRetired','Retired','Active'))
print('Changed Rocket StatusActive/StatusRetired to simply Active/Retired')

## -- Mission_status is a categorycal type, let's replace it like that to save on future problems -- ##
data['Mission_Status'] = data['Mission_Status'].astype('category')


## -- Checking for duplicates -- ##
duplicated_entries = data[data.duplicated(keep=False)]


## -- A lot of prices are missing, but I don't want to throw the rows away -- ##
data['Price'].fillna(0, inplace=True)
#data['Price?'] = pd.Series(np.where(data.Price.values == 0,'No','Yes'))
data['Price'] = data['Price'].replace(',','', regex=True)
data['Price'] = pd.to_numeric(data['Price'])


## -- Sea Launch multinational missions unfolding -- ##
sl_first = data[(data['Organisation']=='Sea Launch') & (data['Year/Month']<= datetime(2010,8,27))].reset_index(drop=True)
sl_second = data[(data['Organisation']=='Sea Launch') & (data['Year/Month']> datetime(2010,8,27))].reset_index(drop=True)
data = data[data['Organisation']!='Sea Launch']
with ChainedAssignent():
    sl_first['Country'] =sl_first['Country'].map(lambda x: ['usa','russian federation','norway','ukraine'])
    sl_second['Country'] = sl_second['Country'].map(lambda x: ['usa','russian federation','norway'])
sl = pd.concat([sl_first,sl_second],ignore_index=True)
sl = sl.explode('Country')
data = pd.concat([data, sl],ignore_index=True)

## -- Country color codes -- ##
country_color = []
for i in range(data['Country'].nunique()):
    r = random.randint(0,255)
    b = random.randint(0,255)
    g = random.randint(0,255)
    country_color.append('#%02x%02x%02x' % (r, g, b))   
country_colors = np.array([data['Country'].unique(),country_color])
country_colors = pd.DataFrame(country_colors.T).rename(columns={0: "Country", 1: "Color", "C": "c"})
data = data.merge(country_colors,how='left', on='Country')
print('Added randomly-generated country color codes as a column')

## -- Print indicating the amount of duplicated columns -- ##
print('The number of duplicated entries is: '+str(len( duplicated_entries )))
print('Thus, we should expect to reduce the complete dataset number of entries'\
      +'by a number of '+str(len(duplicated_entries.drop_duplicates())) +' entries.')
print('Number of entries before dropping duplicates = '+str(len(data)))
data = data.drop_duplicates()
print('Number of entries after dropping duplicates = '+str(len(data)))


data = data[['Organisation','Country','Color','Year','Year/Month','Location','Location_Country','Price','Mission_Status','Rocket_Status','Date']]
data.to_csv('data/missions_formatted.csv',index=False)
print('Saved the new dataframe as "data/missions_formatted.csv"')

print('The resulting information of the dataframe is: ')
data.info()
