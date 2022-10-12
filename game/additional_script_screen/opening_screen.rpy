screen opening_screen(text):

    #scene black
    #with Pause(0.1)
    #add "images/background/nursing hallway.png"
    frame:
        background Null()
        xalign 0.5
        yalign 0.5
        xmaximum 1300
        ymaximum 500
        text "[text]" slow_cps True  style "narration1"
    
    imagebutton:
        idle "images/dialogue/transparent.png"
        xalign 0.5
        yalign 0.5
        xmaximum 5500
        ymaximum 5500
        #action Start()
        action Return(True)
    
style narration1:
    size 150
    outlines [(5, "#000000", 0, 0)]
    line_spacing 15

screen opening_screen_0:
    #add "images/background/nursing hallway.png"
    add "images/background/black.png"

    #add "images/main_menu/overlay.png"
    #add "images/black page.png"
    frame:
        background Null()
        xalign 0.5
        yalign 0.5
        xmaximum 1300
        ymaximum 500
        text "Prologue" slow_cps True  style "narration1"
    
    imagebutton:
        idle "images/dialogue/transparent.png"
        xalign 0.5
        yalign 0.5
        xmaximum 5500
        ymaximum 5500
        action Start()
        #action Return(True)