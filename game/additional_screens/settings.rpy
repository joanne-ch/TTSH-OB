define persistent.window = True
define persistent.transition = False
define persistent.afterTransition = False
default barValue_change = False 

screen preferences_custom():

    tag menu

    use overlay


    use game_menu1(_("Preferences"), scroll="viewport"):

        if renpy.variant("pc") or renpy.variant("web"):
            text _("{u}Display{u}") style "mainText"  xpos 100 ypos 100
            imagebutton:
                xpos 1470
                ypos 780
                idle "images/main_menu/hide_button.png"
                hover "images/main_menu/hide_button_hover.png" 
                action Return()
            text "Back" size 80 xpos 1620 ypos 650

            #Text Speed Settings
            text _("{u}Text Speed{u}") style "mainText" xpos 900 ypos -270 size 70
            bar value Preference("text speed") ymaximum 70 xmaximum 510 xpos 900 ypos -265 
            textbutton "Test Text Speed: " action Show("text_test") text_style "TestTextSpeed" xpos 900 ypos -260
            
            #Auto-Forward Time Settings
            text _("{u}Auto Forward Time{u}") style "mainText" xpos 900 ypos -260 size 70
            bar value Preference("auto-forward time") ymaximum 70 xmaximum 510 xpos 900 ypos -255 

            if config.has_music:
                text _("{u}Music Volume{u}") style "mainText" xpos 900 ypos -255 size 70
                bar value Preference("music volume") ymaximum 70 xmaximum 510 xpos 900 ypos -250 

            if config.has_sound:
                text _("{u}Sound Volume{u}") style "mainText" xpos 900 ypos -245 size 70
                bar value Preference("sound volume") ymaximum 70 xmaximum 510 xpos 900 ypos -240

                if config.sample_sound:
                    textbutton _("Test") action Play("sound", config.sample_sound)

            if config.has_voice:
                text _("{u}Voice Volume{u}") style "mainText" xpos 900 ypos -230 size 70
                bar value Preference("voice volume") ymaximum 70 xmaximum 510 xpos 900 ypos -225 
                if config.sample_voice:
                    textbutton _("Test") action Play("voice", config.sample_voice)

            if config.has_music or config.has_sound or config.has_voice:
                null height gui.pref_spacing

                textbutton _("Mute All"):
                    action Preference("all mute", "toggle")
                    style "mute_all_button"

            #Display Setting
            if persistent.window: 
                imagebutton:
                    idle "images/settings/checkbox_check.png"
                    action Preference('display', 'window')
                    xpos 90  ypos -1000
                
                imagebutton:
                    idle "images/settings/checkbox_uncheck.png"
                    hover "images/settings/checkbox_check.png"
                    action ToggleVariable("persistent.window"),  Preference('display', 'fullscreen')
                    xpos 90  ypos -1000

                text "Window" xpos 250 ypos -1270 color "#000000ff" size 70
                text "Fullscreen" xpos 240 ypos -1205 color "#000000ff" size 70
            else:
                imagebutton:
                    idle "images/settings/checkbox_uncheck.png"
                    hover "images/settings/checkbox_check.png"
                    action ToggleVariable("persistent.window"),  Preference('display', 'window')
                    xpos 90  ypos -1000

                imagebutton:
                    idle "images/settings/checkbox_check.png"
                    action Preference('display', 'fullscreen')
                    xpos 90  ypos -1000

                text "Window" xpos 250 ypos -1270 color "#000000ff" size 70
                text "Fullscreen" xpos 240 ypos -1205 color "#000000ff" size 70    
            
            #Skip Setting
            text _("{u}Skip{u}") style "mainText"  xpos 100 ypos -1150
            if persistent.transition: 
                imagebutton:
                    idle "images/settings/checkbox_uncheck.png"
                    hover "images/settings/checkbox_check.png"
                    action InvertSelected(Preference("transitions", "toggle")),ToggleVariable("persistent.transition")
                    xpos 90  ypos -1140
            else:
                imagebutton:
                    idle "images/settings/checkbox_check.png"
                    hover "images/settings/checkbox_uncheck.png"
                    action InvertSelected(Preference("transitions", "toggle")),ToggleVariable("persistent.transition")
                    xpos 90  ypos -1140      
            text "Transition" xpos 220 ypos -1255 color "#000000ff" size 68
            
            if persistent.afterTransition: 
                imagebutton:
                    idle "images/settings/longcheckbox_check.png"
                    hover "images/settings/longcheckbox_uncheck.png"
                    action Preference("after choices", "toggle"),ToggleVariable("persistent.afterTransition")
                    xpos 90  ypos -1220
            else: 
                imagebutton:
                    idle "images/settings/longcheckbox_uncheck.png"
                    hover "images/settings/longcheckbox_check.png"
                    action Preference("after choices", "toggle"),ToggleVariable("persistent.afterTransition")
                    xpos 90  ypos -1220
            text "After Choices" xpos 220 ypos -1332 color "#000000ff" size 68
    
screen text_test:
    frame:
        background Null()
        text "This is a test text." slow_cps True color "#000" size 50 xpos 1250 ypos 270 
    timer 2.0 action Hide("text_test")

