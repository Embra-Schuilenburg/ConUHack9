from itertools import islice

from db import *

archetypes = get_all_archetypes()

def safest_matchups(archetype):
    matches = exclude_low_sample(archetype).sort()
    return list(islice(matches, 5))

def exclude_low_sample(archetype):
    return [arch for arch in get_archetype(archetype) if archetype.game > 10]
