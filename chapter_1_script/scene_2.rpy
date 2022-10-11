label scene_2_2_1: #chapter1_scene2_part1
    voice "audio/footstep.mp3"
    scene bg main_background
    show doctor_icon at right #import character doctor A
    with dissolve

    call screen narration("After sometime, Doctor A returns from his call")
    menu:
        "Yes, let's resume our tour."
        jump scene_2_2_2
        "Do you know anything about that patient over there? I was just talking with her about her queue for SOC."
        d "Ah, that is Madam Merry Ho. She has been visiting quite frequently lately due to her recent knee replacement surgery."
        d "I hope she hasn’t given you too much trouble, she is a bit hard of hearing and could come off quite loud and rude sometimes."
        d "Speaking of which, here’s a pop quiz for you, did you manage to parse what her shape is?"
        m "Uh What’s a shape?"
        d "Oh, I’m guessing the six tools are still a bit of a foreign concept to you."
        d "Well, just a heads start, but these are the tools we use to engage with problems in our line of work. Maybe I’ll run you through about shape just briefly today."
        d "But don’t worry, you'll get plenty of opportunities to practise these concepts as you start working."
        


label scene_2_2_2: #progress scene




