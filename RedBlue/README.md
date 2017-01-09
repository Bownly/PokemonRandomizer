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

- Eevee/Vaporeon/Jolteon/Flareon
- Jynx
- Mr. Mime
- Lapras
- Porygon
- Snorlax
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
- 12 GEODUDE, 14 ONIX
- 18 GRAVELER, 21 ONIX
- 21 GRAVELER, 18 AERODACTYL, 24 ONIX
- 29 GOLEM, 24 AERODACTYL, 29 ONIX
- 37 OMANYTE, 39 GOLEM, 37 AERODACTYL, 43 ONIX
- 38 OMASTAR, 37 GOLEM, 38 AERODACTYL, 43 ONIX
- 42 OMASTAR, 40 GOLEM, 42 AERODACTYL, 47 ONIX

Misty:
- 12 PSYDUCK, 14 STARYU
- 18 PSYDUCK, 21 STARMIE
- 21 PSYDUCK, 18 LAPRAS, 24 STARMIE
- 29 GOLDUCK, 24 LAPRAS, 29 STARMIE
- 37 TENTACOOL, 39 GOLDUCK, 37 LAPRAS, 43 STARMIE
- 38 TENTACRUEL, 37 GOLDUCK, 38 LAPRAS, 43 STARMIE
- 42 TENTACRUEL, 40 GOLDUCK, 42 LAPRAS, 47 STARMIE

Lt. Surge:
- 12 VOLTORB, 14 PIKACHU
- 18 VOLTORB, 21 RAICHU
- 21 VOLTORB, 18 ELECTABUZZ, 24 RAICHU
- 29 ELECTRODE, 24 ELECTABUZZ, 29 RAICHU
- 37 MAGNEMITE, 39 ELECTRODE, 37 ELECTABUZZ, 43 RAICHU
- 38 MAGNETON, 37 ELECTRODE, 38 ELECTABUZZ, 43 RAICHU
- 42 MAGNETON, 40 ELECTRODE, 42 ELECTABUZZ, 47 RAICHU

Erika:
- 12 BELLSPROUT, 14 ODDISH
- 18 WEEPINBELL, 21 GLOOM
- 21 WEEPINBELL, 18 TANGELA, 24 VILEPLUME
- 29 VICTREEBEL, 24 TANGELA, 29 VILEPLUME
- 37 EXEGGCUTE, 39 VICTREEBEL, 37 TANGELA, 43 VILEPLUME
- 38 EXEGGUTOR, 37 VICTREEBEL, 38 TANGELA, 43 VILEPLUME
- 42 EXEGGUTOR, 40 VICTREEBEL, 42 TANGELA, 47 VILEPLUME

Koga:
- 12 GRIMER, 14 KOFFING
- 18 GRIMER, 21 WEEZING
- 21 GRIMER, 18 GOLBAT, 24 WEEZING
- 29 MUK, 24 GOLBAT, 29 WEEZING
- 37 NIDORINO, 39 MUK, 37 GOLBAT, 43 WEEZING
- 38 NIDOKING, 37 MUK, 38 GOLBAT, 43 WEEZING
- 42 NIDOKING, 40 MUK, 42 GOLBAT, 47 WEEZING

Sabrina:
- 12 VENONAT, 14 KADABRA
- 18 VENONAT, 21 KADABRA
- 21 VENONAT, 18 MR_MIME, 24 KADABRA
- 29 VENOMOTH, 24 MR_MIME, 29 ALAKAZAM
- 37 SLOWPOKE, 39 MR_MIME, 37 VENOMOTH, 43 ALAKAZAM
- 38 SLOWBRO, 37 MR_MIME, 38 VENOMOTH, 43 ALAKAZAM
- 42 SLOWBRO, 40 MR_MIME, 42 VENOMOTH, 47 ALAKAZAM

Blaine:
- 12 PONYTA, 14 GROWLITHE
- 18 PONYTA, 21 ARCANINE
- 21 PONYTA, 18 MAGMAR, 24 ARCANINE
- 29 RAPIDASH, 24 MAGMAR, 29 ARCANINE
- 37 VULPIX, 39 RAPIDASH, 37 MAGMAR, 43 ARCANINE
- 38 NINETALES, 37 RAPIDASH, 38 MAGMAR, 43 ARCANINE
- 42 NINETALES, 40 MAGMAR, 42 RAPIDASH, 47 ARCANINE


# Possible future features

- Include trade/gift/game corner/overworld/etc pokemon
- Add some options like:
  - swap starters or not
  - swap TM locations
  - swap gym leaders (?)


