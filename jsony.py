import os
import glob
import json
from itertools import chain

outindex = "games_list.json"
outdir = "./gfiles/"
html5gamesin = "html5/"
rarchgamesin = "rarch/"
romdir = "roms/*"
flashgamesin = "flash/"

pregba = [".gba", ".gb", ".gbc"]
pregen = [".mdx", ".md", ".smd", ".gen", ".sms", ".gg", ".sg"]
prenes = [".nes", ".fds", ".unf", ".unif"]
pren64 = [".n64", ".v64", ".z64", ".ndd"]
presnes = [".smc", ".sfc", ".swc", ".fig"]

html5names = {"adarkroom": "A Dark Room", "asciispace": "ASCII Space", "blackholesquare": "Black Hole Square", "bounceback": "Bounce Back", "captaincallisto": "Captain Callisto", "chromaincident": "Chroma Incident", "chromedino": "Chrome Dino", "connect3": "Connect 3", "cookieclicker": "Cookie Clicker", "edgenotfound": "Edge not Found", "evilglitch": "Evil Glitch", "factoryballsforever": "Factory Balls Forever", "flappybird": "Flappy Bird", "geometrydash": "Geometry Dash", "ninjavsevilcorp": "Ninja vs Evilcorp", "pacman": "Pac-Man", "particleclicker": "Particle Clicker", "pushback": "Push Back", "radiusraid": "Radius Raid", "roadblocks": "Road Blocks", "run3": "Run 3", "sleepingbeauty": "Sleeping Beauty", "spacecompany": "Space Company", "spacegarden": "Space Garden", "spacehuggers": "Space Huggers", "themazeofspacegoblins": "The Maze of Space Goblins", "xx142-b2exe": "xx142-b2.exe"}

games_data = []

# Helper function to add game metadata to the list
def add_game(game_type, display_name, path, core=None):
    game_info = {
        "type": game_type,
        "name": display_name,
        "path": path
    }
    if core:
        game_info["core"] = core
    games_data.append(game_info)

# Process HTML5 games
html5_1 = next(os.walk(outdir + html5gamesin))[1]
add_game("HTML5", "webretro", outdir + rarchgamesin)
for game in html5_1:
    display_name = html5names.get(game, game.capitalize())
    add_game("HTML5", display_name, outdir + html5gamesin + game + "/")

# Process GBA games
gba_1 = list(chain.from_iterable([glob.glob(outdir + rarchgamesin + romdir + ext) for ext in pregba]))
add_game("GBA", "Upload ROM", outdir + rarchgamesin, "mgba")
for game in gba_1:
    game_name = os.path.splitext(os.path.basename(game))[0].capitalize()
    add_game("GBA", game_name, outdir + rarchgamesin + "?core=mgba&rom=" + os.path.basename(game))

# Process Genesis / Master System games
gen_1 = list(chain.from_iterable([glob.glob(outdir + rarchgamesin + romdir + ext) for ext in pregen]))
add_game("Genesis / Master System", "Upload ROM", outdir + rarchgamesin, "genesis_plus_gx")
for game in gen_1:
    game_name = os.path.splitext(os.path.basename(game))[0].capitalize()
    add_game("Genesis / Master System", game_name, outdir + rarchgamesin + "?core=genesis_plus_gx&rom=" + os.path.basename(game))

# Process N64 games
n64_1 = list(chain.from_iterable([glob.glob(outdir + rarchgamesin + romdir + ext) for ext in pren64]))
add_game("Nintendo 64", "Upload ROM", outdir + rarchgamesin, "mupen64plus_next")
for game in n64_1:
    game_name = os.path.splitext(os.path.basename(game))[0].capitalize()
    add_game("Nintendo 64", game_name, outdir + rarchgamesin + "?core=mupen64plus_next&rom=" + os.path.basename(game))

# Process NES games
nes_1 = list(chain.from_iterable([glob.glob(outdir + rarchgamesin + romdir + ext) for ext in prenes]))
add_game("NES", "Upload ROM", outdir + rarchgamesin, "nestopia")
for game in nes_1:
    game_name = os.path.splitext(os.path.basename(game))[0].capitalize()
    add_game("NES", game_name, outdir + rarchgamesin + "?core=nestopia&rom=" + os.path.basename(game))

# Process SNES games
snes_1 = list(chain.from_iterable([glob.glob(outdir + rarchgamesin + romdir + ext) for ext in presnes]))
add_game("Super Nintendo", "Upload ROM", outdir + rarchgamesin, "snes9x")
for game in snes_1:
    game_name = os.path.splitext(os.path.basename(game))[0].capitalize()
    add_game("Super Nintendo", game_name, outdir + rarchgamesin + "?core=snes9x&rom=" + os.path.basename(game))

# Process Flash games
flash_1 = ['1on1soccer.swf', '3dtanks.swf', 'abobosbigadventure.swf', 'achievementunlocked.swf', 'achievementunlocked2.swf', 'achievementunlocked3.swf', 'actionturnip.swf', 'adaran.swf', 'adrenaline.swf', 'americanracing1.swf', 'americanracing2.swf', 'arkandianrevenant.swf', 'armyofages.swf', 'awesomecars.swf', 'awesomeplanes.swf', 'battlepanic.swf', 'bloonsplayerpack2.swf', 'bloonsplayerpack3.swf', 'bloonsplayerpack4.swf', 'bloonsplayerpack5.swf', 'bloonstd1.swf', 'bloonstd3.swf', 'bloonstd4.swf', 'bloonstd5.swf', 'bobtherobber.swf', 'boombot2.swf', 'boxhead2play.swf', 'bubbletanks2.swf', 'bulletbill.swf', 'bullettimefighting.swf', 'burritobison.swf', 'burritobisonrevenge.swf', 'cactusmccoy.swf', 'cactusmccoy2.swf', 'cannonbasketball2.swf', 'cargobridge.swf', 'causality.swf', 'chibiknight.swf', 'clickerheroes.swf', 'computerbashing.swf', 'crushthecastle.swf', 'crushthecastle2.swf', 'cubefield.swf', 'cyclomaniacs2.swf', 'diggy.swf', 'donkeykong.swf', 'dontshootthepuppy.swf', 'doodledefender.swf', 'doom.swf', 'dragracing.swf', 'ducklife.swf', 'ducklife2.swf', 'ducklife3.swf', 'ducklife4.swf', 'earntodie.swf', 'earntodie2.swf', 'earntodiesuperwheel.swf', 'electricman2.swf', 'elephantquest.swf', 'epicbattlefantasy3.swf', 'epiccomboredux.swf', 'exitpath.swf', 'factoryballs.swf', 'factoryballs2.swf', 'factoryballs3.swf', 'factoryballs4.swf', 'fancypantsadventure.swf', 'fancypantsadventure2.swf', 'fancypantsadventure3.swf', 'flashflightsimulator.swf', 'flight.swf', 'fracuum.swf', 'freerider2.swf', 'getontop.swf', 'giveuprobot.swf', 'giveuprobot2.swf', 'hanger.swf', 'hanger2.swf', 'happywheels.swf', 'hobo.swf', 'hobo2.swf', 'hobo3.swf', 'hobo4.swf', 'hobo5.swf', 'hobo6.swf', 'hobo7.swf', 'houseofwolves.swf', 'interactivebuddy.swf', 'jacksmith.swf', 'jellytruck.swf', 'johnnyupgrade.swf', 'jumpix2.swf', 'knightmaretower.swf', 'learn2fly.swf', 'learn2fly2.swf', 'learn2fly3.swf', 'magnetface.swf', 'mariocombat.swf', 'marioracingtournament.swf', 'meatboy.swf', 'megamanprojectx.swf', 'metroidelements.swf', 'mineblocks.swf', 'minesweeper.swf', 'mirrorsedge.swf', 'moneymovers.swf', 'moneymovers3.swf', 'motherload.swf', 'motox3m.swf', 'multitask.swf', 'mutilateadoll2.swf', 'myangel.swf', 'nanotube.swf', 'newgroundsrumble.swf', 'ngame.swf', 'nitromemustdie.swf', 'nucleus.swf', 'nv2.swf', 'nyancatlostinspace.swf', 'offroaders.swf', 'onemanarmy2.swf', 'outofthisworld.swf', 'pacman.swf', 'pandemic.swf', 'pandemic2.swf', 'papalouie.swf', 'papalouie2.swf', 'papalouie3.swf', 'picosschool.swf', 'picosschool2.swf', 'pirates.swf', 'polarjump.swf', 'portal.swf', 'portal2d.swf', 'quadrobarreldefence.swf', 'qubeythecube.swf', 'qwop.swf', 'raftwars.swf', 'raftwars2.swf', 'raze.swf', 'redball.swf', 'redball2.swf', 'redball4.swf', 'redball4v2.swf', 'redball4v3.swf', 'redshift.swf', 'revenant2.swf', 'riddleschool1.swf', 'riddleschool2.swf', 'riddleschool3.swf', 'riddleschool4.swf', 'riddleschool5.swf', 'riddletransfer.swf', 'riddletransfer2.swf', 'run2.swf', 'run3.swf', 'saszombieassault3.swf', 'sentryknight.swf', 'shoppingcarthero3.swf', 'siftheads.swf', 'siftheads2.swf', 'siftheads3.swf', 'siftheads4.swf', 'siftheads5.swf', 'sniperassassin4.swf', 'sportsheadsfootball.swf', 'sportsheadsracing.swf', 'sportsheadstennis.swf', 'stickrpg.swf', 'stickrun2.swf', 'stickwar.swf', 'strikeforceheroes2.swf', 'strikeforcekittylaststand.swf', 'sugarsugar.swf', 'sugarsugar2.swf', 'sugarsugar3.swf', 'superd.swf', 'superfighters.swf', 'supermario63.swf', 'supermarioflash.swf', 'supermarioflash2.swf', 'supersmashflash.swf', 'swordsandsandals2.swf', 'tacticalassassin.swf', 'tanks.swf', 'tanktrouble.swf', 'tetris.swf', 'thebindingofisaac.swf', 'thegame.swf', 'theimpossiblequiz.swf', 'theimpossiblequiz2.swf', 'theworldshardestgame2.swf', 'thingthingarena.swf', 'thisistheonlylevel.swf', 'tosstheturtle.swf', 'truckloader4.swf', 'ultimateflashsonic.swf', 'ultimatetactics.swf', 'unrealflash.swf', 'vex.swf', 'vex2.swf', 'vex3.swf', 'warfare1917.swf', 'warfare1944.swf', 'warp.swf', 'xenos.swf', 'xtremecliffdiving.swf', 'yearofthesnake.swf', 'yuriusshouseofspooks.swf', 'zombiealienparasites.swf']
add_game("Flash", "Upload SWF", outdir + flashgamesin)
for game in flash_1:
    game_name = os.path.splitext(os.path.basename(game))[0].capitalize()
    add_game("Flash", game_name, outdir + flashgamesin + "?swf=" + os.path.basename(game))

# Write to JSON file
with open(outindex, "w") as json_file:
    json.dump(games_data, json_file, indent=4)

print("\nJSON Output Done!")
