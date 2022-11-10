label start_chapter2:
    #show screen show_npc_status
    #$ npc_shape = "Null"
    show screen guidebook_icon()
    image chapter2_bganimation:
        "chapter2_bg"
        alpha 0.0 truecenter zoom 0.5
        linear 2.0 alpha 1.0 zoom 1.0
        repeat
    
    image chapter2_bganimation_run:
        "chapter2_bg"
        alpha 0.0 truecenter zoom 0.5
        linear 0.5 alpha 1.0 zoom 1.0
        repeat
        

    call screen opening_screen("Chapter 2: Ladder of Inference")
    call screen narration("It’s been a week since your first introduction to Tan Tock Seng Hospital. You are still in the process of settling in but you feel very welcome by all your colleagues.")
    call screen narration("You were assigned to work closely with Doctor A, and another day at the hospital begins.")
    show chapter2_bg 
    show chapter2_bganimation
    show patient rush:
        zoom 1.5
        alpha 1.0
        xpos 800 ypos 200
        linear 0.5 alpha 0.0 xpos 1000
        zoom 0.5
        alpha 1.0
        xpos 800 ypos 400
        linear 0.5 alpha 0.0 xpos 1000
        repeat

    call screen narration("It’s a brand new day at the hospital, you enter the hospital grounds with a pep in your step, eager to learn about the tasks that await you.")
    call screen narration("However, someone caught your eye as you walked past the cafeteria.")
    hide chapter2_bganimation
    show cafeteria background:
        alpha 0.0 truecenter zoom 0.5
        linear 2.0 alpha 1.0 zoom 1.0
    centered " "
    call screen narration("You see your colleague, Cheng, dozing off in his seat. He seems to be in deep sleep and does not look like he will be waking up anytime soon.")
    show zzz:
        xpos 520
        ypos 300
        zoom 1.0
        easeout 1.0 zoom 1.1
        easein 1.0 zoom 1.0
        repeat
    centered " "
    call screen narration("A flurry of thoughts ran through your head. Doctor A spoke so highly of him yesterday, mentioning that he was a hard worker that would go the extra mile for his patients.")
    call screen narration("It was puzzling how those compliments do not align with the behaviour you are seeing.")

    centered ""
    call screen narration("Knowing that today was a jam-packed day, you contemplated on what to do since Cheng was needed at the wards today, and certainly cannot be snoozing on the job.")
    call screen narration("What would you do?")

    menu:
        "Let the Nursing Manager know about the situation first thing when you meet him.":
            jump chapter2_1
        "Call Jia immediately and let her know that you saw Cheng sleeping the cafeteria.":
            jump chapter2_2
    
    return

label chapter2_1:
    hide cafeteria background
    hide zzz
    show chapter2_bganimation_run
    call screen narration("You rushed up to the wards and look for the Nursing Manager. Upon meeting her, you immediately relate what you saw at the cafeteria.")
    hide sleeping nurse
    hide zzz
    show chapter2_bg 
    show chapter2_bganimation_run
    centered ""
    hide chapter2_bg
    hide chapter2_bganimation_run
    show ward background
    show nurse icon:
        xpos 730 ypos 250
    pause 0.5
    hide nurse icon
    show nurse_icon ahead:
        xpos 730 ypos 250
    with Dissolve(10.0)
    show exclamation icon:
        zoom 0.5 xpos 1150 ypos 150
    centered ""

    m "I just saw Cheng dozing off at the cafeteria, it’s such a busy day, how can he afford to be sleeping when the hospital is overflowing with patients?"
    hide nurse_icon ahead
    hide exclamation ixon
    show nurse_icon ahead:
        xpos 780 ypos 250
        zoom 0.5
        parallel:
            easein 0.2 ypos 250
            easeout 0.2 ypos 350
            easein 0.2 ypos 250
            easeout 0.2 ypos 350
            easein 0.2 ypos 250
        parallel:
            linear 1.0 zoom 2.0
        
        linear 1.0 xpos 500 ypos 0
    d "Woah there, making such harsh comments do not align with the understanding culture we practise. Do you realise that you just made a huge assumption and an unsympathetic accusation that could cause Cheng to get a huge scolding?"
    hide nurse_icon ahead
    show nurse_icon angry:
        xpos 500 ypos 0 zoom 2.0
    d "Cheng just worked an overnight shift and that was his first break in 24 hours! In the future, do consider clarifying with others on the situation before making such bold assertions to prevent conflicts and miscommunications."
    hide nurse_icon angry 
    hide ward background with fade(10)
    
    jump end_chapter2
    
    return

label chapter2_2:
    play audio "audio/phone.mp3"
    call screen narration("You whip out your phone and dial for Jia in a panic, hoping she can meet you as soon as possible to bring Cheng back up to the wards to continue his duty.")
    m "Hello Jia, I just saw Cheng sleeping in the cafeteria. Can you meet me here as soon as you can so we can bring him back up to the wards to attend to his patients?"
    m "I can’t believe Cheng would be sleeping during office hours, it is totally unbecoming for the image of the hospital!"

    j "Slow down! I have known Cheng for a long time, I know he is not one to skive. It is not advisable to be making such assumptions before finding out the truth of the situation, you will land yourself into many conflicts in the future for jumping to conclusions!"
    j "This is probably his first break since working the overnight shift covering for me since I was feeling unwell and could not stay to continue tending to my patients."
    j "He will be taking a longer break in the morning to rest and recuperate while I fill in for him, I’m sure he will head to the wards once he is recharged!"

    jump end_chapter2

    return

label end_chapter2:
    hide patient rush
    show visual_1
    centered ""
    hide visual_1
    # $ renpy.music.set_volume(0.00, delay=0, channel='music')
    # $ renpy.movie_cutscene ("video/Ladder_of_Inference.webm")
    # $ renpy.music.set_volume(1.00, delay=0, channel='music')
    call screen narration("You just narrowly escaped a conflict!")
    call screen narration("This happened because you jumped up the ladder of inference from your observations to assumptions and conclusions, but you have missed a few rungs like attaching meaning to your observation that would have prevented you from making the wrong conclusion.")
    call screen narration("To prevent yourself from forming misleading assumptions and conclusions, keep in mind that you have to step up the ladder rungs one by one.")

    jump start_chapter2_2
    return

screen tutorial_Inference(text):
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
            text "[text]"
            text ""
            textbutton "Ok":
                action [Return(True), Hide("guidebook_icon")]    
    
    use guidebook_icon
    
    frame:
        background Null()
        xpos 210
        ypos 30
        imagebutton at redbutton:
            idle "images/dialogue/arrow red.png"       

screen ladder(text):
    use overlay
    modal True
    frame:
        background Null()
        xalign 0.5
        yalign 0.5
        xmaximum 1300
        ymaximum 500
        add "images/ladder.png" ypos -300 xpos -150
        #add "images/rectangle icon.png" ypos -300 xpos -150
        transclude

    frame:
        xmaximum 700
        ymaximum 200
        xminimum 700 
        yminimum 200
        xpos 1150 ypos 700
        frame:
            background Null()
            xalign 0.5
            yalign 0.5
            xmaximum 600
            ymaximum 100
            xminimum 600 
            yminimum 100
            text "[text]" xalign 0.5 yalign 0.5

    imagebutton:
        idle "images/dialogue/transparent.png"
        xalign 0.5
        yalign 0.5
        xmaximum 5500
        ymaximum 5500
        #action Start()
        action Return(True)


transform fadeout:
    alpha 1.0
    linear 1.0 alpha 0.0

transform fadein:
    alpha 0.0
    linear 1.0 alpha 1.0

screen ladder1(text):
    use ladder(text):
        imagebutton at fadein:
            idle "images/rectangle icon.png" ypos -300 xpos -150 

screen ladder2(text):
    use ladder(text):
        imagebutton at fadeout:
            idle "images/rectangle icon.png" ypos -300 xpos -150 
        imagebutton at fadein:
            idle "images/rectangle icon.png" ypos -400 xpos -150

screen ladder3(text):
    use ladder(text):
            imagebutton at fadeout:
                idle "images/rectangle icon.png" ypos -400 xpos -150
            imagebutton at fadein:
                idle "images/rectangle icon.png" ypos -505 xpos -150

screen ladder4(text):
    use ladder(text):
            imagebutton at fadeout:
                idle "images/rectangle icon.png" ypos -505 xpos -150
            imagebutton at fadein:
                idle "images/rectangle icon.png" ypos -605 xpos -150

screen ladder5(text):
    use ladder(text):
            imagebutton at fadeout:
                idle "images/rectangle icon.png" ypos -605 xpos -150
            imagebutton at fadein:
                idle "images/rectangle icon.png" ypos -705 xpos -150

screen ladder6(text):
    use ladder(text):
            imagebutton at fadeout:
                idle "images/rectangle icon.png" ypos -705 xpos -150
            imagebutton at fadein:
                idle "images/rectangle icon.png" ypos -805 xpos -150

screen ladder7(text):
    use ladder(text):
            imagebutton at fadeout:
                idle "images/rectangle icon.png" ypos -805 xpos -150
            imagebutton at fadein:
                idle "images/rectangle icon.png" ypos -905 xpos -150

label start_chapter2_2:
    show doctor_room_background:
        alpha 0.0 truecenter zoom 0.5
        linear 2.0 alpha 1.0 zoom 1.0
        
    call screen narration("After the hectic morning, it is time to start work. Your first task today is to attend to a patient under Doctor A’s supervision. As you enter the room, you see a teenager with her mother.")
    show teen mom icon toscale
    show sick teen
    centered ""
    $ label_ladder = True
    hide screen guidebook_icon
    call screen tutorial_Inference("You will work on using the ladder of inference as learnt earlier. Refer to the guidebook to refresh your memory on the different rungs and remember to move up the ladder rungs one by one to prevent misunderstandings!")
    show screen guidebook_icon
    show doctor_icon reverse at left
    d "Good morning! I am Doctor A and with me is [persistent.user_name]. She will be attending to you today under my supervision."
    m "Hello, what seems to be the problem today?"
    hide teen mom icon toscale
    show teen mom icon:
        xpos 1000 ypos 130
        parallel:
            easein 0.1 ypos -50
            easeout 0.1 ypos -0
            easein 0.1 ypos -50
            easeout 0.1 ypos 0
            easein 0.1 ypos -50
        parallel:
            easein 0.5 zoom 2.5

    mo "My daughter has been suffering with pneumonia for the past week and does not seem to be getting better."
    call screen ladder1("The patient's information has brought us to the first ladder of inference")
    dau "I think I know why I have not been able to recover, it’s because I have not been taking my medication."
    call screen ladder2("Patient provides information to allow for better interpretation of her situation ")
    
    call screen narration("How will you respond to the patient?")
    jump chapter2_2choice
    
    return

label chapter2_2choice:
    hide fail2
    menu:
        "Why haven’t you been taking your medications? If you do not follow the doctor’s instructions, you definitely won't be able to recover!":
            call screen narration("As you were about to go off on the patient, Doctor A sensed what you were going to say and tapped on your shoulder")
            hide teen mom icon
            show doctor_icon ahead at center
            d "Hey, I understand it sounds bad, [persistent.user_name], but perhaps we should listen to their reasoning first. It is important to remind them to follow instructions, but let’s try not to overdo it."
            centered ""
            show fail1
            pause 2
            hide fail1
            show fail2
            pause 2
            centered ""
            jump chapter2_2choice
        "I’m sorry you have not been feeling great. It’s difficult to recover from pneumonia without taking regular medication!":
            jump chapter2_22
            



label chapter2_22:
    show doctor_icon reverse at left
    show teen mom icon:
        xpos 1000 ypos 0
        zoom 2.5
    call screen ladder3("Good Job! You are actively trying to interpret the meaning of data provided.")
    dau "Yes, I understand. I have been trying but it’s been so difficult!"
    call screen narration("How will you respond to the patient?")
    jump chapter2_22choice
    return

label chapter2_22choice:
    hide fail1
    hide fail3
    menu:
        "It’s hard for us to assess your condition if you do not take your medication. Perhaps you can set reminders on your phone to make sure you don’t forget to take them!":
            d "Sorry about it, my colleague is simply very concerned about your condition,"
            show doctor_icon at center
            hide teen mom icon
            d "I believe what they meant to say is…"
            centered ""
            show fail1
            pause 2
            show fail3
            pause 2
            jump chapter2_22choice
        "Is there a reason why you have not been taking the medications?":
            jump chapter2_222
        "Do you have adverse reactions to the medication that is preventing you from taking it?":
            jump chapter2_222

label chapter2_222:
    show doctor_icon reverse at left
    show teen mom icon:
        xpos 1000 ypos 0
        zoom 2.5
    call screen ladder4("You have learned to use INQUIRY, and don't jump to conclusions!")
    dau "I don’t have allergies to the medication, but my phobia of swallowing pills has been giving me a hard time."
    dau "I’ve tried cutting the pills into smaller pieces, swallowing them with smooth foods and many other methods, but I always end up choking and spitting the pill out!"
    call screen narration("How will you respond to the patient?")
    jump chapter2_222choice
    return

label chapter2_222choice:
    hide fail1
    hide fail4
    menu:
        "Teenagers should already be able to swallow pills, as you grow older there are not many medications in liquid form that have the effective dosage to cure illnesses.":
            call screen narration("Having gone through a few rounds of inquiry already, you stopped yourself before saying this.")
            call screen narration("Is this truly the right thing to say under these circumstances… You decide to reconsider")
            show fail1
            pause 2
            show fail4
            pause 2
            jump chapter2_222choice
        "I totally understand where you are coming from. Don’t worry, this is a common problem amongst many patients.":
            jump chapter2_2221
    return

label chapter2_2221:
    call screen ladder5("You are able to reach an effective conclusion that appeases the patient's fear!")
    dau "Thank you for the reassurance, but how can I recover if I am unable to take the medications?"
    call screen narration("How will you respond to the patient?")

    jump chapter2_2221choice

    return

label chapter2_2221choice:
    hide fail1
    hide fail5
    menu:
        "You should overcome your fear and try again until you do it successfully, some pills do not have alternative forms so there is really no choice.":
            show fail1
            pause 2
            show fail5
            pause 2
            jump chapter2_2221choice
        "One effective method is using a bottle with a narrow opening, and the pressure of the bottle’s narrow opening will ease the pill down your throat.":
            jump chapter2_22221

label chapter2_22221:
    m "Learning how to swallow pills is important especially since not all medications have liquid forms."
    m "One effective method is using a bottle with a narrow opening, and the pressure of the bottle’s narrow opening will ease the pill down your throat, you won’t feel a thing!"
    call screen ladder6("You have adjusted your beliefs, understanding that this is a problem patients face and has provided good advice")
    dau "I will try that, thanks for the suggestion! In the meantime, what can I do to recover?"
    call screen narration("How will you respond to the patient?")
    jump chapter2_22221choice
    return

label chapter2_22221choice:
    hide fail6
    menu:
        "There is no room for alternatives, you should search some methods online on how to swallow pills. It’s the only way you can get better.":
            centered ""
            show fail6
            pause 2
            jump chapter2_22221choice
        "Let me consult the pharmacist and see if there are liquid alternatives for you. ":
            jump chapter2_222221
        
    return

label chapter2_222221:
    call screen ladder7("You have taken a positive action based on your beliefs.")
    hide teen mom icon
    
    show teen mom icon:
        xpos 1000 ypos 0
        parallel:
            easein 0.1 ypos -50
            easeout 0.1 ypos -0
            easein 0.1 ypos -50
            easeout 0.1 ypos 0
            easein 0.1 ypos -50
        parallel:
            easein 0.5 zoom 2.5
        linear 0.5 xpos -1000 ypos 0
    hide sick teen
    mo "Thank you both, I’m sure my daughter will be able to recover with your help today!"
    show doctor_icon at center
    d "Good job on handling the consultation session, I can see that you have applied the ladder of inference accurately which prevented the patient from feeling anxious about her phobia."
    d "You definitely helped to ease the patient’s concerns and provided positive follow up action. Stellar first interaction with a patient!"
    
    p "Thanks Doc, I now understand the importance of using the ladder of inference which allows me to comprehend the whole situation before making decisions to prevent misunderstandings."
    p "I will definitely use this tool to prevent conflicts in the future!"

    jump final_chap2
    return

label final_chap2:
    scene black
    with Pause(1)

    #choose chapter
    call screen chapter_selection
    if(chap_num == 1):
        jump scene_1_3
    elif (chap_num == 2):
        jump start_chapter2
    elif(chap_num == 3):
        call screen start_chapter3
        jump final_chap2
    elif(chap_num == 0):
        jump end
    
    return