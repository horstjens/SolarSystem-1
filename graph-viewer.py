#!/usr/bin/env python
'''
Viewer for Fortran-datafile
'''

import PySimpleGUI as sg
import matplotlib.pyplot as plt
import numpy as np

def create_layout():
    return [
        [sg.Text('N-body data viewer', size=(30, 1))],
         [sg.Text("body nr"), sg.InputText("7", size=(3,1), key="bodynr")],
         [sg.Text("lines"), sg.InputText("1000", size=(3,1), key="lines")],
         [sg.Text("x"), sg.InputText("x", size=(3,1), key="lines")],
         [sg.Text("y"), sg.InputText("y", size=(3,1), key="lines")],
         [sg.Text("z"), sg.InputText("z", size=(3,1), key="lines")],
         [sg.Ok(),sg.Cancel()],
        ]

layout = create_layout()
window = sg.Window("Viewer window",location=(100,100)).Layout(layout)

while True:
    event, values = window.read()
    print("=== event:", event, "===")
    if event in [None, "Cancel"]:
        break

print("Bye")
