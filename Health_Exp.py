import pandas as pd
import matplotlib.pyplot as plt


World_H_Exp = pd.read_csv('Health expenditure.csv') 

Continents1 = pd.read_csv('C and C.csv')

WH_Exp = World_H_Exp.merge(Continents1, 
                      on="Country", 
                      how='inner', 
                      validate='1:m')

index1 = WH_Exp.pop('Cont.')
WH_Exp.insert(1, 'Cont.', index1)
WH_Exp = WH_Exp.drop_duplicates(subset=['Country'])
WH_Exp = WH_Exp.set_index('Country')
WH_Exp = WH_Exp.dropna()

Top_ten_HE = WH_Exp.nlargest(10, ['2018'])
print('\nTop 10 Countries- Highest Health Expenditure in 2018:')
print('\n',round(Top_ten_HE[['Cont.','2018']], 2))

Low_ten_HE = WH_Exp.nsmallest(10, ['2018'])
print('\nBottom 10 Countries- Lowest Health Expenditure in 2018:')
print('\n',round(Low_ten_HE[['Cont.','2018']], 2))

WH_Exp["Average"] = round(WH_Exp.loc[: , ['2010', '2011', '2012',
                                      '2013', '2014', '2015',
                                      '2016', '2017', '2018',
                                      ]].sum(axis=1)/9, 2)

Africa2 = WH_Exp.loc[WH_Exp['Cont.'] == 'Africa']
Avg_HEAF = Africa2['Average']
Avg_HEAF1 = round(Avg_HEAF.sum()/43, 2)

Europe2 = WH_Exp.loc[WH_Exp['Cont.'] == 'Europe']
Avg_HEEU = Europe2['Average']
Avg_HEEU1 = round(Avg_HEEU.sum()/35, 2)

Asia2 = WH_Exp.loc[WH_Exp['Cont.'] == 'Asia']
Avg_HEAS = Asia2['Average']
Avg_HEAS1 = round(Avg_HEAS.sum()/37, 2)

Oceania2 = WH_Exp.loc[WH_Exp['Cont.'] == 'Oceania']
Avg_HEOC = Oceania2['Average']
Avg_HEOC1 = round(Avg_HEOC.sum()/12, 2)

N_America2 = WH_Exp.loc[WH_Exp['Cont.'] == 'North America']
Avg_HENA = N_America2['Average']
Avg_HENA1 = round(Avg_HENA.sum()/12, 2)

S_America2 = WH_Exp.loc[WH_Exp['Cont.'] == 'South America']
Avg_HESA = S_America2['Average']
Avg_HESA1 = round(Avg_HESA.sum()/9, 2)


Data_HEx = [['Africa', Avg_HEAF1],
        ['Europe', Avg_HEEU1],
        ['North America', Avg_HEAS1],
        ['South America', Avg_HEOC1],
        ['Oceania', Avg_HENA1],
        ['Asia', Avg_HESA1]]

HE_by_Cont = pd.DataFrame(Data_HEx, columns =['Cont.', 'Avg. Health Exp.'])

print('\nContinents Average Health Expenditure 2010-2018 (% of GDP):')
print('\n', HE_by_Cont)
HE_by_Cont.to_csv("Continents Average Health Expenditure 2010-2018.csv", index=False)

HE_by_Cont = HE_by_Cont.set_index('Cont.')
fig, ax1 = plt.subplots()
bars = ['Avg. Health Exp.']
HE_by_Cont[bars].plot.bar(ax=ax1, color ='orange')
fig.suptitle("Avg. Health Exp.(% of GDP)")
ax1.set_xlabel("Continents")
ax1.set_ylabel('(% of GDP)')
fig.tight_layout() 
fig.savefig("Avg. Health Exp.", dpi=300)

GDP= pd.read_csv('World_GDP2021.csv')
HE_by_Cont = HE_by_Cont.merge(GDP, 
                      on="Cont.", 
                      how='inner', 
                      validate='1:m')

HE_by_Cont["2021 Health Exp. (US $ Billions)"] = HE_by_Cont["Avg. Health Exp."]*HE_by_Cont["GDP (US$billion) 2021"]/100

HE_by_Cont = HE_by_Cont.set_index('Cont.')
fig, ax1 = plt.subplots()
bars = ["2021 Health Exp. (US $ Billions)"]
HE_by_Cont[bars].plot.bar(ax=ax1, color ='blue')
fig.suptitle("Estimated 2021 Health Expenditure")
ax1.set_xlabel("Continents")
ax1.set_ylabel('US $ Billion')
fig.tight_layout() 
fig.savefig("Estimated 2021 Health Expenditure", dpi=300)

print('\nContinents Estimated Health Exp. 2021:')
print('\n', HE_by_Cont)

