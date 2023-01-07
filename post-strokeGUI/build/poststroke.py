from tkinter import *
from tkinter.ttk import *
from pathlib import Path
from tkinter import ttk
from tkinter import Tk, Canvas, Entry,Button, PhotoImage
from newWindow import openNewWindow
from classtype import *


def recommend():
    if entry_10.get()=='0' or entry_10.get()=='1':
        if entry_11.get()=='1' or entry_11.get()=='2': 
            if entry_9.get()>='1' and entry_9.get()<='3' or entry_9.get()=='7':
                if entry_8.get()=='4' or entry_8.get()=='6' or entry_8.get()=='7':
                    if entry_7.get()>='1' and entry_7.get()<='4':
                        if entry_2.get()<='2' and entry_2.get()>='0':
                            if entry_1.get()<'2' or entry_1.get()>='0':
                                if entry_3.get()<'2' and entry_3.get()>='0':
                                    if entry_1.get()=='0':
                                        classtype3()
                                    elif entry_1.get()>'0' and entry_1.get()<='4':
                                        if entry_4.get()=='0':
                                            classtype3()
                                        elif entry_4.get()>'0' and entry_4.get()<='4':
                                            classtype3()
                                        else:
                                            furtherevaluation()
                                    else:
                                        furtherevaluation()
                                elif entry_3.get()>'1' and entry_3.get()<='4':
                                    classtype2()
                                else:
                                    furtherevaluation()
                            elif entry_1.get()>='2' and entry_1.get()<='4':
                                if entry_3.get()<='2' and entry_3.get()>='0':
                                    if entry_3.get()<='2' and entry_3.get()>='0':
                                        if entry_2.get()<='2' and entry_2.get()>='0':
                                            if entry_4.get()=='0':
                                                classtype2()
                                            elif entry_4.get()>'0' and entry_4.get()<='4':
                                                if entry_1.get()<='2' and entry_1.get()>='0':
                                                    if entry_2.get()<='2' and entry_2.get()>='0':
                                                        classtype2()
                                                    elif entry_2.get()>='3' and entry_2.get()<='4':
                                                        classtype3()
                                                    else:
                                                        furtherevaluation()
                                                elif entry_1.get()>='3' and entry_1.get()<='4':
                                                    classtype2()
                                            else:
                                                furtherevaluation()
                                        elif entry_2.get()>='3' and entry_2.get()<='4':
                                            classtype1()
                                        else:
                                                furtherevaluation()
                                    elif entry_3.get()>='3' and entry_3.get()<='4':
                                        if entry_2.get()<='2' and entry_2.get()>='0':
                                            if entry_4.get()<='2' and entry_4.get()>='0':
                                                if entry_1.get()<='2' and entry_1.get()>='0':
                                                    classtype2()
                                                elif entry_1.get()>='3' and entry_1.get()<='4':
                                                    classtype2()
                                                else:
                                                    furtherevaluation()
                                            elif entry_4.get()>='3' and entry_4.get()<='4':
                                                classtype2()
                                            else:
                                                furtherevaluation()
                                        elif entry_2.get()>='3' and entry_2.get()<='4':
                                            classtype2()
                                elif entry_3.get()>='3' and entry_3.get()<='4':
                                    if entry_2.get()<='2' and entry_2.get()>='0':
                                        classtype2()
                                    elif entry_2.get()>='3' and entry_2.get()<='4':
                                        if entry_4.get()<='2' and entry_4.get()>='0':
                                            classtype2()
                                        elif entry_4.get()>='3' and entry_4.get()<='4':
                                            if entry_4.get()<='2' and entry_4.get()>='0':
                                                if entry_1.get()<='2' and entry_1.get()>='0':
                                                    classtype1()
                                                elif entry_1.get()>='3' and entry_1.get()<='4':
                                                    classtype1()
                                            elif entry_4.get()>='3' and entry_4.get()<='4':
                                                classtype1()
                        elif entry_2.get()>='3' and entry_2.get()<='4':
                            if entry_4.get()<='2' and entry_4.get()>='0':
                                if entry_3.get()<='2' and entry_3.get()>='0':
                                    classtype1()
                                elif entry_3.get()>='3' and entry_3.get()<='4':
                                    if entry_1.get()<='2' and entry_1.get()>='0':
                                        classtype1()
                                    elif entry_1.get()>='3' and entry_1.get()<='4':
                                        classtype1()
                            elif entry_4.get()>='3' and entry_4.get()<='4':
                                classtype1()
                    else:
                        referscore()
                else:
                    referscore()
            else:
                referscore()
        elif entry_10.get()>'2' or entry_1.get()<'1':
            referscore()
    elif entry_10.get()=='':
        novalues()
    elif entry_10.get()>'1' or entry_1.get()<'0':
        referscore()

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"C:\Users\User\OneDrive\Documents\PrototypeFYP\post-strokeGUI\build\assets\frame0")

def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

window = Tk()
window.title("Post-Stroke Rehabilitation Prediction System")
window.geometry("857x476")

canvas = Canvas(
    window,
    bg = "#FFFFFF",
    height = 476,
    width = 857,
)

canvas.place(x = 0, y = 0)

entry_1 = Entry( #Ambulation when discharging
    bd=0.5,
    bg="#D9D9D9",
)
entry_1.place(
    x=724.0,
    y=225.0,
    width=52.0,
    height=13.0
)

canvas.create_text( #Ambulation when discharging
    501.0,
    225.0,
    anchor="nw",
    text="Ambulation when discharging",
    font=("Inter", 12 * -1)
)

entry_2 = Entry( #Dressing when discharging
    bg="#D9D9D9",
    fg="#000716",
)
entry_2.place(  
    x=724.0,
    y=205.0,
    width=52.0,
    height=13.0
)

canvas.create_text( #Dressing when discharging
    501.0,
    205.0,
    anchor="nw",
    text="Dressing when discharging",
    font=("Inter", 12 * -1)
)

entry_3 = Entry( #Bathing when discharging
    bg="#D9D9D9",
    fg="#000716",
)
entry_3.place(
    x=724.0,
    y=184.0,
    width=52.0,
    height=13.0
)

canvas.create_text( #Bathing when discharging
    501.0,
    184.0,
    anchor="nw",
    text="Bathing when discharging",
    font=("Inter", 12 * -1)
)

canvas.create_text( #Barthel Index at Discharge
    501.0,
    156.0,
    anchor="nw",
    text="Barthel Index at Discharge",
    font=("Inter SemiBold", 14 * -1)
)

entry_4 = Entry( #Ambulation at admission
    bg="#D9D9D9",
    fg="#000716",
)
entry_4.place( 
    x=724.0,
    y=98.0,
    width=52.0,
    height=13.0
)

canvas.create_text( #Ambulation at admission
    501.0,
    98.0,
    anchor="nw",
    text="Ambulation at admission",
    font=("Inter", 12 * -1)
)


canvas.create_text( #Barthel Index at Admission
    501.0,
    70.0,
    anchor="nw",
    text="Barthel Index at Admission",
    font=("Inter SemiBold", 14 * -1)
)

entry_7 = Entry( #Manipulation impairment
    bg="#D9D9D9",
    fg="#000716",
)
entry_7.place(
    x=377.0,
    y=314.0,
    width=52.0,
    height=13.0
)

canvas.create_text( #Manipulation impairment
    154.0,
    314.0,
    anchor="nw",
    text="Manipulation impairment",
    font=("Inter", 12 * -1)
)

canvas.create_text( #Impairment
    154.0,
    286.0,
    anchor="nw",
    text="Impairment",
    font=("Inter SemiBold", 14 * -1)
)

canvas.create_text( #Main pathology
    154.0,
    221.0,
    anchor="nw",
    text="Main pathology",
    font=("Inter SemiBold", 14 * -1)
)

canvas.create_text( #Main pathology
    154.0,
    249.0,
    anchor="nw",
    text="Main pathology",
    font=("Inter", 12 * -1)
)

entry_8 = Entry( #Main pathology
    bg="#D9D9D9",
    fg="#000716"
)
entry_8.place(
    x=377.0,
    y=249.0,
    width=52.0,
    height=13.0
)

canvas.create_text( #Pathology responsible
    154.0,
    156.0,
    anchor="nw",
    text="Pathology responsible for intervention",
    font=("Inter SemiBold", 14 * -1)
)

canvas.create_text( #Pathology responsible
    154.0,
    184.0,
    anchor="nw",
    text="Pathology responsible ",
    font=("Inter", 12 * -1)
)

entry_9 = Entry( #Pathology responsible
    bg="#D9D9D9",
    fg="#000716",
)
entry_9.place(
    x=377.0,
    y=184.0,
    width=52.0,
    height=13.0
)

canvas.create_text( #Demographic Data
    154.0,
    70.0,
    anchor="nw",
    text="Demographic Data",
    font=("Inter SemiBold", 14 * -1)
)

canvas.create_text( #Sex
    154.0,
    98.0,
    anchor="nw",
    text="Sex",
    font=("Inter", 12 * -1)
)

entry_10 = Entry( #Sex
    bg="#D9D9D9",
    fg="#000716"
)
entry_10.place(
    x=377.0,
    y=98.0,
    width=52.0,
    height=13.0
)

canvas.create_text( #Marital Status
    154.0,
    119.0,
    anchor="nw",
    text="Marital Status",
    font=("Inter", 12 * -1)
)

entry_11 = Entry( #Marital Status
    bg="#D9D9D9",
    fg="#000716",
)
entry_11.place(
    x=377.0,
    y=119.0,
    width=52.0,
    height=13.0
)

button_1 = Button(
    text="Recommend",
    borderwidth=0,
    command=recommend
)
button_1.place(
    x=718.0,
    y=355.0,
    width=79.0,
    height=20.0
)


button_2 = Button(
    text="Index/scores",
    borderwidth=0,
    command = openNewWindow
)

button_2.place(
    x=25.0,
    y=77.0,
    width=103.0,
    height=20.0
)

canvas.create_text(
    259.0,
    20.0,
    anchor="nw",
    text="Post-Stroke Rehabilitation Prediction System",
    font=("Inter Bold", 16 * -1)
)
window.resizable(False, False)

mainloop()