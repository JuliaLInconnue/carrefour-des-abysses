python early:


    class Achievement(NoRollback):
        def __init__(self, name='', image='', message='', priority=None, **kwargs):
            ## The name of the achievement.
            self.name = name

            ## The image of the achievement.
            if image == '':
                ## If image is None, a default image will be used.
                self.image = Transform('gui/trophy_icon.webp', fit='contain')
            else:
                self.image = Transform(image, fit='contain')

            ## The message associated with the achievement.
            self.message = message

            ## Set the priority of the achievement.
            ##            None = default (greyed out and can see the name and description of the achievement.)
            ##        'hidden' = Achievements with this tag will be displayed as 'hidden'.
            ##      'platinum' = The final achievement to be granted once all other achievements have been granted.
            self.priority = priority

        def __eq__(self, value):
            ## Since we are using a persistent list we need to do an equality check.
            ## Below we are simply checking 'self.name == value.name, self.message == value.message'
            return all((self.name == value.name, self.message == value.message))

        def add(trophy):
            ## Add/Grant Trophies/Achievements to the list.
            ## As a standard python expression  ::  Achievement.add( <trophy> )
            ## As a screen action  ::  Function( Achievement.add, <trophy> )
            if not achievement.has(trophy.name):
                achievement.grant(trophy.name)
                store.achievement_is_done = False
                store.achievement_notification_timer = 3.0
                store.achievement_notification_list.append(trophy)

            if trophy not in persistent.my_achievements:
                ## New acheievements will appear first in the list.
                persistent.my_achievements.insert(0, trophy)
            achievement.sync()

        def purge(self):
            ## This will clear the achievements AND persistent list.
            ## As a standard python expression  ::  achievements.purge()
            ## As a screen action  ::  Function( achievements.purge )
            achievement.clear_all()
            persistent.my_achievements.clear()


## DO NOT TOUCH/REUSE/CHANGE THIS AT ANY TIME!
## To clear this list use ::  achievements.purge()
default persistent.my_achievements = []
default achievements = Achievement()

init python:

    ## Note - This has not been implemented to work with Steam.
    ##        You'll have to work that out on your own if you want it to work with steam.
    ##        I have left some Steam stuff in place, but these haven't been elaborated upon.
    achievement.steam_position = "bottom right"

    achievement_name = {

        ## -------------------------- IMPORTANT (1) --------------------------
        ## 
        ## How to set up achievements
        ## "achievement_key": Achievement(name=_("Name of Achievement"), message=_("Description"), image='<image_path_here>', priority='<type>'),

        ## -------------------------- IMPORTANT (2) --------------------------
        ## Note: If you decide to add/amend any achievement's data long after the game has started or
        ##       an achievement has been granted you will have to do a full reset of the game for those
        ##       changes to be reflected. I.e. Delete persistent data.

        ## -------------------------- EXAMPLES -------------------------- 

        "nobitches": Achievement(name=_("No Bitches"), message=_("Joue avec la RNG"), image='gui/trophy_icon.webp', priority=None),
        "Disconnected": Achievement(name=_("Hard Reboot"), message=_("Couper la connexion"), image='gui/trophy_icon.webp', priority=None),
        "techdimanche": Achievement(name=_("Technicien du dimanche"), message=_("Débrancher et rebrancher est parfois inutile"), image='gui/trophy_icon.webp', priority=None),
        "codedate": Achievement(name=_("Autopsie"), message=_("Déduit la date de fin du monde"), image='gui/trophy_icon.webp', priority=None),
        "doxxed": Achievement(name=_("Astronogeeked"), message=_("S'est fait doxxé pour \"harcèlement\" présumé"), image='gui/trophy_icon.webp', priority=None),
        "brainrot": Achievement(name=_("Couple Shitposter"), message=_("Est la deuxième face de la pièce de résistance"), image='gui/trophy_icon.webp', priority=None),
        "vétéran": Achievement(name=_("vétéran"), message=_("Sort des refs de 2018, se qualifie sous le reigne d'ikhatuni 3.15"), image='gui/trophy_icon.webp', priority=None),
        "TeamSweep": Achievement(name=_("Team Sweep forever"), message=_("Est un.e artiste exceptionnel.le"), image='gui/trophy_icon.webp', priority=None),
        "Inception": Achievement(name=_("Inception"), message=_("Est rentré dans l'écran de l'écran"), image='gui/trophy_icon.webp', priority=None),
        "Jubreakdownadmin": Achievement(name=_("Administrateurs ?"), message=_("A compris qui étaient les administrateurs"), image='gui/trophy_icon.webp', priority=None),
        "fnaf 6": Achievement(name=_("FFPS"), message=_("Joue encore avec la RNG"), image='gui/trophy_icon.webp', priority=None),
        "Integrité Journalistique": Achievement(name=_("Integrité Journalistique"), message=_("Refuse de divulguer ses sources sensibles"), image='gui/trophy_icon.webp', priority=None),
        "Oiseau bleu": Achievement(name=_("Oiseau bleu"), message=_("Oui Valentin, le libre arbitre est une illusion"), image='gui/trophy_icon.webp', priority=None),
        "Bad Mulch": Achievement(name=_("Bad Mulch"), message=_("Ressasse la possible victoire de la gauche en 2022"), image='gui/trophy_icon.webp', priority=None),
        "pacrel": Achievement(name=_("L'orphelin"), message=_("A commencé à lire l'histoire de Julien Pacrel"), image='gui/trophy_icon.webp', priority=None),
        "Picombre": Achievement(name=_("Détermination flamboyante"), message=_("A résisté au premier pic d'ombre d'une anomalie surpuissante contre toute attente"), image='gui/trophy_icon.webp', priority=None),
        "Douceur": Achievement(name=_("Pacrel FailRP"), message=_("Persiste dans sa douceur avec les portes"), image='gui/trophy_icon.webp', priority=None),
        "deez": Achievement(name=_("Deez nuts"), message=_("A fait une blague pas tip-top face à X"), image='gui/trophy_icon.webp', priority=None),
        "idle": Achievement(name=_("Transports en commun"), message=_("A traversé un trajet en train moyen"), image='gui/trophy_icon.webp', priority=None),

        ## The prio, means that the achievement will be displayed greyed-out before it is granted (or achieved).
        ## I use these terms to describe the types of achievements;
        ##            None = default (greyed out and can see the name and description of the achievement.)
        ##        'hidden' = Achievements with this label will be displayed as 'hidden'.
        ##      'platinum' = The final achievement to be granted once all other achievements have been granted.

        "sheep": Achievement(name=_("Sheep in wolf clothing"), message=_("Usurpe une identité sans réfléchir et en subit les conséquences"), image='gui/trophy_icon.webp', priority='hidden'),
        "delete": Achievement(name=_("Mauvaise manip'"), message=_("A effacé le monde tel qu'on le connait"), image='gui/trophy_icon.webp', priority='hidden'),
        "white": Achievement(name=_("Perte de soi"), message=_("A transcendé son enveloppe corporelle"), image='gui/trophy_icon.webp', priority='hidden'),
        "antifa": Achievement(name=_("Rhinocéros"), message=_("A résumé quatres livres en un"), image='gui/trophy_icon.webp', priority='hidden'),
        "tuedansloeuf": Achievement(name=_("Tué dans l'oeuf"), message=_("Est tombé dans l'emprise d'Edmes"), image='gui/trophy_icon.webp', priority='hidden'),
        "Inconnu": Achievement(name=_("Plongée dans l'Inconnu"), message=_("A démasqué le véritable antagoniste d'Histoire Multiple"), image='gui/trophy_icon.webp', priority='hidden'),



        "archive": Achievement(name=_("L'Archiviste"), message=_("A tout fait, ou du moins pour l'instant"), image='gui/trophy_icon.webp', priority='platinum'),

        ## More of this is explained in 'achievement_screen.rpy'.

    }

    ## Here we are simply registering the achievements.
    ## This is solely for backend use.
    for k, v in achievement_name.items():
        achievement.register(v.name)

