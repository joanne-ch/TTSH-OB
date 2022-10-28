default quiz_score = 0

label quiz_shape:
    #Choose which Chapter Quiz
    call screen quiz_selection
    if(quiz_num == 1):
        jump question1_shape
    elif (quiz_num == 2):
        jump question2_shape
    elif(quiz_num == 3):
        call screen under_constructionDialog
        jump quiz_shape

    jump quiz_shape

label question1_shape:
    centered "{u}Personality Shapes{u}"
    call screen quiz_screen("1. Some characteristics of a Square-personality type individual:")
    menu:
        "a)	Works best in teams, empathetic & compassionate, can’t say no":
            jump question2_shape
        "b)	Detail-oriented, Analytical & hesitant to change":
            $quiz_score += 1
            jump question2_shape
        "c)	Like to be in-charge, rarely apologize & extremely confident":
            jump question2_shape
        "d)	Love to try new things, idea generators and not as organized as they should be":
            jump question2_shape

label question2_shape:
    call screen quiz_screen("2.	Pick the one characteristic unlike of a Circle-personality type individual:")
    menu:
        "a)	Welcomes peer motivation to succeed":
            jump question3_shape
        "b)	Loves working  with data, policies and procedures over people":
            $quiz_score += 1
            jump question3_shape
        "c)	Get along well with squiggles best:":
            jump question3_shape
        "d)	Dislikes conflicts and confrontation, better at mediating ":
            jump question3_shape

label question3_shape:
    call screen quiz_screen("3.	Some characteristics of a Triangle-personality type individual:")
    menu:
        "a)	Prioritizes bottom line and accomplishing set goals":
            $quiz_score += 1
            jump question4_shape
        "b)	Don’t like to be told what to do":
            jump question4_shape
        "c)	Believes in working hard than working smart":
            jump question4_shape
        "d)	Loves to have fun and laugh":
            jump question4_shape

label question4_shape:
    call screen quiz_screen("4.	Pick the {u}one{u} characteristic unlike of a Squiggle-personality type individual:")
    menu:
        "a)	Shoot from the hip – don’t always do deep research first":
            jump question5_shape
        "b)	Visionary; but others may not get what they are saying/seeing":
            jump question5_shape
        "c)	More logical than creative":
            $quiz_score += 1
            jump question5_shape
        "d)	Speak before they think; Able to shift from topic to topic easily ":
            jump question5_shape

label question5_shape:
    call screen quiz_screen("5.	We typically have a dominant personality and may have a secondary personality at work. It may be influenced by our role functions. Understanding ourselves is the first step to working well with others.")
    menu:
        "True":
            $quiz_score += 1
            jump question6_shape
        "False":
            jump question6_shape
        
label question6_shape:
    call screen quiz_screen("6.	The awareness of your own personality and working tendencies, as well as those of others you work with, is to:")
    menu:
        "a)	Insist that your personality is better than others":
            jump end_quiz
        "b)	Be more efficient and effective on your own":
            jump end_quiz
        "c)	Flex your personality range to work better with others and serve our patients well":
            $quiz_score += 1
            jump end_quiz
        "d)	Forecast what actions other may take because personality typing guarantees stereotypes all the time":
            jump end_quiz

label question1_ladder:
    centered "{u}Ladder of Inference{u}"
    call screen quiz_screen("1.	People often draw meaning and inferences from what others say and do, based on their past experience which could lead to misunderstandings and conflicts. Time permitting, we should reflect instead of taking the reflex responses.")
    menu:
        "True":
            $quiz_score += 1
            jump question2_ladder
        "False":
            jump question2_ladder

label question2_ladder:
    call screen quiz_screen("2.	What are the thinking steps of the Ladder of Inference?")
    menu:
        "a)	Actions – Analysis – Criticism – Recommendations":
            jump question3_ladder
        "b)	Observations – Selected Data – Meanings – Assumptions – Beliefs – Actions - Conclusions":
            jump question3_ladder
        "c)	Select Data – Observation – Assumptions – Meanings – Actions - Conclusions":
            jump question3_ladder
        "c)	Select Data – Observation – Assumptions – Meanings – Actions - Conclusions":
            $quiz_score += 1
            jump question3_ladder

label question3_ladder:
    call screen quiz_screen("3.	To avoid jumping to conclusions, we should access how we think and break down the assumptions, meaning, selected data and observations we made. ")
    menu:
        "True":
            $quiz_score += 1
            jump end_quiz
        "False":
            jump end_quiz


label end_quiz:
    centered "Your score is [quiz_score]"
    $quiz_score = 0