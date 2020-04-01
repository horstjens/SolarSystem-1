#!/usr/bin/env python
'''
Viewer for Fortran-datafile
'''

import PySimpleGUI as sg
import matplotlib.pyplot as plt
import numpy as np
import os


SOURCEFILE = os.path.join("data", "coo.dat")

def create_layout():
    return [
        [sg.Text('N-body data viewer', size=(30, 1))],
         [sg.Text("body nr"), sg.InputText("7", size=(3,1), key="bodynr")],
         [sg.Text("lines"), sg.InputText("1000", size=(3,1), key="lines")],
         [sg.Text("xfeld"), sg.InputText("1", size=(3,1), key="x")],
         [sg.Text("yfeld"), sg.InputText("2", size=(3,1), key="y")],
         [sg.Text("zfeld"), sg.InputText("3", size=(3,1), key="z")],
         [sg.Ok(),sg.Cancel()],
        ]

layout = create_layout()
window = sg.Window("Viewer window",location=(100,100)).Layout(layout)
cols= "xyz"
while True:
    event, values = window.read()
    print("=== event:", event, "===")
    if event in [None, "Cancel"]:
        break
    if event == "Ok":
        data = {"x":[], "y": [], "z":[]}
        with open(SOURCEFILE) as f:
            for number, line in enumerate(f):
                if number < 7:
                    continue
                fields = line.split(" ")
                print(fields)
                counter = -1 
                for field in fields:
                    if field == "":
                        continue
                    counter += 1
                    #print("counter, field;",counter, field)
                    #input("...")
                    if counter == 0:   # body spalte, index 0
                        body = int(field)
                        if int(values["bodynr"]) != body:
                            break
                    if counter == int(values["x"]):
                        data["x"].append(float(field))
                    elif counter == int(values["y"]):
                        data["y"].append(float(field))
                    elif counter == int(values["z"]):
                        data["z"].append(float(field))
        input("x")
        print(data["x"])
        input("y")
        print(data["y"])
                    
                    
                    
                    
                
                
            

print("Bye")
