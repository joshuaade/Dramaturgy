# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.
init python:
    from python import card

define e = Character("Eileen")
image plasticbag = "plasticbag.png"


default tst = 0 # variable for testing

screen stats_screen():
    frame:
        xalign 0.0
        yalign 0.0
        vbox:
            text "Name" 
            bar value audience range 10
            text "Energy: [energy]"
        text "\nAudience"

screen card_display():
    if initialize:
        for display_card in card_list:
            $ tst = 0
            draggroup:
                drag:
                    # possibly somehow turning false after first card since all cards spawn in same area
                    xpos slot
                    ypos 0.5
                    drag_raise True
                    draggable True
                    frame:
                        xalign 0.0
                        yalign 0.0
                        vbox:
                            text "[display_card.type]"
                            text "Energy: [display_card.energy]"
                            text "Audience: [display_card.audience]"
            $ slot += 1/7
        

# The game starts here.

label start:
    default audience = 10
    default energy = 10
    default card_list = []
    default slot = 0
    default initialize = True

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    #scene bg room

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    #show eileen happy

    # These display lines of dialogue.

    play music "ConceptThemeWIP.mp3"

    e "Welcome Director to the game"

    e "You will talk to characters and pick cards"

    e "Card stuff"

    e "Do you want to play cards?"

    menu:
        "Yes":
            jump play_cards
        "No":
            jump no_cards
    return
"""
    e "You've created a new Ren'Py game."

    $ audience -= 1
    #$ energy -= testcard.energy

    e "Once you add a story, pictures, and music, you can release it to the world!"

    $ audience -= 1
    #$ energy -= testcard.energy

    e "Do you ever feel like:"

    $ audience -= 1
    #$ energy -= testcard.energy

    show plasticbag at topleft with dissolve
    show plasticbag at truecenter with dissolve
    show plasticbag at right with dissolve



    menu:
        "Yes":
            jump Choice_1
        "No":
            jump Choice_2

    
    e "End"

    hide plasticbag at right

    # This ends the game.

    return"""



label Choice_1:
    e "Plastic bag"
    e "Plastic bag"
    return

label Choice_2:
    e "EEEEEEEEEEE"
    e "Rewind"
    jump start
    return

label play_cards:
    show plasticbag at top with dissolve
    $ card_list = (card.generate_list()) # Currently will not generate new set of cards each game (fixed at launching game)
    show screen stats_screen()
    show screen card_display()
    pause
    return

label no_cards:
    e "How unfortunate!"
    e "Back to the start it is"
    jump start
    return
