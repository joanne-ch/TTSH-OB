screen guidebook_sample():
    use overlay
    frame:
        background Null()
        add "images/notebook/notebook.png" xalign 0.5 yalign 0.5

        imagebutton:
            idle "images/notebook/cross icon.png" xpos 1550 ypos 110
            action [Hide("guidebook_sample"), Hide("tutorial_guidebook_2"), Show("tutorial_trustpoint")]

screen guidebook():
    use overlay
    frame:
        background Null()
        add "images/notebook/notebook.png" xalign 0.5 yalign 0.5

        imagebutton:
            idle "images/notebook/cross icon.png" xpos 1530 ypos 90
            action [Hide("guidebook")]

screen guidebook_icon():
    frame:
        background Null()
        xminimum 500
        xmaximum 500
        ymaximum 150
        yminimum 150
        xpos 20
        ypos 20
        imagebutton:
            idle "images/notebook/guidebook icon.png" 
            hover "images/notebook/guidebook icon hover.png"
            action Show("guidebook")