import os
import shutil
import datetime
import xlwings as xw

class dataexport():
    def __init__(self,*args,**kwargs):
        pass
    def __del__(self):
        self.wb.save()  
        pass

    def export2excel(self,*args,**kwargs):
        now = datetime.datetime.now().strftime('%Y%m%d%H%M%S')

        if hasattr(kwargs,'template'):
            # template = open(kwargs['template'])
            # filename = str(now) + '_' + str(file)
            # file = open(filename,'wb')
            # shutil.copyfileobj(template, file)
            print('not implemented yet!')

        self.wb = xw.Book(kwargs['file'])
        self.sheet = self.wb.sheets['meas_data']
        self.index = self.sheet.range('A5').end('down').row
        return self

    def put(self,data,*args,**kwargs):
        if (len(data) != 6):
            print('Check number of parameters supplied.')
            return 0
        else:
            pass
        i = str(self.index + 1)
        self.sheet.range('A' + i + ':F' + i).value = data
        self.index = int(i)
        return self