screen profile():
    add "images/main_menu/profile_frame.png" ypos 20
    add "images/main_menu/nurse_icon.png" ypos 90 xpos 85

    #User name, need to limit characters
    text "Kamala Harris" style "user_name"

    #Progress Check
    text "Progress: Chapter 1 - 1" style "progress_check"

    imagebutton:
        ypos 245
        xpos 865
        idle "images/main_menu/profile_icon.png"
        hover "images/main_menu/profile_icon_hover.png" 
        action Start()

style user_name:
    ypos 230
    xpos 420

    color "#000000"
    size 60

style progress_check:
    ypos 340
    xpos 400
    size 45
    take user_name

screen selection():

    imagebutton:
        ypos 440
        xpos 100
        idle "images/main_menu/orange_box.png" 
        hover "images/main_menu/orange_box_hover.png"
        action Start()
    
    imagebutton:
        ypos 725
        xpos 260
        idle "images/main_menu/orange_box.png" 
        hover "images/main_menu/orange_box_hover.png"
        action Start()

    text "Main Chapter" style "main_chapter"

style main_chapter:
    font "font/LondrinaBlack_Regular.otf"
    ypos 440
    xpos 100
    
    take user_name


