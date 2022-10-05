screen map():

    modal True #prevent users from interact with lower layer
    frame:
        background Null()
        add "images/map/shadow_page.png" xpos 0 ypos 0
        add "images/map/map_bg_copy.png" xpos 0 ypos 0

        #close map page
        imagebutton:
            idle "images/map/cross.png" xpos 1650 ypos 90
            hover "images/map/cross_hover.png"
            action [Hide("map"),Return(True)]

        #map buildings (imagebutton)
        imagebutton:
            idle "images/map/main_bd.png" xpos 200 ypos 310
            hover "images/map/main_bd_hover.png"
            action [Hide("map"), Show("intro_building_main")]

        imagebutton:
            idle "images/map/annex_1.png" xpos 625 ypos 60
            hover "images/map/annex_1_hover.png"
            action [Hide("map"), Show("intro_building_anx_1")]

        imagebutton:
            idle "images/map/CHI.png" xpos 920 ypos 150
            hover "images/map/CHI_hover.png"
            action [Hide("map"), Show("intro_building_CHI")]

        imagebutton:
            idle "images/map/NCID.png" xpos 1210 ypos 390
            hover "images/map/NCID_hover.png"
            action [Hide("map"), Show("intro_building_NCID")]

        imagebutton:
            idle "images/map/annex_2.png" xpos 880 ypos 590
            hover "images/map/annex_2_hover.png"
            action [Hide("map"), Show("intro_building_anx_2")]

