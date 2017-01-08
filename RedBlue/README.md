# Pokemon Prism Randomizer

This script randomizes which pokemon are encountered on which routes. It swaps pokemon by family groupings of the same size. The swaps aren't guaranteed to be reciprocal, but the changes will remain consistent throughout every route. To illustrate: You could end up with a result where Venonat/Venomoth get replaced with Onix/Steelix, and Onix/Steelix gets replaced with Tangela/Tangrowth and Tangela/Tangrowth gets replaced with... well, you get the point. In vanilla Prism, you can catch Venonat in the Acqua Mines and the Health Gym, and Venomoth in Castro Forest and Eagulou Park. Given the same example as before, you would instead encounter Onix in the Acqua mines and the Health Gym, and Steelix in Castro Forest and Eagulou Park. And you'd find Tangela wherever Onix are found in vanilla Prism, etc.


# How to use

Note: You have to supply your own copy of the Prism source code for this to work. Put the Prism source folder in the same directory as randomize.py, and then run randomize.py. Afterwards, build the Prism ROM as you normally would.


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

- Include gift/starter/fossil pokemon
- Adapt the script for RBGY/GSC/Brown/etc
- Have the code output an ips instead of requiring the users to build their own ROM
- Add some options



