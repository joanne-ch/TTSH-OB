screen CodexPage():
    tag menu
    
    use game_menu1(_("ProfilePage"), scroll="viewport"):
        style_prefix "about"

    use overlay

    add "main_menu/profile_background.png" xpos 130
    text "{u}Codex{u}" style "mainText" xpos 270 ypos 200 size 100

    imagebutton:
        xpos 1400
        ypos 850
        idle "images/main_menu/hide_button.png"
        hover "images/main_menu/hide_button_hover.png" 
        action Return()

    text "Back" size 80 xpos 1550 ypos 890
    
screen overlay():
    add "images/main_menu/overlay.png" zoom 2





