import random
import renpy
import renpy.store as store
from renpy.exports import restart_interaction

card_list = []
card_names = []
card_types = ["plot", "buff", "?"]
plot_points = ["succeed", "fail"]
dragged_card = None
played_card = None
#TODO: make play card detection based on position rather than depending on dragged function. Possibly move screen into python?
class card:
    def __init__(self, slot, name, card_type, energy, audience, plot_point):
        self.name = name
        self.slot = slot
        self.type = card_type
        self.energy = energy
        self.audience = audience
        self.plot = plot_point


def generate_list():
    global card_list
    card_list = []
    slot_num = 1 # slot index starts at 1, could change to 0 to make math positioning a bit easier though
    while len(card_list) < 7: # Somehow tie this to renpy thing, possibly put it in card class?
        new_card = card(name = "test", slot = slot_num, card_type = random.choice(card_types), energy = random.randint(0,3), audience = 0, plot_point = "")
        if new_card.type == "buff":
            new_card.audience = random.randint(-17,-7)
        elif new_card.type == "plot":
            new_card.plot = random.choice(plot_points)
        card_list.append(new_card)
        slot_num += 1

    return card_list    

def dragged_func(dragged, dropped): 
    global dragged_card
    global played_card
    #played_card = None
    dragged_card = dragged[0].drag_name
    #print("Slot num", dragged_card.slot)
    #print("NAME:", dragged_card)
    #print("type", dragged_card.type)
    #print("energy", dragged_card.energy)
    #print("audience", dragged_card.audience)
    #print("plot", dragged_card.plot)
    #print("\n")
    
    if dropped is not None:
        print("Drop", dropped.drag_name) # After first card played, any card dropped on top is dropped onto None, which means old drag is still remaining there
        if dropped.drag_name == "use": # When a card is dragged onto 'use'
            played_card = dragged[0].drag_name
            dragged[0].snap(dropped.x, dropped.y, 0.25)
            print(dragged[0].x)
            print(dragged[0].y)
            print(dropped.x)
            print(dropped.y)
        else:
            dragged[0].snap((dragged_card.slot - 1) * 1/7, 0.75, 0.25)
    else:
        dragged[0].snap((dragged_card.slot - 1) * 1/7, 0.75, 0.25) # doesn't currently snap to 'slot' draggable, only the specified position for each card

def play_card():
    global played_card
    global card_list
    if played_card is not None:
        store.energy -= played_card.energy

        store.audience += played_card.audience
        if store.audience > 10:
            store.audience = 10

        if played_card.type == "plot":
            store.ending = played_card.plot

        try:
            card_list[card_list.index(played_card)] = None
        except:
            print("This card is not in the list")

        restart_interaction() # refreshes stats screen
    new_card()

def new_card():
    global played_card
    global card_list
    store.new_cards = True
    #print("new card")
    # Right now, this replaces 'None' with an random card but it gets placed in 'use' because that is where last position was.
    try:
        card_list[card_list.index(None)] = card(name = "test", slot = card_list.index(None) + 1, card_type = random.choice(card_types), energy = random.randint(0,3), audience = 0, plot_point = "")
    except:
        print("Full card list")

# Not working properly
"""def snap_card(card_object):
    drag_group = renpy.get_displayable("card_display", "card_drag_group")

    if drag_group is None:
        print("Drag group not found.")
        return

    drag = drag_group.get_child_by_name(card_object)

    if drag is not None:
        drag.snap(400, 300, 0.2)
    else:
        print("Card drag not found:", card_object)"""


    