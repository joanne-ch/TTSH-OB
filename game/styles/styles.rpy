transform ClickAnimation:
    linear 0.25 alpha 0.25 
    linear 0.25 alpha 1 

transform TextAnimation:
    linear 0.35 alpha 0.70 
    linear 0.35 alpha 1 

style mainText:
    font "font/LondrinaBlack_Regular.otf"
    size 90
    color "#000000"

style subMain:
    font "font/LondrinaThin-Regular.otf"
    size 70
    color "#000000"

style TestTextSpeed:
    # idle "#fe3eed"
    # hover "#d2d2d2"
    font "font/LondrinaBlack_Regular.otf"
    size 50
    color "#000000"

    

style greyDialogue:
    size 35
    ypos 710 
    xpos 960
    color "#000000"

screen game_menu1(title, scroll=None, yinitial=0.0):

    style_prefix "game_menu"

    if main_menu:
        add gui.main_menu_background

    vbox:
        transclude