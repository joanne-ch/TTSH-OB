style title:
    font "font/LeagueSpartan-Bold.ttf"
    size 160

screen conflict_win():
    modal True
    add "images/background/black.png"
    add "images/dialogue/pink box.png" xpos 200 ypos 230
    add "images/dialogue/sparkle icon.png" xpos -50 ypos 450
    text " CONFLICT\nRESOLVED!" style "title" xpos 550 ypos 380
    imagebutton:
        idle "images/dialogue/transparent.png"
        xalign 0.5
        yalign 0.5
        xmaximum 5500
        ymaximum 5500
        action Return(True)


screen conflict_failure():
    modal True
    add "images/background/black.png"
    add "images/dialogue/pink box.png" xpos 200 ypos 230
    add "images/dialogue/exclamation icon.png" xpos -50 ypos 450
    text "      CONFLICT\n NOT RESOLVED!" style "title" xpos 350 ypos 380
    imagebutton:
        idle "images/dialogue/transparent.png"
        xalign 0.5
        yalign 0.5
        xmaximum 5500
        ymaximum 5500
        action Return(True)
    
