default quiz_num = 0
screen quiz_selection:
    imagebutton:
        idle "images/quiz_selection/chap1.png" xpos -100 ypos 124
        hover "images/quiz_selection/chap1_hover.png"
        action [Hide("quiz_selection"),SetVariable("quiz_num", 1),Return(True)]
    
    imagebutton:
            idle "images/quiz_selection/chap2.png" xpos 470 ypos 280
            hover "images/quiz_selection/chap2_hover.png"
            action [Hide("quiz_selection"),SetVariable("quiz_num", 2),Return(True)]
    
    imagebutton:
        idle "images/quiz_selection/chap3.png" xpos 421 ypos 632
        hover "images/quiz_selection/chap3_hover.png"
        action [Hide("quiz_selection"),SetVariable("quiz_num", 3),Return(True)]

    imagebutton:
        idle "images/map/back.png" xpos 1500 ypos 850
        hover "images/map/back_hover.png"
        action [Hide("quiz_selection"), SetVariable("quiz_num", 0),Return(True)]