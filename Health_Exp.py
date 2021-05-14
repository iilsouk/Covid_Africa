# 1. Import pandas & matplotlib.pyplot
import pandas as pd
import matplotlib.pyplot as plt

# 2. Create World_H_Exp by reading continents health expenditure data csv input file. 
# 3. Create Continents1  by reading List of countries and continents input csv file.
World_H_Exp = pd.read_csv('Health expenditure.csv') 
Continents1 = pd.read_csv('C and C.csv')

# 4. create "WH_Exp" by match countries in "World_H_Exp" with their continents using an inner join. 

WH_Exp = World_H_Exp.merge(Continents1, 
                      on="Country", 
                      how='inner', 
                      validate='1:m')

# 5. move the 'cont.' column to the second column of WH_Exp, drop duplicates, and set Country as the index. 
index1 = WH_Exp.pop('Cont.')
WH_Exp.insert(1, 'Cont.', index1)
WH_Exp = WH_Exp.drop_duplicates(subset=['Country'])
WH_Exp = WH_Exp.set_index('Country')

# 6. drop rows that are missing data. 
WH_Exp = WH_Exp.dropna()

# 7.a) set Top_ten_HE equal to to the top 10 largest values of '2018' in WH_Exp.
# 7.b) print the 'Country', 'Cont.' and '2018' columns of Top_ten_HE.
Top_ten_HE = WH_Exp.nlargest(10, ['2018'])
print('\nTop 10 Countries- Highest Health Expenditure in 2018:')
print('\n',round(Top_ten_HE[['Cont.','2018']], 2))

# 8. Follow a simila approach to print the data of the Bottom 10 Countries with the lowest Health Expenditure in 2018
Low_ten_HE = WH_Exp.nsmallest(10, ['2018'])
print('\nBottom 10 Countries- Lowest Health Expenditure in 2018:')
print('\n',round(Low_ten_HE[['Cont.','2018']], 2))

# 8. Create an average column in WH_Exp (Countries average expenditure between 2010 and 2018)
WH_Exp["Average"] = round(WH_Exp.loc[: , ['2010', '2011', '2012',
                                      '2013', '2014', '2015',
                                      '2016', '2017', '2018',
                                      ]].sum(axis=1)/9, 2)

# 8.a) Create a dataframe Africa2 which consists of African countries average expenditure.
Africa2 = WH_Exp.loc[WH_Exp['Cont.'] == 'Africa']
# 8.b) set Avg_HEAF equal to Average column of Africa2
Avg_HEAF = Africa2['Average']
# 8.c) set Avg_HEAF1 equal to the sum of Avg_HEAF divided by the number of countries in Africa2
# This will give us the continent's average expenditure. 
Avg_HEAF1 = round(Avg_HEAF.sum()/43, 2)

# 9) follow the same approach wit Europe2. 
Europe2 = WH_Exp.loc[WH_Exp['Cont.'] == 'Europe']
Avg_HEEU = Europe2['Average']
Avg_HEEU1 = round(Avg_HEEU.sum()/35, 2)

# 10) follow the same approach wit Asia2.
Asia2 = WH_Exp.loc[WH_Exp['Cont.'] == 'Asia']
Avg_HEAS = Asia2['Average']
Avg_HEAS1 = round(Avg_HEAS.sum()/37, 2)

# 11) follow the same approach wit Oceania2.
Oceania2 = WH_Exp.loc[WH_Exp['Cont.'] == 'Oceania']
Avg_HEOC = Oceania2['Average']
Avg_HEOC1 = round(Avg_HEOC.sum()/12, 2)

# 12) follow the same approach wit N_America2.
N_America2 = WH_Exp.loc[WH_Exp['Cont.'] == 'North America']
Avg_HENA = N_America2['Average']
Avg_HENA1 = round(Avg_HENA.sum()/12, 2)

# 13) follow the same approach wit S_America2.
S_America2 = WH_Exp.loc[WH_Exp['Cont.'] == 'South America']
Avg_HESA = S_America2['Average']
Avg_HESA1 = round(Avg_HESA.sum()/9, 2)


# 14) Create a list called Data_HEx consisting of each continent's name and 
#  average health expenditure. 

Data_HEx = [['Africa', Avg_HEAF1],
        ['Europe', Avg_HEEU1],
        ['North America', Avg_HEAS1],
        ['South America', Avg_HEOC1],
        ['Oceania', Avg_HENA1],
        ['Asia', Avg_HESA1]]

# 18) Put the data into a dataframe called HE_by_Cont. 
HE_by_Cont = pd.DataFrame(Data_HEx, columns =['Cont.', 'Avg. Health Exp.'])

# 19) Print health expenditure by Continent (HE_by_Cont) and save it to a csv file. 
print('\nContinents Average Health Expenditure 2010-2018 (% of GDP):')
print('\n', HE_by_Cont)
HE_by_Cont.to_csv("Continents Average Health Expenditure 2010-2018.csv", index=False)

# 20) set 'Cont.' as the index of HE_by_Cont
HE_by_Cont = HE_by_Cont.set_index('Cont.')

# 21) Create and save a histogram using 'Avg. Health Exp.' column of HE_by_Cont. 
fig, ax1 = plt.subplots()
bars = ['Avg. Health Exp.']
HE_by_Cont[bars].plot.bar(ax=ax1, color ='orange')
fig.suptitle("Avg. Health Exp.(% of GDP)")
ax1.set_xlabel("Continents")
ax1.set_ylabel('(% of GDP)')
fig.tight_layout() 
fig.savefig("Avg. Health Exp.", dpi=300)

# 22) Create GDP by reading World_GDP2021 csv input file and use an inner join to attach it to HE_by_Cont. 
GDP= pd.read_csv('World_GDP2021.csv')
HE_by_Cont = HE_by_Cont.merge(GDP, 
                      on="Cont.", 
                      how='inner', 
                      validate='1:m')


# 23) create a new column in HE_by_Cont called "2021 Health Exp. (US $ Billions)". 
HE_by_Cont["2021 Health Exp. (US $ Billions)"] = HE_by_Cont["Avg. Health Exp."]*HE_by_Cont["GDP (US$billion) 2021"]/100

# 24) Create and save a histogram using "2021 Health Exp. (US $ Billions)" column of HE_by_Cont. 
HE_by_Cont = HE_by_Cont.set_index('Cont.')
fig, ax1 = plt.subplots()
bars = ["2021 Health Exp. (US $ Billions)"]
HE_by_Cont[bars].plot.bar(ax=ax1, color ='blue')
fig.suptitle("Estimated 2021 Health Expenditure")
ax1.set_xlabel("Continents")
ax1.set_ylabel('US $ Billion')
fig.tight_layout() 
fig.savefig("Estimated 2021 Health Expenditure", dpi=300)

# 25) print continents estimated health expenditure in 2021 (HE_by_Cont)
print('\nContinents Estimated Health Exp. 2021:')
print('\n', HE_by_Cont)

# 26) Create pop_sum by reading population_summary csv input file and use an inner join to attach it to HE_by_Cont. 
pop_sum= pd.read_csv('population_summary.csv')
pop_sum['Cont.'] = pop_sum['Continent']
pop_exp = pop_sum.merge(HE_by_Cont, 
                      on="Cont.", 
                      how='inner', 
                      validate='1:m')

# 27) drop 'Cont.' column of pop_exp
pop_exp.drop(pop_exp.columns[4],axis=1,inplace=True)

# 28) print Continents Population and Estimated Health Exp . 2021 
print('\nContinents Population and Estimated Health Exp . 2021:')
print('\n', pop_exp[['Continent', 'Population (billions)', '2021 Health Exp. (US $ Billions)']]) 

