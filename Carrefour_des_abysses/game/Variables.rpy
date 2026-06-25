#phrase d'intro

define fun = renpy.random.randint(40,40)
#1,len(splashtexts)
default projecteur = 1

#variables et codes
define piplet = ""
define code = '31122034'
define splash = renpy.random.randint(1,10)
define oversplash = renpy.random.randint(1,2)
define worldpick = renpy.random.randint(1,5)
default name  = "XDDCC"
default TriggerWarning = False
default off = False
default visite = False
default oob = False
default puni = False
default corrupt = False
default persistent.p0 = False
default persistent.p1 = False
default persistent.p2 = False
default persistent.p3 = False
default persistent.p4 = False
default persistent.LJDV0 = False
default persistent.LJDV1 = False
default persistent.Powart0 = False
default persistent.av = False
default conseil = 0
default inconnu = 0
default integrité = 0
default player = os.environ.get('username')
default inverted = False
default Inconnu = False
default complique = False
default expé = False
default rpg_path = os.path.join(config.basedir, "Carrefour des Abysses - RPG/Game.exe") 
default fond_tetris = 1
default tupin = False
default borne_noticed = False
default choc = True
default floscreenswitch = True

init -1 python:
    import datetime, time
    from datetime import date
    today_event = ""
    today = datetime.datetime.now().strftime('%y_%m-%d')
    if '10-31' in today:
        today_event = "_halloween"
    elif '04-01' in today:
        today_event = "_pwasson"
    elif "12-24" in today or "12-25" in today:
        today_event = "_krima"
    elif "12-31" in today or "01-01" in today:
        today_event = "_NY"
    elif "05-01" in today:
        today_event = "_Komrad"
    elif "02-14" in today:
        today_event = "_keur"
    elif "03-18" in today:
        today_event = "_patoche"
    elif "_03" in today or "_04" in today:
        today_event = "_egg"



