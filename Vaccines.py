
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

Vaccines= pd.read_csv('Vaccines.csv') 
Continents3 = pd.read_csv('C and C.csv')

vacc_Cont = Vaccines.merge(Continents3, 
                      on="Country", 
                      how='inner', 
                      validate='1:m')

vacc_Cont = vacc_Cont.drop_duplicates(subset=['Country'])
index = vacc_Cont.pop('Cont.')
vacc_Cont.insert(1, 'Cont.', index)

vacc_Cont = vacc_Cont.set_index('Country')

Top_ten_doses = vacc_Cont.nlargest(10, ['Total doses per 100 residents'])
print('\nTop 10 Countries- Total doses per 100 residents:')
print('\n',round(Top_ten_doses[['Cont.', 'Total doses per 100 residents']], 2))

Bot_ten_doses = vacc_Cont.nsmallest(10, ['Total doses per 100 residents'])
print('\nBottom 10 Countries- Total doses per 100 residents:')
print('\n',round(Bot_ten_doses[['Cont.', 'Total doses per 100 residents']], 2))


vacc_Cont2 = vacc_Cont.dropna()

Top_ten_vac = vacc_Cont2.nlargest(10, ['Percent vaccinated'])
print('\nTop 10 Countries- Percent vaccinated:')
print('\n',round(Top_ten_vac[['Cont.', 'Percent vaccinated']], 2))

Bot_ten_vac = vacc_Cont.nsmallest(10, ['Percent vaccinated'])
print('\nBottom 10 Countries- Percent vaccinated:')
print('\n',round(Bot_ten_vac[['Cont.', 'Percent vaccinated']], 2))

Top_ten_fvac = vacc_Cont2.nlargest(10, ['Percent fully vaccinated'])
print('\nTop 10 Countries- Fully vaccinated:')
print('\n',round(Top_ten_fvac[['Cont.', 'Percent fully vaccinated']], 2))

Bot_ten_fvac = vacc_Cont.nsmallest(10, ['Percent fully vaccinated'])
print('\nBottom 10 Countries- Percent vaccinated:')
print('\n',round(Bot_ten_fvac[['Cont.', 'Percent fully vaccinated']], 2))

Africa_vac = vacc_Cont.loc[vacc_Cont['Cont.'] == 'Africa']
Afr_v100 = Africa_vac['Total doses per 100 residents']
Afr_v10 = round(Afr_v100.sum()/44, 2)

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

Data_vac = [['Africa', Afr_v10],
        ['Europe', Eur_v10],
        ['North America', Asia_v10],
        ['South America', Oce_v10],
        ['Oceania', NAm_v10],
        ['Asia', SAm_v10]]

Data_vac1 = pd.DataFrame(Data_vac, columns =['Cont.', 'Tot. Doses per 100 Residents'])

Data_vac1 = Data_vac1.set_index('Cont.')
fig, ax1 = plt.subplots()
bars = ['Tot. Doses per 100 Residents']
Data_vac1[bars].plot.bar(ax=ax1, color ='green')
fig.suptitle("Total Doses per 100 Residents")
ax1.set_xlabel("Continents")
ax1.set_ylabel('Doses per 100 Residents')
fig.tight_layout() 
fig.savefig("Total Doses per 100 Residents", dpi=300)

