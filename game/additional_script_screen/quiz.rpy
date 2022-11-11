default quiz_score = 0

label quiz_shape:
    #Choose which Chapter Quiz

    call screen quiz_selection
    if(quiz_num == 1):
        jump question1_shape
    elif (quiz_num == 2):
        jump question2_ladder
    elif(quiz_num == 3):
        jump quiz3_inquiry

    return

label question1_shape:
    centered "{u}Personality Shapes{u}"
    $quiz_score = 0
    call screen quiz_screen_question(True, "Some characteristics of a Square-personality type individual:", "1", 2
    , "a)	Works best in teams, empathetic & compassionate, can’t say no"
    , "b)	Detail-oriented, Analytical & hesitant to change"
    , "c)	Like to be in-charge, rarely apologize & extremely confident"
    , "d)	Love to try new things, idea generators and not as organized as they should be")


    call screen quiz_screen_question(True, "Pick the one characteristic unlike of a Circle-personality type individual:","2", 2
    , "a)	Welcomes peer motivation to succeed"
    , "b)	Loves working with data, policies and procedures over people"
    , "c)	Get along well with squiggles best"
    , "d)	Dislikes conflicts and confrontation, better at mediating ")

    
    call screen quiz_screen_question(True, "Some characteristics of a Triangle-personality type individual:","3", 1
    , "a)	Prioritizes bottom line and accomplishing set goals"
    , "b)	Don’t like to be told what to do"
    , "c)	Believes in working hard than working smart"
    , "d)	Loves to have fun and laugh")

    call screen quiz_screen_question(True, "Pick the one characteristic unlike of a Squiggle-personality type individual:","4", 3
    , "a)	Shoot from the hip – don’t always do deep research first"
    , "b)	Visionary; but others may not get what they are saying/seeing"
    , "c)	More logical than creative"
    , "d)	Speak before they think; Able to shift from topic to topic easily ")


    call screen quiz_screen_question(False, "We typically have a dominant personality and may have a secondary personality at work. It may be influenced by our role functions. Understanding ourselves is the first step to working well with others.","5", 1
    , "a)	True"
    , "b)	False"
    , Null
    , Null)

    call screen quiz_screen_question(True, "6.	The awareness of your own personality and working tendencies, as well as those of others you work with, is to:","6" , 3
    , "a)	Insist that your personality is better than others"
    , "b)	Be more efficient and effective on your own"
    , "c)	Flex your personality range to work better with others and serve our patients well"
    , "d)   Forecast other's action because personality typing guarantees stereotypes")

    jump end_quiz
    
label question2_ladder:
    centered "{u}Ladder of Inference{u}"
    $quiz_score = 0

    call screen quiz_screen_question(False, "People often draw meaning and inferences from what others say and do, based on their past experience which could lead to misunderstandings and conflicts. Time permitting, we should reflect instead of taking the reflex responses.","1", 1
    , "a)	True"
    , "b)	False"
    , Null
    , Null)

    call screen quiz_screen_question(True, "What are the thinking steps of the Ladder of Inference?", "2", 4
    , "a)	Actions – Analysis – Criticism – Recommendations"
    , "b)	Observations – Selected Data – Meanings – Assumptions – Beliefs – Actions - Conclusions"
    , "c)	Select Data – Observation – Assumptions – Meanings – Actions - Conclusions"
    , "d)	Observations – Selected Data – Meanings – Assumptions – Conclusions – Beliefs – Actions")

    call screen quiz_screen_question(False, "To avoid jumping to conclusions, we should access how we think and break down the assumptions, meaning, selected data and observations we made. ","3", 1
    , "a)	True"
    , "b)	False"
    , Null
    , Null)

    jump end_quiz

label quiz3_inquiry:
    centered "{u}Inquiry and Advocacy{u}"
    $quiz_score = 0

    call screen quiz_screen_question(True, "What makes quality interactions? ", "1", 3
    , "a)	Just focus on listening and keep quiet"
    , "b)	Share everything you think in your left-hand column to show that you trust the other person"
    , "c)	Exercise a good balance of inquiry (ask) and advocacy (tell)"
    , "d)	Criticize when mistakes are made so that they learn ")

    call screen quiz_screen_question(True, "What makes quality interactions? ", "2", 4
    , "a)	To gain insights"
    , "b)	By asking from a position of curiosity and not criticism"
    , "c)	To not misinterpret matters according to our own mental models"
    , "d)	To gain brownie points from our bosses by being seen as enthusiastic")

    call screen quiz_screen_question(False, "12.	To understand either position in a conversation, all parties involved will need to exercise deep listening.","3", 1
    , "a)	True"
    , "b)	False"
    , Null
    , Null)

    jump end_quiz




label end_quiz:
    centered "Your score is [quiz_score]"
    $quiz_score = 0
    jump quiz_shape