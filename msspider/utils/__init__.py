from .maple_variables import *
from .helper import *
from .loggers import *

M = {}

Source_Links = {
    "EXP": "https://strategywiki.org/wiki/MapleStory/EXP_and_Pet_Closeness",
    "Starforce": "https://strategywiki.org/wiki/MapleStory/Spell_Trace_and_Star_Force",
    "Spell Trace": "https://strategywiki.org/wiki/MapleStory/Spell_Trace_and_Star_Force",
    "Flames": "https://strategywiki.org/wiki/MapleStory/Bonus_Stats",
    "Maple Union": "https://strategywiki.org/wiki/MapleStory/Maple_Union",
    "Hyper Stat": "https://strategywiki.org/wiki/MapleStory/Hyper_Stats",
    "Monster Life": "https://strategywiki.org/wiki/MapleStory/Monster_Life",
    "Potential": "https://strategywiki.org/wiki/MapleStory/Potential_System",
    "Armor": "https://maplestory.fandom.com/wiki/Equipment",
    "Weapon": "https://maplestory.fandom.com/wiki/Equipment",
    "Secondary": "https://maplestory.fandom.com/wiki/Equipment",
}

Allowed_Domains = [
    "strategywiki.org/wiki",
    "maplestory.fandom.com/wiki",
]

Data_Categories = ["Stat", "Equips", "Content"]


def Link_Compile(spider_tag):
    if spider_tag in Source_Links:
        return Source_Links[spider_tag]
    else:
        raise Exception("Invalid Spider tag")
