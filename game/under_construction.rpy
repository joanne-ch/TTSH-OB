screen under_construction:
    add "images/under_construction.png"
    imagebutton:
            idle "images/map/cross.png" xpos 1650 ypos 90
            hover "images/map/cross_hover.png"
            action [Hide("under_construction"),Show("main_menu")]