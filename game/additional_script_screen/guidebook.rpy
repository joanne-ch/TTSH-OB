screen guidebook_sample():
    use overlay
    frame:
        background Null()
        add "images/notebook/notebook.png" xalign 0.5 yalign 0.5

        imagebutton:
            idle "images/notebook/cross icon.png" xpos 1550 ypos 110
            action [Hide("guidebook_sample"), Hide("tutorial_guidebook_2"), Show("tutorial_trustpoint")]


default label_trust = False
default label_mental = False
default label_shape = False
default label_ladder = False
default label_left = False
default label_inquiry = False

init python:
    def exclusive_check(clicked):
        global label_trust
        global label_mental
        global label_shape
        global label_ladder
        global label_left
        global label_inquiry

        index = 0
        labels = [label_trust, label_mental, label_shape, label_ladder, label_left, label_inquiry]

        for i in labels:
            if ( index != clicked and labels[index] == True):
                if (index == 0):
                    label_trust = False
                elif (index == 1):
                    label_mental = False
                elif (index == 2):
                    label_shape = False
                elif (index == 3):
                    label_ladder = False
                elif (index == 4):
                    label_left = False
                elif (index == 5):
                    label_inquiry = False

            index+=1


screen guidebook():
    modal True
    use overlay

    frame:
        background Null()
        add "images/notebook/new notebook.png" xalign 0.5 yalign 0.5
        if (tutorial):
            imagebutton:
                idle "images/notebook/cross icon.png" xpos 1650 ypos 130
                action [Hide("guidebook"), Hide("tutorial_guidebook_2"), Show("tutorial_trustpoint"), SetVariable("tutorial", False)]
        else:
            imagebutton:
                idle "images/notebook/cross icon.png" xpos 1650 ypos 130
                action [Hide("guidebook")]
        vbox:
            xanchor -90
            yanchor -150
            frame:
                background Null()
                ymaximum 120
                xmaximum 200
                imagebutton:
                    idle "images/notebook/click bg.png"
                    action [SetVariable("label_trust", True), Function(exclusive_check, 0)]

            frame:
                background Null()
                ypos 15
                ymaximum 120
                xmaximum 200
                imagebutton:
                    idle "images/notebook/click bg.png"
                    action [SetVariable("label_mental", True), Function(exclusive_check, 1)]
            frame:
                background Null()
                ypos 30
                ymaximum 100
                xmaximum 200
                imagebutton:
                    ypos 5
                    idle "images/notebook/click bg.png"
                    action [SetVariable("label_shape", True), Function(exclusive_check, 2)]
            frame:
                background Null()
                ypos 45
                ymaximum 100
                xmaximum 200
                imagebutton:
                    ypos 15
                    idle "images/notebook/click bg.png"
                    action [SetVariable("label_ladder", True), Function(exclusive_check, 3)]
                    
            frame:
                background Null()
                ypos 85
                ymaximum 100
                xmaximum 
                imagebutton:
                    ypos 15
                    idle "images/notebook/click bg.png"
                    action [SetVariable("label_left", True), Function(exclusive_check, 4)]
            frame:
                background Null()
                ypos 105
                ymaximum 100
                xmaximum 200
                imagebutton:
                    ypos 15
                    idle "images/notebook/click bg.png"
                    action [SetVariable("label_inquiry", True), Function(exclusive_check, 5)]
    
        if (label_trust):
            imagebutton:
                xpos 60
                ypos 120
                idle  "images/notebook/yellow label.png"
            add "images/notebook/trust text.png"xpos 300 ypos 290
            add "images/notebook/trust image.png" xpos 1200 ypos 220
        elif (label_mental):
            imagebutton:
                xpos 60
                ypos 250
                idle "images/notebook/orange label.png"
            add "images/notebook/shape title.png" xpos 280 ypos 150
            add "images/notebook/shape text1.png" xpos 300  ypos 250
            add "images/notebook/shape text2.png" xpos 1100 ypos 180
        elif (label_shape):
            imagebutton:
                xpos 60
                ypos 380
                idle "images/notebook/red label.png"
            add "images/notebook/mental text1.png" xpos 290 ypos 180
            add "images/notebook/mental text2.png" xpos 300  ypos 530
            add "images/notebook/mental text3.png" xpos 1130 ypos 260
        
        elif (label_ladder):
            imagebutton:
                xpos 60
                ypos 505
                idle "images/notebook/purple label.png"
            add "images/notebook/ladder image.png" xpos 185 ypos 60
            add "images/notebook/ladder text.png" xpos 1120  ypos 280
        elif (label_left):
            imagebutton:
                xpos 60
                ypos 635
                idle "images/notebook/blue label.png"
            add "images/notebook/left text1.png" xpos 295 ypos 180
            add "images/notebook/left text2.png" xpos 1150  ypos 200
        elif (label_inquiry):
            imagebutton:
                xpos 60
                ypos 765
                idle "images/notebook/teal label.png"
            add "images/notebook/inquire text1.png" xpos 295 ypos 180
            add "images/notebook/inquire text2.png" xpos 1150  ypos 300

        
        

        


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