import os
import shutil
import io
import codecs
import warnings
import re
import pandas as pd


class data():
    def __init__(self,*args,**kwargs):
        self.dataframe = False
        self.attrs = {}
        pass
    def __del__(self,*args,**kwargs):
        pass

    def parse(self,*args,**kwargs):
        # if 'file' exists and 'type' satwave/powersweep
        data_ascii = open(kwargs['file'], 'r',encoding="utf-8")
        data_string = str(data_ascii.read())
        data_line = open(kwargs['file'], 'r').readlines()

        header_start_string = '! TITLES:'
        ###########################
        # https://dzone.com/articles/finding-line-number-when
        src = data_string
        pattern = header_start_string
        for m in re.finditer(pattern, src):
            start = m.start()
            lineno = src.count('\n', 0, start) + 1
        ###########################
        header_line_index = lineno

        data_comment_block = data_line[0:header_line_index-3]
        self.attrs['metadata'] = data_comment_block

        header_dataframe = pd.read_csv(io.StringIO(data_line[header_line_index-1]), sep='\\s+')
        self.dataframe = pd.DataFrame(columns=header_dataframe.columns[2:].to_list())

        _j = 0
        for i in range(header_line_index + 1, len(data_line)):
            _data = pd.read_csv(io.StringIO(data_line[i]), sep='\\s+', header=None).loc[0].fillna(0).to_list()
            self.dataframe.loc[_j] = _data
            _j = _j + 1

        powerIndex_col = self.dataframe.pop("PowerIndex")
        self.dataframe.insert(0, "PowerIndex", powerIndex_col)
