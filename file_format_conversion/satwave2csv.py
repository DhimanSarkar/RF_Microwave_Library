import focusdatatypes
import tkinter
import tkinter.filedialog

root = tkinter.Tk()
root.withdraw()
file_path = tkinter.filedialog.askopenfilenames(parent=root, title='Choose a file', filetypes=[("Focus Microwaves Data File", "*.satwave")])
file = list(file_path)


for i in range(1,len(file)+1):
    ps = focusdatatypes.data()
    ps.parse(file = file[i-1])
    data_csv = ps.dataframe.to_csv(index=False)
    open(str(file[i-1] + '.csv'),'w').write(''.join(ps.attrs['metadata']))
    ps.dataframe.to_csv(str(file[i-1]) + '.csv', index=False,  mode='a')
    ps.dataframe.to_html(str(file[i-1]) + '.html', index=False)