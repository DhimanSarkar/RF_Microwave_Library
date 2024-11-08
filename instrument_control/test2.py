import dataexport

meas_data = dataexport.dataexport()
meas_data.export2excel(file = 'C:\\Users\\GEECI\\Downloads\\data.xlsx')
meas_data.put([1,2,3,4,5,6])
meas_data.put([4,6,2,7,9,3])