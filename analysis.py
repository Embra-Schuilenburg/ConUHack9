from itertools import islice

from db import *

archetypes = get_all_archetypes()

def safest_matchups(archetype):
    matches = get_archetype(archetype).sort()
    return matches[:5]

def risky_matchups(archetype):
    matches = get_archetype(archetype).sort()
    return list(islice(matches, 5))

def most_likely_to_win(archetype):
    return