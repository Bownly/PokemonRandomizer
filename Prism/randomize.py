import codecs
import os
import sys
from random import randint

famlist1 = [
    ["VOLBEAT"],
    ["ILLUMISE"],
    ["HITMONLEE"],
    ["HITMONCHAN"],
    ["HITMONTOP"],
    ["KANGASKHAN"],
    ["LUNATONE"],
    ["SOLROCK"],
    ["SABLEYE"],
    ["SPIRITOMB"],
    ["DITTO"],
    ["SNORLAX"],
    ["TORKOAL"],
    ["MAWILE"],
    ["RELICANTH"],
    ["ABSOL"],
    ["CARNIVINE"]
]
famlist2 = [
    ["SNORUNT", "GLALIE"],
    ["GLIGAR", "GLISCOR"],
    ["TAILLOW", "SWELLOW"],
    ["SENTRET", "FURRET"],
    ["CACNEA", "CACTURNE"],
    ["JIGGLYPUFF", "WIGGLYTUFF"],
    ["PARAS", "PARASECT"],
    ["NATU", "XATU"],
    ["BRONZOR", "BRONZONG"],
    ["YANMA", "YANMEGA"],
    ["FEEBAS", "MILOTIC"],
    ["SLOWPOKE", "SLOWKING"],
    ["TEDDIURSA", "URSARING"],
    ["ONIX", "STEELIX"],
    ["VENONAT", "VENOMOTH"],
    ["SKORUPI", "DRAPION"],
    ["SPINARAK", "ARIADOS"],
    ["SCYTHER", "SCIZOR"],
    ["KOFFING", "WEEZING"],
    ["MAGIKARP", "GYARADOS"],
    ["MISDREAVUS", "MISMAGIUS"],
    ["CHANSEY", "BLISSEY"],
    ["PHANPY", "DONPHAN"],
    ["MAKUHITA", "HARIYAMA"],
    ["PINECO", "FORRETRESS"],
    ["EXEGGCUTE", "EXEGGUTOR"],
    ["MARILL", "AZUMARILL"],
    ["TENTACOOL", "TENTACRUEL"],
    ["DRIFLOON", "DRIFBLIM"],
    ["SHUPPET", "BANETTE"],
    ["DUSKULL", "DUSCLOPS"],
    ["CHINGLING", "CHIMECHO"],
    ["SPEAROW", "FEAROW"],
    ["WAILMER", "WAILORD"],
    ["SURSKIT", "MASQUERAIN"],
    ["SHROOMISH", "BRELOOM"],
    ["SWABLU", "ALTARIA"],
    ["TANGELA", "TANGROWTH"],
    ["GOLDEEN", "SEAKING"],
    ["SNEASEL", "WEAVILE"],
    ["RIOLU", "LUCARIO"],
    ["BUNEARY", "LOPUNNY"]
]
famlist3 = [
    ["BAGON", "SHELGON", "SALAMENCE"],
    ["GEODUDE", "GRAVELER", "GOLEM"],
    ["ZUBAT", "GOLBAT", "CROBAT"],
    ["PIDGEY","PIDGEOTTO", "PIDGEOT"],
    ["LOTAD", "LOMBRE", "LUDICOLO"],
    ["CATERPIE", "METAPOD", "BUTTERFREE"],
    ["RALTS", "KIRLIA", "GALLADE"],
    ["ABRA", "KADABRA", "ALAKAZAM"],
    ["EEVEE", "LEAFEON", "GLACEON"],
    ["MACHOP", "MACHOKE", "MACHAMP"],
    ["BELLSPROUT", "WEEPINBELL", "VICTREEBEL"],
    ["SWINUB", "PILOSWINE", "MAMOSWINE"],
    ["ARON", "LAIRON", "AGGRON"],
    ["WHISMUR", "LOUDRED", "EXPLOUD"],
    ["RHYHORN", "RHYDON", "RHYPERIOR"],
    ["GASTLY", "HAUNTER", "GENGAR"],
    ["TRAPINCH", "VIBRAVA", "FLYGON"],
    ["PORYGON", "PORYGON2", "PORYGONZ"],
    ["GIBLE", "GABITE", "GARCHOMP"],
    ["BELDUM", "METANG", "METAGROSS"]
]
fire_famlist2 = [
    ["VULPIX", "NINETALES"],
    ["HOUNDOUR", "HOUNDOOM"],
    ["SLUGMA", "MAGCARGO"],
    ["NUMEL", "CAMERUPT"],
    ["PONYTA", "RAPIDASH"],
    ["GROWLITHE", "ARCANINE"],
    ["MAGMAR", "MAGMORTAR"]
]
elec_famlist2 = [
    ["PIKACHU", "RAICHU"],
    ["ELECTRIKE", "MANECTRIC"],
    ["ELECTABUZZ", "ELECTIVIRE"],
    ["CHINCHOU", "LANTURN"]
]
elec_famlist3 = [
    ["SHINX", "LUXIO", "LUXRAY"],
    ["MAREEP", "FLAAFFY", "AMPHAROS"],
    ["MAGNEMITE", "MAGNETON", "MAGNEZONE"]
]

base_dex = {
    "BAGON"       : ["BAGON", "SHELGON", "SALAMENCE"],
    "SNORUNT"     : ["SNORUNT", "GLALIE"],
    "GEODUDE"     : ["GEODUDE", "GRAVELER", "GOLEM"],
    "ZUBAT"       : ["ZUBAT", "GOLBAT", "CROBAT"],
    "PIDGEY"      : ["PIDGEY","PIDGEOTTO", "PIDGEOT"],
    "LOTAD"       : ["LOTAD", "LOMBRE", "LUDICOLO"],
    "GLIGAR"      : ["GLIGAR", "GLISCOR"],
    "CATERPIE"    : ["CATERPIE", "METAPOD", "BUTTERFREE"],
    "TAILLOW"     : ["TAILLOW", "SWELLOW"],
    "RALTS"       : ["RALTS", "KIRLIA", "GALLADE"],
    "SENTRET"     : ["SENTRET", "FURRET"],
    "CACNEA"      : ["CACNEA", "CACTURNE"],
    "ABRA"        : ["ABRA", "KADABRA", "ALAKAZAM"],
    "JIGGLYPUFF"  : ["JIGGLYPUFF", "WIGGLYTUFF"],
    "PARAS"       : ["PARAS", "PARASECT"],
    "NATU"        : ["NATU", "XATU"],
    "BRONZOR"     : ["BRONZOR", "BRONZONG"],
    "YANMA"       : ["YANMA", "YANMEGA"],
    "EEVEE"       : ["EEVEE", "LEAFEON", "GLACEON"],
    "FEEBAS"      : ["FEEBAS", "MILOTIC"],
    "MACHOP"      : ["MACHOP", "MACHOKE", "MACHAMP"],
    "BELLSPROUT"  : ["BELLSPROUT", "WEEPINBELL", "VICTREEBEL"],
    "SLOWPOKE"    : ["SLOWPOKE", "SLOWKING"],
    "TEDDIURSA"   : ["TEDDIURSA", "URSARING"],
    "ONIX"        : ["ONIX", "STEELIX"],
    "VENONAT"     : ["VENONAT", "VENOMOTH"],
    "VOLBEAT"     : ["VOLBEAT"],
    "ILLUMISE"    : ["ILLUMISE"],
    "SKORUPI"     : ["SKORUPI", "DRAPION"],
    "SPINARAK"    : ["SPINARAK", "ARIADOS"],
    "SCYTHER"     : ["SCYTHER", "SCIZOR"],
    "HITMONLEE"   : ["HITMONLEE"],
    "HITMONCHAN"  : ["HITMONCHAN"],
    "HITMONTOP"   : ["HITMONTOP"],
    "KOFFING"     : ["KOFFING", "WEEZING"],
    "MAGIKARP"    : ["MAGIKARP", "GYARADOS"],
    "SWINUB"      : ["SWINUB", "PILOSWINE", "MAMOSWINE"],
    "MISDREAVUS"  : ["MISDREAVUS", "MISMAGIUS"],
    "CHANSEY"     : ["CHANSEY", "BLISSEY"],
    "KANGASKHAN"  : ["KANGASKHAN"],
    "ARON"        : ["ARON", "LAIRON", "AGGRON"],
    "WHISMUR"     : ["WHISMUR", "LOUDRED", "EXPLOUD"],
    "RHYHORN"     : ["RHYHORN", "RHYDON", "RHYPERIOR"],
    "PHANPY"      : ["PHANPY", "DONPHAN"],
    "LUNATONE"    : ["LUNATONE"],
    "SOLROCK"     : ["SOLROCK"],
    "MAKUHITA"    : ["MAKUHITA", "HARIYAMA"],
    "PINECO"      : ["PINECO", "FORRETRESS"],
    "EXEGGCUTE"   : ["EXEGGCUTE", "EXEGGUTOR"],
    "MARILL"      : ["MARILL", "AZUMARILL"],
    "TENTACOOL"   : ["TENTACOOL", "TENTACRUEL"],
    "DRIFLOON"    : ["DRIFLOON", "DRIFBLIM"],
    "SABLEYE"     : ["SABLEYE"],
    "SPIRITOMB"   : ["SPIRITOMB"],
    "SHUPPET"     : ["SHUPPET", "BANETTE"],
    "DUSKULL"     : ["DUSKULL", "DUSCLOPS"],
    "GASTLY"      : ["GASTLY", "HAUNTER", "GENGAR"],
    "CHINGLING"   : ["CHINGLING", "CHIMECHO"],
    "SPEAROW"     : ["SPEAROW", "FEAROW"],
    "TRAPINCH"    : ["TRAPINCH", "VIBRAVA", "FLYGON"],
    "WAILMER"     : ["WAILMER", "WAILORD"],
    "SURSKIT"     : ["SURSKIT", "MASQUERAIN"],
    "SHROOMISH"   : ["SHROOMISH", "BRELOOM"],
    "SWABLU"      : ["SWABLU", "ALTARIA"],
    "TANGELA"     : ["TANGELA", "TANGROWTH"],
    "GOLDEEN"     : ["GOLDEEN", "SEAKING"],
    "PORYGON"     : ["PORYGON", "PORYGON2", "PORYGONZ"],
    "GIBLE"       : ["GIBLE", "GABITE", "GARCHOMP"],
    "SNEASEL"     : ["SNEASEL", "WEAVILE"],
    "BELDUM"      : ["BELDUM", "METANG", "METAGROSS"],
    "DITTO"       : ["DITTO"],
    "SNORLAX"     : ["SNORLAX"],
    "TORKOAL"     : ["TORKOAL"],
    "MAWILE"      : ["MAWILE"],
    "RELICANTH"   : ["RELICANTH"],
    "ABSOL"       : ["ABSOL"],
    "CARNIVINE"   : ["CARNIVINE"],
    "RIOLU"       : ["RIOLU", "LUCARIO"],
    "BUNEARY"     : ["BUNEARY", "LOPUNNY"]
}
fire_base_dex = {
    "VULPIX"      : ["VULPIX", "NINETALES"],
    "HOUNDOUR"    : ["HOUNDOUR", "HOUNDOOM"],
    "SLUGMA"      : ["SLUGMA", "MAGCARGO"],
    "NUMEL"       : ["NUMEL", "CAMERUPT"],
    "PONYTA"      : ["PONYTA", "RAPIDASH"],
    "GROWLITHE"   : ["GROWLITHE", "ARCANINE"],
    "MAGMAR"      : ["MAGMAR", "MAGMORTAR"],
}
elec_base_dex = {
    "SHINX"       : ["SHINX", "LUXIO", "LUXRAY"],
    "MAREEP"      : ["MAREEP", "FLAAFFY", "AMPHAROS"],
    "PIKACHU"     : ["PIKACHU", "RAICHU"],
    "MAGNEMITE"   : ["MAGNEMITE", "MAGNETON", "MAGNEZONE"],
    "ELECTRIKE"   : ["ELECTRIKE", "MANECTRIC"],
    "ELECTABUZZ"  : ["ELECTABUZZ", "ELECTIVIRE"],
    "CHINCHOU"    : ["CHINCHOU", "LANTURN"],
}
end_dex = {}


# these blocks are in charge of determining how the pokemon get switched around
# majority of the pokemon
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

# fire pokemon
for pokemon in fire_base_dex:
    ogfam = fire_base_dex[pokemon]
    famsize = 2

    famlist = fire_famlist2
        
    newfam = famlist[randint(0, len(famlist)-1)]
    for i in range(famsize):
        end_dex[ogfam[i]] = (newfam[i])
    famlist.remove(newfam)
    
# elec pokemon
for pokemon in elec_base_dex:
    ogfam = elec_base_dex[pokemon]
    famsize = len(ogfam)

    if (famsize == 2):
        famlist = elec_famlist2
    elif (famsize == 3):
        famlist = elec_famlist3
        
    newfam = famlist[randint(0, len(famlist)-1)]
    for i in range(famsize):
        end_dex[ogfam[i]] = (newfam[i])
    famlist.remove(newfam)

# this block builds out the list of files that need editing
files_list = []
# wild locations
dir = os.path.join( os.getcwd(), 'source','data','wild')
for f in os.listdir(dir):
    if f.endswith(".asm"):
        files_list.append(dir + "/" + f)

# this block does the actual data replacement in the rom files
for fl in files_list:
    with open(fl) as f:
        content = [x.strip('\n') for x in f.readlines()]
        out_lines = []
        for line in content:
            new_line = ''
            for word in line.split():
                if word in end_dex:
                    line = line.replace(word, end_dex[word])
            out_lines.append(line)
        out = open(fl, 'w')
        out_content = "\n".join(out_lines)
        out.write(out_content)
        out.close()



