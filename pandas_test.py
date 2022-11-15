
import numpy as np
import pandas as pd
import re

# np_nump_array = np.random.rand(3)
# type(np_nump_array)
# print(np_nump_array)

# my_series = pd.Series(data= np_nump_array, index=['a', 'b', 'c'])
# print(my_series)
# print(my_series.index)

# np_array_2d = np.random.rand(3,2)


# df = pd.DataFrame(data= np_array_2d,index=["first","second","third"] )
# df.columns =  ['a', 'b']

# print(df)
# print(my_series.index)

#df = pd.read_csv(r'C:\Users\insre\OneDrive\Desktop\python\pokemon_data.csv')
#df = pd.read_excel(r'C:\Users\insre\OneDrive\Desktop\python\pokemon_data.xlsx')
df = pd.read_csv(r'C:\Users\insre\OneDrive\Desktop\python\pokemon_data.txt',delimiter='\t')

#print(df.head(3))
#print(df.tail(5))

########### read headers

#print(df.columns)

########### read each columns

#print(df[['Name',"Type 1","Attack"]])
#print(df.Name)

########### read each row
# print(df.iloc[1:4])

########### read a specific location

#print(df.iloc[2,1])

# for index,row in df.iterrows():
#     print(index,row['Name'])
# print(df.loc[df["Type 1"]== 'Fire'])
# print(df.describe())

########### sorting

#print(df.sort_values(['Name','Type 1'],ascending=[1,0]))

df['Total'] = df['HP'] + df['Attack'] + df['Defense'] + df['Sp. Atk'] + df['Sp. Def'] + df['Speed']

# print(df)

# df = df.drop(columns=['Total'])


# df['Total'] = df.iloc[:, 4:10].sum(axis=1)

# cols = list(df.columns)
# df = df[cols[0:4] + [cols[-1]]+cols[4:12]]

# df.head(5)
# print(df)


########### saving

#df.to_csv(r'C:\Users\insre\OneDrive\Desktop\python\modified.csv', index=False)

#df.to_excel('modified.xlsx', index=False)

#df.to_csv('modified.txt', index=False, sep='\t')


########### filtering data & regex


#new_df = df.loc[(df['Type 1'] == 'Grass') & (df['Type 2'] == 'Poison') & (df['HP'] > 70)]

#new_df = df.loc[(df['Name'].str.contains('Mega'))]

#new_df = df.loc[(df['Type 1'].str.contains('fire|grass',flags =re.I, regex=True))]


#new_df=df.loc[df['Type 1'] == 'Fire','Type 1'] ="Flamer"
print(df)
new_df = df.loc[df['Total'] > 500 ,['Generation','Type 1']] = ['Test','Value']


#new_df = df.loc[(df['Name'].str.contains('^pi[a-z]*',flags =re.I, regex=True))]

#new_df = df.loc[(df['Type 1'].str.contains('^fl[a-z]*',flags =re.I, regex=True))]

#new_df.reset_index(drop=True, inplace=True)
print(df.groupby(['Type 1', 'Type 2']).count()['#'])
new_df =df.groupby(['Type 1']).mean().sort_values('Defense',ascending=False)
print(new_df)



#new_df.to_csv('filtered.csv')