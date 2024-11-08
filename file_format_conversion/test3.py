import os
import shutil
import io
import codecs
import warnings
import re
import pandas as pd
import focusdatatypes

# satwave_ascii = open('C:\\Users\\GEECI\\Desktop\\satwave.satwave','r',encoding="utf-8")
# satwave_data = str(satwave_ascii.read())
# satwave_data_lines = open('C:\\Users\\GEECI\\Desktop\\satwave.satwave','r').readlines()


# # print(satwave_data)


# header_start_string = '! TITLES:   '

# ###########################
# # https://dzone.com/articles/finding-line-number-when
# src = satwave_data
# pattern = header_start_string
# for m in re.finditer(pattern, src):
# 	start = m.start()
# 	lineno = src.count('\n', 0, start) + 1
# ###########################


# header_line_index = lineno-1

# header_line = satwave_data_lines[header_line_index]


# df = pd.read_csv(io.StringIO(header_line), sep='\\s+')

# # print(df.columns[3])
# # print(len(df.columns))

# # print(len(satwave_data_lines))

# dat1 = pd.read_csv(io.StringIO(satwave_data_lines[header_line_index + 2]), sep='\\s+')
# # print(dat1.columns[1])

# pwr_swp_dataframe = pd.DataFrame(columns = df.columns[2:].to_list())

# print(pwr_swp_dataframe)


