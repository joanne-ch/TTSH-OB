screen map():
    modal True 
    frame:
        background Null()
        add "images/map/shadow_page.png" xpos 0 ypos 0

        imagebutton:
            idle "images/map/singapore.png" xalign 0.5 yalign 0.5
            hover "images/map/singapore_hover.png"
            action [Hide("map"),Show("map_1")]
        imagebutton:
            idle "images/map/cross.png" xpos 1650 ypos 90
            hover "images/map/cross_hover.png"
            action [Hide("map"),Return(True)]

screen map_1():
    modal True
    frame:
        background Null()
        add "images/map/shadow_page.png" xpos 0 ypos 0

        #add "images/map/singapore.png"
        #hide "images/map/singapore.png"
        #with dissolve
        imagebutton:
            idle "images/map/back.png" xpos 1400 ypos 790
            hover "images/map/back_hover.png"
            action [Hide("map_1"), Show("map")]

        imagebutton:
            idle "images/map/novena.png" xalign 0.5 yalign 0.5
            hover "images/map/novena_hover.png"
            action [Hide("map_1"),Show("map_2")]
        imagebutton:
            idle "images/map/cross.png" xpos 1650 ypos 90
            hover "images/map/cross_hover.png"
            action [Hide("map_1"),Return(True)]


screen map_2():
    modal True #prevent users from interact with lower layer
    frame:
        background Null()
        add "images/map/shadow_page.png" xpos 0 ypos 0
        add "images/map/material/ttsh_bg.png" xpos 0 ypos 0

        imagebutton:
            idle "images/map/back.png" xpos 1600 ypos 840
            hover "images/map/back_hover.png"
            action [Hide("map_2"), Show("map_1")]

        #close map page
        imagebutton:
            idle "images/map/cross.png" xpos 1650 ypos 90
            hover "images/map/cross_hover.png"
            action [Hide("map_2"),Return(True)]

        #map buildings (imagebutton)
        imagebutton:
            idle "images/map/material/main.png" xpos 600 ypos 93
            hover "images/map/material/main_hover.png"
            action [Hide("map_2"), Show("intro_building_main")]

        imagebutton:
            idle "images/map/material/annex_1.png" xpos 934 ypos 97
            hover "images/map/material/annex_1_hover.png"
            action [Hide("map_2"), Show("intro_building_anx_1")]

        imagebutton:
            idle "images/map/material/CHI.png" xpos 1145 ypos 343
            hover "images/map/material/CHI_hover.png"
            action [Hide("map_2"), Show("intro_building_CHI")]

        imagebutton:
            idle "images/map/material/NCID.png" xpos 969 ypos 308
            hover "images/map/material/NCID_hover.png"
            action [Hide("map_2"), Show("intro_building_NCID")]

        imagebutton:
            idle "images/map/material/annex_2.png" xpos 309 ypos 312
            hover "images/map/material/annex_2_hover.png"
            action [Hide("map_2"), Show("intro_building_anx_2")]

