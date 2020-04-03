#!/usr/bin/env python
'''
Viewer for Fortran-datafile
'''

import PySimpleGUI       as sg
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D # eigentlich ab 3.2.0 nicht nötig
import numpy             as np
import os                # os.path.join

SOURCE_FILE = os.path.join("data", "coo.dat")

def create_layout():
    return [
        [sg.Text('N-body data viewer')],
        [sg.Text("Planeten-Nummer:"),      sg.InputText( "7", key="bodynr", size=(3,1))],
        [sg.Text("x axis:"), sg.InputText("1", key="xnr", size=(3,1))], # combo !
        [sg.Text("y axis:"), sg.InputText("2", key="ynr", size=(3,1))], # combo !
        [sg.Text("z axis:"), sg.InputText("0", key="znr", size=(3,1))], # combo !
        [sg.Ok(), sg.Cancel()],
        [sg.Text("Number of last lines to show:"), sg.InputText("10", key="linesnr", size=(7,1)),
         sg.Button("Show")],
        ]

layout = create_layout()
window = sg.Window("Viewer window",location=(200,200)).Layout(layout)

data = {"x":[], "y":[], "z":[]}

while True:
    event, values = window.read()
    print("=== event:", event, "===")
    if event in [None, "Cancel"]:
        break
    if event == "Ok":
        body_nr = int(values["bodynr"])
        x_nr = int(values["xnr"])
        y_nr = int(values["ynr"])
        z_nr = int(values["znr"])
        dim3 = (z_nr != 0) # 3D: 3-DIMensional
        print("body_nr:", body_nr)
        print("dim3:   ", dim3)
        #counter = 0
        with open(SOURCE_FILE) as sf:
            for number, line in enumerate(sf):
                #print("number:", number)
                #print("line:", line)
                if number < 7: # 1st 6 lines commentary
                    continue
                fields = line.split() # separation by any whitespace
                #print("fields:", fields)
                #input()
                if int(fields[0]) != body_nr:
                    continue # for-loop -> next number, line
                #counter += 1
                #print(f"Got {counter}. datapoint:")
                #print(" x-value:", fields[x_nr])
                #print(" y-value:", fields[y_nr])
                data["x"].append(float(fields[x_nr]))
                data["y"].append(float(fields[y_nr]))
                if dim3:
                    data["z"].append(float(fields[z_nr]))
                    #print(" z-value:", fields[z_nr])
                #print("len(data['x']):", len(data['x']))
                #print("len(data['y']):", len(data['y']))
                #print("len(data['z']):", len(data['z']))
                #input()
            #end for
        #end with
        #input()
        print("len(data['x']):", len(data['x']))
        print("len(data['y']):", len(data['y']))
        print("len(data['z']):", len(data['z']))
    if event == "Show":
        if len(data['x']) == 0 or len(data['y']) == 0:
            sg.Popup("No data read!")
            continue
        lines_nr = int(values["linesnr"])
        visual_data = {'x':data["x"][-lines_nr:],
                       'y':data["y"][-lines_nr:],
                       'z':data["z"][-lines_nr:]}
        print("len(visual_data['x']:",len(visual_data['x']))
        if dim3:
            fig = plt.figure()
            ax = fig.add_subplot(111, projection='3d')
            ax.plot(visual_data["x"],visual_data["y"],visual_data["z"], '.')
        else:
            plt.plot(visual_data["x"],visual_data["y"])
        plt.show()
print("Bye")
