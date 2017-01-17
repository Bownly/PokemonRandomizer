# Pokemon Red/Blue Randomizer

This script randomizes pokemon locations and gym leader order. Consult this repository's main README for general details on this script.


# Version compatibility

Tested for compatibility with the current build (as of Jan 7, 2017) of:
Disassembly of [**Pokémon Red/Blue**][pokered]
[pokered]: https://github.com/iimarckus/pokered


# How to use

Ensure that the folder containing the Red disassembly is named "pokered". Then put the pokered folder in the same directory as randomize.py, and run randomize.py. Afterwards, build the Red and/or Blue ROMs as you normally would. Badabing, badaboom.


# Pokemon shuffle


## Notes/exceptions

- Starter and fossil pokemon families are shuffled, however, the overworld texts etc are not changed to reflect this. Also, your rival's pokemon does not get altered.
- Trade-exclusive families are not randomized, nor are gift-exclusive families. Same for overworld-exlusive pokemon and Game Corner-exclusive pokemon.


## Full list of non-shuffled pokemon

- Vaporeon/Jolteon/Flareon
- Articuno/Zapdos/Moltres
- Mewtwo/Mew


# Gym leader shuffle


## Explanation

This script shuffles around the order of the gym leaders (excluding Giovanni). Their teams are scaled/altered to maintain the same relative balance as in the vanilla experience. 

Things that are shuffled by the script:
- Gym leader locations/order
- Gym leader sprites

Things that are not shuffled by the script:
- Badge order/distribution
- The order/distribution of the gym TM prizes
- Any corresponding text/dialog


## Full teams listing

I had to make up pretty much all of these teams. They should all be roughly equal in terms of balance. Format is {level} {pokemon}. 

Brock:
- 12 Geodude, 14 Onix
- 18 Graveler, 21 Onix
- 21 Graveler, 18 Aerodactyl, 24 Onix
- 29 Golem, 24 Aerodactyl, 29 Onix
- 37 Omanyte, 39 Golem, 37 Aerodactyl, 43 Onix
- 38 Omastar, 37 Golem, 38 Aerodactyl, 43 Onix
- 42 Omastar, 40 Golem, 42 Aerodactyl, 47 Onix

Misty:
- 12 Psyduck, 14 Staryu
- 18 Psyduck, 21 Starmie
- 21 Psyduck, 18 Lapras, 24 Starmie
- 29 Golduck, 24 Lapras, 29 Starmie
- 37 Tentacool, 39 Golduck, 37 Lapras, 43 Starmie
- 38 Tentacruel, 37 Golduck, 38 Lapras, 43 Starmie
- 42 Tentacruel, 40 Golduck, 42 Lapras, 47 Starmie

Lt. Surge:
- 12 Voltorb, 14 Pikachu
- 18 Voltorb, 21 Raichu
- 21 Voltorb, 18 Electabuzz, 24 Raichu
- 29 Electrode, 24 Electabuzz, 29 Raichu
- 37 Magnemite, 39 Electrode, 37 Electabuzz, 43 Raichu
- 38 Magneton, 37 Electrode, 38 Electabuzz, 43 Raichu
- 42 Magneton, 40 Electrode, 42 Electabuzz, 47 Raichu

Erika:
- 12 Bellsprout, 14 Oddish
- 18 Weepinbell, 21 Gloom
- 21 Weepinbell, 18 Tangela, 24 Vileplume
- 29 Victreebel, 24 Tangela, 29 Vileplume
- 37 Exeggcute, 39 Victreebel, 37 Tangela, 43 Vileplume
- 38 Exeggutor, 37 Victreebel, 38 Tangela, 43 Vileplume
- 42 Exeggutor, 40 Victreebel, 42 Tangela, 47 Vileplume

Koga:
- 12 Grimer, 14 Koffing
- 18 Grimer, 21 Weezing
- 21 Grimer, 18 Golbat, 24 Weezing
- 29 Muk, 24 Golbat, 29 Weezing
- 37 Nidorino, 39 Muk, 37 Golbat, 43 Weezing
- 38 Nidoking, 37 Muk, 38 Golbat, 43 Weezing
- 42 Nidoking, 40 Muk, 42 Golbat, 47 Weezing

Sabrina:
- 12 Venonat, 14 Kadabra
- 18 Venonat, 21 Kadabra
- 21 Venonat, 18 Mr. Mime, 24 Kadabra
- 29 Venomoth, 24 Mr. Mime, 29 Alakazam
- 37 Slowpoke, 39 Mr. Mime, 37 Venomoth, 43 Alakazam
- 38 Slowbro, 37 Mr. Mime, 38 Venomoth, 43 Alakazam
- 42 Slowbro, 40 Mr. Mime, 42 Venomoth, 47 Alakazam

Blaine:
- 12 Ponyta, 14 Growlithe
- 18 Ponyta, 21 Arcanine
- 21 Ponyta, 18 Magmar, 24 Arcanine
- 29 Rapidash, 24 Magmar, 29 Arcanine
- 37 Vulpix, 39 Rapidash, 37 Magmar, 43 Arcanine
- 38 Ninetales, 37 Rapidash, 38 Magmar, 43 Arcanine
- 42 Ninetales, 40 Magmar, 42 Rapidash, 47 Arcanine


# Moveset changes

I added a few moves to a handful of pokemon that otherwise wouldn't learn any moves at a low level. I wouldn't want anyone to catch a Rhyhorn on route 1 and be stuck with only Horn Attack until it learns its next move at level 30, for example. Below is the complete list of moveset changes that I made:

- Exeggcute: 20, Psywave
- Grimer: 15, Sludge; 37, Toxic
- Rhyhorn: 15, Rock Slide
- Shellder: 15, Water Gun
- Tangela: 15, Vine Whip
- Psyduck: 15, Water Gun
- Magmar: 15, Rage
- Electabuzz: 15, Thundershock; 34, Swift
- Koffing: 24, Sludge
- Seel: 15, Water Gun
- Venonat: 15, Confusion
- Dratini: 15, Water Gun
- Kabuto: 15, Water Gun
- Goldeen: 15, Water Gun
- Aerodactyl: 20, Rock Throw
- Magnemite: 15, Thundershock


# Possible future features

- Include bird trio/Mewtwo/(Mew?)
- Include Giovanni/E4 in the gym leader swap
- Shuffle misc boss fights like with your Rival and Giovanni in Silph Co.
- Shuffle trainers' pokemon
- Shuffle TMs
- Shuffle route/town locations (I don't even know what I mean by this, but it sounds cool)
- Include Gen 2+ pokemon
- Add some options and maybe a GUI for them

