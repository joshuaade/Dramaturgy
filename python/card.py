import random

card_list = []
card_names = []
card_types = ["plot", "buff", "?"]

class card:
    def __init__(self, name, card_type, energy, audience):
        self.name = name
        self.type = card_type
        self.energy = energy
        self.audience = audience


def generate_list():
    while len(card_list) < 7: # Somehow tie this to renpy thing, possibly put it in card class?
        new_card = card("test", random.choice(card_types), random.randint(0,3), random.randint(-3,3))
        card_list.append(new_card)

    return card_list    
