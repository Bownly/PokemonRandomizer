import codecs
import os
import sys
from random import randint

famlist1 = [
    ["FARFETCHD"],
    ["ONIX"],
    ["HITMONLEE"],
    ["HITMONCHAN"],
    ["LICKITUNG"],
    ["CHANSEY"],
    ["TANGELA"],
    ["KANGASKHAN"],
    ["SCYTHER"],
    ["ELECTABUZZ"],
    ["MAGMAR"],
    ["PINSIR"],
    ["TAUROS"],
    ["DITTO"],
    ["AERODACTYL"]
]
famlist2 = [
    ["RATTATA", "RATICATE"],
    ["SPEAROW", "FEAROW"],
    ["EKANS", "ARBOK"],
    ["PIKACHU", "RAICHU"],
    ["SANDSHREW", "SANDSLASH"],
    ["CLEFAIRY", "CLEFABLE"],
    ["VULPIX", "NINETALES"],
    ["JIGGLYPUFF", "WIGGLYTUFF"],
    ["ZUBAT", "GOLBAT"],
    ["PARAS", "PARASECT"],
    ["VENONAT", "VENOMOTH"],
    ["DIGLETT", "DUGTRIO"],
    ["MEOWTH", "PERSIAN"],
    ["PSYDUCK", "GOLDUCK"],
    ["MANKEY", "PRIMEAPE"],
    ["GROWLITHE", "ARCANINE"],
    ["PONYTA", "RAPIDASH"],
    ["SLOWPOKE", "SLOWBRO"],
    ["MAGNEMITE", "MAGNETON"],
    ["TENTACOOL", "TENTACRUEL"], 
    ["DODUO", "DODRIO"],
    ["SEEL", "DEWGONG"],
    ["GRIMER", "MUK"],
    ["SHELLDER", "CLOYSTER"],
    ["DROWZEE", "HYPNO"],
    ["KRABBY", "KINGLER"],
    ["VOLTORB", "ELECTRODE"],
    ["EXEGGCUTE", "EXEGGUTOR"],
    ["CUBONE", "MAROWAK"],
    ["KOFFING", "WEEZING"],
    ["RHYHORN", "RHYDON"],
    ["HORSEA", "SEADRA"],
    ["GOLDEEN", "SEAKING"],
    ["STARYU", "STARMIE"],
    ["MAGIKARP", "GYARADOS"],
    ["OMANYTE", "OMASTAR"],
    ["KABUTO", "KABUTOPS"]
]
famlist3 = [
    ["BULBASAUR", "IVYSAUR", "VENUSAUR"],
    ["CHARMANDER", "CHARMELEON", "CHARIZARD"],
    ["SQUIRTLE", "WARTORTLE", "BLASTOISE"],
    ["CATERPIE", "METAPOD", "BUTTERFREE"],
    ["WEEDLE", "KAKUNA", "BEEDRILL"],
    ["PIDGEY", "PIDGEOTTO", "PIDGEOT"],
    ["NIDORAN_F", "NIDORINA", "NIDOQUEEN"],
    ["NIDORAN_M", "NIDORINO", "NIDOKING"],
    ["ODDISH", "GLOOM", "VILEPLOOM"],
    ["POLIWAG", "POLIWHIRL", "POLIWRATH"],
    ["ABRA", "KADABRA", "ALAKAZAM"],
    ["MACHOP", "MACHOKE", "MACHAMP"],
    ["BELLSPROUT", "WEEPINBELL", "VICTREEBEL"],
    ["GEODUDE", "GRAVELER", "GOLEM"],
    ["GASTLY", "HAUNTER", "GENGAR"],
    ["DRATINI", "DRAGONAIR", "DRAGONITE"]
]

base_dex = {
    "BULBASAUR"   : ["BULBASAUR", "IVYSAUR", "VENUSAUR"],
    "CHARMANDER"  : ["CHARMANDER", "CHARMELEON", "CHARIZARD"],
    "SQUIRTLE"    : ["SQUIRTLE", "WARTORTLE", "BLASTOISE"],
    "CATERPIE"    : ["CATERPIE", "METAPOD", "BUTTERFREE"],
    "WEEDLE"      : ["WEEDLE", "KAKUNA", "BEEDRILL"],
    "PIDGEY"      : ["PIDGEY", "PIDGEOTTO", "PIDGEOT"],
    "RATTATA"     : ["RATTATA", "RATICATE"],
    "SPEAROW"     : ["SPEAROW", "FEAROW"],
    "EKANS"       : ["EKANS", "ARBOK"],
    "PIKACHU"     : ["PIKACHU", "RAICHU"],
    "SANDSHREW"   : ["SANDSHREW", "SANDSLASH"],
    "NIDORAN_F"   : ["NIDORAN_F", "NIDORINA", "NIDOQUEEN"],
    "NIDORAN_M"   : ["NIDORAN_M", "NIDORINO", "NIDOKING"],
    "CLEFAIRY"    : ["CLEFAIRY", "CLEFABLE"],
    "VULPIX"      : ["VULPIX", "NINETALES"],
    "JIGGLYPUFF"  : ["JIGGLYPUFF", "WIGGLYTUFF"],
    "ZUBAT"       : ["ZUBAT", "GOLBAT"],
    "ODDISH"      : ["ODDISH", "GLOOM", "VILEPLOOM"],
    "PARAS"       : ["PARAS", "PARASECT"],
    "VENONAT"     : ["VENONAT", "VENOMOTH"],
    "DIGLETT"     : ["DIGLETT", "DUGTRIO"],
    "MEOWTH"      : ["MEOWTH", "PERSIAN"],
    "PSYDUCK"     : ["PSYDUCK", "GOLDUCK"],
    "MANKEY"      : ["MANKEY", "PRIMEAPE"],
    "GROWLITHE"   : ["GROWLITHE", "ARCANINE"],
    "POLIWAG"     : ["POLIWAG", "POLIWHIRL", "POLIWRATH"],
    "ABRA"        : ["ABRA", "KADABRA", "ALAKAZAM"],
    "MACHOP"      : ["MACHOP", "MACHOKE", "MACHAMP"],
    "BELLSPROUT"  : ["BELLSPROUT", "WEEPINBELL", "VICTREEBEL"],
    "TENTACOOL"   : ["TENTACOOL", "TENTACRUEL"], 
    "GEODUDE"     : ["GEODUDE", "GRAVELER", "GOLEM"],
    "PONYTA"      : ["PONYTA", "RAPIDASH"],
    "SLOWPOKE"    : ["SLOWPOKE", "SLOWBRO"],
    "MAGNEMITE"   : ["MAGNEMITE", "MAGNETON"],
    "FARFETCHD"   : ["FARFETCHD"],
    "DODUO"       : ["DODUO", "DODRIO"],
    "SEEL"        : ["SEEL", "DEWGONG"],
    "GRIMER"      : ["GRIMER", "MUK"],
    "SHELLDER"    : ["SHELLDER", "CLOYSTER"],
    "GASTLY"      : ["GASTLY", "HAUNTER", "GENGAR"],
    "ONIX"        : ["ONIX"],
    "DROWZEE"     : ["DROWZEE", "HYPNO"],
    "KRABBY"      : ["KRABBY", "KINGLER"],
    "VOLTORB"     : ["VOLTORB", "ELECTRODE"], 
    "EXEGGCUTE"   : ["EXEGGCUTE", "EXEGGUTOR"],
    "CUBONE"      : ["CUBONE", "MAROWAK"],
    "HITMONLEE"   : ["HITMONLEE"],
    "HITMONCHAN"  : ["HITMONCHAN"],
    "LICKITUNG"   : ["LICKITUNG"],
    "KOFFING"     : ["KOFFING", "WEEZING"],
    "RHYHORN"     : ["RHYHORN", "RHYDON"],
    "CHANSEY"     : ["CHANSEY"],
    "TANGELA"     : ["TANGELA"],
    "KANGASKHAN"  : ["KANGASKHAN"],
    "HORSEA"      : ["HORSEA", "SEADRA"],
    "GOLDEEN"     : ["GOLDEEN", "SEAKING"],
    "STARYU"      : ["STARYU", "STARMIE"],
    "SCYTHER"     : ["SCYTHER"],
    "ELECTABUZZ"  : ["ELECTABUZZ"],
    "MAGMAR"      : ["MAGMAR"],
    "PINSIR"      : ["PINSIR"],
    "TAUROS"      : ["TAUROS"],
    "MAGIKARP"    : ["MAGIKARP", "GYARADOS"],
    "DITTO"       : ["DITTO"],
    "OMANYTE"     : ["OMANYTE", "OMASTAR"],
    "KABUTO"      : ["KABUTO", "KABUTOPS"],
    "AERODACTYL"  : ["AERODACTYL"],
    "DRATINI"     : ["DRATINI", "DRAGONAIR", "DRAGONITE"]
}

end_dex = {}

# this block is in charge of determining how the pokemon get switched around
for pokemon in base_dex:
    ogfam = base_dex[pokemon]
    famsize = len(ogfam)
    
    if (famsize == 1):
        famlist = famlist1
    elif (famsize == 2):
        famlist = famlist2
    elif (famsize == 3):
        famlist = famlist3
        
    newfam = famlist[randint(0, len(famlist)-1)]
    for i in range(famsize):
        end_dex[ogfam[i]] = (newfam[i])
    famlist.remove(newfam)

# this block builds out the list of files that need editing
files_list = []
# wild locations
dir = os.path.join(os.getcwd(), 'pokered', 'data', 'wildPokemon')
for f in os.listdir(dir):
    if f.endswith('.asm'):
        files_list.append(dir + "/" + f)
# starters
dir = os.path.join(os.getcwd(), 'pokered', 'constants')
dir += '/starter_mons.asm'
files_list.append(dir)
# fossils
dir = os.path.join(os.getcwd(), 'pokered', 'engine', 'overworld')
dir += '/cinnabar_lab.asm'
files_list.append(dir)

# this block does the actual data replacement in the rom files
for fl in files_list:
    print fl
    with open(fl) as f:
        content = [x.strip('\n') for x in f.readlines()]
        out_lines = []
        for line in content:
            new_line = ''
            for word in line.split():
                if word in end_dex:
                    line = line.replace(word, end_dex[word])
            for word in line.split(","):
                if word in end_dex:
                    line = line.replace(word, end_dex[word])
            out_lines.append(line)
        
        out = open(fl, 'w')
        out_content = "\n".join(out_lines)
        out.write(out_content)
        out.close()





# gym leader stuff to consider:
    # whatever this stuff is:
        # pokered/blob/master/data/trainer_moves.asm
    # TM stuff (for all gyms, not just pewter):
        # pokered/blob/master/scripts/pewtergym
    # parties list:
        # master/data/trainer_parties.asm






