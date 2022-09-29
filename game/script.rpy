
######################import scene 1 character, "doctor A" and "me"
define d = Character('Doctor A', color="#c8ffc8", what_outlines=[(5, "#000000", 0, 0)])
define m = Character('me', color="#c8c8ff")
define p = Character('Patient', color="#c8c8ff", what_outlines=[(5, "#000000", 0, 0)])

##################start scene_1_1 (chapter1_scene1)

label start: 
    scene black
    with Pause(1)
    voice "audio/scene_1/scene1_1.ogg"
    centered "You have just become a new-hire of TTSH, it is your first day at the hospital as an official worker (Nurse)."
    
    voice "audio/scene_1/scene1_2.ogg"
    centered "You were informed that you will be given a tour today around the hospital and possibly get to know some of your colleagues."
    
    voice "audio/scene_1/scene1_3.ogg"
    centered "Excited and a bit nervous, you enter the main lobby of Tan Tock Seng Hospital."
    $ renpy.movie_cutscene ("video/Opening.webm")

    scene bg main_background #import background
    with fade
    show doctor_icon at right #import character doctor A
    with dissolve

    d "Good morning, so good to finally meet you in person [persistent.user_name]. We are very excited to have you on board of TTSH. My name is Doctor A. "

    d "I believe HR has briefed you that you’d be working with me for the first few months of your appointment."

    d "Today, I will just be showing you around the hospital, our offices and do feel free to ask any questions."

    #make choice 

    #TUTORIALL(FOR CHOICE PICKING) 

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

    play sound "audio/phone.mp3"
    centered "Doctor A receives a phone call, after taking the call, she needed to leave for an emergency situation, she promises she will be back in sometime later"
    stop sound fadeout 0.5
    
    call screen narration("You are now in the nursing ward hallway. As you patiently wait for A’s return, you notice a patient sitting impatiently with her arm crossed.")
    show hallway_grandma
    centered ""
    call screen narration("She seems quite upset and is clearly waiting for some sort of appointment.")
    $ renpy.movie_cutscene ("video/angry grandma.webm")
    call screen narration("While you have been hired as a nurse, it is not your first official day of work, do you want to approach this upset patient?")

    call screen tutorial 

    menu:
        "Even though my shift hasn’t officially started, I should help this patient. They seem very upset.":
            jump scene_1_3_1

        "I should focus on the tour, besides, I am sure it is nothing urgent.":
            jump scene_1_3_2
    return

default look = False
default second_loop = False
label scene_1_3_1:

    image grandma icon leg:
        animation
        xpos 1350
        ypos 1100
        zoom 1.2
        "grandma icon leg.png" 
        rotate 0.0
        easeout 0.3 rotate 4.0
        easein 0.3 rotate 0.0
        repeat

    image grandma icon:
        animation
        xpos 1350
        ypos 1100
        zoom 1.2
        "grandma icon.png" 
        rotate 0.0
        easeout 0.3 rotate 4.0
        easein 0.3 rotate 0.0
        repeat

    image angry icon:
        animation
        xpos 1150 
        ypos 400
        "angry icon.png"
        zoom 0.6 
        easeout 0.3 zoom 1.0
        easein 0.3 zoom 0.6
        repeat
    
    image grandma icon static:
        ypos 2000
        xpos 1450
        "grandma icon static.png"
        zoom 2.8
        
    if (second_loop == False):
        call screen narration("You see a elderly female patient impatiently seated in the hallway. She seems to be waiting for something, tapping her thumbs and cursing under her lips.")
    
    show nursing hallway
    if look: 
        show grandma icon leg
    else:
        show grandma icon
    
    show angry icon
    
    voice "audio/angry-grandma.ogg"
    centered ""

    menu:
        "*Take a closer look at the patient before speaking*":
            call screen narration("You got a closer look at the patient. She is an elderly lady likely in her 60s. She seems to be mumbling to herself while seated in the patient ward hall. You see that she also carries a walking stick, and there were signs of recent operation on her right leg.")
            $ look = True
            $ second_loop = True
            jump scene_1_3_1

        "Mam, can I help you?":
            hide grandma icon leg
            hide grandma icon
            
            show grandma icon static

            p"You can help me by getting my appointment started! I’ve been waiting here for 2 HOURS, can you imagine? And I just had my surgery! This is unacceptable!"
            
            jump scene_1_3_1_2
    
    return

label scene_1_3_1_2:
    image happy grandma:
        ypos 2000
        xpos 1450
        "happy grandma.png"
        zoom 2.8
    
    call screen narration("The patient continues to rant as if you are not there. What should you do in this situation?")
    
    call screen tutorial_2
    
    centered ""
    
    jump scene_1_3_1_3

    return

label scene_1_3_1_3:
    call screen narration("You decide to try to calm her down first")
    show screen show_npc_status
    show screen guidebook_icon

    menu:
        "I’m so sorry for your situation mam, it is a busy day for the hospital so I hope you may understand.":
            $trust_level += 1
            hide angry icon
            hide grandma icon static
            show happy grandma
            p "I’m sure you’re sorry, but I have already waited for so long. But I guess you are right, there are a lot of people today for some reason. But your hospital really ought to improve your wait time."
            jump scene_1_3_1_4
        "I’m so sorry that you feel this way, but it is a busy day for the hospital so I hope you understand.":
            p "How I feel is irrelevant, the fact is that I have been waiting here for 2 hours and there has been no update. It doesn’t matter if there’s a lot of people, we all deserve better treatment and wait time!"
            jump scene_1_3_1_4
        "Mam. I need you to calm down, this isn’t going to help you get in any sooner. You are only making a scene.":
            $trust_level -= 1
            p "How dare you tell me what to do? I am making a scene? How about you go and ask why they are making us wait for so long?"
            jump scene_1_3_1_4
        "Mam, I will go talk to the doctor in charge right away, but I think you should also calm down first.":
            $trust_level = trust_level + 2
            hide angry icon
            hide grandma icon static
            show happy grandma          
            p "That’s what I like to hear, you better go check what’s going on with the clinic today."
            jump scene_1_3_1_4
    
    return

    
label scene_1_3_1_4:
    call screen narration("You decide to learn more about the patient now that she has calmed down a bit")
    menu:
        "What is your name madam?":
            p"It’s Merry Ho."
            jump scene_1_3_1_5

        "What are you visiting SOC for?":
            p"I have to check on my knee after the surgery."
            jump scene_1_3_1_5
        
        "How long have you been waiting?":
            p"TWO HOURS! Can you believe it, I know the hospital is busy and all but this is simply outrageous…"
            call screen narration("You quickly dropped the subject to prevent another rant")
            jump scene_1_3_1_5
        
        "Have you been admitted to TTSH before?":
            p"I was admitted for a couple months due to my knee surgery."
            jump scene_1_3_1_5
        
        "Is it unusual to wait this long?":
            p"Obviously! I don’t think I’ve had to wait this long for anything in my life, ever! They must have made a mistake or something!"
            jump scene_1_3_1_5

    return 

default tried = False

label scene_1_3_1_5:
    call screen narration("You contemplate what is the best course of action next, hopefully this can resolve the situation")

    menu:
        "You decide to further reassure Mdm Ho that the long wait time is normal and there’s really nothing you can do for now.":
            if (trust_level >= 1):
                call screen conflict_win
                jump final_scene1A
            else:
                if tried:
                    jump final_scene1A
                else:
                    call screen conflict_failure
                    jump scene_1_3_1_5

        
        "You decide to talk to the nurse at the reception and inquire about the long wait time":
            call screen conflict_win
            jump final_scene1A

        "You decide to ask the help from another nurse to take over and assist the situation. You observe how the nurse resolves the conflict.":
            call screen narration("You observed how the nurse calmly and patiently explained the congested waiting time for SOC to the patient.")
            call screen narration(" You feel that you learnt something new about resolving conflict with patients. It seems that you will have to do a better job at using the six tools to analyse the patient and the nature of the conflict.")
            call screen narration("Refer to your guidebook next time to better deal with conflicts.")
            jump final_scene1A
    return

label final_scene1A:
    call screen narration("It seems that the situation has been resolved, regardless of the outcome, you return to the spot where you were meeting for Doctor A, Doctor A soon returns and reconvenes with the player")

    return

