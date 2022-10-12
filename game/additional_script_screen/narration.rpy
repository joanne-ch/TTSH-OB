screen narration(text):
    #add "images/background/nursing hallway.png"
    add "images/dialogue/narration box.png" xpos 100 ypos 280
    frame:
        background Null()
        xalign 0.5
        yalign 0.5
        xmaximum 1300
        ymaximum 500
        text "[text]" slow_cps True  style "narration"
    
    imagebutton:
        idle "images/dialogue/transparent.png"
        xalign 0.5
        yalign 0.5
        xmaximum 5500
        ymaximum 5500
        action Return(True)
    
    
        

style narration:
    outlines [(5, "#000000", 0, 0)]
    line_spacing 15
