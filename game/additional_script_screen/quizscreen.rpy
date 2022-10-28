screen quiz_screen(text):
    #add "images/background/nursing hallway.png"
    add "images/quiz bg.png" xpos 0 ypos 0
    frame:
        background Null()
        xalign 0.5
        yalign 0.5
        xmaximum 1000
        ymaximum 500
        text "[text]" slow_cps True  style "narration"
    
    imagebutton:
        idle "images/dialogue/transparent.png"
        xalign 0.5
        yalign 0.5
        xmaximum 5500
        ymaximum 5500
        action Return(True)