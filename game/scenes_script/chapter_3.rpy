label start_chapter3:
    call screen opening_screen("Chapter 3: Inquiry & Advocacy")
    voice "audio/office_bgm.mp3"
    call screen narration("It’s another day at Tan Tock Seng Hospital and you reported early to Doctor Siti to reconvene to discuss your task of the day. It seems that Sarah, the nurse manager has requested you both to attend to a matter that will require some pair work.")
    call screen narration("You and Doctor Siti were called to Sarah’s office for a debrief on a task.")
    show bg office
    show doctor_icon at right
    show sarah 1 at left
    sarah  "Morning folks, I have an urgent task that needs you both to attend to. We are updating the information system for one of our wards as an experiment for upping the efficiency of patient information management. "
    show sarah 2
    image digi = "chap3/digitalise.png"
    show digi:
        xpos 440
        ypos 10
        easeout 1.0 rotate 4.0 
        easein 1.0 rotate 0.0
        repeat
    sarah "We are moving from paper inventory to fully digital, that means you will need to download a tracking dashboard from the hospital server and begin filling in the existing inventory while double checking if there has been any discrepancy with the actual ward arrangement right now. "
    sarah "Additionally, it’d be good if you can come up with any additional entries you want to add into the database, be it from asking the patients or coming up by yourself. Kopi on me if you guys do a good job out there!"
    show sarah 1
    sarah "So, any question?"
    hide digi
    jump chap3_1

label chap3_1:
    show screen guidebook_icon()
    $ label_inquiry = True
    #show sarah 2
    show doctor_icon ahead
    m "(You are pondering a bit and contemplate what to say)"
    $ tutorial = False
    menu:
        "A. I don’t really have any questions.":
            call screen narration("(Before you can say this, Siti leaned towards you)")
            show doctor_icon whisper at right
            d "(Whispers) That is a lot of information to take in, before you say anything, are you sure you understand all the tasks she has listed? I suppose this is a good time for some {b}inquiry{b}."
            #call screen inquiry("Inquiry")
          #  image clarity= "chap3/clarity.png"
           # show clarity:
            #    xalign 0.5 
             #   yalign 0.5
      #      show clarity_txt:
       #         "chap3/Seeking Clarity.png"
        #        xpos 434
         #       ypos 482
          #      easeout 1.0 zoom 1.1
           #     easein 1.0 zoom 1.0

            #call screen narration("TODO - codex <inquiry>")
            #todo - codex "inquiry"
            jump chap3_1
        "B. Could you explain what this information system is?":
            show sarah 2
            show idea_2:
                xalign 0.5
                yalign 0.5
                "chap3/idea 2.png"
                easeout 1.0 rotate 4.0
                easein 1.0 rotate 0.0
                repeat
            sarah "Certainly, essentially, the hospital’s health information system aims to digitalise and manage the healthcare data we have,"
            show sarah 1
            sarah "so ranging from logistics inventory to patient record, we want to have a digital record of everything instead of the traditional paper record. It’s easier to record, store and access."
            hide idea_2
            call screen tutorial_text("Nice work, you’ve taken your first step to initiate proper inquiry. There are many aspects to how one makes an inquiry as well as the quality of inquiry they make. What you have done can be categorised as Seeking {b}Clarity{b}")
            #call screen narration("TODO - codex <seeking clarity>")
            #call screen inquiry("Seeking Clarity")
            call screen narration("You decide to ask a bit more questions to gain some clarity of the situation")
            
            jump chap3_1_2

label chap3_1_2:
    show sarah 1
    show doctor_icon ahead
    menu:
        "A. Where can I download this dashboard?":
            show ask:
                xalign 0.5 
                yalign 0.5
                "chap3/ask.png"
                easeout 1.0 rotate 4.0
                easein 1.0 rotate 0.0
                repeat
            show sarah 2
            sarah "Ah, good things you asked, otherwise I would have forgotten. Let me send you the link through messenger."
            sarah " It is operational on mobile devices, so it should be pretty easy to handle."
            hide ask
            call screen tutorial_text("An important part of inquiry is to facilitate discussion, mentioning an important part of the assignment that may have been left out during the discussion will help improve the smooth execution of the assignment.")
            jump chap3_1_2
        "B. Do you have any suggestions on how we can do this?":
            show ask:
                xalign 0.5 
                yalign 0.5
                "chap3/ask.png"
                easeout 1.0 rotate 4.0
                easein 1.0 rotate 0.0
                repeat
            show sarah 2
            sarah "Hmm, while it is up to you two to figure out the details, I will suggest double checking the existing entry first against the details in the patient ward first, to ensure there aren't any mistakes there before transferring the data."
            hide ask
            show sarah 1
            call screen tutorial_text("Good work! It is always important to keep track of the “How” in the assignment, if you have trouble approaching an assignment, don’t be afraid to consult your colleague or expert opinion on how you could approach the issue. Hearing another’s perspective could usually assist your own decision-making.")
            jump chap3_1_2
        "C. (You turn to Doctor Siti) I wonder what kopi we should get… ":
            show angry:
                "chap3/angry.png"
                xalign 0.5
                yalign 0.5
                easeout 0.5 rotate 4.0
                easein 0.5 rotate 0.0
                repeat
            show sarah unhappy at left
            show doctor_icon whisper 
            d "(Whispers) I don’t think that’s a priority for now, but if anything, kopi c with extra sugar."
            hide angry
            call screen narration("You sense Sarah glaring at you, remember not to stray away from the problem at hand, good inquiry means it should be relevant to the task and involving the key stakeholders")
            jump chap3_1_2
        "D. I don’t have any questions for now. ":
            show sarah 2
            sarah "Good, then I’ll leave it to you two to working out the detail."
            hide sarah
            jump chap3_2

label chap3_2:
    call screen inquiry_advocacy(1)
    call screen narration("Having received the assignment, you and Doctor Siti make your way to the ward and get ready to begin. Before starting, Doctor Siti suggest you to review the plan of action with her")
    show bg lab
    hide sarah 2
    hide sarah 1
    show doctor_icon at right
    d "Good work clarifying about the task just now, since you’re new here, there are going to be many things that at first would seem unclear or too complicated. Always remember the rule of inquiry, never be afraid to ask questions."
    show doctor_icon ahead
    d "But before we get started, I also want to hear your take on the assignment. "
    d "You know, {b}inquiry{/b} and {b}advocacy{/b} are the two sides of the same coin, you will often need to state your own idea and make a judgement to convince others."
    show doctor_icon
    d " Let’s have a quick exercise of advocacy. Sell me on how you would conduct this assignment ."
    jump chap3_2_1

label chap3_2_1:
    menu:
        "A. I think we should immediately get started on transferring the data into the dashboard.":
            show idea:
                xalign 0.5
                yalign 0.5
                "chap3/idea.png"
                easeout 1.0 rotate 4.0 
                easein 1.0 rotate 0.0
                repeat
            show doctor_icon ahead
            d "Why do you think this is the best course of action?"
            menu: 
                "a.I think we need to try to finish this task as efficiently as possible, and verifying all the existing data would simply take too much time. If we are careful during our transfer, we should be able to spot any discrepancy":
                    d "I suppose you have a point there, while I do not entirely agree with your decision, I think you raise some valid points. "
                    d " I think we can try this method first and see how it turns out."
                    hide idea
                "b. I think it is too much work to verify everything again, so to save time, we should get right to the task.":
                    d "That just won’t do. I don’t really agree with your thought process here. I think it is worthwhile for you to reconsider your decision."
                    call screen narration("You were unsuccessful in advocating for your case. Refer back to the tools of engagement and think how you may better present your position in a convincing manner")
                    hide idea
                    jump chap3_2_1
        "B. I think we should take our time and verify the existing data first against the ward.":
            show idea_2:
                xalign 0.5
                yalign 0.5
                "chap3/idea 2.png"
                easeout 1.0 rotate 4.0 
                easein 1.0 rotate 0.0
                repeat
            d "Why do you think this is the best course of action?"
            menu:
                "a. I think it is never wrong to be cautious, and ensuring there is no discrepancy now will make things easier for the work proceeding the transfer. It is also what Sarah has recommended us doing, so I trust it would be the best course of action.":
                    d "Well said, I agree with this course of action, and I think you’ve done a good job advocating it too."
                    d " I’m glad you understand your decision well and have the confidence to advocate it to others. Let’s get to work then."
                    hide idea_2
                "b. I am afraid of making any mistakes, if it turns out that one of the entries is wrong, we will definitely be blamed for it, so better safe than sorry.":
                    d "While I agree with the specifics of the plan, I don’t exactly agree with this rationale. I think we should be driven by delivering the best results as opposed to out of fear of making mistakes."
                    d "I hope that you will remember this in your future work. But in any case, let’s proceed with this course of action."
                    hide idea_2
    call screen inquiry_advocacy(2)
    call screen narration("As you and Doctor Siti finish discussing, you set out to conduct the assignment. Following your decision and with the help of Doctor Siti, you were successful in executing the task")
    jump chap3_3

label chap3_3:
    show bg office
    show sarah 1 at left
    show doctor_icon at right
    voice "audio/footstep.mp3"
    call screen narration("You and Siti return to Sarah’s office to report the completion of the assignment")
    sarah "Good work, you two. I hope you all learnt something from this experience, especially you, green horn."
    show sarah 2 at left
    sarah "How about a quick retrospect? Aside from the assignment itself, what did you do to reach its conclusion?"
    jump chap3_3_1

#global tag
#default tag = 0

label chap3_3_1:
    menu:
        "A. Siti taught me to make inquiries… ":
            show sarah 1 
            sarah "And what would that be?"
            menu:
                "a.It’s about seeking clarities and learning about the “how” to problems":
                    show sarah 1
                    sarah "That’s right. Clarity and knowing what to do is some of the most important qualities you need to get things done in our line of work. Did you learn anything else?"
                "b. It’s about asking all sorts of questions":
                    sarah "A bit vague, but I suppose one has to start somewhere, here, have some material you can read up upon about making good inquiries."
                    #call screen tutorial_inquiryReview(2)
    sarah "Did you learn anything else?"
    menu:
        "A. I had to advocate for a solution…":
            show sarah 2
            sarah "Good, how did you manage that?"
            menu:
                "a. I had to justify my position and promote it to others with clarity and confidence.":
                    show sarah 1
                    sarah "Well said, there will come a time that you will be required to state your views, always keep this in mind when you advocate for your positions."
                    sarah "Provide proper justification, and more importantly, explain the ‘how’ in your solution."
                
                "b. It’s about stating my opinion on a problem.":
                    sarah "A little vague, but nothing we can’t work on. You should have a bit more confidence in stating your opinion, but do also keep in mind you’ll need to back it up with proper rationale."
                    sarah "Here, have some material to read on advocating."
                    call screen tutorial_inquiryReview
    call screen narration(" You think you’ve covered the bases of today’s learning and told Sarah so.")
    sarah "Good. I think you will do just fine going forward in our hospital. As I’ve promised, kopi on me tomorrow. I’ll leave you both to do your duties."
    call screen inquiry_advocacy(3)
    jump chap3_4

label chap3_4:
    show bg staff_pantry
    show doctor_icon at right
    hide sarah 
    call screen narration("You and Siti took a breather at the lounge after leaving Sarah’s office")
    d "Good work today, I think you picked up a lot by doing the assignment. Say, what do you think inquiry & advocacy are really used for in our line of work at the end of the day?"
    menu:
        "A. Communication?":
            show doctor_icon laugh
            d "That’s right! Making high quality inquiry and advocacy makes it easier for you to resolve problems and while doing so with people. "
            show doctor_icon ahead
            d " If you ever have to lead a team, you may have to practise both inquiry and advocacy at the same time, if that ever comes, you’ll have to do your best to balance the two while making the most out of each."
            d "But don’t be afraid, you can always refer back to your guidebook for a refresher on the details."
        "B. Problem-solving?":
            show doctor_icon laugh
            d "Clase but not quite. It’s more about effective communication really."
            d "Making high quality inquiry and advocacy makes it easier for you to resolve problems and while doing so with people."
            show doctor_icon ahead
            d " If you ever have to lead a team, you may have to practise both inquiry and advocacy at the same time, if that ever comes, you’ll have to do your best to balance the two while making the most out of each."
            d "But don’t be afraid, you can always refer back to your guidebook for a refresher on the details."
        "C. *sigh* Can we just take a break for a quick sec…":
            show doctor_icon laugh
            d "(Laughs) Sure, sure, I’ll let you off the hook on this one."
            d "But to answer my own question, it’s about facilitating effective communication."
            show doctor_icon ahead
            d " If you ever have to lead a team, you may have to practice both inquiry and advocacy at the same time, if that ever comes, you’ll have to do your best to balance the two while making the most out of each."
            d "But don’t be afraid, you can always refer back to your guidebook for a refresher on the details"
    
    call screen narration("You nod in agreement, taking a sip from your cup and getting ready to get back to the busy yet fruitful hospital life.")
    hide guidebook_icon
    jump final_chap3
    return

label final_chap3:
    scene black
    with Pause(1)

    #choose chapter
    call screen chapter_selection
    if(chap_num == 1):
        jump scene_1_3
    elif (chap_num == 2):
        jump start_chapter2
    elif(chap_num == 3):
        #call screen under_constructionDialog
        jump start_chapter3
    elif(chap_num == 0):
        jump end
    
    return