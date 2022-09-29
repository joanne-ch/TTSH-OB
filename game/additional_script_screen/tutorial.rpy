screen tutorial():
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
            text "While playing this game, you will often be {color=#f4b157}making choices {/color}that may {color=#f4b157}change the trajectory of your story {/color}and the challenges you will have to overcome.Don’t worry about missing out, after finishing each chapter, you will be able to {color=#f4b157}replay and choose the different choices {/color} .With that said, we encourage you to fully experience the game at least once before replaying any sequence"
            text ""
            textbutton "Ok":
                action Return(True)