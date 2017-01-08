# Pokemon Prism Randomizer

Consult this repository's main README for general details on this script.


# Version compatibility

I've tested this with the version 0.92, build 0144 source. It should work with any and all versions, assuming the general layout of the files is left unchanged.


# How to use

Ensure that the folder containing the Prism disassembly is named "source". Then put the source folder in the same directory as randomize.py, and run randomize.py. Afterwards, build the Prism ROM as you normally would. 


# Notes/exceptions

- Pokemon families that can't be caught are left unchanged (starters, gifts, fossils, etc)
- Legendaries are left unchanged
- Fire families only swap with other fire families, and the same for electric families (this is to prevent a scenario in which you can't catch a fire and/or electric pokemon before that one early cave)
  - Except Torkoal who is the only fire or electric with a type 1 stage family, and is therefore shuffled with all other 1 stage families
- Snorunt/Froslass are treated as a 2 stage family, omitting Glalie because I had to omit one and Froslass is rarer
- Ralts/Kirlia/Gallade are treated as a 3 stage family, omitting Gardevoir because I had to omit one and Gallade is rarer
- Eevee/Glaceon/Leafeon are treated as a 3 stage family (since you can catch wild Glaceon and Leafeon in vanilla Prism)
- Slowpoke/Slowking are treated as a 2 stage family, omitting Slowbro because I had to omit one and Slowking is rarer
- Baby pokemon are omitted, treating their families as one size shorter than normal (ex: Pikachu/Raichu becomes a 2 stage family)
  - Except the Chingling family is treated as 2 stages since you can catch Chingling in the wild in vanilla Prism
  - Also except Hitmonchan/Hitmonlee/Hitmontop are treated as 3 separate 1 stage familes, and Tyrogue is omitted


# Full list of non-shuffled pokemon

- Chikorita/Bayleef/Meganium
- Totodile/Croconaw/Feraligatr
- Cyndaquil/Quilava/Typhlosion
- Glalie
- Gardevoir
- Slowbro
- Pichu/Tyrogue/Elekid/Magby
- Togepi/Togetic/Togekiss
- Cranidos/Rampardos
- Shieldon/Bastiodon
- Lileep/Cradily
- Anorith/Armaldo
- Bulbasaur/Ivysaur/Venusaur
- Charmander/Charmeleon/Charizard
- Squirtle/Wartortle/Blastoise
- Phancero/Articuno/Zapdos/Moltres
- Mewtwo/Mew
- Lugia/Ho-oh
- Groudon/Kyogre/Rayquaza
- Varaneous
- Raiwato
- Libabeel


# Possible future features

- Include trade/gift/game corner/overworld/etc pokemon
- Add some options like:
  - swap starters or not
  - swap TM locations
  - swap gym leaders (?)

