#default inq = 0
screen inquiry_advocacy(num):
    use overlay
    modal True
    add "shadow page.png" xalign 0.5 yalign 0.5
    add "chap3/image.png"  xalign 0.5 yalign 0.5
    if(num == 1):
        add "chap3/inquiry.png" xalign 0.5 yalign 0.5
    elif(num == 2):
        add "chap3/advocacy.png" at fade_in xalign 0.5 yalign 0.5
    elif(num == 3):
        add "chap3/balance.png" xalign 0.5 yalign 0.5

    imagebutton:
        idle "images/dialogue/transparent.png"
        xalign 0.5
        yalign 0.5
        xmaximum 5500
        ymaximum 5500
        #action Start()
        action Return(True)

transform fade_in:
    parallel:
        block:
            alpha 0.0
            linear 1.0 alpha 1.0

screen inquiry(text):
    use overlay
    modal True
    add "shadow page.png" xalign 0.5 yalign 0.5
    add "chap3/in_ad.png" xalign 0.5 yalign 0.5
    frame:
        background Null()
        xpos 375
        ypos 445
        xmaximum 
        ymaximum 100
        xminimum 150 
        yminimum 100
        text "{=balance}[text]{=balance}" at text_effect xalign 0.5 yalign 0.5

    imagebutton:
        idle "images/dialogue/transparent.png"
        xalign 0.5
        yalign 0.5
        xmaximum 5500
        ymaximum 5500
        #action Start()
        action Return(True)

transform text_effect:
    parallel:
        block:
            linear 0.5 xoffset -5 yoffset 2 
            linear 0.5 xoffset 5 yoffset -3 
            linear 0.5 xoffset 5 yoffset -2
            linear 0.5 xoffset -5 yoffset 3
            linear 0.5 xoffset 0 yoffset 0
            repeat
    parallel:
        block:
            alpha .8
            linear 1.0 alpha 1.0
            linear 1.0 alpha 1.0
            repeat

style balance is text:
    size 60
    color '#FFFFFF' # without hash
    #font 'Kollektif.ttf'
    outlines [(40, "#000000", 1, 1)]

