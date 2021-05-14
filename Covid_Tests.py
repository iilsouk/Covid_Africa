# 1. Import pandas & matplotlib.pyplot
import pandas as pd
import matplotlib.pyplot as plt

# 2. Create "Tests" by reading World Covid Data csv input file. 
# 3. Create "Continents"  by reading List of countries and continents input csv file.

Tests = pd.read_csv('Covid_wrld.csv')
Continents = pd.read_csv('C and C.csv')

# 4. create "Vac_Country" by match countries in "Tests" with their continents using an inner join. 
Vac_Country = Tests.merge(Continents, 
                      on="Country", 
                      how='inner', 
                      validate='1:m')

# 4. drop columns from "Vac_Country" and only keep the columns: 
    # 'Country", 'Cont.', 'Total Tests', and 'Tests/1M pop'..
Vac_Country.drop(Tests.iloc[:,2:11], inplace = True, axis = 1)

# 5. drop the index, then move 'Cont.' to be the second column and set 'Country' as the new index. 
Vac_Country.drop(Vac_Country.columns[0],axis=1,inplace=True)
index = Vac_Country.pop('Cont.')
Vac_Country.insert(1, 'Cont.', index)
Vac_Country = Vac_Country.set_index('Country')

# 5. drop duplicates in Vac_Country using 'Total Tests' as tthe subset. 
Vac_Country = Vac_Country.drop_duplicates(subset=['Total Tests'])

# 6.a) set 'Top_ten_vac' equal to to the top 10 largest values of 'Total Tests' in Vac_Country.
# 6.b) print the 'Country', 'Cont.' and 'Total Tests' columns of Top_ten_vac.
Top_ten_vac = Vac_Country.nlargest(10, ['Total Tests'])
print('\nTop 10 Countries- Total Covid Tests:')
print('\n',Top_ten_vac[['Cont.','Total Tests']])

# 7) follow the same approach to print the data of the Top 10 Countries in terms of tests per 1M people. 
Top_ten_VM = Vac_Country.nlargest(10, ['Tests/1M pop'])
print('\nTop 10 Countries- Tests per 1M pop:')
print('\n',Top_ten_VM[['Cont.','Tests/1M pop']])

# 8.a) Create a dataframe Africa1 which consists of African countries tests Data.
Africa1 = Vac_Country.loc[Vac_Country['Cont.'] == 'Africa']
# 8.B) set TT_Afr equal to the "Total Tests" column of Africa1.
TT_Afr = Africa1["Total Tests"]
# 8.c) set Total_Tests_Afr equal to the sum of TT_Afr.
Total_Tests_Afr = TT_Afr.sum()
# 8.d) set TTM_Afr equal to the "Tests/1M pop" column of Africa1.
TTM_Afr = Africa1["Tests/1M pop"]
# 8.e) set TT_perM_Afr equal to the sum of TTM_Afr.
TT_perM_Afr = TTM_Afr.sum()
# 8.e) set Avgtt_Afr equal to Total_Tests_Afr divided by the number of countries in Africa1.
Avgtt_Afr = round(Total_Tests_Afr/len(Africa1),2)


# 9) Follow the same approach with Europe1.
Europe1 = Vac_Country.loc[Vac_Country['Cont.'] == 'Europe']
TT_Euro = Europe1["Total Tests"]
Total_Tests_Euro = TT_Euro.sum()
TTM_Euro = Europe1["Tests/1M pop"]
TT_perM_Euro = TTM_Euro.sum()
Avgtt_Euro = round(Total_Tests_Euro/len(Europe1),2)

# 10) Follow the same approach with Asia1.
Asia1 = Vac_Country.loc[Vac_Country['Cont.'] == 'Asia']
TT_Asia = Asia1["Total Tests"]
Total_Tests_Asia = TT_Asia.sum()
TTM_Asia = Asia1["Tests/1M pop"]
TT_perM_Asia = TTM_Asia.sum()
Avgtt_Asia = round(Total_Tests_Asia/len(Asia1),2)

# 11) Follow the same approach with NTAmerica.
NTAmerica = Vac_Country.loc[Vac_Country['Cont.'] == 'North America']
TT_NAm = NTAmerica["Total Tests"]
Total_Tests_NAm = TT_NAm.sum()
TTM_NAm = NTAmerica["Tests/1M pop"]
TT_perM_NAm = TTM_NAm.sum()
Avgtt_NAm = round(Total_Tests_NAm/len(NTAmerica),2)

# 12) Follow the same approach with STAmerica.
STAmerica = Vac_Country.loc[Vac_Country['Cont.'] == 'South America']
TT_SAm = STAmerica["Total Tests"]
Total_Tests_SAm = TT_SAm.sum()
TTM_SAm = STAmerica["Tests/1M pop"]
TT_perM_SAm = TTM_SAm.sum()
Avgtt_SAm = round(Total_Tests_SAm/len(STAmerica),2)

# 13) Follow the same approach with Oceania1.
Oceania1 = Vac_Country.loc[Vac_Country['Cont.'] == 'Oceania']
TT_Oce = Oceania1["Total Tests"]
Total_Tests_Oce = TT_Oce.sum()
TTM_Oce = Oceania1["Tests/1M pop"]
TT_perM_Oce = TTM_Oce.sum()
Avgtt_Oce = round(Total_Tests_Oce/len(Oceania1),2)


# 14) create a list called World_Tests which consists of continents' total covid tests.  
World_Tests = [Total_Tests_Afr, Total_Tests_Euro, Total_Tests_Asia,
               Total_Tests_NAm, Total_Tests_SAm, Total_Tests_Oce]

# 15) create World_TT equal to the sum of World_Tests
World_TT = sum(World_Tests)

# 16) print the total number of covid test in the world (World_TT)
print('\nTotal World Covid Tests:', World_TT)

# 17) Create a list called Data_Tests consisting of each continent's name, 
# total covid tests, number of tests per 1M pop, and its share of world tests. 

Data_Tests = [['Africa', Total_Tests_Afr, TT_perM_Afr, Avgtt_Afr, round((Total_Tests_Afr/ World_TT*100), 2)],
        ['Europe', Total_Tests_Euro, TT_perM_Euro, Avgtt_Euro, round(Total_Tests_Euro/ World_TT*100, 2)],
        ['North America', Total_Tests_NAm, TT_perM_NAm, Avgtt_NAm, round(Total_Tests_NAm/ World_TT*100, 2)],
        ['South America', Total_Tests_SAm, TT_perM_SAm,  Avgtt_SAm, round(Total_Tests_SAm/ World_TT*100, 2)],
        ['Oceania', Total_Tests_Oce, TT_perM_Oce, Avgtt_Oce, round(Total_Tests_Oce/ World_TT*100, 2)],
        ['Asia', Total_Tests_Asia, TT_perM_Asia, Avgtt_Asia, round(Total_Tests_Asia/ World_TT*100, 2)]]

# 18) Put the data into a dataframe called Tests_by_Cont. 
Tests_by_Cont = pd.DataFrame(Data_Tests, columns = ['Cont.',
                                              'Tot. Tests',
                                              'Tests /1M pop',
                                              'Avg. N. Tests',
                                              '% of Glob. Tests'])

# 19) Print Covid test Data by Continent (Tests_by_Cont) and save it to a csv file. 
print('\nCovid Tests by Continent:')
print('\n', Tests_by_Cont)
Tests_by_Cont.to_csv("TestsbyContinent.csv", index=False)

# 20) set 'Cont.' as the index of Tests_by_Cont 
Tests_by_Cont = Tests_by_Cont.set_index('Cont.')

# 21) Create and save a histogram using 'Tot. Tests' column of Tests_by_Cont. 
fig, ax1 = plt.subplots()
bars = ['Tot. Tests']
Tests_by_Cont[bars].plot.bar(ax=ax1, color ='grey')
fig.suptitle("Total Covid Tests by Continent")
ax1.set_xlabel("Continents")
ax1.set_ylabel("Covid Tests")
fig.tight_layout() 
fig.savefig("World-Tests", dpi=300)

# 22)Create and save a pie chart of continents' share of world tests.
 
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
















