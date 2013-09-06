#!/usr/bin/env pythonw

import matplotlib as mp
import Tkinter as tk
import ttk
import numpy as np

from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure as MatplotlibFigure

ROOT = tk.Tk()

# STYLE = ttk.Style()
# STYLE.configure('TFrame', background='red')
# print(STYLE.lookup('TFrame','background'))

ICON = """
R0lGODlhIAAgAPcAAAAAAAAAMwAAZgAAmQAAzAAA/wArAAArMwArZgArmQArzAAr/wBVAA
BVMwBVZgBVmQBVzABV/wCAAACAMwCAZgCAmQCAzACA/wCqAACqMwCqZgCqmQCqzACq/wDV
AADVMwDVZgDVmQDVzADV/wD/AAD/MwD/ZgD/mQD/zAD//zMAADMAMzMAZjMAmTMAzDMA/z
MrADMrMzMrZjMrmTMrzDMr/zNVADNVMzNVZjNVmTNVzDNV/zOAADOAMzOAZjOAmTOAzDOA
/zOqADOqMzOqZjOqmTOqzDOq/zPVADPVMzPVZjPVmTPVzDPV/zP/ADP/MzP/ZjP/mTP/zD
P//2YAAGYAM2YAZmYAmWYAzGYA/2YrAGYrM2YrZmYrmWYrzGYr/2ZVAGZVM2ZVZmZVmWZV
zGZV/2aAAGaAM2aAZmaAmWaAzGaA/2aqAGaqM2aqZmaqmWaqzGaq/2bVAGbVM2bVZmbVmW
bVzGbV/2b/AGb/M2b/Zmb/mWb/zGb//5kAAJkAM5kAZpkAmZkAzJkA/5krAJkrM5krZpkr
mZkrzJkr/5lVAJlVM5lVZplVmZlVzJlV/5mAAJmAM5mAZpmAmZmAzJmA/5mqAJmqM5mqZp
mqmZmqzJmq/5nVAJnVM5nVZpnVmZnVzJnV/5n/AJn/M5n/Zpn/mZn/zJn//8wAAMwAM8wA
ZswAmcwAzMwA/8wrAMwrM8wrZswrmcwrzMwr/8xVAMxVM8xVZsxVmcxVzMxV/8yAAMyAM8
yAZsyAmcyAzMyA/8yqAMyqM8yqZsyqmcyqzMyq/8zVAMzVM8zVZszVmczVzMzV/8z/AMz/
M8z/Zsz/mcz/zMz///8AAP8AM/8AZv8Amf8AzP8A//8rAP8rM/8rZv8rmf8rzP8r//9VAP
9VM/9VZv9Vmf9VzP9V//+AAP+AM/+AZv+Amf+AzP+A//+qAP+qM/+qZv+qmf+qzP+q///V
AP/VM//VZv/Vmf/VzP/V////AP//M///Zv//mf//zP///wAAAAAAAAAAAAAAACH5BAEAAP
wALAAAAAAgACAAAAj/AB9UqCCQ4MCCCA8qNMiw4MAKDg5SMEjB4cOLGDPu28ix48aMIEF6
HBktpMmHI0eevGhhIIcKHFJ6hAnzJQebNjfQLAKkyA8LRSp0rBCUww8jR5PyXNqzpxGBRo
wUidrRCBCpWKdezer0B8KKP37A6fjGSFk1cIyoMWsWCJy0DRcK7Pj27Ru7dX8QjPigYgUK
fiNC7CiQL8EiHoP6PehQ4IOOhitCS6lMYMWJgSEK5ZhwrEw4juMe7Hh5sMyNi0vzpUD4IG
LODh5zHGj46+aNhj3v0/RQ075o+/Q=
"""

class LineFigure(ttk.Frame):

    def __init__(self, master=None):
        ttk.Frame.__init__(self, master)

        bgColor = '#%02x%02x%02x' % tuple([c/255 for c in \
            ROOT.winfo_rgb('SystemButtonFace')])

        self.f = MatplotlibFigure(figsize=(5,4), facecolor=bgColor)
        self.a = self.f.add_subplot(111)

        self.canvas = FigureCanvasTkAgg(self.f, master=self)

        self.widget = self.canvas.get_tk_widget()
        self.widget.config(highlightthickness=0)
        self.widget.config(background=bgColor)
        self.widget.pack(side=tk.TOP, fill=tk.BOTH, expand=True)

        self.canvas.show()

        self.render()

    def render(self):
        t = np.arange(0.0,3.0,0.01)
        s = np.sin(2*np.pi*t)
        line1, = self.a.plot(t, s, color='k')

class GUI(ttk.Frame):

    def __init__(self, master=None):
        ttk.Frame.__init__(self, master)
        self.grid(sticky='NSEW')
        self._initControls()

    def _initControls(self):
        lf, rf = self._initSideBySidePanes(self,
                                            left='Model Configuration',
                                            right='Graphics')
        self._initModelConfigControls(lf)

        figure = LineFigure(rf)
        figure.grid(sticky='NSEW')
        rf.columnconfigure(0, weight=1)
        rf.rowconfigure(0, weight=1)

        # self.columnconfigure(0, weight=0)
        # self.columnconfigure(1, weight=1)
        # self.rowconfigure(0, weight=1)

    def _initSideBySidePanes(self, master, left='', right=''):
        p = ttk.Panedwindow(master, orient=tk.HORIZONTAL)
        p.grid(sticky='NSEW', padx=3, pady=3)
        master.columnconfigure(0, weight=1)
        master.rowconfigure(0, weight=1)
        lf = ttk.Labelframe(p, text=left)
        rf = ttk.Labelframe(p, text=right)
        p.add(lf)
        p.add(rf)
        return (lf,rf)

    def _initModelConfigControls(self, master):
        notebook = ttk.Notebook(master)
        notebook.grid(sticky='NSEW')

        dataProcessFrame = ttk.Frame(notebook, style='My.TFrame')
        self._initDataProcessingControls(dataProcessFrame)
        notebook.add(dataProcessFrame, text='Data')

        calibrationFrame = ttk.Frame(notebook)
        self._initCalibrationControls(calibrationFrame)
        notebook.add(calibrationFrame, text='Calibration')

        progress = ttk.Progressbar(master,
                                   orient=tk.HORIZONTAL,
                                   mode='determinate')
        progress.grid(row=1, column=0, sticky='EW', padx=20)

        button = ttk.Button(master, text=u'Ok', command=self.onOkClicked)
        button.grid(row=2, column=0)

        progress['value'] = 50

        master.columnconfigure(0, weight=1)
        master.rowconfigure(0, weight=1)

        return notebook

    def _initDataProcessingControls(self, master):
        self.entry1 = tk.StringVar()
        entry = ttk.Entry(master, textvariable=self.entry1)
        entry.grid(column=0, row=0, sticky='EW')
        master.columnconfigure(0, weight=1)

        self.combo = tk.StringVar()
        combo = ttk.Combobox(master, textvariable=self.combo, state='readonly')
        combo['values'] = ('one', 'two', 'three')
        combo.current(0)
        combo.grid(column=0, row=2, sticky='EW')

    def _initCalibrationControls(self, master):
        self.entry2 = tk.StringVar()
        entry = ttk.Entry(master, textvariable=self.entry2)
        entry.grid(column=0, row=0, sticky='NEW')

        button = ttk.Button(master, text=u'Ok', command=self.onOkClicked)
        button.grid(column=0, row=1)


    def onOkClicked(self):
        self.entry1.set('Ok pressed.')

ROOT.title('Tropical Cyclone Risk Model')
ROOT.tk.call('wm', 'iconphoto', ROOT._w, tk.PhotoImage(data=ICON))
ROOT.columnconfigure(0, weight=1)
ROOT.rowconfigure(0, weight=1)

app = GUI(master=ROOT)
app.mainloop()
