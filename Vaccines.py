# 1. Import pandas & matplotlib.pyplot
import pandas as pd
import matplotlib.pyplot as plt

# 2. Create Vaccines by reading Vaccines csv input file. 
# 3. Create Continents3  by reading List of countries and continents input csv file.
Vaccines= pd.read_csv('Vaccines.csv') 
Continents3 = pd.read_csv('C and C.csv')

# 4. create vacc_Cont by match countries in Vaccines with their continents using an inner join.
vacc_Cont = Vaccines.merge(Continents3, 
                      on="Country", 
                      how='inner', 
                      validate='1:m')

# 5. Drop duplicates in vacc_Cont
vacc_Cont = vacc_Cont.drop_duplicates(subset=['Country'])

# 6. Rearrange the columns so that Cont. comes after 'Country'
index = vacc_Cont.pop('Cont.')
vacc_Cont.insert(1, 'Cont.', index)

# 7. set 'Country' as the index of vacc_Cont
vacc_Cont = vacc_Cont.set_index('Country')

# 8. print the list and data of top 10 countries with the highest number of doses per 100 residents
Top_ten_doses = vacc_Cont.nlargest(10, ['Total doses per 100 residents'])
print('\nTop 10 Countries- Total doses per 100 residents:')
print('\n',round(Top_ten_doses[['Cont.', 'Total doses per 100 residents']], 2))

# 9. print the list and data of top 10 countries with the lowest number of doses per 100 residents
Bot_ten_doses = vacc_Cont.nsmallest(10, ['Total doses per 100 residents'])
print('\nBottom 10 Countries- Total doses per 100 residents:')
print('\n',round(Bot_ten_doses[['Cont.', 'Total doses per 100 residents']], 2))

# 10. drop rows with missing data in vacc_Cont2
vacc_Cont2 = vacc_Cont.dropna()

# 11. print the list and data of top 10 countries with the highest percent of vaccinated people. 
Top_ten_vac = vacc_Cont2.nlargest(10, ['Percent vaccinated'])
print('\nTop 10 Countries- Percent vaccinated:')
print('\n',round(Top_ten_vac[['Cont.', 'Percent vaccinated']], 2))

# 12. print the list and data of top 10 countries with the lowest percent of vaccinated people. 
Bot_ten_vac = vacc_Cont.nsmallest(10, ['Percent vaccinated'])
print('\nBottom 10 Countries- Percent vaccinated:')
print('\n',round(Bot_ten_vac[['Cont.', 'Percent vaccinated']], 2))

# 13. print the list and data of top 10 countries with the highest percent of fully vaccinated people.
Top_ten_fvac = vacc_Cont2.nlargest(10, ['Percent fully vaccinated'])
print('\nTop 10 Countries- Fully vaccinated:')
print('\n',round(Top_ten_fvac[['Cont.', 'Percent fully vaccinated']], 2))

# 14. print the list and data of top 10 countries with the lowest percent of fully vaccinated people.
Bot_ten_fvac = vacc_Cont.nsmallest(10, ['Percent fully vaccinated'])
print('\nBottom 10 Countries- Percent vaccinated:')
print('\n',round(Bot_ten_fvac[['Cont.', 'Percent fully vaccinated']], 2))

# 15.a) Create a dataframe Africa_vac which consists of African countries vaccines data.
Africa_vac = vacc_Cont.loc[vacc_Cont['Cont.'] == 'Africa']
# 15.b) set Afr_v100 to 'Total doses per 100 residents'columns of Africa_vac
Afr_v100 = Africa_vac['Total doses per 100 residents']
# 15.b) set Afr_v10 equal to the sum of Afr_v100 divided by the number of countries in Africa_vac.
Afr_v10 = round(Afr_v100.sum()/44, 2)

# 16) Follow a similar approach with the other continents
Europe_vac = vacc_Cont.loc[vacc_Cont['Cont.'] == 'Europe']
Eur_v100 = Europe_vac['Total doses per 100 residents']
Eur_v10 = round(Eur_v100.sum()/38, 2)

Asia_vac = vacc_Cont.loc[vacc_Cont['Cont.'] == 'Asia']
Asia_v100 = Asia_vac['Total doses per 100 residents']
Asia_v10 = round(Asia_v100.sum()/48, 2)

Oceania_vac = vacc_Cont.loc[vacc_Cont['Cont.'] == 'Oceania']
Oce_v100 = Oceania_vac['Total doses per 100 residents']
Oce_v10 = round(Oce_v100.sum()/5, 2)

NAmerica_vac = vacc_Cont.loc[vacc_Cont['Cont.'] == 'North America']
NAm_v100 = NAmerica_vac['Total doses per 100 residents']
NAm_v10 = round(NAm_v100.sum()/16, 2)

SAmerica_vac = vacc_Cont.loc[vacc_Cont['Cont.'] == 'South America']
SAm_v100 = SAmerica_vac['Total doses per 100 residents']
SAm_v10 = round(SAm_v100.sum()/12, 2)


# 17) Create a list called Data_vac consisting of each continent's name and 
# total doses per 100 Residents 
Data_vac = [['Africa', Afr_v10],
        ['Europe', Eur_v10],
        ['North America', Asia_v10],
        ['South America', Oce_v10],
        ['Oceania', NAm_v10],
        ['Asia', SAm_v10]]

# 18) Put the data into a dataframe called Data_vac1.
Data_vac1 = pd.DataFrame(Data_vac, columns =['Cont.', 'Tot. Doses per 100 Residents'])

# 19) Set 'Cont.' as the index of Data_vac1.
Data_vac1 = Data_vac1.set_index('Cont.')

# 20) Create and save a histogram using 'Tot. Doses per 100 Residents' column of Data_vac1. 
fig, ax1 = plt.subplots()
bars = ['Tot. Doses per 100 Residents']
Data_vac1[bars].plot.bar(ax=ax1, color ='green')
fig.suptitle("Total Doses per 100 Residents")
ax1.set_xlabel("Continents")
ax1.set_ylabel('Doses per 100 Residents')
fig.tight_layout() 
fig.savefig("Total Doses per 100 Residents", dpi=300)

# 21) print the list and data of top ten african countries with the highest percent of fully vaccinated people. 
Africa_vac1 = Africa_vac.dropna()
Africa_vac1.drop(Africa_vac1.iloc[:,1:3], inplace = True, axis = 1)
print(Africa_vac1.nlargest(10, ['Percent fully vaccinated']))