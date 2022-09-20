screen chooseCharacters():
    tag menu
    
    use game_menu1(_("About"), scroll="viewport"):
        style_prefix "about"

    use overlay

    imagebutton:
        xpos 1400
        ypos 850
        idle "images/main_menu/hide_button.png"
        hover "images/main_menu/hide_button_hover.png" 
        action Return()

    text "Back" size 80 xpos 1550 ypos 890
    
screen overlay():
    add "images/main_menu/overlay.png" zoom 2

screen game_menu1(title, scroll=None, yinitial=0.0):

    style_prefix "game_menu"

    if main_menu:
        add gui.main_menu_background

    vbox:
        transclude



