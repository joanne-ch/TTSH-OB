
######################import scene 1 character, "doctor A" and "me"
define d = Character('doctor A', color="#c8ffc8")
define m = Character('me', color="#c8c8ff")

##################start scene_1_1 (chapter1_scene1)
label start: 

    scene bg main_background #import background
    with fade
    show doctor_icon at right #import character doctor A
    with dissolve

    d "Good Morning! So good to finally meet you in person Kamala. We are very excited to have you on board of TTSH. My name is Doctor A. "

    d " I believe HR has briefed you that you’d be working with me for the first few months of your appointment."

    d "Today, I will just be showing you around the hospital and our office. Do feel free to ask me any questions."

    #make choice 
    menu:
        "Good to meet you too, A, looking forward to working with you!":
            jump scene_1_1_1  #go to chapter1_scene1_branch1

        "Great, let’s get started then!":
            jump scene_1_1_2 #go to chapter1_scene1_branch2

        "Before we start the tour, I do have some questions…":
            jump scene_1_1_3 #go to chapter1_scene1_branch3

        "(Specific Content TBD, placeholder for now)":
            jump scene_1_1_4 # go to chapter1_scene1_branch4

    return 


label scene_1_1_1: #scene 1, branch 1

    show doctor_icon at right #import character doctor A
    with dissolve 

    d "The pleasure is all mine!"
    d "I’ve heard great things about you, but just a heads-up, this job can be quite demanding, I hope you’ll keep up your spirit! Now then, do you want to start the tour? "

    menu:
        "Yes, let’s get started then!":
            jump scene_1_2 #straightly to scene_1_2

        "I do have some questions...":
            jump scene_1_1_3 # go to the third branch

    return 

label scene_1_1_2:

    show doctor_icon at right
    with dissolve

    d " I like your spirit, getting right to the point! Then let’s get started."
    jump scene_1_2 # go to scene2
    
    return 

label scene_1_1_3:

    show doctor_icon at right
    with dissolve

    d "You’re an eager one, aren’t you!"
    d " There’s no rush, we have plenty of time for Q&A as we tour, but I don’t mind giving any clarifications now."

    jump scene_1_2 #finish scene_1_1, jump to scene_1_2 (chapter1, scene2)
    return

label scene_1_1_4:

    show doctor_icon at right
    with dissolve

    d "(TBD)"
    m "jump tob scene 2"

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
    d "On the first floor, we have..." #scene shows image of area
    d "On the second floor we have..." #scene shows image of area
    d "On the third floor we have..." #scene shows image of area
    d "This is our main office and where you can work and rest off-hours" #scene shows image of area
    d "Here is the nurse ward..." #scene shows image of area
    d "This is where you will be working most of the day, tending to patients assigned to you."
    d "Do you have any questions so far?"
    return
    #make choice 
label scene_1_2_1
    show doctor_icon at truecenter
    with dissolve
    menu:
        "No, I have no questions at the moment":
            jump scene_1_2_2  #go to chapter1_scene1_branch1

        "Actually I do have some questions":
            jump scene_1_2_3 #go to chapter1_scene1_branch2

    return

label scene_1_2_2:

    show doctor_icon at right
    with dissolve

    d "Great, well, I think we are almost done with the tour, now we just..."

    jump scene_1_3 
    return

label scene_1_2_3:

    show doctor_icon at right
    with dissolve

    menu:
        "Can you run me through the first floor again..."
            jump scene_1_2_4
        "Can you run me through the second floor again..."
            jump scene_1_2_4
        "Can you run me through the third floor again..."
            jump scene_1_2_4
        "Can you run me through the main office area again..."
            jump scene_1_2_4
        "Can you run me through the nursing ward again..."
            jump scene_1_2_4

     return

label scene_1_2_4:

    show doctor_icon at right
    with dissolve

    d "Alright, I hope that clarifies everything, now do you have any more questions?"
    Jump scene_1_2_2

    return

label scene_1_3:

############# the following is to indicate "has entered scene_1_3"
    scene bg main_background
    with dissolve
    show doctor_icon at truecenter
    with dissolve

    "scene_1_3"
    

