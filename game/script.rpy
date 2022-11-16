
######################import scene 1 character, "doctor A" and "me"
define d = Character('Doctor A', color="#c8ffc8", what_outlines=[(5, "#000000", 0, 0)])
define m = Character('[persistent.user_name]', color="#c8c8ff", what_outlines=[(5, "#000000", 0, 0)])
define p = Character('Patient', color="#c8c8ff", what_outlines=[(5, "#000000", 0, 0)])
define j = Character('Jia', color="#c8c8ff", what_outlines=[(5, "#000000", 0, 0)])
define mo = Character('Mother', color="#c8c8ff", what_outlines=[(5, "#000000", 0, 0)])
define dau = Character('Daughter', color="#c8c8ff", what_outlines=[(5, "#000000", 0, 0)])
##################start scene_1_1 (chapter1_scene1)

label start:
    #call screen opening_screen("Prologue")

    scene black
    with Pause(1)
    voice "audio/scene_1/scene1_1.ogg"

    ##########################################################
    #jump start_chapter3
#########################################################
    
    call screen narration("You are a new-hire at TTSH, this is your first day of work as a nurse.") #changed
    
    voice "audio/scene_1/scene1_2.ogg"
    #centered "You were informed that you will be given a tour today around the hospital and possibly get to know some of your colleagues."
    call screen narration("Welcome! You will be brought on a tour and meet some of your new collegues.") #changed

    voice "audio/scene_1/scene1_3.ogg"
    call screen narration("Excited and a bit nervous, you enter the main lobby of Tan Tock Seng Hospital.")
    $ renpy.movie_cutscene ("video/Opening.webm")

    scene bg main_background #import background
    with fade
    show doctor_icon at right #import character doctor A
    with dissolve

    #doctor A uses Heather
    voice "audio/scene_1/Good morning, so good to finally meet you in perso.mp3"
    d "Good morning, so good to finally meet you in person [persistent.user_name]. We are very excited to have you on board of TTSH. My name is Doctor A. "
    voice "audio/scene_1/I believe H R has briefed you that you'd be workin.mp3"
    d "I believe HR has briefed you that you’d be working with me for the first few months of your appointment."
    voice "audio/scene_1/Today, I will just be showing you around the hospi.mp3"
    d "Today, I will just be showing you around the hospital, our offices and do feel free to ask any questions."

    #make choice 

    #TUTORIALL(FOR CHOICE PICKING) 
    call screen direction_1

    menu:
        "Good to meet you too, A, looking forward to working with you!":
            jump scene_1_1_1  #go to chapter1_scene1_branch1

        "Great, let’s get started then!":
            jump scene_1_1_2 #go to chapter1_scene1_branch2

        "Before we start the tour, I do have some questions…":
            jump scene_1_1_3 #go to chapter1_scene1_branch3

    return 

# Scene ONE
label end_ofscene1:
    scene black
    with Pause(1)

    jump scene_1_2
    return

label scene_1_1_1: #scene 1, branch 1
    show doctor_icon at right #import character doctor A
    with dissolve 

    #tutorial
    call screen direction_function
    voice "audio/scene_1/The pleasure is all mine!.mp3"
    d "The pleasure is all mine!"

    voice "audio/scene_1/ve heard.mp3"
    d "I’ve heard great things about you, but just a heads-up, this job can be quite demanding, I hope you’ll keep up your spirit! Now then, do you want to start the tour? "

    menu:
        "Yes, let’s get started.":
            jump end_ofscene1 

        "I do have some questions…":
            jump scene_1_1_3 # go to the third branch
    return 

label scene_1_1_2:
    show doctor_icon at right
    with dissolve
    #tutorial
    call screen direction_function
    voice "audio/scene_1/I like your spirit, getting right to the point! Th.mp3"
    d " I like your spirit, getting right to the point! Then let’s get started."

    jump end_ofscene1 # go to scene2
    
    return 

label scene_1_1_3:
    show doctor_icon at right
    with dissolve
    #tutorial
    call screen direction_function
    voice "audio/scene_1/an eager one.mp3"
    d "You’re an eager one, aren’t you!"
    
    voice "audio/scene_1/no rush, we have plenty of time for Q&A as.mp3"
    d " There’s no rush, we have plenty of time for Q&A as we tour, but I don’t mind giving any clarifications now."


    jump scene_1_2
    #################################
    menu:
        "What will be my duty as a (Job role: Nurse)?":
            call screen under_constructionDialog
            jump end_ofscene1
        "Can you tell me more about TTSH?":
            d "let me intro to you where you are at."
            call screen map
            jump end_ofscene1
        "Who else will I be working with?":
            call screen under_constructionDialog
            jump end_ofscene1
        "Which area will I be working at the most?":
            call screen under_constructionDialog
            jump end_ofscene1
        "I think I have no further questions":
            voice "audio/scene_1/Great, as I was saying, today.mp3"
            d"Great, as I was saying, today we’re just here to see around the office space and the hospital ground, no 	need to rush yourself to anything yet. "
            jump end_ofscene1
    
    return


#Scene TWO
label end_ofscene2:
    scene black
    with Pause(1)
    #return
    #choose chapter
    call screen quiz_chapter_selection
    #call screen chapter_selection
    
    if(chap_num == 1):
        jump scene_1_3
    elif (chap_num == 2):
        jump start_chapter2
    elif(chap_num == 3):
        jump start_chapter3
    elif(chap_num == 0):
        jump end
    elif(chap_num == -1):
        #$quiz_chapter == 1
        jump quiz_shape
        

label end:
    scene black
    with Pause(1)
    return

label scene_1_2: #chapter1_scene2
    scene bg nursing hallway
    #call screen map #second page delete

    #voice "audio/scene_2/On the first floor.mp3"
    #d"On the first floor, we have…"
    #voice "audio/scene_2/On the second floor.mp3"
    #d "On the second floor, we have…"
    #voice "audio/scene_2/On the third  floor.mp3"
    #d "On the third  floor, we have…"
    #voice "audio/scene_2/This is our main office and where you can work & r.mp3"
    #d "This is our main office and where you can work & rest during off-hour"
    #voice "audio/scene_2/Here is the nurse war.mp3"
    #d "Here is the nurse ward…"
    #voice "audio/scene_2/This is where you will be working most of the day,.mp3"
    #d "This is where you will be working most of the day, tending to patients assigned to you. Do you have any questions so far? "

    menu:
        "No, I have no question at the moment.":
            jump scene_1_2_1 #chapter1_scene2_branch1
        "Actually, I do have some questions…":
            jump scene_1_2_2 #chapter1_scene2_branch2
    
    return

label scene_1_2_1:
    voice "audio/scene_2/Great, well, I think we are almost done with today.mp3"
    d "Great, well, I think we are almost done with today’s tour, now we just--…"
    jump end_ofscene2
    return

label scene_1_2_2:
    menu:
        "What will be my duty as a (Job role: Nurse)?":
            call screen under_constructionDialog
            jump scene_1_2_2
        "Can you tell me more about TTSH?":
            d "let me intro to you where you are at."
            call screen map
            jump scene_1_2_2
        "Who else will I be working with?":
            call screen under_constructionDialog
            jump scene_1_2_2
        "Which area will I be working at the most?":
            call screen under_constructionDialog
            jump scene_1_2_2
        "I think I have no further questions":
            jump scene_1_2_1

    return