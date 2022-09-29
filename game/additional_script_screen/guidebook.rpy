screen guidebook():
    use overlay
    frame:
        background Null()
        add "images/notebook/notebook.png" xalign 0.5 yalign 0.5

        imagebutton:
            idle "images/notebook/cross icon.png" xpos 1530 ypos 90
            action [Hide("guidebook"), Show("tutorial_trustpoint")]

screen guidebook_icon():
    imagebutton:
        idle "images/notebook/guidebook icon.png" xpos 50 ypos 50
        hover "images/notebook/guidebook icon hover.png"