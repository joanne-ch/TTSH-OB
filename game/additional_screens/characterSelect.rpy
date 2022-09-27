init python:
    def placeholderFunc():
        pass

default btn_selected = False
screen characterSelect():
    tag menu
    
    use game_menu1(_("ProfilePage"), scroll="viewport"):
        style_prefix "about"

    use overlay

    #add "main_menu/profile_background.png" xpos 130
    #text "{u}Codex{u}" style "mainText" xpos 270 ypos 200 size 100

    imagebutton:
        idle "images/Selection Page (Confirmation)/Nurse.png" xpos 200 ypos 100
        hover "images/Selection Page (Confirmation)/Nurse hover.png" 
        selected_idle "images/Selection Page (Confirmation)/Nurse hover.png"
        selected_hover "images/Selection Page (Confirmation)/Nurse hover.png" 
        selected (btn_selected)
        action ToggleVariable("btn_selected", True, False)

    imagebutton:
        idle "images/Selection Page (Confirmation)/Patient.png" xpos 850 ypos 100

    imagebutton:
        idle "images/Selection Page (Confirmation)/Doctor.png" xpos 1400 ypos 100





    imagebutton:
        xpos 1400
        ypos 900
        idle "images/main_menu/hide_button.png"
        hover "images/main_menu/hide_button_hover.png" 
        action Start()

    text "Continue" size 76 xpos 1480 ypos 943
    
screen overlay():
    add "images/main_menu/overlay.png" zoom 2
