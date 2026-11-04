# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.
init python:
    from python import card

define d = Character("Dramaturgy")
define a = Character("Alcaeus")
define mom = Character("Alcaeus's Mother")
define dad = Character("Alcaeus's Father")
define statue = Character("Voice of the Statue")
define s1 = Character("Pausidio")
define s2 = Character("Marilis")


image plasticbag = "plasticbag.png"
image good_end = "stronk.jpg"
image bad_end = "patrickrock.png"
image game_over = "game_over.jpg"

image comedy_card = "Comedy_Plot_Card.png"


default tst = 0 # variable for testing

screen stats_screen():
    timer 0.1 repeat True
    frame:
        xalign 0.0
        yalign 0.0
        vbox:
            text "Name" 
            bar value audience range 10
            text "Energy: [energy]"
            text "Ending: [ending]"
        text "\nAudience"

screen card_display(): # make button that when pressed, will check for None objects then replace up to 3 with a card and place it based on slot attribute
    default is_hovered = False
    if initialize:
        draggroup:
            id "card_drag_group"
            for i in range(7):
                drag:  # Not currently used
                    xpos (i) * (1/7)
                    ypos 0.75
                    draggable False
                    drag_name "slot%s" % str(i + 1)
                    image Solid("#181313") xysize(100,100)

            for display_card in card_list:
                #$ drag_list = [display_card, card_list.index(display_card)]
                drag:
                    xpos slot
                    ypos 0.75
                    drag_raise True
                    draggable True
                    #drag_name "display_card%s" % card_list.index(display_card)  # Incompatible: If using string, can't access object. If using object, can't use index
                    drag_name display_card
                    dragged card.dragged_func
                    hovered SetScreenVariable("is_hovered", True) # Can access index of each, might have to make separate variables for each? or make list/dict of 7?
                    unhovered SetScreenVariable("is_hovered", False)
                    
                    if display_card is not None:
                        frame at move_card:
                            if display_card.type == "plot":
                                xysize 240, 240
                                background Frame("Comedy_Plot_Card.png")
                            xalign 0.0
                            yalign 0.0        
                            vbox:
                                text "[display_card.type]"
                                text "Energy: [display_card.energy]"
                                text "Audience: [display_card.audience]"
                                #if is_hovered:
                                    #text "[drag_name]"
                    else: # Makes used cards go suuuuuuuuuuuuuper far away!
                        xpos 99999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999.0
                        ypos 99999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999.0
                        #$ print(99999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999.0)

                $ slot += 1/7
            $ slot = 0
            drag: # Where cards are dropped
                #child At("plasticbag.png", move_card)
                align(0.5, 0.5)
                draggable False
                #dropped card.test
                drag_name "use"
                image Solid("#575757") xysize(100,100)

        frame:
            align(0.25, 1.0)
            textbutton "play":
                action Jump("play")

        # Not working properly
        #frame:
        #    align(0.75, 1.0)
        #    textbutton "draw":
        #        action Function(card.snap_card, card_list[0])

            
        # TODO: make slots that cards snap to if not placed in "use" drag; will probably have to modify slot variable from before to be fixed to these spots
        
                
        
    


transform move_card:
    #zoom 1.5
    on hover:
        ease 0.25 zoom 1.5
    on idle:
        ease 0.25 zoom 0.2
        

# The game starts here.

label start:
    default audience = 10
    default energy = 10
    default card_list = []
    default slot = 0
    default initialize = True
    default ending = ""
    default new_cards = False
    #default drag_list = []

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

    d "Welcome Director to the game"

    d "From the day he was born, Alcaeus felt like he had been missing something. Like something greater has been calling to him. A familiar voice, just out of reach."

    d "He didn’t have a name for it. Or why he felt that way. Alcaeus had two loving parents, and a comfortable life on the farmland they call home. Every day moved like clockwork. Tending to farm chores. Tending to the sheep. Eat. Sleep. Repeat."

    d "That was until one night a great storm came, ravaging their farm. A great wind shook the foundations of their home, pillars cracked, the house collapsing beneath its weight, trapping Alcaeus and his parents."

    d "In desperation, Alcaeus struggled against the stone piled above him."

    d "Do you want to play cards?"

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
    d "Plastic bag"
    d "Plastic bag"
    return

label Choice_2:
    d "EEEEEEEEEEE"
    d "Rewind"
    jump start
    return

label play: # When play button pressed
    $ card.play_card()
    if audience <= 0:
        jump game_over
    pause
    if ending == "succeed":
        jump good_end
    elif ending == "fail":
        jump bad_end
    return

label play_cards: # Sets out cards
    show plasticbag at top with dissolve
    $ card_list = (card.generate_list())
    show screen stats_screen
    show screen card_display
    #$ print(renpy.get_showing_tags())
    hide plasticbag
    pause 
    return

label no_cards:
    d "How unfortunate!"
    d "Back to the start it is"
    jump start
    return

# Game paths, letter is fate momements and number is which choice made
label a1:
    hide screen card_display
    hide screen stats_screen
    d "Alcaeus grit his teeth as he struggled against the rock. Debris crumbled around him as it shifted under his strength. With a mighty shove, the rock flew."
    d "He rushed over to his parents, lifting the rocks covering them, before rushing them out of the still crumbling house."
    a "Are you alright, Mama? Baba?"
    mom "We are, thanks to you."
    dad "Thank you, son."
    a "I’m just so glad you’re safe. I have no clue how I did that."
    d "Alcaeus’s mother and father shared a look."
    dad "Alcaeus, the truth is that when you were a baby, we found you in a distant wheat field. We raised you as our own. But, maybe this strength in you comes from your birth parents."
    a "But, who could it be? What happened to my birth parents?"
    dad "We don’t know unfortunately. But, maybe the Temple of Knowledge would have answers."
    a "Then, I have to go."
    mom "We understand. And we’ll always support you, Alcaeus."
    d "Alcaeus hugged them"
    a "Thank you. No matter what, you will always be my mama and baba."
    d "Alcaeus packed whatever food and water they could salvage and then headed off towards the Temple of Knowledge. He traveled for a day and night until he found the torches outside the temple shining at the top of the hill."
    d "Heading inside, Alcaeus stopped in front of a giant statue of a man."
    statue "Welcome, Alcaeus"
    a "Woah! How did you know my name?"
    statue "I have knowledge of all people in this world, my boy."
    a "Can you… Do you know who I am, then?"
    statue "I do. But, I cannot tell you yet."
    a "Is there something I need to do?"
    statue "In order to reveal the truth of your past, you must first become a true hero."
    a "A true hero..."
    statue "Go to insert city name. There you will find Pausidio. He will guide you."
    d "And so Alcaeus set off for insert city name. There he found a training ground for warriors."
    a "Greetings. My name is Alcaeus. Are you Sir Pausidio?"
    s1 "That is correct, young one. How may I assist you?"
    a "The Temple of Knowledge has guided me here. He said I need to become a true hero before I can obtain the knowledge I seek."
    s1 "You have come to the right place then, Alcaeus. I have trained many young warriors in my time. "
    d "Thus, Alcaeus’s training began. He rescued nearby villages by defeating various monsters. From small harpies and gargoyles. To even a minotaur. The townspeople he helped spread his name far and wide."
    s2 "Thank you, Hero Alcaeus. We can finally begin to rebuild our town thanks to you relinquishing us of the minotaur."
    a "It’s no trouble at all, I’m glad I could help!"
    s2 "Where are you heading to next?"
    a "I think I will head to the Temple of Knowledge."
    d "Once again, Alcaeus found himself at the temple."
    a "Greetings, O Wise Voice.  I ask if I may discover who my birth parents are now?"
    statue "You still have not become a true hero, young Alcaeus."
    a "But-"
    d "A loud commotion came from outside the temple. Alcaeus ran back out, looking down into the valley. "
    d "From a distance, he saw a large shadowy figure looming over the village. It looked draconic, or perhaps serpentine, in appearance. When it roared, the ground shook."
    d "Alcaeus ran"
    a "How did such a large monster appear so suddenly?"
    d "Screams and cries from the villagers rang in his ears."
    d "There, towering above him, was a creature with thick draconic scales and a long serpentine neck. Its menacing glare scoped around the town as it crushed anything underneath it."
    d "An acrid smell permeated the air, forcing heaving coughs from aa"
    s1 "Alcaeus!"
    a "Teacher, what happened?"
    s1 "The monster appeared as if made of darkness itself, Alcaeus!"
    d "From further away, Alcaeus saw Marilis leading frantic villagers out of the premises. "
    d "He turned back to the creature. "
    jump play_cards
    # TODO: Have some way to switch out plot points for second fate moment

label a2:
    pass

label b1:
    pass

label b2:
    pass
# Game endings
label good_end:
    play sound "yippeeeeeeeeeeeeee.mp3"
    show good_end at truecenter
    a "I very stronk"
    return

label bad_end:
    play sound "roblox-death-sound_1.mp3"
    hide screen card_display
    hide screen stats_screen
    show bad_end at truecenter
    a "Oof"
    return

label game_over:
    stop music
    hide screen card_display
    hide screen stats_screen
    play music "worlds-smallest-violin.mp3"
    show game_over at truecenter
    d "Wow. The audience hates you. You lose!"
    return
