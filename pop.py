# 1. Import pandas & matplotlib.pyplot
import pandas as pd
import matplotlib.pyplot as plt

# 2. Create World_pop by reading World_POP csv input file. 
# 3. Create Continent_pop  by reading List of countries and continents input csv file.
World_pop = pd.read_csv('World_POP.csv') 
Continent_pop = pd.read_csv('C and C.csv')

# 4. create merged_pop by match countries in World_pop with their continents using an inner join. 
merged_pop = World_pop.merge(Continent_pop, 
                      on="Country", 
                      how='inner', 
                      validate='1:m')

# 5. Rearrange the columns so that Cont. comes after 'Country'
cont_Column = merged_pop.pop('Cont.')
merged_pop.insert(1, 'Cont.', cont_Column)

# 6. Drop duplicates in merged_pop
merged_pop = merged_pop.drop_duplicates(subset=['Population 2020'])

# 7.a) set Top_ten_POP equal to the top 10 largest values of 'Population 2020' in merged_pop.
# 7.b) print the 'Country', 'Cont.' and 'Population 2020' columns of Top_ten_POP.
Top_ten_POP = merged_pop.nlargest(10, ['Population 2020'])
print('\nTop 10 Countries- Total Population:')
print('\n',Top_ten_POP[['Country', 'Cont.','Population 2020']])

# 8) Use a similar approach to print the list and data of ten countries with the lowest population. 
Low_ten_POP = merged_pop.nsmallest(10, ['Population 2020'])
print('\nBottom 10 Countries- Total Population:')
print('\n',Low_ten_POP[['Country', 'Cont.','Population 2020']])


# 9.a) Create a dataframe Africa_pop which consists of African countries population data.
Africa_pop = merged_pop.loc[merged_pop['Cont.'] == 'Africa']
# 9.b) set pop_Afr equal to the sum of 'Population 2020' in Africa_pop divided by 1e9
pop_Afr = Africa_pop['Population 2020'].sum()/1e9  

#10) Follow a similar approach with the other continents. 
Asia_pop = merged_pop.loc[merged_pop['Cont.'] == 'Asia']
pop_Asia = Asia_pop['Population 2020'].sum()/1e9

Oceania_pop = merged_pop.loc[merged_pop['Cont.'] == 'Oceania']
pop_Oceania = Oceania_pop['Population 2020'].sum()/1e9

NAm_pop = merged_pop.loc[merged_pop['Cont.'] == 'North America']
pop_NAm = NAm_pop['Population 2020'].sum()/1e9

SAm_pop = merged_pop.loc[merged_pop['Cont.'] == 'South America']
pop_SAm = SAm_pop['Population 2020'].sum()/1e9

Eur_pop = merged_pop.loc[merged_pop['Cont.'] == 'Europe']
pop_Eur = Eur_pop['Population 2020'].sum()/1e9


#11) Set Afr_share equal to 'World Share' column of Africa_pop
# follow a similar approach wiht the other continents 
Afr_share = Africa_pop['World Share'].sum()
Asia_share = Asia_pop['World Share'].sum()
Oce_share = Oceania_pop['World Share'].sum()
NAm_share = NAm_pop['World Share'].sum()
SAm_share = SAm_pop['World Share'].sum()
Eur_share = Eur_pop['World Share'].sum()

# 12) set Africa_age equal to the median of the 'Med. Age' column of Africa_pop
# Follow a similar approach with the other continenets
# drop rows where the data is missing if needed. 

Africa_age = Africa_pop['Med. Age'].median()
Asia_age = Asia_pop['Med. Age'].median()

Oceania_age = Oceania_pop.dropna()
Oceania_age1 = Oceania_age['Med. Age'].median()

Europe_age = Eur_pop.dropna()
Europe_age1 = Europe_age['Med. Age'].median()

SAmerica_age = SAm_pop.dropna()
SAmerica_age1 = SAmerica_age['Med. Age'].median()

NAmerica_age = NAm_pop.dropna()
NAmerica_age1 = NAmerica_age['Med. Age'].median()

# 13) Create a list called Data_pop consisting of each continent's name, 
#  population, share of world population, and median age. 

Data_pop = [['Asia', round(pop_Asia, 2), round(Asia_share*100, 3), round(Asia_age)],
            ['Africa', round(pop_Afr, 2), round(Afr_share*100, 3), round(Africa_age)],
            ['Europe', round(pop_Eur, 2), round(Eur_share*100, 3), round(Europe_age1)],
            ['North America', round(pop_NAm, 2), round(NAm_share*100, 3), round(NAmerica_age1)],
            ['South America', round(pop_SAm, 2), round(SAm_share*100, 3),  round(SAmerica_age1)],
            ['Oceania', round(pop_Oceania, 2), round(Oce_share*100, 3), round(Oceania_age1)]]
    
# 14) Put the data into a dataframe called Summary.

Summary = pd.DataFrame(Data_pop, columns = ['Continent',
                                              'Population (billions)',
                                              '% Population',
                                              'Median Age'])

# 15) Print World Population Summary (Summary).
print('\nWorld Population Summary:')
print('\n', Summary)

# 16) Set 'Continent' as the index of Summary.
Summary = Summary.set_index('Continent')

# 17) Create and save a histogram using "Median Age" column of Summary. 
fig, ax1 = plt.subplots()
bars = ["Median Age"]
Summary[bars].plot.bar(ax=ax1, color ='brown')
fig.suptitle("Median Age")
ax1.set_xlabel("Continents")
ax1.set_ylabel('Age')
fig.tight_layout() 
fig.savefig("Median-Age", dpi=300)

# 18) save Summary to a csv file named 'population_summary.csv'
Summary.to_csv('population_summary.csv')

# 19) Create covid_population by reading the Covid_population csv file
covid_population = pd.read_csv('Covid_population.csv') 

# 20) Print the data of the top ten countries with the highest deaths and their median age. 
Test_ten = covid_population.nlargest(10, ['Total Deaths'])
print('\nTop 10 Countries- Total deaths:')
print('\n',Test_ten[['Country','Total Deaths','Med. Age']])




