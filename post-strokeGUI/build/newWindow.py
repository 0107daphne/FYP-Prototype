from tkinter import *
from tkinter import Canvas


def openNewWindow():
    newWindow = Toplevel()
    newWindow.title("Index Scoring References")
    newWindow.geometry("869x689")
    newWindow.configure(bg = "#FFFFFF")


    canvas = Canvas(
        newWindow,
        bg = "#FFFFFF",
        height = 745,
        width = 847,
        bd = 0,
        highlightthickness = 0,
        relief = "ridge"
    )

    canvas.place(x = 0, y = 0)
    canvas.create_rectangle(
        377.0,
        564.0,
        770.0,
        680.0,
        fill="#D9D9D9",
        outline="")

    canvas.create_text(
        397.0,
        574.0,
        anchor="nw",
        text="Scores",
        fill="#000000",
        font=("Inter Medium", 12 * -1)
    )

    canvas.create_text(
        473.0,
        576.0,
        anchor="nw",
        text="Manipulation Impairment",
        fill="#000000",
        font=("Inter Medium", 12 * -1)
    )

    canvas.create_text(
        473.0,
        594.0,
        anchor="nw",
        text="no difficulties",
        fill="#000000",
        font=("Inter", 12 * -1)
    )

    canvas.create_text(
        473.0,
        612.0,
        anchor="nw",
        text="difficulty in prehension of upper limb right side",
        fill="#000000",
        font=("Inter", 12 * -1)
    )

    canvas.create_text(
        473.0,
        630.0,
        anchor="nw",
        text="difficulty in prehension of upper limb left side",
        fill="#000000",
        font=("Inter", 12 * -1)
    )

    canvas.create_text(
        397.0,
        631.0,
        anchor="nw",
        text="3",
        fill="#000000",
        font=("Inter SemiBold", 12 * -1)
    )

    canvas.create_text(
        473.0,
        648.0,
        anchor="nw",
        text="difficulty in prehension of both upper limbs",
        fill="#000000",
        font=("Inter", 12 * -1)
    )

    canvas.create_text(
        397.0,
        650.0,
        anchor="nw",
        text="4",
        fill="#000000",
        font=("Inter SemiBold", 12 * -1)
    )

    canvas.create_text(
        397.0,
        612.0,
        anchor="nw",
        text="2",
        fill="#000000",
        font=("Inter SemiBold", 12 * -1)
    )

    canvas.create_text(
        397.0,
        593.0,
        anchor="nw",
        text="1",
        fill="#000000",
        font=("Inter SemiBold", 12 * -1)
    )

    canvas.create_text(
        380.0,
        542.0,
        anchor="nw",
        text="Impairment",
        fill="#000000",
        font=("Inter SemiBold", 14 * -1)
    )

    canvas.create_text(
        96.0,
        542.0,
        anchor="nw",
        text="Main pathology",
        fill="#000000",
        font=("Inter SemiBold", 14 * -1)
    )

    canvas.create_rectangle(
        98.0,
        564.0,
        356.0,
        666.0,
        fill="#D9D9D9",
        outline="")

    canvas.create_text(
        116.0,
        576.0,
        anchor="nw",
        text="Category",
        fill="#000000",
        font=("Inter Medium", 12 * -1)
    )

    canvas.create_text(
        191.0,
        576.0,
        anchor="nw",
        text="Pathology Classes",
        fill="#000000",
        font=("Inter Medium", 12 * -1)
    )

    canvas.create_text(
        191.0,
        594.0,
        anchor="nw",
        text="Neoplasm of brain",
        fill="#000000",
        font=("Inter", 12 * -1)
    )

    canvas.create_text(
        191.0,
        612.0,
        anchor="nw",
        text="Diseases of spinal cord",
        fill="#000000",
        font=("Inter", 12 * -1)
    )

    canvas.create_text(
        191.0,
        630.0,
        anchor="nw",
        text="Others neurologic",
        fill="#000000",
        font=("Inter", 12 * -1)
    )

    canvas.create_text(
        116.0,
        633.0,
        anchor="nw",
        text="7",
        fill="#000000",
        font=("Inter SemiBold", 12 * -1)
    )

    canvas.create_text(
        116.0,
        615.0,
        anchor="nw",
        text="6",
        fill="#000000",
        font=("Inter SemiBold", 12 * -1)
    )

    canvas.create_text(
        116.0,
        597.0,
        anchor="nw",
        text="4",
        fill="#000000",
        font=("Inter SemiBold", 12 * -1)
    )

    canvas.create_text(
        96.0,
        365.0,
        anchor="nw",
        text="Pathology responsible for intervention",
        fill="#000000",
        font=("Inter SemiBold", 14 * -1)
    )

    canvas.create_rectangle(
        96.0,
        391.0,
        639.0,
        514.0,
        fill="#D9D9D9",
        outline="")

    canvas.create_text(
        120.0,
        401.0,
        anchor="nw",
        text="Category",
        fill="#000000",
        font=("Inter Medium", 12 * -1)
    )

    canvas.create_text(
        195.0,
        401.0,
        anchor="nw",
        text="Pathology Classes",
        fill="#000000",
        font=("Inter Medium", 12 * -1)
    )

    canvas.create_text(
        195.0,
        419.0,
        anchor="nw",
        text="Hereditary and degenerative diseases of the central nervous system",
        fill="#000000",
        font=("Inter", 12 * -1)
    )

    canvas.create_text(
        195.0,
        437.0,
        anchor="nw",
        text="Other disorders of the central nervous system",
        fill="#000000",
        font=("Inter", 12 * -1)
    )

    canvas.create_text(
        195.0,
        455.0,
        anchor="nw",
        text="Cerebrovascular disease",
        fill="#000000",
        font=("Inter", 12 * -1)
    )

    canvas.create_text(
        195.0,
        473.0,
        anchor="nw",
        text="Late effects of injuries, poisonings, toxic effects, and other external causes",
        fill="#000000",
        font=("Inter", 12 * -1)
    )

    canvas.create_text(
        120.0,
        476.0,
        anchor="nw",
        text="7",
        fill="#000000",
        font=("Inter SemiBold", 12 * -1)
    )

    canvas.create_text(
        120.0,
        458.0,
        anchor="nw",
        text="3",
        fill="#000000",
        font=("Inter SemiBold", 12 * -1)
    )

    canvas.create_text(
        120.0,
        440.0,
        anchor="nw",
        text="2",
        fill="#000000",
        font=("Inter SemiBold", 12 * -1)
    )

    canvas.create_text(
        120.0,
        422.0,
        anchor="nw",
        text="1",
        fill="#000000",
        font=("Inter SemiBold", 12 * -1)
    )

    canvas.create_text(
        99.0,
        241.0,
        anchor="nw",
        text="Demographic Data",
        fill="#000000",
        font=("Inter SemiBold", 14 * -1)
    )

    canvas.create_rectangle(
        98.0,
        266.0,
        257.0,
        339.0,
        fill="#D9D9D9",
        outline="")

    canvas.create_text(
        116.0,
        276.0,
        anchor="nw",
        text="Sex",
        fill="#000000",
        font=("Inter Medium", 12 * -1)
    )

    canvas.create_text(
        190.0,
        276.0,
        anchor="nw",
        text="Values",
        fill="#000000",
        font=("Inter Medium", 12 * -1)
    )

    canvas.create_text(
        206.0,
        294.0,
        anchor="nw",
        text="0",
        fill="#000000",
        font=("Inter", 12 * -1)
    )

    canvas.create_text(
        116.0,
        297.0,
        anchor="nw",
        text="Male",
        fill="#000000",
        font=("Inter SemiBold", 12 * -1)
    )

    canvas.create_text(
        207.0,
        312.0,
        anchor="nw",
        text="1",
        fill="#000000",
        font=("Inter", 12 * -1)
    )

    canvas.create_text(
        116.0,
        315.0,
        anchor="nw",
        text="Female",
        fill="#000000",
        font=("Inter SemiBold", 12 * -1)
    )

    canvas.create_rectangle(
        307.0,
        266.0,
        643.0,
        339.0,
        fill="#D9D9D9",
        outline="")

    canvas.create_text(
        345.0377197265625,
        276.0,
        anchor="nw",
        text="Marital Status",
        fill="#000000",
        font=("Inter Medium", 12 * -1)
    )

    canvas.create_text(
        511.56787109375,
        276.0,
        anchor="nw",
        text="Values",
        fill="#000000",
        font=("Inter Medium", 12 * -1)
    )

    canvas.create_text(
        524.0,
        294.0,
        anchor="nw",
        text="2",
        fill="#000000",
        font=("Inter", 12 * -1)
    )

    canvas.create_text(
        345.0377197265625,
        297.0,
        anchor="nw",
        text="Single",
        fill="#000000",
        font=("Inter SemiBold", 12 * -1)
    )

    canvas.create_text(
        525.0,
        312.0,
        anchor="nw",
        text="1",
        fill="#000000",
        font=("Inter", 12 * -1)
    )

    canvas.create_text(
        345.0377197265625,
        315.0,
        anchor="nw",
        text="Relationship",
        fill="#000000",
        font=("Inter SemiBold", 12 * -1)
    )

    canvas.create_rectangle(
        96.0,
        66.0,
        792.0,
        215.0,
        fill="#D9D9D9",
        outline="")

    canvas.create_text(
        104.0,
        179.88377380371094,
        anchor="nw",
        text="Bathing",
        fill="#000000",
        font=("Inter", 12 * -1)
    )

    canvas.create_text(
        104.0,
        156.94189453125,
        anchor="nw",
        text="Dressing",
        fill="#000000",
        font=("Inter", 12 * -1)
    )

    canvas.create_text(
        104.0,
        134.0,
        anchor="nw",
        text="Ambulation",
        fill="#000000",
        font=("Inter", 12 * -1)
    )

    canvas.create_text(
        104.0,
        105.0,
        anchor="nw",
        text="Activity",
        fill="#000000",
        font=("Inter Medium", 12 * -1)
    )

    canvas.create_text(
        230.0,
        179.88377380371094,
        anchor="nw",
        text="0",
        fill="#000000",
        font=("Inter", 12 * -1)
    )

    canvas.create_text(
        230.0,
        156.94189453125,
        anchor="nw",
        text="0",
        fill="#000000",
        font=("Inter", 12 * -1)
    )

    canvas.create_text(
        230.0,
        134.0,
        anchor="nw",
        text="0",
        fill="#000000",
        font=("Inter", 12 * -1)
    )

    canvas.create_text(
        181.0,
        105.0,
        anchor="nw",
        text="Unable to perform",
        fill="#000000",
        font=("Inter Medium", 12 * -1)
    )

    canvas.create_text(
        355.0,
        178.88377380371094,
        anchor="nw",
        text="1",
        fill="#000000",
        font=("Inter", 12 * -1)
    )

    canvas.create_text(
        354.0,
        155.94189453125,
        anchor="nw",
        text="1",
        fill="#000000",
        font=("Inter", 12 * -1)
    )

    canvas.create_text(
        354.0,
        133.0,
        anchor="nw",
        text="1",
        fill="#000000",
        font=("Inter", 12 * -1)
    )

    canvas.create_text(
        299.0,
        105.0,
        anchor="nw",
        text="Attempts but unsafe",
        fill="#000000",
        font=("Inter Medium", 12 * -1)
    )

    canvas.create_text(
        493.0,
        179.88377380371094,
        anchor="nw",
        text="2",
        fill="#000000",
        font=("Inter", 12 * -1)
    )

    canvas.create_text(
        493.0,
        156.51205444335938,
        anchor="nw",
        text="2",
        fill="#000000",
        font=("Inter", 12 * -1)
    )

    canvas.create_text(
        493.0,
        134.0,
        anchor="nw",
        text="2",
        fill="#000000",
        font=("Inter", 12 * -1)
    )

    canvas.create_text(
        429.0,
        105.0,
        anchor="nw",
        text="Moderate help required",
        fill="#000000",
        font=("Inter Medium", 12 * -1)
    )

    canvas.create_text(
        634.0,
        179.8300323486328,
        anchor="nw",
        text="3",
        fill="#000000",
        font=("Inter", 12 * -1)
    )

    canvas.create_text(
        634.0,
        156.45831298828125,
        anchor="nw",
        text="3",
        fill="#000000",
        font=("Inter", 12 * -1)
    )

    canvas.create_text(
        634.0,
        134.0,
        anchor="nw",
        text="3",
        fill="#000000",
        font=("Inter", 12 * -1)
    )

    canvas.create_text(
        577.0,
        105.0,
        anchor="nw",
        text="Minimal help required",
        fill="#000000",
        font=("Inter Medium", 12 * -1)
    )

    canvas.create_text(
        746.0,
        179.8300323486328,
        anchor="nw",
        text="4",
        fill="#000000",
        font=("Inter", 12 * -1)
    )

    canvas.create_text(
        745.0,
        156.60415649414062,
        anchor="nw",
        text="4",
        fill="#000000",
        font=("Inter", 12 * -1)
    )

    canvas.create_text(
        745.0,
        134.0,
        anchor="nw",
        text="4",
        fill="#000000",
        font=("Inter", 12 * -1)
    )

    canvas.create_text(
        714.0,
        105.0,
        anchor="nw",
        text="Independent",
        fill="#000000",
        font=("Inter Medium", 12 * -1)
    )

    canvas.create_text(
        106.0,
        77.0,
        anchor="nw",
        text="Barthel Index Score",
        fill="#000000",
        font=("Inter SemiBold", 14 * -1)
    )

    canvas.create_text(
        328.0,
        18.0,
        anchor="nw",
        text="Index Scoring References",
        fill="#000000",
        font=("Inter Bold", 16 * -1)
    )
