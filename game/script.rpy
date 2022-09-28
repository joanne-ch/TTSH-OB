
######################import scene 1 character, "doctor A" and "me"
define d = Character('doctor A', color="#c8ffc8", what_outlines=[(5, "#000000", 0, 0)])
define m = Character('me', color="#c8c8ff")
define p = Character('patient', color="#c8c8ff")

##################start scene_1_1 (chapter1_scene1)

label start: 

    scene black
    with Pause(1)
    centered "You have just become a new-hire of TTSH, it is your first day at the hospital as an official worker (Nurse)."
    centered "You were informed that you will be given a tour today around the hospital and possibly get to know some of your colleagues."
    centered "Excited and a bit nervous, you enter the main lobby of Tan Tock Seng Hospital."
    $ renpy.movie_cutscene("video/Opening.ogg")
    with Pause(3)

    scene bg main_background #import background
    with fade
    show doctor_icon at right #import character doctor A
    with dissolve

    d "Good morning, so good to finally meet you in person [persistent.user_name]. We are very excited to have you on board of TTSH. My name is Doctor A. "

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

# Scene ONE
label end_ofscene1:
    scene black
    with Pause(1)

    jump scene_1_2 
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

    menu:
        "What will be my duty as a (Job role: Nurse)?":
            return
        "Can you tell me more about TTSH?":
            return
        "Who else will I be working with?":
            return
        "Which area will I be working at the most?":
            return
        "I think I have no further questions":
            d"Great, as I was saying, today we’re just here to see around the office space and the hospital ground, no 	need to rush yourself to anything yet. "
            jump end_ofscene1
    
    return


#Scene TWO
label end_ofscene2:
    scene black
    with Pause(1)

    jump scene_1_3
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
            jump scene_1_2_1 #chapter1_scene2_branch1
        "Actually, I do have some questions…":
            jump scene_1_2_2 #chapter1_scene2_branch2
    
    return

label scene_1_2_1:
    d "Great, well, I think we are almost done with today’s tour, now we just--…"
    jump end_ofscene2
    return

label scene_1_2_2:
    menu:
        "Can you run me through the first floor again…":
            jump scene_1_2_2
        "Can you run me through the second floor again…":
            jump scene_1_2_2
        "Can you run me through the third floor again…":
            jump scene_1_2_2
        "Can you run me through the main office area again…":
            jump scene_1_2_2
        "Can you run me through the nursing ward again…":
            jump scene_1_2_2
        "I think I have no further questions":
            jump end_ofscene2

    return

#Scene THREE
label scene_1_3:
    d "Alright, I hope that clarifies everything"

    centered "(Doctor A receives a phone call, after taking the call, he needed to leave for an emergency situation, he promises he will be back in sometime later)"
    centered "You are now in the nursing ward hallway. As you patiently wait for A’s return, you notice a patient sitting impatiently with her arm crossed."
    centered "She seems quite upset and is clearly waiting for some sort of appointment."
    centered "While you have been hired as a nurse, it is not your first official day of work, do you want to approach this upset patient?"

    call screen tutorial 

    menu:
        "Even though my shift hasn’t officially started, I should help this patient. They seem very upset.":
            jump scene_1_3_1

        "I should focus on the tour, besides, I am sure it is nothing urgent.":
            jump scene_1_3_2
    return

label scene_1_3_1:
    centered "You see a elderly female patient impatiently seated in the hallway. She seems to be waiting for something, tapping her thumbs and cursing under her lips."

    menu:
        "*Take a closer look at the patient before speaking*":
            centered "You got a closer look at the patient. She is an elderly lady likely in her 60s. She seems to be mumbling to herself while seated in the patient ward hall. You see that she also carries a walking stick, and there were signs of recent operation on her right leg."
            jump scene_1_3_1
        "Mam, can I help you?":
            p"You can help me by getting my appointment started! I’ve been waiting here for 2 HOURS, can you imagine? And I just had my surgery! This is unacceptable!"
            jump scene_1_3_1_2

label scene_1_3_1_2:
    centered "You decide to try to calm her down first"
    call screen show_trust
    menu:
        "I’m so sorry for your situation mam, it is a busy day for the hospital so I hope you may understand.":
            $trust_level += 1
            p "I’m sure you’re sorry, but I have already waited for so long. But I guess you are right, there are a lot of people today for some reason. But your hospital really ought to improve your wait time."
            jump scene_1_3_1_3
        "I’m so sorry that you feel this way, but it is a busy day for the hospital so I hope you understand.":
            p "How I feel’ is irrelevant, the fact is that I have been waiting here for 2 hours and there has been no update. It doesn’t matter if there’s a lot of people, we all deserve better treatment and wait time!”"
            jump scene_1_3_1_3
        "Mam. I need you to calm down, this isn’t going to help you get in any sooner. You are only making a scene.":
            $trust_level -=1
            p "How dare you tell me what to do? I am making a scene? How about you go and ask why they are making us wait for so long?"
            jump scene_1_3_1_3
        "Mam, I will go talk to the doctor in charge right away, but I think you should also calm down first.":
            $trust_level = trust_level + 2
            p"That’s what I like to hear, you better go check what’s going on with the clinic today."
            jump scene_1_3_1_3

label scene_1_3_1_3:
    call screen show_trust
    return
