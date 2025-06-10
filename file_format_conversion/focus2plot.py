import matplotlib.pyplot
import focusdatatypes
import tkinter
import tkinter.filedialog
import re
import matplotlib
import numpy



# root = tkinter.Tk()
# root.wm_attributes("-topmost", 1)
# root.withdraw()

# ifMore = True

# while(ifMore == True):
#     file_path = tkinter.filedialog.askopenfilenames(parent=root, title='Choose a Focus Microwaves Data File', filetypes=[("Focus Microwaves Data File", "*.satwave"),("Focus Microwaves Data File", "*.lpcwave"),("Focus Microwaves Data File", "*.lpwave")])
#     file = list(file_path)
    
#     for i in range(1,len(file)+1):
#         focusData = focusdatatypes.data()
#         filename = file[i-1]
#         fileext = re.search(r'(?i)(.(lp)?(lpc)?(sat)?wave$)', filename).group(1)

#         if(fileext.lower() == '.lpcwave'):
#             focusData.parseLPCWAVE(file = file[i-1], type=fileext)
#         elif(fileext.lower() == '.lpwave'):
#             focusData.parseLPWAVE(file = file[i-1], type=fileext)
#         elif(fileext.lower() == '.satwave'):
#             focusData.parseSATWAVE(file = file[i-1], type=fileext)
#         else:
#             print('Wrong data format selected')

#         print(filename)

#         metadata = focusData.attrs['metadata']  # Expecting string or array/list of string
#         data = focusData.dataframe              # Expecting pandas.dataframe


# Plot Smith_Chart
r = numpy.arange(0, 2, 0.01)
theta = 2 * numpy.pi * r

sm = matplotlib.pyplot

# sm.polar()
# sm.thetagrids(angles=[])    # setting theta axis labels off
# sm.rgrids(radii=[])         # setting radius axis labes off

sm.plot()
sm.grid(visible=False)      # setting polar grid off
sm.box()
sm.xticks([])
sm.yticks([])
sm.xlim([-1,1])
sm.ylim([-1,1])
sm.gca().set_aspect("equal")


# Constant Resistance circles
rL_list = [0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1, 1.2, 1.4, 1.6, 1.8, 2, 2.5, 3, 4, 5, 10]
deg = numpy.linspace(-numpy.pi, numpy.pi, 1000)
rad = numpy.ones(1000)

for rL in rL_list:
    x_shift = rL/(1+rL)
    const_rad = 1/(1+rL)
    [x,y] = [const_rad*rad*numpy.cos(deg)+x_shift, const_rad*rad*numpy.sin(deg)]
    sm.plot(x,y, color='gray', lw=0.5)

# Constant Reactance Circles
xL_list = [ -0.1, -0.2, -0.3, -0.45, -0.7, -1, -1.5, -2, -2.5, -3, -4, -5, -10, 10, 5, 4, 3, 2.5, 2, 1.5, 1, 0.7, 0.45, 0.3, 0.2, 0.1]
deg = numpy.linspace(-numpy.pi, numpy.pi, 1000)
rad = numpy.ones(1000)

for xL in xL_list:
    x_shift = 1
    y_shift = 1/xL
    const_rad = 1/xL
    [x,y] = [const_rad*rad*numpy.cos(deg)+x_shift, const_rad*rad*numpy.sin(deg)+y_shift]
    sm.plot(x,y, color='gray', lw=0.5)

matplotlib.pyplot.show()
