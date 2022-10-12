default trust_level = 0
default npc_shape = "Square"

screen show_npc_status():
    frame:
        xalign 0.5
        xmaximum 1000
        ymaximum 300
        xpos 1650 ypos 30
        xpadding 30
        ypadding 30
        vbox:
            text "Trust Level: [trust_level]"
            text "Shape: [npc_shape]"
            
