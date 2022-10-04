screen tutorial():
    use overlay
    modal True
    frame:
        xalign 0.5
        yalign 0.5
        xmaximum 1500
        ymaximum 600
        xpadding 30
        ypadding 30
        vbox:
            text "{u}{b}TUTORIAL{b}{u}"
            text ""
            text "While playing this game, you will often be {color=#f4b157}making choices {/color}that may {color=#f4b157}change the trajectory of your story {/color}and the challenges you will have to overcome.Don’t worry about missing out, after finishing each chapter, you will be able to {color=#f4b157}replay and choose the different choices {/color} .With that said, we encourage you to fully experience the game at least once before replaying any sequence"
            text ""
            textbutton "Ok":
                action Return(True)

init python:
    def increase_page():
        global page_number
        if (page_number >= 3):
            page_number = 3
        else:
            page_number += 1

    def decrease_page():
        global page_number
        if (page_number == 1):
            page_number = 1
        else:
            page_number -= 1

default page_number = 1
screen tutorial_2():
    
    use overlay
    modal True
    frame:
        text "{u}{b}TUTORIAL{b}{u}" ypos 30 xpos 30
        xalign 0.5
        yalign 0.5
        yminimum 600
        xminimum 1500
        xmaximum 1500
        ymaximum 600
        xpadding 30
        ypadding 30
        frame:
            background Null()
            xalign 0.5
            yalign 0.5
            xmaximum 1500
            ymaximum 600
            xpadding 30
            ypadding 30
            vbox:
                text ""
                if (page_number == 1):
                    text "Hey there green horn, welcome to your first conflict. While working at Tan Tock Seng hospital, you will inevitably have to {color=#f4b157}resolve situations whether with your colleague or patient {/color}. The same is true for this game."
                elif (page_number == 2):
                    text "In this section of the game, you will need to {color=#f4b157}resolve the conflict through your decisions {/color} while trying your best to {color=#f4b157}raise trust points with other characters{/color}. Know that these two features are not mutually exclusive, sometimes {color=#f4b157}even with high trust points with a character in conflict, you may fail to resolve {/color} the situation because the accumulation of your choice is not optimal. Vice versa."
                else:
                    text "So make your choice wisely! {color=#f4b157}If you are able to resolve conflict with a high trust point, you may get some surprise rewards afterward!{/color}"
                text ""

        hbox:
            xalign 0.5
            yalign 0.95
            imagebutton:
                xpadding 100
                idle "images/dialogue/arrow left.png"
                hover "images/dialogue/arrow left hover.png"
                action Function(decrease_page)
            
            text "[page_number]" ypos 20 
            imagebutton:
                xpadding 100
                idle "images/dialogue/arrow right.png"
                hover "images/dialogue/arrow right hover.png"
                action Function(increase_page)
        
        if (page_number == 3):
            textbutton "Continue":
                ypos 450 xpos 1150
                action [Hide("tutorial_2"), Show("tutorial_guidebook_1")]

transform redbutton:
    xpos 0
    easeout 0.3 xpos 20
    easein 0.3 xpos 0
    repeat

default tutorial = True
screen tutorial_guidebook_1:
    modal True
    use overlay
    
    hbox:
        imagebutton:
            idle "images/notebook/guidebook icon.png" xpos 50 ypos 50
            hover "images/notebook/guidebook icon hover.png"
            action [Hide("tutorial_guidebook_1"), Show("tutorial_guidebook_2"), SetVariable("tutorial", True)]

        imagebutton at redbutton:
            idle "images/dialogue/arrow red.png" xpos 40 ypos 60



    frame:
        xalign 0.5
        yalign 0.5
        yminimum 600
        xminimum 1500
        xmaximum 1500
        ymaximum 600
        xpadding 30
        ypadding 30
        text "{u}{b}Six Tools Guidebook Tutorial{b}{u}" ypos 30 xpos 30
        frame:
            background Null()
            xalign 0.5
            yalign 0.5
            xmaximum 1500
            ymaximum 300
            xpadding 30
            ypadding 30
            vbox:
                text ""
                text "This guidebook will contain a set of essential tools needed to complete challenges you will face in TTSH both in game and real life."
                text ""

screen tutorial_guidebook_2_text:
    modal True
    frame:
        xalign 0.5
        yalign 0.5
        yminimum 600
        xminimum 1500
        xmaximum 1500
        ymaximum 600
        xpadding 30
        ypadding 30
        text "{u}{b}Six Tools Guidebook Tutorial{b}{u}" ypos 30 xpos 30
        frame:
            background Null()
            xalign 0.5
            yalign 0.5
            xmaximum 1500
            ymaximum 300
            xpadding 30
            ypadding 30
            vbox:
                text "For this tutorial, you will primarily be {color=#f4b157}utilising the shape tool and the trust tool{/color}. You {color=#f4b157}may refer to the guidebook at any time to look up terminologies and cases {/color}, but you will have to make the decision in problem solving yourself. Read up and determine your best course of actions."
                text ""
                textbutton "Close":
                    action Hide("tutorial_guidebook_2_text") ypos 20

screen tutorial_guidebook_2:
    modal True
    on "show" action Show("guidebook")
    on "show" action Show("tutorial_guidebook_2_text")
    
       
screen tutorial_trustpoint:
    use overlay
    $Tutorial = False
    frame:
        background Null()
        xmaximum 600
        ymaximum 200
        xpos 50
        ypos 20
        use show_npc_status
    
    frame:
        background Null()
        xpos 1150 ypos 10
        imagebutton at redbutton:
            idle "images/dialogue/arrow red reverse.png" xpos 2540 ypos 40

    frame:
        xalign 0.5
        yalign 0.5
        yminimum 600
        xminimum 1500
        xmaximum 1500
        ymaximum 600
        xpadding 30
        ypadding 30
        text "{u}{b}Trust Point Tutorial{b}{u}" ypos 30 xpos 30
    
        frame:
            background Null()
            xalign 0.5
            yalign 0.5
            xmaximum 1500
            ymaximum 300
            xpadding 30
            ypadding 30
            vbox:
                text ""
                text "Trust point will determine the level of bond and affection you have with certain characters. {color=#f4b157}Accumulating enough trust point may help you achieve alternative approaches to conflict resolution{/color}, it may even get you some sweet reward down the line"
                text ""
                textbutton "Close":
                    action [Hide("tutorial_trustpoint"), Return(True)] ypos 20

    
                
                



