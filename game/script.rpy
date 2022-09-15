define d = Character('doctor A', color="#c8ffc8")
define m = Character('me', color="#c8c8ff")

label start: #scene_1_1 (chapter1_scene1)

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

#story continues in other scenes now
    return


label scene_1_1_1: #scene 1, branch 1

    show doctor_icon at right #import character doctor A
    with dissolve 

    d "The pleasure is all mine!"
    d "I’ve heard great things about you, but just a heads-up, this job can be quite demanding, I hope you’ll keep up your spirit! Now then, do you want to start the tour? "

    menu:
        "Good to meet you too, A, looking forward to working with you!":
            jump scene_1_2 #straightly to scene_1_2

        "Great, let’s get started then!":
            jump scene_1_1_3 #to the third branch

    return 

label scene_1_1_2:

    scene bg main_background
    with dissolve
    show doctor_icon at right
    with dissolve

    d " I like your spirit, getting right to the point! Then let’s get started."
    jump scene_1_2 # go to scene2
    
    return 

label scene_1_1_3:

    scene bg main_background
    with dissolve
    show doctor_icon at right
    with dissolve

    d "You’re an eager one, aren’t you!"
    d " There’s no rush, we have plenty of time for Q&A as we tour, but I don’t mind giving any clarifications now."
    "(Specific Content TBD, placeholder for now)"

    jump scene_1_2 #finish scene_1_1, jump to scene_1_2 (chapter1, scene2)
    return

label scene_1_2:

############# the following is to indicate "has entered scene_1_2"
    scene bg main_background
    with dissolve
    show doctor_icon at truecenter
    with dissolve

    "scene_1_2"
############# start real code bellow

    return



