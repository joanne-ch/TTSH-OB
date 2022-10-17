transform arrow_1:
    xpos 1120
    ypos -100
    easeout 0.3 xpos 1030
    easein 0.3 xpos 1120
    repeat

transform arrow_down_1:
    xpos 610
    ypos 975
    easeout 0.3 ypos 985
    easein 0.3 ypos 975
    repeat

transform arrow_down_2:
    xpos 691
    ypos 975
    easeout 0.3 ypos 985
    easein 0.3 ypos 975
    repeat

transform arrow_down_3:
    xpos 960
    ypos 975
    easeout 0.3 ypos 985
    easein 0.3 ypos 975
    repeat
##########################
#the direction should contains:
#1. choice box
#2. 
#
###########################

screen direction_1:
    #add "images/shadow page.png"
    add "images/direction/choice_direction_1.png" xalign 0.5 yalign 0.5
    add "images/map/go_left.png" at arrow_1

    #click anywhere to next direction
    imagebutton:
        idle "images/transparent.png" xpos 0 ypos 0
        action [Hide("direction_1"),Show("direction_2")]

    #close the window
    #imagebutton:
      #      idle "images/map/cross.png" xpos 1650 ypos 90
       #     hover "images/map/cross_hover.png"
        #    action [Hide("direction_1"),Show("direction_2")]

screen direction_2:
    add "images/direction/choice_direction_2.png" xalign 0.5 yalign 0.5
    add "images/map/go_left.png" at arrow_1

    #click part
    imagebutton:
        idle "images/transparent.png" xpos 0 ypos 0
        action [Hide("direction_2"),Return(True)]

    #close the window
    imagebutton:
            idle "images/map/cross.png" xpos 1650 ypos 90
            hover "images/map/cross_hover.png"
            action [Hide("direction_2"),Return(True)]


###############################tutorial of button funtions
screen direction_function:
    add "images/shadow page.png" xalign 0.5 yalign 0.5
    add "images/direction/direction_1.png" xpos 419 ypos 681
    add "images/direction/arrow_down.png" at arrow_down_1

    #click anywhere
    imagebutton:
        idle "images/transparent.png" xpos 0 ypos 0
        action [Hide("direction_function"),Show("direction_function_2")]
    #close the window
    imagebutton:
            idle "images/map/cross.png" xpos 1650 ypos 90
            hover "images/map/cross_hover.png"
            action [Hide("direction_function"),Return(True)]

screen direction_function_2:
    add "images/shadow page.png" xalign 0.5 yalign 0.5
    add "images/direction/direction_2.png" xpos 507 ypos 681
    add "images/direction/arrow_down.png" at arrow_down_2

    #click naywhere
    imagebutton:
        idle "images/transparent.png" xpos 0 ypos 0
        action [Hide("direction_function_2"),Show("direction_function_3")]
    #close the window
    imagebutton:
            idle "images/map/cross.png" xpos 1650 ypos 90
            hover "images/map/cross_hover.png"
            action [Hide("direction_function_2"),Return(True)]

screen direction_function_3:
    add "images/shadow page.png" xalign 0.5 yalign 0.5
    add "images/direction/direction_3.png" xpos 763 ypos 681
    add "images/direction/arrow_down.png" at arrow_down_3

    #click naywhere
    imagebutton:
        idle "images/transparent.png" xpos 0 ypos 0
        action [Hide("direction_function_3"),Return(True)]
    #close the window
    imagebutton:
            idle "images/map/cross.png" xpos 1650 ypos 90
            hover "images/map/cross_hover.png"
            action [Hide("direction_function_3"),Return(True)]