label scene_1_5:
    call screen narration("You reconvene with Doctor A after your talk with Jia and Cheng")
    #trust level integration TBD
    d "I hope Jia and Cheng have been nice to you. They like giving challenges to new hires. Speaking of which, are you interested in learning about their shape too?"

    jump final_scene1C
    #menu:
     #   "A. Yes, definitely! ":

label final_scene1C:
    call screen narration("chapter 1 scene 3 not finished")

    scene black
    with Pause(1)

    jump start_chapter2
