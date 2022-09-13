screen profilePopUp():
    tag menu
    
    use game_menu1(_("About"), scroll="viewport"):
        style_prefix "about"

    use overlay

    imagebutton:
        xpos 1200
        ypos 750
        idle "images/main_menu/hide_button.png"
        hover "images/main_menu/hide_button_hover.png" 
        action Return()

    text "Close"  size 80 xpos 1330 ypos 70
    
screen overlay():
    add "images/main_menu/overlay.png" zoom 2

screen game_menu1(title, scroll=None, yinitial=0.0):

    style_prefix "game_menu"

    if main_menu:
        add gui.main_menu_background

    vbox:
        transclude


style mainText:
    font "font/LondrinaBlack_Regular.otf"
    size 90
    color "#000000"

style subMain:
    font "font/LondrinaThin-Regular.otf"
    size 70
    color "#000000"


