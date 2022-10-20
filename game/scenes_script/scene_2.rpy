label scene_1_4: #chapter1_scene2_part1
    voice "audio/footstep.mp3"
    scene bg main_background
    show doctor_icon at right #import character doctor A
    with dissolve

    call screen narration("After sometime, Doctor A returns from his call")
    $ npc_shape = "Null"
    menu:
        "Yes, let's resume our tour.":
            jump scene_1_4_2
        "Do you know anything about that patient over there? I was just talking with her about her queue for SOC.":
            jump scene_1_4_3
            

label scene_1_4_3:
    $tutorial = False
    d "Ah, that is Madam Merry Ho. She has been visiting quite frequently lately due to her recent knee replacement surgery."

    d "I hope she hasn’t given you too much trouble, she is a bit hard of hearing and could come off quite loud and rude sometimes."
    d "Speaking of which, here’s a pop quiz for you, did you manage to parse what her shape is?"
    menu:
        "A.Uh What’s a shape?":
            d "Oh, I’m guessing the six tools are still a bit of a foreign concept to you."
            d "Well, just a heads start, but these are the tools we use to engage with problems in our line of work. Maybe I’ll run you through about shape just briefly today."
            d "But don’t worry, you'll get plenty of opportunities to practise these concepts as you start working."
            $ label_shape = True
            call screen tutorial_shapeReview(0)
        "B. A triangle?":
            d "Close, but not quite. Madam Ho would most likely fall under the square category."
            call screen tutorial_shapeReview(1)
            #call screen guidebook
        "C. A square! I’m sure of it!":
            d "Right on the money! I’d say she’s a square too."
            #call screen guidebook
            call screen tutorial_shapeReview(2)
        "D. Circle, maybe?":
            d "A little off. Madam Ho would most likely fall under the square category."
            call screen tutorial_shapeReview(3)
            #call screen guidebook
            d "But good try nonetheless."
        "E. She definitely gave off squiggle vibes.":
            d "A bit of a stretch. Madam Ho would most likely fall under the square category. "
            #call screen guidebook
            call screen tutorial_shapeReview(4)
            $ label_shape = False
            d "But good try nonetheless."
                ###########scene to be improved##############
    d "Now then, let’s pick up where we stopped with the tour."
    jump scene_1_4_2

define j = Character('Jia', image = "images/nurse_2" ,color="#cc0000", what_outlines=[(5, "#000000", 0, 0)])
define c = Character('Cheng',image= "images/nurse_icon", color="#e6e9fa", what_outlines=[(5, "#000000", 0, 0)])

label scene_1_4_2: #progress scene
    image j = "images/nurse_2.png"
    image j say = "images/nurse_2 2.png"
    image j happy = "images/nurse_2 3.png"
    image c = "images/nurse_icon 2.png"
    image c say= "images/nurse_icon 3.png"
    image c change= "images/nurse_icon 1.png"
    image d = "images/doctor_icon.png"

    show screen show_npc_status

    call screen narration("Doctor A and you continued the tour for a while before stopping by the staff pantry. He wanted you to meet some of your colleagues before concluding the tour.")
    scene bg staff_pantry
    show doctor_icon reverse at left
    d "Meet Jia and Cheng, they are the 2 colleagues that you will be working closely with! "
    show j at center
    with dissolve
    $ npc_shape = "Circle"#################not show? to be revealed 
    d "Jia is full of fun and love, and patients love to talk about their days with her."
    show c at right
    with dissolve
    $ npc_shape = "Triangle"#################
    d "Cheng has great attention to detail and is a hard worker who is willing to go the extra mile for his patients."
    d " They sure make a great team, but the job of a nurse is often challenging."
    $ npc_shape = "Circle"
    show j say
    j "Yes! While being working partners with Cheng is always fulfilling, we sometimes have disagreements due to differences in our personalities."
    show j at center
    $ npc_shape = "Triangle"
    show c say
    c "Let me share a scenario we recently experienced, let’s see how you will solve this conflict!"
    show c change
    c " Jia and I usually work 6 days a week and have Sundays off,"
    show c at right
    c "but due to the spike in Covid cases, we have been working overtime at 7 days a week for a month to manage the influx of patients."
    show c say
    c"In the week when we were finally given our Sunday off, we were called back in to help as some of our colleagues contracted Covid, causing us to be short-staffed. "
    c "How would you react?"
    show c at right

    menu:
        "A:  I will help out because i cannot leave my patients in the lurk":
            # [Trust level +1 with circle]
            $ npc_shape = "Circle"
            show j happy
            j"This was my first reaction too! After all, our patients are dependent on our care to get better."
        "B: Let the team know that we cannot accommodate the extra shift as we have been overworked for 1 month already.":
            #[Trust level +1 with triangle] 
            # this is a operational decision → both should be positive/ negative to be fair in the judgement 
            $ npc_shape = "Triangle"
            c @ 1"Precisely, nurses are humans too and we also need time to rest and recuperate…"
        "C:  Let the team know that we cannot accommodate the extra shift and that we also plan to take Monday off to restore our physical and mental well-being":
            #circle_trustlevel -1 && triangle -1
            $ npc_shape = "Circle"
            show j say 
            j "Hmm, I’m not sure if that will sit well with the team."
            $ npc_shape = "Triangle"
            c @ 1"The team is going to be so overworked and this will lower their productivity in the long run!"
        "D: Delegate work between both people, agreeing to take half day shifts so the other can still take a half day break.":
            #circle+1 triangle+1
            $ npc_shape = "Circle"
            show j happy
            j @ 2"Spot on, this was how we resolved our situation!"
            $ npc_shape = "Triangle"
            show c say
            c @ 1"It was the best of both worlds, we still came back refreshed the next day."
    hide j 
    hide c
    show doctor_icon ahead at right
    call screen conflict_win
    hide screen show_npc_status
    $ npc_shape = "Null"
    m " Insightful! I’ve taken note on how to reach compromises if future conflicts occur."
   # jump final_scene1B
    show doctor_icon
    d " We need to ensure balance between personal and professional needs, do reconsider your course of action in the future for maximum benefit."
    jump final_scene1B

label final_scene1B:
    $ trust_level = 0
    
    scene black
    with Pause(1)

    jump scene_1_5