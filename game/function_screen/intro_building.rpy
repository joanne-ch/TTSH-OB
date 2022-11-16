init python:
    def map_increase_page():
        global map_page_number
        if (map_page_number >= 3):
            map_page_number = 3
        else:
            map_page_number += 1

    def map_decrease_page():
        global map_page_number
        if (map_page_number == 1):
            map_page_number = 1
        else:
            map_page_number -= 1
default map_page_number = 1

# the tranform that notice player to change page
transform right_button:
    xpos 1670
    easeout 0.3 xpos 1690
    easein 0.3 xpos 1670
    repeat
transform left_button:
    xpos 240
    easeout 0.3 xpos 230
    easein 0.3 xpos 240
    repeat

screen intro_building_main:
    modal True
    add "images/map/shadow_page.png" xpos 0 ypos 0
    add "images/map/pick_background.png" 
    frame:
        background Null()
        xpos 1080
        ypos 500
        xalign 0.5
        yalign 0.5
        xmaximum 1200
        ymaximum 800
        xpadding 30
        ypadding 30
        vbox:
            text "{u}{b}MAIN BUILDING{b}{u}" slow_cps True  style "narration"
            text ""
            if(map_page_number == 1):
                text "While playing this game, you will often be {color=#f4b157}making choices {/color}that may {color=#f4b157}change the trajectory of your story {/color}and the challenges you will have to overcome.Don’t worry about missing out, after finishing each chapter, you will be able to {color=#f4b157}replay and choose the different choices {/color} .With that said, we encourage you to fully experience the game at least once before replaying any sequence" slow_cps True  style "narration"
            elif(map_page_number == 2):
                text "Hey there green horn, welcome to your first conflict. While working at Tan Tock Seng hospital, you will inevitably have to {color=#f4b157}resolve situations whether with your colleague or patient {/color}. The same is true for this game." slow_cps True  style "narration"
            else:
                text "So make your choice wisely! {color=#f4b157}If you are able to resolve conflict with a high trust point, you may get some surprise rewards afterward!{/color}" slow_cps True  style "narration"
            text ""
            text "[map_page_number]/3" xalign 0.5

    #button to go right (need notice at first page)
    if(map_page_number == 1):
        imagebutton at right_button:
            idle "images/map/go_right.png" xpos 1670 ypos 0
            hover "images/map/go_right_hover.png"
            action Function(map_increase_page)
    else:
        imagebutton:
            idle "images/map/go_right.png" xpos 1670 ypos 0
            hover "images/map/go_right_hover.png"
            action Function(map_increase_page)

    #button to go left
    if(map_page_number == 3):
        imagebutton at left_button:
            idle "images/map/go_left.png" xpos 240 ypos 0
            hover "images/map/go_left_hover.png"
            action Function(map_decrease_page)
    else:
        imagebutton:
            idle "images/map/go_left.png" xpos 240 ypos 0
            hover "images/map/go_left_hover.png"
            action Function(map_decrease_page)  

    #add building icon
    add "images/map/main_bd_hover.png" xpos 45 ypos 500
    imagebutton:
        idle "images/map/back.png" xpos 1400 ypos 790
        hover "images/map/back_hover.png"
        action [Hide("intro_building_main"), Show("map")]


screen intro_building_anx_1:
    modal True
    add "images/map/shadow_page.png" xpos 0 ypos 0
    add "images/map/pick_background.png" 
    add "images/map/annex_1_hover.png" xpos 100 ypos 525 #add the building icon
    frame:
        background Null()
        xpos 1080
        ypos 500
        xalign 0.5
        yalign 0.5
        xmaximum 1200
        ymaximum 800
        xpadding 30
        ypadding 30
        vbox:
            text "{u}{b}ANNEX 1{b}{u}" slow_cps True  style "narration"
            text ""
            text "While playing this game, you will often be {color=#f4b157}making choices {/color}that may {color=#f4b157}change the trajectory of your story {/color}and the challenges you will have to overcome.Don’t worry about missing out, after finishing each chapter, you will be able to {color=#f4b157}replay and choose the different choices {/color} .With that said, we encourage you to fully experience the game at least once before replaying any sequence" slow_cps True  style "narration"
            text ""

    #imagebutton:
    #    idle "images/map/video.png" xpos 480 ypos 790
    #    hover "images/map/video_hover.png"
    #    action (Show("video_play_1"),Hide("intro_building_anx_1"))

    imagebutton:
        idle "images/map/back.png" xpos 1400 ypos 790
        hover "images/map/back_hover.png"
        action [Hide("intro_building_anx_1"), Show("map")]



screen video_play_1:
    modal True
    $ renpy.movie_cutscene("images/map/ttsh_1.mp4")
    imagebutton:
        idle "images/map/back.png" xpos 1400 ypos 790
        hover "images/map/back_hover.png"
        action [Hide("video_play_1")]



screen intro_building_CHI:
    modal True
    add "images/map/shadow_page.png" xpos 0 ypos 0
    add "images/map/pick_background.png" 
    frame:
        background Null()
        xpos 1080
        ypos 500
        xalign 0.5
        yalign 0.5
        xmaximum 1200
        ymaximum 800
        xpadding 30
        ypadding 30
        vbox:
            text "{u}{b}CHI{b}{u}" slow_cps True  style "narration"
            text ""
            text "The CHI Co-Learning Network aims to deepen co-learning and create opportunities for collaboration between our partners. With the support of CHI’s Co-Learning Management Committee and Faculty, we seek to spread the culture of innovation and translate innovations into actual practice." slow_cps True  style "narration"
            text ""

    add "images/map/CHI_hover.png" xpos 60 ypos 500
    imagebutton:
        idle "images/map/back.png" xpos 1400 ypos 790
        hover "images/map/back_hover.png"
        action [Hide("intro_building_CHI"), Show("map")]

screen intro_building_NCID:
    modal True
    add "images/map/shadow_page.png" xpos 0 ypos 0
    add "images/map/pick_background.png" 
    frame:
            background Null()
            xpos 1080
            ypos 500
            xalign 0.5
            yalign 0.5
            xmaximum 1200
            ymaximum 800
            xpadding 30
            ypadding 30
            vbox:
                text "{u}{b}NCID{b}{u}" slow_cps True  style "narration"
                text ""
                text "While playing this game, you will often be {color=#f4b157}making choices {/color}that may {color=#f4b157}change the trajectory of your story {/color}and the challenges you will have to overcome.Don’t worry about missing out, after finishing each chapter, you will be able to {color=#f4b157}replay and choose the different choices {/color} .With that said, we encourage you to fully experience the game at least once before replaying any sequence" slow_cps True  style "narration"
                text ""

    add "images/map/NCID_hover.png" xpos 60 ypos 500
    imagebutton:
        idle "images/map/back.png" xpos 1400 ypos 790
        hover "images/map/back_hover.png"
        action [Hide("intro_building_NCID"), Show("map")]

screen intro_building_anx_2:
    modal True
    add "images/map/shadow_page.png" xpos 0 ypos 0
    add "images/map/pick_background.png" 
    frame:
            background Null()
            xpos 1080
            ypos 500
            xalign 0.5
            yalign 0.5
            xmaximum 1200
            ymaximum 800
            xpadding 30
            ypadding 30
            vbox:
                text "{u}{b}ANNEX 2{b}{u}" slow_cps True  style "narration"
                text ""
                text "While playing this game, you will often be {color=#f4b157}making choices {/color}that may {color=#f4b157}change the trajectory of your story {/color}and the challenges you will have to overcome.Don’t worry about missing out, after finishing each chapter, you will be able to {color=#f4b157}replay and choose the different choices {/color} .With that said, we encourage you to fully experience the game at least once before replaying any sequence" slow_cps True  style "narration"
                text ""
    
    add "images/map/annex_2_hover.png" xpos 125 ypos 500
    imagebutton:
        idle "images/map/back.png" xpos 1400 ypos 790
        hover "images/map/back_hover.png"
        action [Hide("intro_building_anx_2"), Show("map")]

style narration:
    outlines [(5, "#000000", 0, 0)]
    line_spacing 15
