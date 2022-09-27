
######################import scene 1 character, "doctor A" and "me"
define d = Character('doctor A', color="#c8ffc8")
define m = Character('me', color="#c8c8ff")

##################start scene_1_1 (chapter1_scene1)

screen summary():
    frame:
        xalign 0.5 ypos 50
        vbox:
            text "You have just become a new-hire of TTSH, it is your first day at the hospital as an official worker (Nurse)."
            text "You were informed that you will be given a tour today around the hospital and possibly get to know some of your colleagues."
            text "Excited and a bit nervous, you enter the main lobby of Tan Tock Seng Hospital."
            textbutton "Continue":
                action Return(True)

label start: 

    call screen summary

    scene bg main_background #import background
    with fade
    show doctor_icon at right #import character doctor A
    with dissolve

    d "Good morning, so good to finally meet you in person Kamala. We are very excited to have you on board of TTSH. My name is Doctor A. "

    d " I believe HR has briefed you that you’d be working with me for the first few months of your appointment."

    d "Today, I will just be showing you around the hospital, our offices and do feel free to ask any questions."

    #make choice 
    menu:
        "Good to meet you too, A, looking forward to working with you!":
            jump scene_1_1_1  #go to chapter1_scene1_branch1

        "Great, let’s get started then!":
            jump scene_1_1_2 #go to chapter1_scene1_branch2

        "Before we start the tour, I do have some questions…":
            jump scene_1_1_3 #go to chapter1_scene1_branch3

    return 


label scene_1_1_1: #scene 1, branch 1

    show doctor_icon at right #import character doctor A
    with dissolve 

    d "The pleasure is all mine!"
    d "I’ve heard great things about you, but just a heads-up, this job can be quite demanding, I hope you’ll keep up your spirit! Now then, do you want to start the tour? "

    menu:
        "Yes, let’s get started.":
            jump end_ofscene1 

        "I do have some questions…":
            jump scene_1_1_3 # go to the third branch

    return 

label end_ofscene1:
    scene black
    with Pause(1)

    jump scene_2_1
    return

label scene_1_1_2:

    show doctor_icon at right
    with dissolve

    d " I like your spirit, getting right to the point! Then let’s get started."
    jump end_ofscene1 # go to scene2
    
    return 

label scene_1_1_3:

    show doctor_icon at right
    with dissolve

    d "You’re an eager one, aren’t you!"
    d " There’s no rush, we have plenty of time for Q&A as we tour, but I don’t mind giving any clarifications now."

    jump scene_1_2 #finish scene_1_1, jump to scene_1_2 (chapter1, scene2)
    return

label scene_1_2: #chapter1_scene2
    d"On the first floor, we have…"

    d "On the second floor, we have…"

    d "On the third  floor, we have…"

    d "This is our main office and where you can work & rest during off-hour"

    d "Here is the nurse ward…"

    d "This is where you will be working most of the day, tending to patients assigned to you. Do you have any questions so far? "

    menu:
        "No, I have no question at the moment.":
            jump scene2_2_1 #chapter1_scene2_branch1
        "Actually, I do have some questions…":
            jump scene2_2_2 #chapter1_scene2_branch2
    
    return

label scene2_2_1:
    d "Great, well, I think we are almost done with today’s tour, now we just…"
    jump end_ofscene2
    return

label end_ofscene2:
    scene black
    with Pause(1)

    jump scene_2_1_1
    return

label scene2_2_2:
    # menu:
    #     "Can you run me through the first floor again…"
    #         jump scene2_2_2
    #     "Can you run me through the second floor again…"
    #         jump scene2_2_2
    #     "Can you run me through the third floor again…"
    #         jump scene2_2_2
    #     "Can you run me through the main office area again…"
    #         jump scene2_2_2
    #     "Can you run me through the nursing ward again…"
    #         jump scene2_2_2

    return