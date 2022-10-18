screen under_construction:
    add "images/under_construction.png" xalign 0.5 yalign 0.5
    imagebutton:
            idle "images/map/cross.png" xpos 1650 ypos 90
            hover "images/map/cross_hover.png"
            action [Hide("under_construction"),Show("main_menu")]

screen under_constructionDialog:
    add "images/under_construction.png" xalign 0.5 yalign 0.5
    imagebutton:
            idle "images/map/cross.png" xpos 1650 ypos 90
            hover "images/map/cross_hover.png"
            action [Hide("under_construction"),Return(True)]
            #action Hide("under_constructionDialog")