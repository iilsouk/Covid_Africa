# 1. Import pandas & matplotlib.pyplot
import pandas as pd
import matplotlib.pyplot as plt

# 2. Create "World_Covid" by reading World Covid Data csv input  file. 
# 3. Create "Continents"  by reading List of countries and continents input csv file.
# 4. Create "World_Population" by reading input World population Data csv file.
World_Covid = pd.read_csv('Covid_wrld.csv') 
Continents = pd.read_csv('C and C.csv')
World_Population = pd.read_csv('World_POP.csv')

# 4. create "merged" by match countries in "World_Covid" with their continents using an inner join. 
merged = World_Covid.merge(Continents, 
                      on="Country", 
                      how='inner', 
                      validate='1:m')

# 5. Create "merged1" by match countries in "World_Covid" with their population data using an inner join.
merged1 = World_Covid.merge(World_Population, 
                      on="Country", 
                      how='inner', 
                      validate='1:m')

# 6. Save variable "merged1" to a csv file.
merged1.to_csv("Covid_population.csv", index=False)

# 7.a) Create "merged2" equal to calling the .drop_duplicates on  "merged" using the 'total cases' as the subest.
# 7.b) Drop the index in "merged2"and move 'cont.' to be the second column. 
merged2 = merged.drop_duplicates(subset=['Total Cases'])
merged2.drop(merged2.columns[0],axis=1,inplace=True)
Scnd_Column = merged2.pop('Cont.')
merged2.insert(1, 'Cont.', Scnd_Column)

# 8.a) set 'Top_ten_Cases' equal to to the top 10  largest values of 'Total Cases' in merged2.
# 8.b) print the 'Country', 'Cont.' and 'Total Cases' columns of Top_ten_Cases.
Top_ten_Cases = merged2.nlargest(10, ['Total Cases'])
print('\nTop 10 Countries- Total Cases:')
print('\n',Top_ten_Cases[['Country', 'Cont.','Total Cases']])

# 9.a) set 'Top_ten_M' equal to the top 10 largest values of 'Tot Cases/1M pop' in merged2.
# 9.b) print the 'Country', 'Cont.' and Tot Cases/1M pop' columns of Top_ten_M.
Top_ten_M = merged2.nlargest(10, ['Tot Cases/1M pop'])
print('\nTop 10 Countries- Total Cases per 1M pop:')
print('\n',Top_ten_Cases[['Country', 'Cont.','Tot Cases/1M pop']])

# 10.a) set 'Top_ten_Deaths' equal to the to the top 10 largest values of 'Total Deaths' in merged2.
# 10.b) print the 'Country', 'Cont.' and 'Total Deaths' columns of Top_ten_Deaths.
Top_ten_Deaths = merged2.nlargest(10, ['Total Deaths'])
print('\nTop 10 Countries- Total Deaths:')
print('\n', Top_ten_Deaths[['Country', 'Cont.', 'Total Deaths']])

# 11.a) set 'Top_Deaths_M' equal to the to the top 10 largest values of Deaths/1M pop' in merged2.
# 11.b) print the 'Country', 'Cont.' and 'Deaths/1M pop' columns of Top_Deaths_M.
Top_Deaths_M = merged2.nlargest(10, ['Deaths/1M pop'])
print('\nTop 10 Countries- Total Deaths per 1M pop:')
print('\n', Top_Deaths_M[['Country', 'Cont.', 'Deaths/1M pop']])

# 12.a) Create a dataframe which consists of African countries Covid Data.
Africa = merged2.loc[merged2['Cont.'] == 'Africa']
# 12.B) set TC_Afr equal to the "Total Cases" column of Africa.
TC_Afr = Africa["Total Cases"]
# 12.C) set Total_Cases_Afr equal to the sum of TC_Afr
Total_Cases_Afr = TC_Afr.sum()
# 12.d) set TCM_Afr equal to the "Tot Cases/1M pop" column of Africa.
TCM_Afr = Africa["Tot Cases/1M pop"]
# 12.e) set Total_Cases_perM_Afr equal to the sum of TCM_Afr
Total_Cases_perM_Afr = TCM_Afr.sum()
# 12.f) set Avg_Afr equal to  Total_Cases_perM_Afr divided the number of countries in Africa.
Avg_Afr = round(Total_Cases_perM_Afr/len(Africa),2)
# 12.g)  set TD_Afr equal to "Total Deaths" comuln of Africa.
TD_Afr = Africa["Total Deaths"]
# 12.h) set Total_Deaths_Afr equal to the sum of TD_Afr
Total_Deaths_Afr = TD_Afr.sum()

# 13) Repeat the same step to create a dataframe which consists of European countries Covid Data.
Europe = merged2.loc[merged2['Cont.'] == 'Europe']
TC_Eur = Europe["Total Cases"]
Total_Cases_Euro= TC_Eur.sum()
TCM_Eur = Europe["Tot Cases/1M pop"]
Total_Cases_perM_Eur = TCM_Eur.sum()
Avg_Euro =  round(Total_Cases_perM_Eur/len(Europe),2)
TD_Eur = Europe["Total Deaths"]
Total_Deaths_Eur = TD_Eur.sum()

# 14) Repeat the same step to create a dataframe which consists of North American countries Covid Data.
N_America = merged2.loc[merged2['Cont.'] == 'North America']
TC_NAm = N_America["Total Cases"]
Total_Cases_NAm= TC_NAm.sum()
TCM_NAm = N_America["Tot Cases/1M pop"]
Total_Cases_perM_NAm  = TCM_NAm.sum()
Avg_NAm = round(Total_Cases_perM_NAm/len(N_America),2)
TD_NAm = N_America["Total Deaths"]
Total_Deaths_NAm = TD_NAm.sum()

# 15) Repeat the same step to create a dataframe which consists of South American countries Covid Data.
S_America = merged2.loc[merged2['Cont.'] == 'South America']
TC_SAm = S_America["Total Cases"]
Total_Cases_SAm= TC_SAm.sum()
TCM_SAm = S_America["Tot Cases/1M pop"]
Total_Cases_perM_SAm  = TCM_SAm.sum()
Avg_SAm =  round(Total_Cases_perM_SAm/len(S_America),2)
TD_SAm = S_America["Total Deaths"]
Total_Deaths_SAm = TD_SAm.sum()

# 16) Repeat the same step to create a dataframe which consists of countries Covid Data in Oceania.
Oceania = merged2.loc[merged2['Cont.'] == 'Oceania']
TC_Ocea = Oceania["Total Cases"]
Total_Cases_Ocea= TC_Ocea.sum()
TCM_Ocea = Oceania["Tot Cases/1M pop"]
Total_Cases_perM_Ocea = TCM_Ocea.sum()
Avg_Oceania = round(Total_Cases_perM_Ocea/len(Oceania),2)
TD_Ocea = Oceania["Total Deaths"]
Total_Deaths_Ocea = TD_Ocea.sum()

# 17) Repeat the same step to create a dataframe which consists of Asian countries Covid Data.
Asia = merged2.loc[merged2['Cont.'] == 'Asia']
TC_Asia = Asia["Total Cases"]
Total_Cases_Asia= TC_Asia.sum()
TCM_Asia = Asia["Tot Cases/1M pop"]
Total_Cases_perM_Asia = TCM_Asia.sum()
Avg_Asia = round(Total_Cases_perM_Asia/len(Asia), 2)
TD_Asia = Asia["Total Deaths"]
Total_Deaths_Asia = TD_Asia.sum()

# 18) create a list called World_cases which consists of continents' total covid cases.  
World_cases = [Total_Cases_Afr, Total_Cases_Euro, Total_Cases_NAm,
               Total_Cases_SAm, Total_Cases_Ocea, Total_Cases_Asia]

# 19) create World_TC equal to the sum of World_cases
World_TC = sum(World_cases)
# 19. a) print the total number of covid cases in the world (World_TC)
print('\nTotal World Covid Cases:', World_TC)

# 20) follow a similar to print the world's number of covid deaths (World_Deaths)
World_Deaths = [Total_Deaths_Afr, Total_Deaths_Eur, Total_Deaths_NAm,
               Total_Deaths_SAm, Total_Deaths_Ocea, Total_Deaths_Asia]
World_TD = sum(World_Deaths)
print('\nTotal World Covid Deaths:', World_TD)

# 21) Create a list called Data consisting of each continent's name, total covid cases, Tot. Deaths,
# Avg. cases per 1M pop, and continent's % of world cases. 

Data = [['Africa', Total_Cases_Afr, Total_Deaths_Afr, Avg_Afr, round((Total_Cases_Afr/ World_TC*100), 2)],
        ['Europe', Total_Cases_Euro, Total_Deaths_Eur,Avg_Euro,round(Total_Cases_Euro/ World_TC*100, 2)],
        ['North America', Total_Cases_NAm, Total_Deaths_NAm, Avg_NAm, round(Total_Cases_NAm/ World_TC*100, 2)],
        ['South America', Total_Cases_SAm, Total_Deaths_SAm,  Avg_SAm, round(Total_Cases_SAm/ World_TC*100, 2)],
        ['Oceania', Total_Cases_Ocea, Total_Deaths_Ocea, Avg_Oceania, round(Total_Cases_Ocea/ World_TC*100, 2)],
        ['Asia', Total_Cases_Asia, Total_Deaths_Asia, Avg_Asia, round(Total_Cases_Asia/ World_TC*100, 2)]]

# 22) Put the data into a dataframe called Covid_by_Cont. 
Covid_by_Cont = pd.DataFrame(Data, columns = ['Cont.',
                                              'Tot. Cases',
                                              'Tot. Deaths',
                                              'Avg. cases per 1M pop',
                                              '% of Glob. cases'])

# 23) Print Covid Data by Continent (Covid_by_Cont) and save it to a csv file. 
print('\nCovid Data by Continent:')
print('\n', Covid_by_Cont)
Covid_by_Cont.to_csv("CovidbyContinent.csv", index=False)


# 24) Follow the same approach to print Covid_by_Cont2 (Covid Data by Continent in Millions)                                        
Data2 = [['Africa', Total_Cases_Afr/1e6, Total_Deaths_Afr/1e6, Avg_Afr/1e6],
        ['Europe', Total_Cases_Euro/1e6, Total_Deaths_Eur/1e6,Avg_Euro/1e6],
        ['North America', Total_Cases_NAm/1e6, Total_Deaths_NAm/1e6, Avg_NAm/1e6],
        ['South America', Total_Cases_SAm/1e6, Total_Deaths_SAm/1e6,  Avg_SAm/1e6],
        ['Oceania', Total_Cases_Ocea/1e6, Total_Deaths_Ocea/1e6, Avg_Oceania/1e6],
        ['Asia', Total_Cases_Asia/1e6, Total_Deaths_Asia/1e6, Avg_Asia/1e6]]


Covid_by_Cont2 = pd.DataFrame(Data2, columns = ['Cont.',
                                              'Tot. Cases',
                                              'Tot. Deaths',
                                              'Avg. cases per 1M pop'])

print('\nCovid Data by Continent in Millions:')
print('\n', Covid_by_Cont2)

# 25) set 'Cont.' as the index of Covid_by_Cont and Covid_by_Cont2
Covid_by_Cont = Covid_by_Cont.set_index('Cont.')
Covid_by_Cont2 = Covid_by_Cont2.set_index('Cont.')

# 25) Create and save a histogram using 'Tot. Cases' column of Covid_by_Cont2. 
fig, ax1 = plt.subplots()
bars = ['Tot. Cases']
Covid_by_Cont2[bars].plot.bar(ax=ax1, color ='grey')
fig.suptitle("Total Covid Cases by Continent in Millions")
ax1.set_xlabel("Continents")
ax1.set_ylabel("Covid Cases")
fig.tight_layout() 
fig.savefig("World-Cases", dpi=300)

# 26) Create a save a histogram using ''Tot. Deaths' column of Covid_by_Cont. 
fig, ax1 = plt.subplots()
bars = ['Tot. Deaths']
Covid_by_Cont[bars].plot.bar(ax=ax1, color ="brown")
fig.suptitle("Total Covid Deaths by Continent")
ax1.set_xlabel("Continents")
ax1.set_ylabel("Covid Deaths")
fig.tight_layout() 
fig.savefig("World-Deaths", dpi=300)

# 27) Create and save a histogram using 'Avg. cases per 1M pop' column of Covid_by_Cont. 
fig, ax1 = plt.subplots()
bars = ['Avg. cases per 1M pop']
Covid_by_Cont[bars].plot.bar(ax=ax1, color ='blue')
fig.suptitle("Average cases per 1M pop")
ax1.set_xlabel("Continents")
ax1.set_ylabel("Avg. cases per 1M pop")
fig.tight_layout() 
fig.savefig("Average", dpi=300)

# 28) Create and save a histogram using '% of Glob. cases' column of Covid_by_Cont.
fig, ax1 = plt.subplots()
bars = ['% of Glob. cases']
Covid_by_Cont[bars].plot.bar(ax=ax1, color = 'orange')
fig.suptitle("Continent % of Cases")
ax1.set_xlabel("Continents")
ax1.set_ylabel('% of Glob. cases')
fig.tight_layout() 
fig.savefig("Continent_Share_of_Cases", dpi=300)

