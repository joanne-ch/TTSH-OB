default trust_level = 0
default shape_type = "Square"
screen show_npc_status():
    frame:
        xminimum 500
        xmaximum 500
        ymaximum 150
        yminimum 150
        xpos 20
        ypos 20
        xalign -2.7
        vbox:
            xalign 0.5 yalign 0.5
            text "Trust Level: [trust_level]" xalign 0.5 yalign 0.5
            text "Shape: [shape_type] " xalign 0.5 yalign 0.5
