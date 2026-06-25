init -1 python:
    # Beep boop les sons de discussion du jeu
    def typewriter_voice(event, interact=True, **kwargs):
        if not interact:
            return

        if event == "show_done":
            renpy.sound.play("beeps.ogg", loop = True)
            store.piplet = "show_done"
        elif event == "slow_done":
            renpy.sound.stop()
            store.piplet = "slow_done"
    def fem_voice(event, interact=True, **kwargs):
        if not interact:
            return

        if event == "show_done":
            renpy.sound.play("voice3.ogg", loop = True)
            store.piplet = "show_done"
        elif event == "slow_done":
            renpy.sound.stop()
            store.piplet = "slow_done"
    def masc_voice(event, interact=True, **kwargs):
        if not interact:
            return

        if event == "show_done":
            renpy.sound.play("voice1.ogg", loop = True)
            store.piplet = "show_done"
        elif event == "slow_done":
            renpy.sound.stop()
            store.piplet = "slow_done"
    def andro_voice(event, interact=True, **kwargs):
        if not interact:
            return

        if event == "show_done":
            renpy.sound.play("voice2.ogg", loop = True)
            store.piplet = "show_done"
        elif event == "slow_done":
            renpy.sound.stop()
            store.piplet = "slow_done"
    # Flish flash de quoi parler
    import time
    store.speaking = None
    def _lipsync(st, at, perso, clignement, *frames):
        if store.speaking != perso :
            cligne = st % 3
            if clignement and renpy.loadable(clignement):
                if cligne >= 2.8 :
                    return clignement, 3-cligne
                else :
                    return frames[0], 2.8-cligne
            else:
                return frames[0], None
        else :
            frame = int(st/0.15)
            return frames[frame % len(frames)], 0.15 - (st % 0.15)

    def speaker_callback(perso, event, interact = True, **kwargs):
        if not interact : 
            return
        if event == "show_done":
            store.speaking = perso
        elif event == "slow_done":
            store.speaking = None
    store.speaker = renpy.curry(speaker_callback)

    def AnImage(chemin): 
        def chemins(st, at):
            special = chemin.replace ("[today_event]", store.today_event)
            original = chemin.replace("[today_event]", "")
            if renpy.loadable ("images/"+special):
                return Image("images/" + special), 1
            else :
                if renpy.loadable ("images/"+original) : 
                    return Image("images/" + original), 1
                else :
                    return Null(), None
        return DynamicDisplayable(chemins)

        

# Personnages du jeu
    # Narrateur
define narrator = Character("", what_color = "#ff7700",callback = typewriter_voice)
    # Joueureuse
define p = Character("[name]", color="#3f3f3f", callback = [andro_voice, speaker("p")])
define A = Character("Th3_4rch1v1st", color="#3f3f3f", callback = andro_voice)
    # Personnage inconnu
define HUH = Character("???", color="#111111", callback = andro_voice)
    # Créateurices
define I = Character(_('Julia - L\'Inconnue - X'), color="#003e9c", callback = [fem_voice,speaker("I")])
define IXY = Character(_('Julia - L\'Inconnue - XY'), color="#003e9c", callback = [fem_voice,speaker("IXY")])
define IIG = Character(_("Julien - L'Inconnu - Y - Ink Guy"), color="#00023f", callback = [masc_voice, speaker("IIG")])
define IIGHUH = Character("???", color="#111111", callback = [masc_voice, speaker("IIG")])
define LJDV = Character(_("La Joie de Vivre - La Phoenix"), color = "#602500", callback = [fem_voice,speaker("LJDV")])
define Ajai = Character(_("PowarT - Le Poisson"), color = "#004e29", callback = [masc_voice, speaker("Ajai")])
define clem = Character(_("Charasime - La Clown"), color = "#590000", callback = [fem_voice,speaker("clem")])
define Administrateur = Character(_('Administrateur'), color = "#000000", callback = masc_voice)
define ikha = Character(_("Ikhatuni - L'Artificier"), color = "#000000", callback = masc_voice)
define lemekivi = Character(_("Lemekivi - La Bête"), color = "#000000", callback = masc_voice)
define jeff_wooden = Character(_("Jeff Wooden - L'Ingénieur"), color = "#000000", callback = masc_voice)
define palirus = Character(_("Palirus - Le Fantôme"), color = "#000000", callback = masc_voice)
define emicrea = Character(_("Emilie - La Sorcière"), color = "#000000", callback = fem_voice)
define owo = Character(_("OwOIWonderWhatsThis - L'Ours"), color = "#000000", callback = fem_voice)
define hariboo = Character(_("Hariboo - La Renarde"), color = "#000000", callback = fem_voice)
define julie = Character(_("Julie - La Vigneronne"), color = "#000000", callback = fem_voice)
define manuel = Character(_("Manuel - Le Décripteur"), color = "#000000", callback = masc_voice)
define flo = Character(_("Florian - Le Statisticien"), who_color = "#95ff91", what_color = "#00ff15", window_background = "gui/textbox_terminal.webp", callback = masc_voice)
define doubt = Character(_('Doubt - La Somnambule'), color="#9c0000", callback = [fem_voice,speaker("doubt")])
define bodias = Character(_("Bodias - Le Rhinocéros"), color="#00023f", callback = [masc_voice, speaker("bodias")])

    # Personnages
define Edmes = Character(_("Edmes - L'Anomalie"), color="#680000", callback = [masc_voice, speaker("Edmes")])
define Pacrel = Character("Julien Pacrel", color = "#727272", callback = masc_voice)
define Ilona = Character("Ilona Durand", color = "#005126", callback = fem_voice)
define Miclordes = Character("Miclordes", color = "#006076", callback = fem_voice)
define julien = Character(_("Julien le lapin"), color = "#000000", callback = andro_voice)
define ajai = Character("Ajai Krisei", color = "#000000", callback = masc_voice)
define darisa = Character("Darisa Dangmon", color = "#000000", callback = andro_voice)
define klarsen = Character("Klarsen Maken", color = "#000000", callback = [fem_voice, speaker ("klarsen")])
define thera = Character("Thera Maken", color = "#000000", callback = masc_voice)
define marie = Character("Marie Maken", color = "#000000", callback = fem_voice)
define solrys = Character("Solrys Maken", color = "#000000", callback = masc_voice)
define jf = Character("Jean Fraques", color = "#000000", callback = [masc_voice, speaker("jf")])
define michel = Character(_("Michel Ledisparu "), color = "#000000", callback = masc_voice)
define roger = Character("Roger Ranger", color = "#000000", callback = masc_voice)
define greti = Character(_("Greti"), color = "#000000", callback = fem_voice)
define azcass = Character(_("Azcass"), color = "#000000", callback = masc_voice)
define emilap = Character(_("Emilie la lapine"), color = "#000000", callback = andro_voice)
define amelia = Character("Amelia", color = "#000000", callback = andro_voice)
define dlc = Character(_("Jean-Jacques Delacordière"), color = "#000000", callback = masc_voice)
define z = Character("Z", color = "#000000", callback = [masc_voice, speaker("Z")])
define kyo = Character ("Kyono Kojo", color = "#535353", callback = [masc_voice, speaker("kyo")])
define juge =  Character ("Juge", color = "#000000", callback = [masc_voice, speaker("juge")])
define eight = Character ("Eight", color = "#120c88", callback = [masc_voice, speaker("eight")])