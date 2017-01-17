import codecs
import os
import re
import sys
from random import randint, shuffle

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
    ["JYNX"],
    ["MR_MIME"],
    ["PINSIR"],
    ["TAUROS"],
    ["EEVEE"],
    ["DITTO"],
    ["LAPRAS"],
    ["PORYGON"],
    ["SNORLAX"],
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
    ["ODDISH", "GLOOM", "VILEPLUME"],
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
    "ODDISH"      : ["ODDISH", "GLOOM", "VILEPLUME"],
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
    "JYNX"        : ["JYNX"],
    "MR_MIME"     : ["MR_MIME"],
    "PINSIR"      : ["PINSIR"],
    "TAUROS"      : ["TAUROS"],
    "MAGIKARP"    : ["MAGIKARP", "GYARADOS"],
    "EEVEE"       : ["EEVEE"],
    "DITTO"       : ["DITTO"],
    "LAPRAS"      : ["LAPRAS"],
    "PORYGON"     : ["PORYGON"],
    "SNORLAX"     : ["SNORLAX"],
    "OMANYTE"     : ["OMANYTE", "OMASTAR"],
    "KABUTO"      : ["KABUTO", "KABUTOPS"],
    "AERODACTYL"  : ["AERODACTYL"],
    "DRATINI"     : ["DRATINI", "DRAGONAIR", "DRAGONITE"]
}

new_moves_dex = {
    "EXEGGCUTE"   : '''    db 20,PSYWAVE
    db 25,REFLECT
    db 28,LEECH_SEED
    db 32,STUN_SPORE
    db 37,POISONPOWDER
    db 42,SOLARBEAM
    db 48,SLEEP_POWDER
    db 0''',
    "GRIMER"      : '''    db 15,SLUDGE
    db 30,POISON_GAS
    db 33,MINIMIZE
    db 37,TOXIC
    db 42,HARDEN
    db 48,SCREECH
    db 55,ACID_ARMOR
    db 0''',
    "RHYHORN"     :'''    db 15,ROCK_SLIDE
    db 30,STOMP
    db 35,TAIL_WHIP
    db 40,FURY_ATTACK
    db 45,HORN_DRILL
    db 50,LEER
    db 55,TAKE_DOWN
    db 0''',
    "SHELLDER"   :'''    db 15,WATER_GUN
    db 18,SUPERSONIC
    db 23,CLAMP
    db 30,AURORA_BEAM
    db 39,LEER
    db 50,ICE_BEAM
    db 0''',
    "TANGELA"     :'''    db 15,VINE_WHIP
    db 29,ABSORB
    db 32,POISONPOWDER
    db 36,STUN_SPORE
    db 39,SLEEP_POWDER
    db 45,SLAM
    db 49,GROWTH
    db 0''',
    "PSYDUCK"     :'''    db 15,WATER_GUN
    db 28,TAIL_WHIP
    db 31,DISABLE
    db 36,CONFUSION
    db 43,FURY_SWIPES
    db 52,HYDRO_PUMP
    db 0''',
    "MAGMAR"      :'''    db 15,RAGE
    db 36,LEER
    db 39,CONFUSE_RAY
    db 43,FIRE_PUNCH
    db 48,SMOKESCREEN
    db 52,SMOG
    db 55,FLAMETHROWER
    db 0''',
    "ELECTABUZZ"  :'''    db 15,THUNDERSHOCK
    db 34,SWIFT
    db 37,SCREECH
    db 42,THUNDERPUNCH
    db 49,LIGHT_SCREEN
    db 54,THUNDER
    db 0''',
    "KOFFING"     :'''    db 24,SLUDGE
    db 37,SMOKESCREEN
    db 40,SELFDESTRUCT
    db 45,HAZE
    db 48,EXPLOSION
    db 0''',
    "SEEL"        :'''    db 15,WATER_GUN
    db 30,GROWL
    db 35,AURORA_BEAM
    db 40,REST
    db 45,TAKE_DOWN
    db 50,ICE_BEAM
    db 0''',
    "VENONAT"     :'''    db 15,CONFUSION
    db 24,POISONPOWDER
    db 27,LEECH_LIFE
    db 30,STUN_SPORE
    db 35,PSYBEAM
    db 38,SLEEP_POWDER
    db 43,PSYCHIC_M
    db 0''',
    "DRATINI"     :'''    db 10,THUNDER_WAVE
    db 15,WATER_GUN
    db 20,AGILITY
    db 30,SLAM
    db 40,DRAGON_RAGE
    db 50,HYPER_BEAM
    db 0''',
    "KABUTO"      :'''    db 15,WATER_GUN
    db 34,ABSORB
    db 39,SLASH
    db 44,LEER
    db 49,HYDRO_PUMP
    db 0''',
    "GOLDEEN"     :'''    db 15,WATER_GUN
    db 19,SUPERSONIC
    db 24,HORN_ATTACK
    db 30,FURY_ATTACK
    db 37,WATERFALL
    db 45,HORN_DRILL
    db 54,AGILITY
    db 0''',
    "AERODACTYL"  :'''    db 20,ROCK_THROW
    db 33,SUPERSONIC
    db 38,BITE
    db 45,TAKE_DOWN
    db 54,HYPER_BEAM
    db 0''',
    "MAGNEMITE"   :'''    db 15,THUNDERSHOCK
    db 21,SONICBOOM
    db 29,SUPERSONIC
    db 35,THUNDER_WAVE
    db 41,SWIFT
    db 47,SCREECH
    db 0'''
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

dir = os.path.join(os.getcwd(), 'pokered', 'engine', 'items')  # old rod encounters and the ghost Marowak
dir += '/items.asm'
files_list.append(dir)

dir = os.path.join(os.getcwd(), 'pokered', 'data')  # good rod encounters
dir += '/good_rod.asm'
files_list.append(dir)

dir = os.path.join(os.getcwd(), 'pokered', 'data')  # super rod encounters
dir += '/super_rod.asm'
files_list.append(dir)

dir = os.path.join(os.getcwd(), 'pokered', 'data')  # casino prize pokemon
dir += '/prizes.asm'
files_list.append(dir)
dir = os.path.join(os.getcwd(), 'pokered', 'data')
dir += '/prize_mon_levels.asm'
files_list.append(dir)

dir = os.path.join(os.getcwd(), 'pokered', 'data')  # trade pokemon
dir += '/trades.asm'
files_list.append(dir)

dir = os.path.join(os.getcwd(), 'pokered', 'scripts')  # Magikarp salesman
dir += '/mtmoonpokecenter.asm'
files_list.append(dir)

dir = os.path.join(os.getcwd(), 'pokered', 'constants')  # starters
dir += '/starter_mons.asm'
files_list.append(dir)

dir = os.path.join(os.getcwd(), 'pokered', 'engine', 'overworld') # fossils
dir += '/cinnabar_lab.asm'
files_list.append(dir)

# gift pokemon
dir = os.path.join(os.getcwd(), 'pokered', 'scripts')  # Eevee
dir += '/celadonmansion5.asm'
files_list.append(dir)
dir = os.path.join(os.getcwd(), 'pokered', 'scripts')  # Hitmonlee / Hitmonchan
dir += '/fightingdojo.asm'
files_list.append(dir)
dir = os.path.join(os.getcwd(), 'pokered', 'scripts')  # Snorlax
dir += '/route12.asm'
files_list.append(dir)
dir = os.path.join(os.getcwd(), 'pokered', 'scripts')  # Lapras
dir += '/silphco7.asm'
files_list.append(dir)

# overworld pokemon
dir = os.path.join(os.getcwd(), 'pokered', 'scripts')  # Snorlax
dir += '/route16.asm'
files_list.append(dir)
dir = os.path.join(os.getcwd(), 'pokered', 'data', 'mapObjects')  # powerplant Voltorbs / Electrodes
dir += '/powerplant.asm'
files_list.append(dir)

# A E S T H E T I C S
dir = os.path.join(os.getcwd(), 'pokered', 'data')  # title screen pokemon
dir += '/title_mons.asm'
files_list.append(dir)
dir = os.path.join(os.getcwd(), 'pokered', 'data')  # credits screen pokemon
dir += '/credit_mons.asm'
files_list.append(dir)

# this block does the actual data replacement in the asm files
for fl in files_list:
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

# this block edits the movesets of certain pokemon
dir = os.path.join(os.getcwd(), 'pokered', 'data')
dir += '/evos_moves.asm'
with open(dir) as f:
    content = f.read()
    out = open(dir, 'w')
    out_content = content
    for pogey in new_moves_dex:
        srx = re.search(';' + pogey + '\n(.*\n)*?;Learnset\n((\s*.*\n)*?\s*db 0)', out_content)
        out_content = re.sub( srx.group(2), new_moves_dex[pogey], out_content)
    out.write(out_content)
    out.close()

# gym leader shuffle starts here
class Brock(object):
    def __init__ (self, ordinal):
        self.name = "Brock"
        self.sprite = 'SPRITE_BLACK_HAIR_BOY_2'
        self.opp = 'BROCK'
        self.ordinal = ordinal
        self.ai_line = '\tdb 1,0    ; BROCK'
        self.move_list = [  "db 1,BIDE",
                            "db 1,ROCK_THROW",
                            "db 2,ROCK_SLIDE",
                            "db 2,ROCK_SLIDE",
                            "db 3,ROCK_SLIDE",
                            "db 3,ROCK_SLIDE",
                            "db 3,ROCK_SLIDE"]
        self.team = "BrockData:\n\tdb $FF,"        
        self.team_list = ["12,GEODUDE,14,ONIX,0",
                          "18,GRAVELER,21,ONIX,0",
                          "21,GRAVELER,18,AERODACTYL,24,ONIX,0",
                          "29,GOLEM,24,AERODACTYL,29,ONIX,0",
                          "37,OMANYTE,39,GOLEM,37,AERODACTYL,43,ONIX,0",
                          "38,OMASTAR,37,GOLEM,38,AERODACTYL,43,ONIX,0",
                          "42,OMASTAR,40,GOLEM,42,AERODACTYL,47,ONIX,0"]
        self.team += self.team_list[self.ordinal]

class Misty(object):
    def __init__ (self, ordinal):
        self.name = "Misty"
        self.sprite = 'SPRITE_BRUNETTE_GIRL'
        self.opp = 'MISTY'
        self.ordinal = ordinal
        self.ai_line = '\tdb 1,3,0  ; MISTY'
        self.move_list = [  "db 1,BUBBLE",
                            "db 1,BUBBLEBEAM",
                            "db 2,BUBBLEBEAM",
                            "db 2,BUBBLEBEAM",
                            "db 3,BUBBLEBEAM",
                            "db 3,BUBBLEBEAM",
                            "db 3,BUBBLEBEAM"]
        self.team = "MistyData:\n    db $FF,"
        self.team_list = ["12,PSYDUCK,14,STARYU,0",
                          "18,PSYDUCK,21,STARMIE,0",
                          "21,PSYDUCK,18,LAPRAS,24,STARMIE,0",
                          "29,GOLDUCK,24,LAPRAS,29,STARMIE,0",
                          "37,TENTACOOL,39,GOLDUCK,37,LAPRAS,43,STARMIE,0",
                          "38,TENTACRUEL,37,GOLDUCK,38,LAPRAS,43,STARMIE,0",
                          "42,TENTACRUEL,40,GOLDUCK,42,LAPRAS,47,STARMIE,0"]
        self.team += self.team_list[self.ordinal]

class Surge(object):
    def __init__ (self, ordinal):
        self.name = "LtSurge"
        self.sprite = 'SPRITE_ROCKER'
        self.opp = 'LT_SURGE'
        self.ordinal = ordinal
        self.ai_line = '\tdb 1,3,0  ; LT_SURGE'
        self.move_list = [  "db 1,THUNDERSHOCK",
                            "db 1,THUNDERBOLT",
                            "db 2,THUNDERBOLT",
                            "db 2,THUNDERBOLT",
                            "db 3,THUNDERBOLT",
                            "db 3,THUNDERBOLT",
                            "db 3,THUNDERBOLT"]
        self.team = "LtSurgeData:\n\tdb $FF,"
        self.team_list = ["12,VOLTORB,14,PIKACHU,0",
                          "18,VOLTORB,21,RAICHU,0",
                          "21,VOLTORB,18,ELECTABUZZ,24,RAICHU,0",
                          "29,ELECTRODE,24,ELECTABUZZ,29,RAICHU,0",
                          "37,MAGNEMITE,39,ELECTRODE,37,ELECTABUZZ,43,RAICHU,0",
                          "38,MAGNETON,37,ELECTRODE,38,ELECTABUZZ,43,RAICHU,0",
                          "42,MAGNETON,40,ELECTRODE,42,ELECTABUZZ,47,RAICHU,0"]
        self.team += self.team_list[self.ordinal]

class Erika(object):
    def __init__ (self, ordinal):
        self.name = "Erika"
        self.sprite = 'SPRITE_ERIKA'
        self.opp = 'ERIKA'
        self.ordinal = ordinal
        self.ai_line = '\tdb 1,3,0  ; ERIKA'
        self.move_list = [  "db 1,MEGA_DRAIN",
                            "db 1,MEGA_DRAIN",
                            "db 2,MEGA_DRAIN",
                            "db 2,MEGA_DRAIN",
                            "db 3,MEGA_DRAIN",
                            "db 3,MEGA_DRAIN",
                            "db 3,MEGA_DRAIN"]
        self.team = "ErikaData:\n    db $FF,"
        self.team_list = ["12,BELLSPROUT,14,ODDISH,0",
                          "18,WEEPINBELL,21,GLOOM,0",
                          "21,WEEPINBELL,18,TANGELA,24,VILEPLUME,0",
                          "29,VICTREEBEL,24,TANGELA,29,VILEPLUME,0",
                          "37,EXEGGCUTE,39,VICTREEBEL,37,TANGELA,43,VILEPLUME,0",
                          "38,EXEGGUTOR,37,VICTREEBEL,38,TANGELA,43,VILEPLUME,0",
                          "42,EXEGGUTOR,40,VICTREEBEL,42,TANGELA,47,VILEPLUME,0"]
        self.team += self.team_list[self.ordinal]

class Koga(object):
    def __init__ (self, ordinal):
        self.name = "Koga"
        self.sprite = 'SPRITE_BLACKBELT'
        self.opp = 'KOGA'
        self.ordinal = ordinal
        self.ai_line = '\tdb 1,3,0  ; KOGA'
        self.move_list = [  "db 1,TOXIC",
                            "db 1,TOXIC",
                            "db 2,TOXIC",
                            "db 2,TOXIC",
                            "db 3,TOXIC",
                            "db 3,TOXIC",
                            "db 3,TOXIC"]
        self.team = "KogaData:\n    db $FF,"
        self.team_list = ["12,GRIMER,14,KOFFING,0",
                          "18,GRIMER,21,WEEZING,0",
                          "21,GRIMER,18,GOLBAT,24,WEEZING,0",
                          "29,MUK,24,GOLBAT,29,WEEZING,0",
                          "37,NIDORINO,39,MUK,37,GOLBAT,43,WEEZING,0",
                          "38,NIDOKING,37,MUK,38,GOLBAT,43,WEEZING,0",
                          "42,NIDOKING,40,MUK,42,GOLBAT,47,WEEZING,0"]
        self.team += self.team_list[self.ordinal]

class Sabrina(object):
    def __init__ (self, ordinal):
        self.name = "Sabrina"
        self.sprite = 'SPRITE_GIRL'
        self.opp = 'SABRINA'
        self.ordinal = ordinal
        self.ai_line = '\tdb 1,3,0  ; BLAINE'
        self.move_list = [  "db 1,PSYWAVE",
                            "db 1,PSYWAVE",
                            "db 2,PSYWAVE",
                            "db 2,PSYWAVE",
                            "db 3,PSYWAVE",
                            "db 3,PSYWAVE",
                            "db 3,PSYWAVE"]
        self.team = "SabrinaData:\n    db $FF,"
        self.team_list = ["12,VENONAT,14,KADABRA,0",
                          "18,VENONAT,21,KADABRA,0",
                          "21,VENONAT,18,MR_MIME,24,KADABRA,0",
                          "29,VENOMOTH,24,MR_MIME,29,ALAKAZAM,0",
                          "37,SLOWPOKE,39,MR_MIME,37,VENOMOTH,43,ALAKAZAM,0",
                          "38,SLOWBRO,37,MR_MIME,38,VENOMOTH,43,ALAKAZAM,0",
                          "42,SLOWBRO,40,MR_MIME,42,VENOMOTH,47,ALAKAZAM,0"]
        self.team += self.team_list[self.ordinal]

class Blaine(object):
    def __init__ (self, ordinal):
        self.name = "Blaine"
        self.sprite = 'SPRITE_FAT_BALD_GUY'
        self.opp = 'BLAINE'
        self.ordinal = ordinal
        self.ai_line = '\tdb 1,3,0  ; SABRINA'
        self.move_list = [  "db 1,EMBER",
                            "db 1,FLAMETHROWER",
                            "db 2,FLAMETHROWER",
                            "db 2,FIRE_BLAST",
                            "db 3,FIRE_BLAST",
                            "db 3,FIRE_BLAST",
                            "db 3,FIRE_BLAST"]
        self.team = "BlaineData:\n    db $FF,"
        self.team_list = ["12,PONYTA,14,GROWLITHE,0",
                          "18,PONYTA,21,ARCANINE,0",
                          "21,PONYTA,18,MAGMAR,24,ARCANINE,0",
                          "29,RAPIDASH,24,MAGMAR,29,ARCANINE,0",
                          "37,VULPIX,39,RAPIDASH,37,MAGMAR,43,ARCANINE,0",
                          "38,NINETALES,37,RAPIDASH,38,MAGMAR,43,ARCANINE,0",
                          "42,NINETALES,40,MAGMAR,42,RAPIDASH,47,ARCANINE,0"]
        self.team += self.team_list[self.ordinal]

# shuffles the gym leader order
gyms = [0, 1, 2, 3, 4, 5, 6]
shuffle(gyms)
leaders = [Brock(gyms[0]), Misty(gyms[1]), Surge(gyms[2]), Erika(gyms[3]), Koga(gyms[4]), Sabrina(gyms[5]), Blaine(gyms[6])]
leaders.sort(key=lambda x: x.ordinal)

# rewrites the party data for each leader
dir = os.path.join(os.getcwd(), 'pokered', 'data')
dir += '/trainer_parties.asm'
for leader in leaders:
    with open(dir) as f:
        content = f.read()
        out = open(dir, 'w')
        out_content = re.sub( leader.name+'Data.*\n.*0', leader.team, content)
        out.write(out_content)
        out.close()

# swaps out the map sprites and encounter data for each gym
city_list = ['/pewtergym.asm', '/ceruleangym.asm', '/vermiliongym.asm', 
             '/celadongym.asm', '/fuchsiagym.asm', '/saffrongym.asm', '/cinnabargym.asm']
dir = os.path.join(os.getcwd(), 'pokered', 'data', 'mapObjects')
for city in range(len(city_list)):
    temp_dir = dir + city_list[city]
    leader = leaders[city]
    with open(temp_dir) as f:
        content = f.read()
        out = open(temp_dir, 'w')
        out_content = re.sub( 'object .*?\,', 'object ' + leader.sprite + ',', content, 1)
        out_content = re.sub( 'OPP_.*,', 'OPP_' + leader.opp + ',', out_content, 1)
        out.write(out_content)
        out.close()

# swaps around the special trainer moves
new_moves = ''
for leader in leaders:
    new_moves += ('\t' + leader.move_list[leader.ordinal] + '\n')
dir = os.path.join(os.getcwd(), 'pokered', 'data')
dir += '/trainer_moves.asm'
with open(dir) as f:
    content = f.read()
    out = open(dir, 'w')
    out_content = re.sub('(\tdb \d\,.*\n){7}', new_moves, content)
    out.write(out_content)
    out.close()

# swaps around the ai
dir = os.path.join(os.getcwd(), 'pokered', 'engine', 'battle')
dir += '/trainer_ai.asm'
new_ais = ''  # gotta build out the new_ais string
for leader in leaders:
    new_ais += (leader.ai_line + '\n')
og_ais = ''
with open(dir) as f:  # gotta build out the og_ais string
    content = f.read()
    srx = re.search('db.*BRUNO.*\n(.*\n)(.*\n)(.*\n)(.*\n)(.*\n)(.*\n)(.*\n)', content)
    for g in srx.groups():
        og_ais += g
with open(dir) as f:
    content = f.read()
    out = open(dir, 'w')
    out_content = re.sub( og_ais, new_ais, content)
    out.write(out_content)
    out.close()



# # gym leader stuff to consider:
#     # text stuff:
#         # pokered/scripts/pewtergym.asm
#             # 'Gym1LeaderName:\n\tdb "BROCK@"'
#         # in the same vein, probably pokered/scripts/pewtercity.asm for the sign outside the gym
#     # TM stuff (for all gyms, not just pewter):
#         # pokered/scripts/pewtergym
#         # etc
#     # dialog:
#         # pokered/text/maps/pewter_gym_1.asm
#         # pokered/text/maps/pewter_gym_2.asm
#         # pokered/text/maps/cerulean_gym.asm
#         # etc

