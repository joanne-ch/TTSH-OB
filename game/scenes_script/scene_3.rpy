define sarah = Character('sarah', color="#c8c8ff", what_outlines=[(5, "#000000", 0, 0)])

label scene_1_5:
    
    show bg nursing hallway
    call screen narration("You reconvene with Doctor A after your talk with Jia and Cheng")
    #trust level integration TBD
    show doctor_icon at  right
    d "I hope Jia and Cheng have been nice to you. They like giving challenges to new hires. Speaking of which, are you interested in learning more about their shape too?"
  #  call screen guidebook_icon
    $tutorial = False
    menu:
        "A. Yes, definitely! ":
            call screen tutorial_shapeReview(5)
        "B. No need, I have deduced it myself!":
            d "Awesome, it seems like you’re getting a good grasp of shape tools."
            d "If you have managed to deduce their shapes, maybe you have some idea of the last colleague I’m introducing you to! Let’s get going"
    jump scene_1_5_2

label scene_1_5_2: #progresses scene
    #show screen show_npc_status
    #$ npc_shape = "Squiggle"
    image sarah = "images/sarah.png"
    voice "audio/footstep.mp3"
    call screen narration("You and Doctor A go into an office. You see a woman dressed in a nurse outfit working in front of the desk. She seems quite enthusiastic despite the amount of work that had piled in front of her")
    show doctor_icon at right 
    show sarah work at left 
    with dissolve
    d "Meet Sarah, the nurse manager of this floor, and your boss in a sense!"
    show sarah work at left 
    with dissolve
    call screen narration("Sarah, still seemingly enticed by her own work, acknowledges both of your visit with an exaggerated hand gesture, before addressing you directly")
    
    sarah "Newbie, what’s up? "
    show sarah hi
    sarah "Here’s a question for you, what’s your view on how the hospital is being runned right now, you think we can do better than now?"
    #hide doctor_icon
    jump scene_1_5_3

label scene_1_5_3:
    menu:
        "A. Uhhh… I’m not really sure":
            sarah "Hmm, undeciding huh, we gotta work that out for you."
            sarah"Sometimes you have to go with your guts and just shoot your shot, you know? C’mon, giving you one more chance now."
            jump scene_1_5_3
        "B. Definitely, we can always do better.":
            sarah "Not bad, there are definitely flaws in the hospital system still."
            sarah"There are systematic as well as individual things we can do to better everyone’s experience. Follow your guts sometimes, and you may find your solutions bringing actual changes to the system."
        "C. No, I think what we are doing now is just fine ":
            sarah "A status quo lover huh. Nothing wrong with that. But remember this, innovation is required even to maintain an optimal solution"
            sarah"if you ever have the intuition, try following it once in a while, you may be surprised by the result."
    jump scene_1_5_4

label scene_1_5_4:
    sarah "Now this could be a lot more entertaining than paperwork. Good to have you onboard."

    call screen narration("You, Doctor A and Sarah had a pleasant chat together discussing your past experience, the hospital and many more. You reflect on the day and feel that you’ve learnt a lot more about TTSH and the situations that you’ll come across at your job. The day passes quickly…")
    hide sarah
    with fade
    show bg main_background
    hide screen show_npc_status
    #$ npc_shape = "Null"
    show doctor_icon at center
    d "I hope today’s tour has been insightful. By the way, wanna take a gander at Sarah’s shape?"
    menu:
        "A. Process of elimination, I’d say Squiggle!":
            d "right!"
        "B. C’mon doc, this should be educational! Give me the answer already!":
            d "okay!"
    call screen tutorial_shapeReview(4)
    call screen narration("You feel that you are more in tune with TTSH culture and lifestyle after the tour. You depart from the hospital and look forward to the next day, when your official work will begin.")

    jump final_scene1C


label final_scene1C:
    #call screen narration("chapter 1 scene 3 not finished")
    
    
    scene black
    with Pause(1)

    jump start_chapter2
