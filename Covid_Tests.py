import pandas as pd
import matplotlib.pyplot as plt


Vaccine = pd.read_csv('Covid_wrld.csv')
Continents = pd.read_csv('C and C.csv')

Vac_Country = Vaccine.merge(Continents, 
                      on="Country", 
                      how='inner', 
                      validate='1:m')

Vac_Country.drop(Vaccine.iloc[:,2:11], inplace = True, axis = 1)
Vac_Country.drop(Vac_Country.columns[0],axis=1,inplace=True)
index = Vac_Country.pop('Cont.')
Vac_Country.insert(1, 'Cont.', index)
Vac_Country = Vac_Country.set_index('Country')
Vac_Country = Vac_Country.drop_duplicates(subset=['Total Tests'])

Top_ten_vac = Vac_Country.nlargest(10, ['Total Tests'])
print('\nTop 10 Countries- Total Covid Tests:')
print('\n',Top_ten_vac[['Cont.','Total Tests']])

Top_ten_VM = Vac_Country.nlargest(10, ['Tests/1M pop'])
print('\nTop 10 Countries- Tests per 1M pop:')
print('\n',Top_ten_VM[['Cont.','Tests/1M pop']])

Africa1 = Vac_Country.loc[Vac_Country['Cont.'] == 'Africa']
TT_Afr = Africa1["Total Tests"]
Total_Tests_Afr = TT_Afr.sum()
TTM_Afr = Africa1["Tests/1M pop"]
TT_perM_Afr = TTM_Afr.sum()
Avgtt_Afr = round(Total_Tests_Afr/len(Africa1),2)

Europe1 = Vac_Country.loc[Vac_Country['Cont.'] == 'Europe']
TT_Euro = Europe1["Total Tests"]
Total_Tests_Euro = TT_Euro.sum()
TTM_Euro = Europe1["Tests/1M pop"]
TT_perM_Euro = TTM_Euro.sum()
Avgtt_Euro = round(Total_Tests_Euro/len(Europe1),2)

Asia1 = Vac_Country.loc[Vac_Country['Cont.'] == 'Asia']
TT_Asia = Asia1["Total Tests"]
Total_Tests_Asia = TT_Asia.sum()
TTM_Asia = Asia1["Tests/1M pop"]
TT_perM_Asia = TTM_Asia.sum()
Avgtt_Asia = round(Total_Tests_Asia/len(Asia1),2)

NTAmerica = Vac_Country.loc[Vac_Country['Cont.'] == 'North America']
TT_NAm = NTAmerica["Total Tests"]
Total_Tests_NAm = TT_NAm.sum()
TTM_NAm = NTAmerica["Tests/1M pop"]
TT_perM_NAm = TTM_NAm.sum()
Avgtt_NAm = round(Total_Tests_NAm/len(NTAmerica),2)

STAmerica = Vac_Country.loc[Vac_Country['Cont.'] == 'South America']
TT_SAm = STAmerica["Total Tests"]
Total_Tests_SAm = TT_SAm.sum()
TTM_SAm = STAmerica["Tests/1M pop"]
TT_perM_SAm = TTM_SAm.sum()
Avgtt_SAm = round(Total_Tests_SAm/len(STAmerica),2)


Oceania1 = Vac_Country.loc[Vac_Country['Cont.'] == 'Oceania']
TT_Oce = Oceania1["Total Tests"]
Total_Tests_Oce = TT_Oce.sum()
TTM_Oce = Oceania1["Tests/1M pop"]
TT_perM_Oce = TTM_Oce.sum()
Avgtt_Oce = round(Total_Tests_Oce/len(Oceania1),2)


World_Tests = [Total_Tests_Afr, Total_Tests_Euro, Total_Tests_Asia,
               Total_Tests_NAm, Total_Tests_SAm, Total_Tests_Oce]
World_TT = sum(World_Tests)
print('\nTotal World Covid Tests:', World_TT)


Data_Tests = [['Africa', Total_Tests_Afr, TT_perM_Afr, Avgtt_Afr, round((Total_Tests_Afr/ World_TT*100), 2)],
        ['Europe', Total_Tests_Euro, TT_perM_Euro, Avgtt_Euro, round(Total_Tests_Euro/ World_TT*100, 2)],
        ['North America', Total_Tests_NAm, TT_perM_NAm, Avgtt_NAm, round(Total_Tests_NAm/ World_TT*100, 2)],
        ['South America', Total_Tests_SAm, TT_perM_SAm,  Avgtt_SAm, round(Total_Tests_SAm/ World_TT*100, 2)],
        ['Oceania', Total_Tests_Oce, TT_perM_Oce, Avgtt_Oce, round(Total_Tests_Oce/ World_TT*100, 2)],
        ['Asia', Total_Tests_Asia, TT_perM_Asia, Avgtt_Asia, round(Total_Tests_Asia/ World_TT*100, 2)]]


Tests_by_Cont = pd.DataFrame(Data_Tests, columns = ['Cont.',
                                              'Tot. Tests',
                                              'Tests /1M pop',
                                              'Avg. N. Tests',
                                              '% of Glob. Tests'])


print('\nCovid Tests by Continent:')
print('\n', Tests_by_Cont)
Tests_by_Cont.to_csv("TestsbyContinent.csv", index=False)

Tests_by_Cont = Tests_by_Cont.set_index('Cont.')

fig, ax1 = plt.subplots()
bars = ['Tot. Tests']
Tests_by_Cont[bars].plot.bar(ax=ax1, color ='grey')
fig.suptitle("Total Covid Tests by Continent")
ax1.set_xlabel("Continents")
ax1.set_ylabel("Covid Tests")
fig.tight_layout() 
fig.savefig("World-Tests", dpi=300)


fig, ax1 = plt.subplots()
bars = ['% of Glob. Tests']
Tests_by_Cont[bars].plot.bar(ax=ax1, color ="green")
fig.suptitle(" Continent % of World tests")
ax1.set_xlabel("Continents")
ax1.set_ylabel("% Covid Tests")
fig.tight_layout() 
fig.savefig("Continent_Share_Tests", dpi=300)


# Creating dataset
Cont = ['Africa', 'Europe','Oceania', 'N-America', 'S-America', 'Asia']
  
data = [1.99, 28.46, 0.88, 22.96, 4.87, 40.84]
  
# Creating explode data
explode = (0.5, 0.0, 0.0, 0.0, 0.0, 0.0)
  
# Creating color parameters
colors = ( "red", "grey", "yellow",
          "orange", "brown", "pink")
  
# Wedge properties
wp = { 'linewidth' : 4, 'edgecolor' : "white" }
  
# Creating autocpt arguments
def func(pct, allvalues):
    return "{:.1f}%\n".format(pct)
  
# Creating plot
fig, ax = plt.subplots(figsize =(10, 10))
wedges, texts, autotexts = ax.pie(data, 
                                  autopct = lambda pct: func(pct, data),
                                  explode = explode, 
                                  labels = Cont,
                                  shadow = True,
                                  colors = colors,
                                  startangle = 150,
                                  wedgeprops = wp,
                                  textprops = dict(color ="black"))
  
# Adding legend
ax.legend(wedges, Cont,
          prop={"size":20},
          title ="Continents",
          loc ="center right",
          bbox_to_anchor =(1, 0, 0.5, 1))
  
plt.setp(autotexts, size = 20, weight ="bold")
ax.set_title("Continent % of World Covid Tests", fontsize=30)

#save fig.
plt.savefig('Continent_Share_Tests.png')
















