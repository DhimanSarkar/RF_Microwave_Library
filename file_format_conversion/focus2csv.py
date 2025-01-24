# license: AGPLv3
# github repo: https://github.com/DhimanSarkar/RF_Microwave_Library/

import focusdatatypes
import tkinter
import tkinter.filedialog
import re

root = tkinter.Tk()
root.wm_attributes("-topmost", 1)
root.withdraw()

ifMore = True

while(ifMore == True):
    file_path = tkinter.filedialog.askopenfilenames(parent=root, title='Choose a Focus Microwaves Data File', filetypes=[("Focus Microwaves Data File", "*.satwave"),("Focus Microwaves Data File", "*.lpcwave"),("Focus Microwaves Data File", "*.lpwave")])
    file = list(file_path)
    


    for i in range(1,len(file)+1):
        focusData = focusdatatypes.data()
        filename = file[i-1]
        fileext = re.search(r'(?i)(.(lp)?(lpc)?(sat)?wave$)', filename).group(1)

        if(fileext.lower() == '.lpcwave'):
            focusData.parseLPCWAVE(file = file[i-1], type=fileext)
        elif(fileext.lower() == '.lpwave'):
            focusData.parseLPWAVE(file = file[i-1], type=fileext)
        elif(fileext.lower() == '.satwave'):
            focusData.parseSATWAVE(file = file[i-1], type=fileext)
        else:
            print('Wrong data format selected')

        print(filename)
        data_csv = focusData.dataframe.to_csv(index=False)
        open(str(file[i-1] + '.csv'),'w').write(''.join(focusData.attrs['metadata']))
        focusData.dataframe.to_csv(str(file[i-1]) + '.csv', index=False,  mode='a', float_format='%.10f')
        focusData.dataframe.to_html(str(file[i-1]) + '.html', index=False)


    root.geometry("300x200") 
    w = tkinter.Label(root, text ='GeeksForGeeks', font = "50")  
    w.pack() 
    ifMore= tkinter.messagebox.askyesno("more...", "More files to covert?") 