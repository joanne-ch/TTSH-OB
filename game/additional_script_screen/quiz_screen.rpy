init python:
    def increase_score():
        global quiz_score
        quiz_score +=1

screen quiz_screen_question(isFour, quiz_question, quiz_number, correctChoice, choice1, choice2, choice3, choice4):
    tag quiz
    vbox:
        frame:
            background Null()
            xalign 1.15
            xminimum 500
            xmaximum 500
            yminimum 50
            ymaximum 50
            top_margin 30
            text "Quiz Score: [quiz_score]"
        
        frame:
            background Null()
            xminimum 1900
            xmaximum 1900
            yminimum 300
            ymaximum 300
            xalign 0.5
            top_margin 20
            left_margin 40
            frame:
                background Null()
                xminimum 500
                xmaximum 500
                yminimum 100
                ymaximum 100
                xalign 1.05
                top_margin 50
                if(Clicked_1 or Clicked_2 or Clicked_3 or Clicked_4):
                    textbutton"Continue" xalign 0.5 yalign 0.5:
                        action [Return(True), SetVariable("Clicked_1", False), 
                        SetVariable("Clicked_2", False),  SetVariable("Clicked_3", False), 
                        SetVariable("Clicked_4", False),  SetVariable("SecondClick", False)
                        ]

            vbox:
                #xalign 0.2
                #yalign 0.5
                text "{u}Question [quiz_number]{u}"  style "mainText" color "#ffffff" 
                frame:
                    background Null()
                    xminimum 1900
                    xmaximum 1900
                    yminimum 210
                    ymaximum 210
                    text [quiz_question] style "subMain" color "#ffffff" size 50 xalign 0.5 yalign 0.5
        if (isFour):
            use choice_four(choice1, choice2, choice3, choice4, correctChoice)
        else:
            use choice_two(choice1, choice2, correctChoice)


screen choice_four(choice1, choice2, choice3, choice4, correctChoice):
    tag quiz
    frame:
        background Null()
        top_margin 50
        xminimum 1900
        xmaximum 1900
        yminimum 700
        ymaximum 700
    
        vbox:
            xalign 0.5
            use choicebar_four(choice1, 1, correctChoice)
            use choicebar_four(choice2, 2, correctChoice)
            use choicebar_four(choice3, 3, correctChoice)
            use choicebar_four(choice4, 4, correctChoice)

default Clicked_1 = False
default Clicked_2 = False
default Clicked_3 = False
default Clicked_4 = False
default SecondClick = False

screen choicebar_four(choice, indexNo, CorrectNo):
    frame:
        background Null()
        xminimum 1900
        xmaximum 1900
        yminimum 160
        ymaximum 160
        top_margin 20
        imagebutton:
            idle "images/quiz_selection/choice_small_bg.png"
            hover "images/quiz_selection/choice_small_bg_hover.png"
            if (CorrectNo == indexNo):
                if (indexNo == 1):
                    action [Function(increase_score), ToggleVariable("Clicked_1")]
                elif (indexNo == 2):
                    action [Function(increase_score), ToggleVariable("Clicked_2")]
                elif (indexNo == 3):
                    action [Function(increase_score), ToggleVariable("Clicked_3")]
                elif (indexNo == 4):
                    action [Function(increase_score), ToggleVariable("Clicked_4")]
            else:
                if (indexNo == 1):
                    action [ToggleVariable("Clicked_1")]
                elif (indexNo == 2):
                    action [ToggleVariable("Clicked_2")]
                elif (indexNo == 3):
                    action [ToggleVariable("Clicked_3")]
                elif (indexNo == 4):
                    action [ToggleVariable("Clicked_4")]
        text "[choice]" xalign 0.5 yalign 0.5 color"#000000"

        if(Clicked_1 or Clicked_2 or Clicked_3 or Clicked_4): 
            if (indexNo == CorrectNo):
                imagebutton:
                    idle "images/quiz_selection/choice_small_bg_correct.png"
            elif (Clicked_1 and indexNo == 1):
                imagebutton:
                    idle "images/quiz_selection/choice_small_bg_incorrect.png"
            elif (Clicked_2 and indexNo == 2):
                imagebutton:
                    idle "images/quiz_selection/choice_small_bg_incorrect.png"
            elif (Clicked_3 and indexNo == 3):
                imagebutton:
                    idle "images/quiz_selection/choice_small_bg_incorrect.png"
            elif (Clicked_4 and indexNo == 4):
                imagebutton:
                    idle "images/quiz_selection/choice_small_bg_incorrect.png"

        text "[choice]" xalign 0.5 yalign 0.5 color"#000000"

screen choice_two(choice1, choice2, CorrectNo):
    tag quiz
    frame:
        background Null()
        top_margin 50
        xminimum 1900
        xmaximum 1900
        yminimum 400
        ymaximum 400
        
    
        vbox:
            xalign 0.5
            use choicebar_two(choice1, 1, CorrectNo)
            use choicebar_two(choice2, 2, CorrectNo)

screen choicebar_two(choice, indexNo, CorrectNo):
    
    frame:
        background Null()
        xminimum 1900
        xmaximum 1900
        yminimum 160
        ymaximum 160
        top_margin 20
        imagebutton:
            idle "images/quiz_selection/choice_small_bg.png"
            hover "images/quiz_selection/choice_small_bg_hover.png"
            if (CorrectNo == indexNo):
                if (indexNo == 1):
                    action [Function(increase_score), ToggleVariable("Clicked_1")]
                elif (indexNo == 2):
                    action [Function(increase_score), ToggleVariable("Clicked_2")]
            else:
                if (indexNo == 1):
                    action [ToggleVariable("Clicked_1")]
                elif (indexNo == 2):
                    action [ToggleVariable("Clicked_2")]
        text "[choice]" xalign 0.5 yalign 0.5 color"#000000"

        if(Clicked_1 or Clicked_2): 
            if (indexNo == CorrectNo):
                imagebutton:
                    idle "images/quiz_selection/choice_small_bg_correct.png"
            elif (Clicked_1 and indexNo == 1):
                imagebutton:
                    idle "images/quiz_selection/choice_small_bg_incorrect.png"
            elif (Clicked_2 and indexNo == 2):
                imagebutton:
                    idle "images/quiz_selection/choice_small_bg_incorrect.png"

        text "[choice]" xalign 0.5 yalign 0.5 color"#000000"



