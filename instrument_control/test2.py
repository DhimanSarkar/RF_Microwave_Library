# import dataexport
import pandas

# meas_data = dataexport.dataexport()
# meas_data.export2excel(file = 'C:\\Users\\GEECI\\Downloads\\data.xlsx')
# meas_data.put([1,2,3,4,5,6])
# meas_data.put([4,6,2,7,9,3])

df1 = pandas.DataFrame(columns=['pin', 'pout'])
df2 = pandas.DataFrame(columns=['pin', 'pout'])

df1.loc[len(df1.index)] = [1,2]
df1.loc[len(df1.index)] = [3,4]
df2.loc[len(df2.index)] = [5,6]
df2.loc[len(df2.index)] = [7,8]










print(df1)
print(df2)