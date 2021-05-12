import pandas as pd
import matplotlib.pyplot as plt

World_pop = pd.read_csv('World_POP.csv') 
Continent_pop = pd.read_csv('C and C.csv')

merged_pop = World_pop.merge(Continent_pop, 
                      on="Country", 
                      how='inner', 
                      validate='1:m')

cont_Column = merged_pop.pop('Cont.')
merged_pop.insert(1, 'Cont.', cont_Column)
merged_pop = merged_pop.drop_duplicates(subset=['Population -2020'])

Top_ten_POP = merged_pop.nlargest(10, ['Population -2020'])
print('\nTop 10 Countries- Total Population:')
print('\n',Top_ten_POP[['Country', 'Cont.','Population -2020']])