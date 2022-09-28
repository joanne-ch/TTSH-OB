default trust_level = 0

screen show_trust():
    frame:
        vbox:
            text "[trust_level]"
            textbutton "Okay":
                action Return(True)
