# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define e = Character("Eileen")
image plasticbag = "plasticbag.png"

# The game starts here.

label start:

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

    e "You've created a new Ren'Py game."

    e "Once you add a story, pictures, and music, you can release it to the world!"

    e "Do you ever feel like:"

    show plasticbag at left with dissolve
    show plasticbag at center with dissolve
    show plasticbag at right with dissolve

    e "End"

    hide plasticbag at right

    # This ends the game.

    return
