import os
import shutil
import io
import codecs
import warnings
import re
import pandas


class data():
    def __init__(self,*args,**kwargs):
        hii_message = r'Under Development. If your focus measurement data contains skipped data, this may result in wrong exported data.'
        print(hii_message)

        self.dataframe = False
        self.attrs = {}
        pass
    def __del__(self,*args,**kwargs):
        bye_message = r''
        print(bye_message)
        pass

    def parse(self,*args,**kwargs):
        if(kwargs['type'] == 'power_sweep_data'):
            pass
        elif(kwargs['type'] == 'load_pull_data'):
            pass
        else:
            print('Wrong data format selected')
            return 0
        return self

    def parsePS(self,*args,**kwargs):
        # if 'file' exists and 'type' satwave/powersweep
        data_ascii = open(kwargs['file'], 'r',encoding="utf-8")
        data_string = str(data_ascii.read())
        data_line = open(kwargs['file'], 'r').readlines()

        header_start_string = '!\\sTITLES:\\s*'
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

        header_dataframe = pandas.read_csv(io.StringIO(data_line[header_line_index-1]), sep='\\s+')
        self.dataframe = pandas.DataFrame(columns=header_dataframe.columns[2:].to_list())

        _j = 0
        for i in range(header_line_index + 1, len(data_line)):
            _data = pandas.read_csv(io.StringIO(data_line[i]), sep='\\s+', header=None, float_precision='high').loc[0].fillna(0).to_list()
            self.dataframe.loc[_j] = _data
            _j = _j + 1

        powerIndex_col = self.dataframe.pop("PowerIndex")
        self.dataframe.insert(0, "PowerIndex", powerIndex_col)

        return self

    def parseLP(self,*args,**kwargs):
        # if 'file' exists and 'type' lpcwave/loadpull
        data_ascii = open(kwargs['file'], 'r',encoding="utf-8")
        data_string = str(data_ascii.read())
        data_line = open(kwargs['file'], 'r').readlines()

        header_start_string = 'Point\\s*Gamma'
        ###########################
        # https://dzone.com/articles/finding-line-number-when
        src = data_string
        pattern = header_start_string
        for m in re.finditer(pattern, src):
            start = m.start()
            lineno = src.count('\n', 0, start) + 1
        ###########################
        header_line_index = lineno - 1

        data_comment_block = data_line[0:header_line_index-3]
        self.attrs['metadata'] = data_comment_block

        header_dataframe = pandas.read_csv(io.StringIO(data_line[header_line_index]), sep='\\s+')
        header_columns = header_dataframe.columns[3:].to_list()
        header_columns.insert(0,'GammaMag')
        header_columns.insert(1,'GammaAng')

        # https://dzone.com/articles/finding-line-number-when
        src = data_string
        pattern = "#"
        lineno = list()
        for m in re.finditer(pattern, src):
            start = m.start()
            lineno.append(src.count('\n', 0, start))  
        ###########################
        gamaindex = lineno

        self.dataframe = pandas.DataFrame(columns=header_columns)

        gamma_line_regex_pattern = '#\\s*\\d*\\s*(\\d*\\.?\\d*)\\s*(\\-?\\d*\\.?\\d*)'

        k = 0
        for i in range(0,len(gamaindex)):
            if i != len(gamaindex)-1:
                _pwr_index_len = gamaindex[i+1]-gamaindex[i]
            else:
                 _pwr_index_len = len(data_line)-gamaindex[i]

            load_gamma_data = re.match(gamma_line_regex_pattern, data_line[gamaindex[i]])
            load_gamma_mag = load_gamma_data.group(1)
            load_gamma_ang = load_gamma_data.group(2)

            for j in range(0,_pwr_index_len-1):
                _data = pandas.read_csv(io.StringIO(data_line[gamaindex[i]+1+j]), sep='\\s+', header=None, float_precision='high').loc[0].fillna(0).to_list()
                _data.insert(0,float(load_gamma_mag))
                _data.insert(1,float(load_gamma_ang))
                self.dataframe.loc[k] = _data
                k = k+1

        powerIndex_col = self.dataframe.pop("PowerIndex")
        self.dataframe.insert(2, "PowerIndex", powerIndex_col)
        self.dataframe.sort_values(by=['GammaMag', 'GammaAng'], ascending=True, inplace=True)