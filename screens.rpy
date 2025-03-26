

################################################################################
## Initialisation
################################################################################

init offset = -1


################################################################################
## Styles
################################################################################

style default:
    properties gui.text_properties()
    language gui.language

style input:
    properties gui.text_properties("input", accent=True)
    adjust_spacing False

style hyperlink_text:
    properties gui.text_properties("hyperlink", accent=True)
    hover_underline True

style gui_text:
    properties gui.text_properties("interface")


style button:
    properties gui.button_properties("button")

style button_text is gui_text:
    properties gui.text_properties("button")
    yalign 0.5


style label_text is gui_text:
    properties gui.text_properties("label", accent=True)

style prompt_text is gui_text:
    properties gui.text_properties("prompt")


style bar:
    ysize gui.bar_size
    left_bar Frame("gui/bar/left.png", gui.bar_borders, tile=gui.bar_tile)
    right_bar Frame("gui/bar/right.png", gui.bar_borders, tile=gui.bar_tile)

style vbar:
    xsize gui.bar_size
    top_bar Frame("gui/bar/top.png", gui.vbar_borders, tile=gui.bar_tile)
    bottom_bar Frame("gui/bar/bottom.png", gui.vbar_borders, tile=gui.bar_tile)

style scrollbar:
    ysize gui.scrollbar_size
    base_bar Frame("gui/scrollbar/horizontal_[prefix_]bar.png", gui.scrollbar_borders, tile=gui.scrollbar_tile)
    thumb Frame("gui/scrollbar/horizontal_[prefix_]thumb.png", gui.scrollbar_borders, tile=gui.scrollbar_tile)

style vscrollbar:
    xsize gui.scrollbar_size
    base_bar Frame("gui/scrollbar/vertical_[prefix_]bar.png", gui.vscrollbar_borders, tile=gui.scrollbar_tile)
    thumb Frame("gui/scrollbar/vertical_[prefix_]thumb.png", gui.vscrollbar_borders, tile=gui.scrollbar_tile)

style slider:
    ysize gui.slider_size
    base_bar Frame("gui/slider/horizontal_[prefix_]bar.png", gui.slider_borders, tile=gui.slider_tile)
    thumb "gui/slider/horizontal_[prefix_]thumb.png"

style vslider:
    xsize gui.slider_size
    base_bar Frame("gui/slider/vertical_[prefix_]bar.png", gui.vslider_borders, tile=gui.slider_tile)
    thumb "gui/slider/vertical_[prefix_]thumb.png"


style frame:
    padding gui.frame_borders.padding
    background Frame("gui/frame.png", gui.frame_borders, tile=gui.frame_tile)



################################################################################
## Écrans de jeu
################################################################################


## Écran des dialogues #########################################################
##
## L’écran des dialogues est utilisé pour afficher les dialogues du joueur. Il
## prend deux paramètres, who(qui) et what(quoi) qui sont respectivement le
## nom du personnage en train de parler et le texte à afficher. (Le paramètre
## who(qui) peut être None si aucun nom n’est donné.)
##
## Cet écran affiche le texte correspondant à what. Il peut également créer un
## texte avec le paramètre who et l’identifiant « window » est utilisé pour
## déterminer les styles à appliquer.
##
## https://www.renpy.org/doc/html/screen_special.html#say

screen say(who, what):
    style_prefix "say"

    window:
        id "window"

        if who is not None:

            window:
                id "namebox"
                style "namebox"
                text who id "who"

        text what id "what"


    ## Si il y a une side image, l'afficher au-dessus du texte. Ne pas
    ## l'afficher sur la version téléphone - pas assez de place.
    if not renpy.variant("small"):
        add SideImage() xalign 0.0 yalign 1.0


## Rendre la boîte du nom personnalisable à travers l'objet Character.
init python:
    config.character_id_prefixes.append('namebox')

style window is default
style say_label is default
style say_dialogue is default
style say_thought is say_dialogue

style namebox is default
style namebox_label is say_label


style window:
    xalign 0.5
    xfill True
    yalign gui.textbox_yalign
    ysize gui.textbox_height

    background Image("gui/textbox.png", xalign=0.5, yalign=1.0)

style namebox:
    xpos gui.name_xpos
    xanchor gui.name_xalign
    xsize gui.namebox_width
    ypos gui.name_ypos
    ysize gui.namebox_height

    background Frame("gui/namebox.png", gui.namebox_borders, tile=gui.namebox_tile, xalign=gui.name_xalign)
    padding gui.namebox_borders.padding

style say_label:
    properties gui.text_properties("name", accent=True)
    xalign gui.name_xalign
    yalign 0.5

style say_dialogue:
    properties gui.text_properties("dialogue")

    xpos gui.dialogue_xpos
    xsize gui.dialogue_width
    ypos gui.dialogue_ypos

    adjust_spacing False

## Écran de saisie #############################################################
##
## Cet écran est utilisé pour afficher renpy.input. Le paramètre prompt est
## utilisé pour passer le texte par défaut.
##
## Cet écran doit créer une entrée affichable avec l'id "input" pour accepter
## les différents paramètres.
##
## https://www.renpy.org/doc/html/screen_special.html#input

screen input(prompt):
    style_prefix "input"

    window:

        vbox:
            xanchor gui.dialogue_text_xalign
            xpos gui.dialogue_xpos
            xsize gui.dialogue_width
            ypos gui.dialogue_ypos

            text prompt style "input_prompt"
            input id "input"

style input_prompt is default

style input_prompt:
    xalign gui.dialogue_text_xalign
    properties gui.text_properties("input_prompt")

style input:
    xalign gui.dialogue_text_xalign
    xmaximum gui.dialogue_width


## Écran des choix #############################################################
##
## Cet écran est utilisé pour afficher les choix qui seront fait par le joueur
## dans le jeu. Le premier paramètre, items, est une liste d'objets contenant
## chacun des champs de texte et d'action.
##
## https://www.renpy.org/doc/html/screen_special.html#choice

screen choice(items):
    style_prefix "choice"

    vbox:
        for i in items:
            textbutton i.caption action i.action


style choice_vbox is vbox
style choice_button is button
style choice_button_text is button_text

style choice_vbox:
    xalign 0.5
    ypos 405
    yanchor 0.5

    spacing gui.choice_spacing

style choice_button is default:
    properties gui.button_properties("choice_button")

style choice_button_text is default:
    properties gui.text_properties("choice_button")


## Écran des menus rapides #####################################################
##
## Les menus rapides sont affichés dans le jeu pour permettre un accès rapide à
## certaines fonctions.

screen quick_menu():

    ## Assure qu'il apparaît au-dessus des autres screens.
    zorder 100

    if quick_menu:

        frame:
            xalign 0.5
            yalign 0.98
            hbox:
                style_prefix "quick"

                xalign 0.5
                yalign 0.99

                #textbutton _("Retour") action Rollback() -> Le bouton retour est désormais retiré, tes actes ont des conséquences :)
                textbutton _("Historique") action ShowMenu('history')
                textbutton _("Avance rapide") action Skip() alternate Skip(fast=True, confirm=True)
                textbutton _("Auto") action Preference("auto-forward", "toggle")
                textbutton _("Sauvegarder") action ShowMenu('save')
                textbutton _("Charger") action ShowMenu('load')
                textbutton _("option") action ShowMenu('preferences')



## Ce code garantit que le menu d’accès rapide sera affiché dans le jeu, tant
## que le joueur n’aura pas explicitement demandé à cacher l’interface.
init python:
    config.overlay_screens.append("quick_menu")

default quick_menu = True

style quick_button is default
style quick_button_text is button_text

style quick_button:
    properties gui.button_properties("quick_button")

style quick_button_text:
    properties gui.text_properties("quick_button")


################################################################################
## Screens du menu principal et du menu de jeu
################################################################################

## Écran de navigation #########################################################
##
## Cet écran est disponible dans le menu principal et dans le menu de jeu. Il
## fournit l’accès aux autres menus et permet le démarrage du jeu.

image logomin = "logomin.png"

screen navigation():

    vbox:
        style_prefix "navigation"

        xpos 0
        yalign 0.65

        spacing gui.navigation_spacing

        if main_menu:

            textbutton _("Nouvelle partie") action Start()

        else:

            textbutton _("Historique") action ShowMenu("history")

            textbutton _("Sauvegarde") action ShowMenu("save")

        textbutton _("Charger") action ShowMenu("load")

        textbutton _("Options") action ShowMenu("preferences")

        if _in_replay:

            textbutton _("Fin de la rediffusion") action EndReplay(confirm=True)

        elif not main_menu:

            textbutton _("Menu principal") action MainMenu()

        textbutton _("Extra") action ShowMenu("about")
        
        

        if renpy.variant("pc") or (renpy.variant("web") and not renpy.variant("mobile")):

            ## L'aide n’est ni nécessaire ni pertinente sur les appareils
            ## mobiles.
            textbutton _("Aide") action ShowMenu("help")

        if renpy.variant("pc"):

            ## Le bouton pour quitter est banni sur iOS et inutile sur Android
            ## et sur le Web.
            textbutton _("Quitter") action Quit(confirm=not main_menu)


style navigation_button is gui_button
style navigation_button_text is gui_button_text

style navigation_button:
    size_group "navigation"
    properties gui.button_properties("navigation_button")

style navigation_button_text:
    properties gui.text_properties("navigation_button")


## Écran du menu principal #####################################################
##
## Utilisé pour afficher le menu principal quand Ren'Py démarre.
##
## https://www.renpy.org/doc/html/screen_special.html#main-menu

screen main_menu():

    ## Ceci assure que tout autre screen de menu est remplacé.
    tag menu

    add gui.main_menu_background

    ## Cette frame vide obscurcit le menu principal.
    frame:
        style "main_menu_frame"

    ## L'instruction use inclut un autre écran à l'intérieur de celui-ci. Le
    ## vrai contenu du menu principal se trouve dans l'écran "navigation".
    use navigation

    if gui.show_name:

        vbox:
            style "main_menu_vbox"

            text "[config.name!t]":
                style "main_menu_title"

            text "[config.version]":
                style "main_menu_version"


style main_menu_frame is empty
style main_menu_vbox is vbox
style main_menu_text is gui_text
style main_menu_title is main_menu_text
style main_menu_version is main_menu_text

style main_menu_frame:
    xsize 420
    yfill True

    background "gui/overlay/main_menu.png"

style main_menu_vbox:
    xalign 1.0
    xoffset -30
    xmaximum 1200
    yalign 1.0
    yoffset -30

style main_menu_text:
    properties gui.text_properties("main_menu", accent=True)

style main_menu_title:
    properties gui.text_properties("title")
    outlines [ (absolute(5), "#d9f2ff", absolute(0), absolute(0)) ]

style main_menu_version:
    properties gui.text_properties("version")
    outlines [ (absolute(5), "#d9f2ff", absolute(0), absolute(0)) ]


## Écran du menu de jeu ########################################################
##
## Ceci présente la structure commune de base d'un écran du menu de jeu. Il est
## appelé en lui passant le titre de l'écran, et il affiche l'arrière-plan, le
## titre et la navigation.
##
## Le paramètre de défilement peut être None, ou "viewport" ou "vpgrid". Cet
## écran est destiné à être utilisé avec un ou plusieurs enfants, qui sont
## transclus (placés) à l'intérieur de l'écran.

screen game_menu(title, scroll=None, yinitial=0.0, spacing=0):

    style_prefix "game_menu"

    if main_menu:
        add gui.main_menu_background
    else:
        add gui.game_menu_background

    frame:
        style "game_menu_outer_frame"

        hbox:

            ## Réserve de l'expace pour la section de navigation.
            frame:
                style "game_menu_navigation_frame"

            frame:
                style "game_menu_content_frame"

                if scroll == "viewport":

                    viewport:
                        yinitial yinitial
                        scrollbars "vertical"
                        mousewheel True
                        draggable True
                        pagekeys True

                        side_yfill True

                        vbox:
                            spacing spacing

                            transclude

                elif scroll == "vpgrid":

                    vpgrid:
                        cols 1
                        yinitial yinitial

                        scrollbars "vertical"
                        mousewheel True
                        draggable True
                        pagekeys True

                        side_yfill True

                        spacing spacing

                        transclude

                else:

                    transclude

    use navigation

    textbutton _("Retour"):
        style "return_button"

        action Return()

    label title

    if main_menu:
        key "game_menu" action ShowMenu("main_menu")


style game_menu_outer_frame is empty
style game_menu_navigation_frame is empty
style game_menu_content_frame is empty
style game_menu_viewport is gui_viewport
style game_menu_side is gui_side
style game_menu_scrollbar is gui_vscrollbar

style game_menu_label is gui_label
style game_menu_label_text is gui_label_text

style return_button is navigation_button
style return_button_text is navigation_button_text

style game_menu_outer_frame:
    bottom_padding 70
    top_padding 190

    background "gui/overlay/game_menu.png"

style game_menu_navigation_frame:
    xsize 420
    yfill True

style game_menu_content_frame:
    left_margin 60
    right_margin 30
    top_margin 50

style game_menu_viewport:
    xsize 1320

style game_menu_vscrollbar:
    unscrollable gui.unscrollable

style game_menu_side:
    spacing 15

style game_menu_label:
    xpos 75
    ysize 180


define gui.idle_color = '#000000'

style game_menu_label_text:
    size gui.title_text_size
    color gui.accent_color
    yalign 0.5

style return_button:
    xpos 0
    yalign 1.0
    yoffset -45


## Écran « À propos... » #######################################################
##
## Cet écran présente le générique, les crédits et les informations de copyright
## relatives au jeu et à Ren’Py.
##
## Il n’y a rien de spécial sur cet écran. Par conséquent, il sert aussi
## d’exemple pour créer un écran personnalisé.

screen about():

    tag menu

    ## Cette déclaration concerne l’écran game_menu. L’élément vbox est ensuite
    ## inclus dans la fenêtre de l'écran game_menu.
    use game_menu(_("Extra"), scroll="viewport"):
        style_prefix "extra"
        frame:
            vbox:
                textbutton _("Crédits") action ShowMenu('generique')
                textbutton _("Galerie") action ShowMenu('galerie')
                textbutton _("Changelog") action ShowMenu("Changelog")
                textbutton _('Succès') action ShowMenu("achievement_menu")
               
    python:
        style.extra = Style(style.default)
        style.extra_button.background = None
        style.extra_button_text.color = "#190030"
        style.extra_button_text.hover_color = "#718effff"
        style.extra_button_text.selected_color = "#86f1ff"
        style.extra_button_text.size = 140

style about_label is gui_label
style extra_label_text is gui_label_text
style about_text is gui_text

style extra_label_text:
    size 10
style button_extra:
    background "#6b6bff"
    insensitive_background "#585858"
    hover_background "#60e2ff"

screen generique():

    tag menu

    ## Cette déclaration concerne l’écran game_menu. L’élément vbox est ensuite
    ## inclus dans la fenêtre de l'écran game_menu.
    use game_menu(_("Extra"), scroll="viewport"):
        style_prefix "about"

        vbox:
            
            label "[config.name!t]":
             background Solid('#ffffff')
            text _("Version [config.version!t]\n"):
             outlines [ (absolute(2), "#000000", absolute(0), absolute(0)) ]

            ## gui.about est généralement initialisé dans le fichier
            ## options.rpy.
            if gui.about:
                text "[gui.about!t]\n":
                 outlines [ (absolute(2), "#000000", absolute(0), absolute(0)) ]
            label _("Dessins")
            text _("Julia l'inconnue \n Charasime")
            label _("Animations")
            text _("Julia l'inconnue")
            label _("Musiques")
            text _("Julia l'inconnue \n Charasime")
            label _("Programmation")
            text _("Julia l'inconnue")
            label _("Scénario")
            text _("Julia l'inconnue")
            label _("Beta-testeurices")
            text _("Charasime \n LaJoieDeVivre \n Mobydick \n La ju' \n Furfy")
            label _("Moteur de jeu")
            text _("Conçu avec {a=https://www.renpy.org/}Ren'Py{/a} [renpy.version_only].\n\n[renpy.license!t]"):
             outlines [ (absolute(2), "#000000", absolute(0), absolute(0)) ]
            label _("Inspirations")
            text _("Directement Ace attorney, DDLC, There is no game, \n Indirectement pour l'instant BATIM, FNAF, L'épreuve, gameknignt999, one piece, yo kai watch et basiquement tout ce que j'ai pu lire, voir ou auquel j'ai pu jouer au cours de ma vie.")
            label _("Remerciements")
            text _("PowarT, OwOIWonderWhatsThis, Ikhatuni, Lemekivi, Jeff Wooden, Crazed, Jules, Fitzchevalerie, TheTruePacificDan, Hariboo, Evlyn_dusk_a_girl")


style about_label is gui_label
style about_label_text is gui_label_text
style about_text is gui_text

style about_label_text:
    size gui.label_text_size



screen gain_achieve(achievetext):
     tag achievementalert
     fixed:
         image "sp/achievementbg.png" at Position(xpos=0.85, ypos=0.1, xanchor=0.5, yanchor=0.5)
         text _("{size=22}Nouveau succès débloqué:\n") + achievetext + "{/size}" id "achievetext" at Position(xpos=0.85, ypos=0.1, xanchor=0.5, yanchor=0.5) xmaximum 290 ymaximum 90
     timer 3.0 action Hide("gain_achieve")

init python:

    # Step 1. Create the gallery object.
    g = Gallery()
    g.transition = fade
    g.navigation = True

    # Step 2. Add buttons and images to the gallery.

    # This button has multiple images assocated with it. We use unlock_image
    # so we don't have to call both .image and .unlock. We also apply a
    # transform to the first image.
    g.button("decors")
    g.unlock_image("fond ecole")
    g.unlock_image("fond droite")
    g.unlock_image("fonddroite2")
    g.unlock_image("projecteur1")
    g.unlock_image("fond reboot")
    g.unlock_image("fond Void_room")
    g.unlock_image("fond trans")
    g.unlock_image("fond ecole fake")
    g.unlock_image("fond reboot fake")

    g.button("personnages")
    g.unlock_image("ju splain")
    g.unlock_image("ju splain_T")
    g.unlock_image("ju wu")
    g.unlock_image("ju wu_T")
    g.unlock_image("ju plexe")
    g.unlock_image("ju plexe_T")
    g.unlock_image("ju plexe_C")
    g.image("ju plexe_C2")
    g.unlock_image("ju sad")
    g.unlock_image("ju sad_T")
    g.unlock_image("ju re")
    g.unlock_image("ju re_T")
    g.unlock_image("ju fear")
    g.unlock_image("ju fear_T")
    g.unlock_image("ju ink")
    g.unlock_image("ju ink_T")
    g.unlock_image("juposteur happy")
    g.unlock_image("juposteur fhappy")

    g.button("memes")
    g.unlock_image("Logo2")
    g.image("buff vap")

    g.button("cutscenes")
    g.image("Unfinished")

    # This button has a condition associated with it, allowing the game
    # to choose which images unlock.
    g.button("end1")
    g.condition("persistent.unlock_1")
    g.image("ju re")
    g.image("ju wu")
    g.image("ju re")
    g.image("ju wu")
    g.image("ju re")

    g.button("end2")
    g.condition("persistent.unlock_2")
    g.image("ju wu")
    g.image("ju wu")
    g.image("ju wu")

    # The last image in this button has an condition associated with it,
    # so it will only unlock if the user gets both endings.
    g.button("end3")
    g.condition("persistent.unlock_3")
    g.image("ju wu")
    g.image("ju wu")
    g.image("ju wu")
    g.condition("persistent.unlock_3 and persistent.unlock_4")

    g.button("end4")
    g.condition("persistent.unlock_4")
    g.image("ju wu")
    g.image("ju wu")
    g.image("ju wu")
    g.image("ju wu")
    g.image("ju wu")
    g.image("ju wu")
    g.condition("persistent.unlock_3 and persistent.unlock_4")

    # The final two buttons contain images that show multiple pictures
    # at the same time. This can be used to compose character art onto
    # a background.
    g.button("dawn mary")
    g.unlock_image("ju re", "ju re")
    g.unlock_image("fond ecole", "ju re")
    g.unlock_image("ju re", "fond ecole")

    g.button("dark mary")
    g.unlock_image("ju wu", "mary dark wistful")
    g.unlock_image("fond reset", "ju wu")
    g.unlock_image("anifond", "ju wu")

    # The transition used when switching images.
    g.transition = dissolve

# Step 3. The gallery screen we use.
screen galerie:

    # Ensure this replaces the main menu.
    tag menu

    # The background.
    add "fond Void_room"
    style_prefix "about"

    # A grid of buttons.
    label _("{b}{color=#FFFFFF}{size=100}Galerie") xalign 0.5 yalign 0.1:
         background Solid('#000000d4')
    grid 2 2:

        xfill True
        yfill True

        # Call make_button to show a particular button.
        add g.make_button("decors", "UI/galerie/underground.png", xalign=0.5, yalign=0.5)
        add g.make_button("personnages", "UI/galerie/Edwin.png", xalign=0.5, yalign=0.5)

        add g.make_button("memes", "UI/galerie/klarpear.png", xalign=0.5, yalign=0.5)
        add g.make_button("cutscenes", "UI/galerie/cutscene.png", xalign=0.5, yalign=0.5)


    # The screen is responsible for returning to the main menu. It could also
    # navigate to other gallery screens.
    frame : 
        xalign 0.5
        yalign 0.55
        textbutton _("Retour") action Return() 

# main UI et déplacements
# main UI

screen mainUI:
    imagemap:
       ground "main_UI"
       hotspot (149, 790, 194, 214) action [Jump("aventure"), Hide (screen = None), Hide (screen= "inventory")]
       hotspot (612, 785, 239, 208) action Jump("menu1")
       hotspot (1140, 782, 233, 219) action Jump("menu111face")
       hotspot (1542, 815, 257, 189) action Jump("menu2")
       hotspot (1698, 0, 219, 213) action Jump("menu3")

screen whiteUI:
    imagemap:
       ground "other_UI"
       hotspot (612, 785, 239, 208) action Jump("inverted1")
       hotspot (1140, 782, 233, 219) action Jump("whiteexit")

screen blackUI:
    imagemap:
       ground "other_UI"
       hotspot (612, 785, 239, 208) action Jump("offlinemenu1")
       hotspot (1140, 782, 233, 219) action Jump("blackexit")

#aventure

screen aventure:
    add "Miclordes_trans"
    add "Miclordes"
    add "aventure_annexe"

    imagebutton auto "aventureprincipale %s":
     xpos 0.05
     ypos 0.05
     action [ToggleScreen("aventure_P"), Hide (screen = None), Play("music", "audio/A day in the unknown.ogg", loop=True, fadein=3)]
    frame : 
     xalign 0.5
     yalign 0.95
     textbutton _("Retour") action [Play("music", "audio/A day in the unknown.ogg", loop=True, fadein=3), Jump ("menu0")]

screen aventure_P:
    add "Aventure HP"

    viewport:
        scrollbars "horizontal"
        spacing 5
        mousewheel True
        draggable True
        #area (0, 70, 1920, 1000)
        xpos 720 #à supprimer quand il y en aura plusieurs

        side_yfill True


        imagebutton auto "Aventure_P %s":
         xpos 360
         ypos 0
         action [ToggleScreen("pacrel"), Hide (screen = None)]
        if joaearly:
             imagebutton auto "Aventure_LJDV %s":
                 xpos 900
                 ypos 0
                 action [ToggleScreen("LJDV"), Hide (screen = None)]
    frame : 
     xalign 0.5
     yalign 0.95
     textbutton _("Retour") action [ToggleScreen ("aventure"), Hide (screen = None), Play("music", "audio/Miclordes.ogg", loop=True, fadein=3)]



screen pacrel:
    style_prefix "aventurep"
    add "Aventure_fond pacrel" 
    
    vbox:
        xalign 0.1
        yalign 0.5
        textbutton _("Prologue") action [Jump("prologue_pacrel"), Hide (screen = None)]
        #if persistent.p0:
         #textbutton _("Chapitre 1") action [Jump("Ch1_pacrel"), Hide (screen = None)]
        textbutton _("Retour") action [ToggleScreen ("aventure_P"), Hide (screen = None)]

    python:
     style.aventurep = Style(style.default)
     style.aventurep_button.background = None
     style.aventurep_button_text.color = "#ffffff"
     style.aventurep_button_text.hover_color = "#919090ff"
     style.aventurep_button_text.selected_color = "#d6d6d6"
     style.aventurep_button_text.size = 80

screen LJDV:
    style_prefix "aventurej"
    add "Aventure_fond LJDV" 
    
    vbox:
        xalign 0.1
        yalign 0.5
        textbutton _("Prologue") action [Jump("prologue_LJDV"), Hide (screen = None)]
        textbutton _("Chapitre 1") action [Jump("Ch1_LJDV"), Hide (screen = None)]
        textbutton _("Retour") action [ToggleScreen ("aventure_P"), Hide (screen = None)]

    python:
     style.aventurej = Style(style.default)
     style.aventurej_button.background = None
     style.aventurej_button_text.color = "#ff0000"
     style.aventurej_button_text.hover_color = "#ff9100ff"
     style.aventurej_button_text.selected_color = "#d4ff00"
     style.aventurej_button_text.size = 80

    

# Inventaire

screen inventory:
    zorder 92
    frame:
        background "#99ff9900"
        xalign 0.01
        yalign 0.02

        imagebutton auto "inventory %s":
         xpos 0.01
         ypos 0.02
         action ToggleScreen("inventory_item_description")

    on "hide" action Hide("inventory_item_description")    

default item_descriptions = {_("Trilogie Histoire Multiple") : _("Trois bouquins sur un mec random qui se bat pour sauver sa créatrice de son alter-ego et de dieux"), _("Rapport OFAC 105") : _("Une annonce d'un accord entre des dieux et l'OFAC contre un créateur")}
default inventory_items = []
default item_description = ""

style inv_button is frame:
    xsize 200
    ysize 100

style inv_button_text:
    xalign 0.5
    yalign 0.5

screen inventory_item_description:
    # use this based on your preference
    # modal True
    add "Inventaire"
    window:
        background "#cfcfcf00"
        xsize 600
        ysize 150
        xalign 0.5
        yalign 0.1
        text item_description:
            xfill True
            yfill True

    window:
        background "#cfcfcf00"
        xsize 1290
        ysize 600
        xalign 0.5
        yalign 0.7
        
        hbox:
            box_wrap True
            box_wrap_spacing 10
            spacing 10
            xoffset 20
            yoffset 20
            style_prefix "inv"
            for item in inventory_items:
                imagebutton:
                    idle ("UI/" + item + " idle.png")
                    hover ("UI/" +item + " hover.png")
                    action SetVariable("item_description", item_descriptions.get(item))
                    selected False


    on "hide" action SetVariable("item_description", "")


init python:  
  clickcount = 0
  requiredclicks = 20
  timelimit = 60

  def addclick():
    if store.clickcount < store.requiredclicks:
        store.clickcount += 1
    else:
        clickcount = 0
        renpy.jump("timeskip")
        

screen quicktimebarwhite():

  frame:
    background None
    xpos 640
    ypos 490
    vbox:
        text _("Résiste au vide !")
        bar value AnimatedValue(value=store.clickcount, range=store.requiredclicks, delay=1.0, old_value=store.clickcount):
            xsize 1000
            ysize 50
        textbutton _("{color=#FF0000}{size=50}Résister au vide"):
            action Function(store.addclick)
    
    timer store.timelimit action [Jump ('finwhite'), PauseAudio(channel='music', value=True)]

init python:  
  clickcountedmes = 0
  requiredclicksedmes = 150
  timelimitedmes = 60

  def addclick2():
    if store.clickcountedmes < store.requiredclicksedmes:
        store.clickcountedmes += 1
    else:
        clickcountedmes = 0
        renpy.jump("timeskip")

screen quicktimebaredmes():

  frame:
    background None
    xpos 640
    ypos 490
    vbox:
        text _("Force ton chemin vers l'arrêt d'urgence !")
        bar value AnimatedValue(value=store.clickcountedmes, range=store.requiredclicksedmes, delay=1.0, old_value=store.clickcountedmes):
            xsize 1000
            ysize 50
        textbutton _("{color=#FF0000}{size=50}Tends le bras !"):
            action Function(store.addclick2)
    
    timer store.timelimitedmes action [Jump('finEdmes'), PauseAudio(channel='music', value=True)]

#directions main hub

screen directionsF:
    imagemap:
       ground "Directions"
       hotspot (7, 312, 418, 314) action Jump("menu111gauche")
       hotspot (1504, 308, 412, 313) action Jump("menu111droite")
       hotspot (694, 830, 444, 242) action Jump("menu0")
       hotspot (492, 613, 109, 81) action Jump("menu0bis")
       hotspot (709, 396, 497, 296) action Jump("whiteout")
       hotspot (1582, 972, 123, 94):
         action [Hide ("directionsF"), Hide ("window"), Show("OFAC1")]
       hotspot (417, 373, 192, 64) action Jump("HMlib")
       hotspot (1296, 375, 211, 59) action Jump("capital")
       hotspot (98, 767, 115, 120) action OpenURL("https://youtu.be/BW78t48Zcq8?si=WMnGnrbIKB_4xMDv")
       

screen directionsFbis:
    imagemap:
       ground "none"
       hotspot (500, 408, 102, 43) action Jump("menu0")       

screen directionsD:
    imagemap:
       ground "Directions"
       hotspot (7, 312, 418, 314) action Jump("menu111face")
       hotspot (1504, 308, 412, 313) action Jump("menu111arriere")
       hotspot (694, 830, 444, 242) action Jump("menu0")

screen directionsG:
    imagemap:
       ground "Directions"
       hotspot (7, 312, 418, 314) action Jump("menu111arriere")
       hotspot (1504, 308, 412, 313) action Jump("menu111face")
       hotspot (694, 830, 444, 242) action Jump("menu0")

screen directionsB:
    imagemap:
       ground "Directions"
       hotspot (7, 312, 418, 314) action Jump("menu111droite")
       hotspot (1504, 308, 412, 313) action Jump("menu111gauche")
       hotspot (694, 830, 444, 242) action Jump("menu0")

# screen arrière main hub

screen Arret_urgence:
    imagemap:
       ground "BAU"
       hotspot (811, 438, 216, 219) action Jump("menu111bouton")

# screen avant main hub

screen to_inverted():
    vbox:
     xalign 0.5
     yalign 0.5
     textbutton _("{color=#FF0000}{size=100}Résister au vide") action Jump("inverted")

    timer 3.0 action Jump("finwhite")

# Documents texte
screen OFAC1():
    frame:
     xsize 1400 # Width of your frame
     ysize 1080 # Height of your frame
     background "Rapport_OFAC" #Assuming it is located in the images folder.
     style_prefix "about"
     vbox:
         xpos 200 # offset on the x axis
         ypos 150 # offset on the y axis
         #spacing 20 # if you want to separate your lines a little.
         label _("{b}{size=+2}{color=#000000}Rapport de l'OFAC #105 : Accord avec Dieu")
         text _("{size=-10}Mesdames, Messieurs,\nAprès consultation du bureau d'affaire et du comité permanent de l'OFAC, je suis au plaisir de vous annoncer que nous commençerons dès aujourd'hui un contrat avec Bodias, dieu tout puissant, pour nous assister dans nos tâches. Avec un peu de chance, nous pourrons enfin finir cette affaire Pacrel une fois pour toute ! Il nous a prévenu et demandé la plus grande confidentialité, le prospect de l'existence d'un dieu pouvant créer le chaos et attirer de l'attention sur nos opérations. Plus que jamais, il vous faudra donc détruire ce document dès que consulté. \nUn rendez-vous en personne nous a également permis d'établir que notre existence était sous le couvert d'une autre entité et en danger par cette dernière. Il nous faudra alors sans doute combattre également dans ce cadre cette entité maléfique. \nCordialement, \nFRAQUES Jean, Directeur général de coordination")
         textbutton _("Fermer") action [ Hide ("OFAC1") , Jump ("ofac1")]  # Hides the box you've created, but this part may vary on how you handle screens.
         

## Écran « Changelog » #######################################################
##
## Cet écran présente le générique, les crédits et les informations de copyright
## relatives au jeu et à Ren’Py.
##
## Il n’y a rien de spécial sur cet écran. Par conséquent, il sert aussi
## d’exemple pour créer un écran personnalisé.

screen Changelog():

    tag menu

    ## Cette déclaration concerne l’écran game_menu. L’élément vbox est ensuite
    ## inclus dans la fenêtre de l'écran game_menu.
    use game_menu(_("Changelog"), scroll="viewport"):

        style_prefix "about"

        vbox:

            label "{color=#000000}Old Alpha 1.2":
             background Solid('#ff3232')
           
            label _("\n {color=#1e166f} Ajouts"):
             background Solid('#00bfff')
            text _("-Nouvelle fin, dialogues, décors \n -Menu succès et succès (en soit) \n -liste de CW à l'allumage \n -Texte random en plus (désormais 30)"):
             outlines [ (absolute(2), "#000000", absolute(0), absolute(0)) ]
            
           
            label _("\n{color=#1e166f} Modifications"):
             background Solid('#00ff26')
            text _("-modification et regroupement de plusieurs menus dans extra \n -Réajustement de l'UI (lisibilité de texte)"):
             outlines [ (absolute(2), "#000000", absolute(0), absolute(0)) ]
            
           
            label _("\n{color=#1e166f} Bugfixes"):
             background Solid('#8400ff')
            text _("-Mauvaises redirections"):
             outlines [ (absolute(2), "#000000", absolute(0), absolute(0)) ]
           

            label "\n\n\n{color=#000000}Old Alpha 1.1":
             background Solid('#ff3232')
           
            label _("\n{color=#1e166f} Ajouts"):
             background Solid('#00d5ff')
            text _("- psy à l'entrée de jeu \n -Screen d'introduction pré-menu principal \n -nom définitif du jeu \n 20 répliques randomisées au démarrage \n -Menu changelog (ptdr) \n -nouveau sprite pour l'Inconnue"):
             outlines [ (absolute(2), "#000000", absolute(0), absolute(0)) ]
            
           
            label _("\n{color=#1e166f} Modifications"):
             background Solid('#22ff00')
            text _("-fond s, couleur de texte et logo dans les menus principaux et sous-menus \n -Assets de boite de dialogue/choix \n -approfond issement de certaines questions \n -Nom assigné si refus d'écriture \n -Correction de typos"):
             outlines [ (absolute(2), "#000000", absolute(0), absolute(0)) ]
           
           
            label _("\n{color=#1e166f} Bugfixes"):
             background Solid('#8800ff')
            text _("-Question incomplète redirige vers saisie de code"):
             outlines [ (absolute(2), "#000000", absolute(0), absolute(0)) ]
             


style about_label is gui_label
style about_label_text is gui_label_text
style about_text is gui_text

style about_label_text:
    size gui.label_text_size


## Écran de chargement et de sauvegarde ########################################
##
## Ces écrans permettent au joueur d’enregistrer le jeu et de le charger
## à nouveau. Comme ils partagent beaucoup d’éléments communs, ils sont
## tous les deux implémentés dans un troisième écran, appelé fichiers_slots
## (emplacement_de_fichier).
##
## https://www.renpy.org/doc/html/screen_special.html#save https://
## www.renpy.org/doc/html/screen_special.html#load

screen save():

    tag menu

    use file_slots(_("Sauvegarde"))


screen load():

    tag menu

    use file_slots(_("Charger"))


screen file_slots(title):

    default page_name_value = FilePageNameInputValue(pattern=_("Page {}"), auto=_("Sauvegardes automatiques"), quick=_("Sauvegardes rapides"))

    use game_menu(title):

        fixed:

            ## Cette instruction s’assure que l’évènement enter aura lieu avant
            ## que l’un des boutons ne fonctionne.
            order_reverse True

            ## Le nom de la page, qui peut être modifié en cliquant sur un
            ## bouton.
            button:
                style "page_label"

                key_events True
                xalign 0.5
                action page_name_value.Toggle()

                input:
                    style "page_label_text"
                    value page_name_value

            ## La grille des emplacements de fichiers.
            grid gui.file_slot_cols gui.file_slot_rows:
                style_prefix "slot"

                xalign 0.5
                yalign 0.5

                spacing gui.slot_spacing

                for i in range(gui.file_slot_cols * gui.file_slot_rows):

                    $ slot = i + 1

                    button:
                        action FileAction(slot)

                        has vbox

                        add FileScreenshot(slot) xalign 0.5

                        text FileTime(slot, format=_("{#file_time}%A %d %B %Y, %H:%M"), empty=_("emplacement vide")):
                            style "slot_time_text"

                        text FileSaveName(slot):
                            style "slot_name_text"

                        key "save_delete" action FileDelete(slot)

            ## Boutons pour accéder aux autres pages.
            vbox:
                style_prefix "page"

                xalign 0.5
                yalign 1.0

                hbox:
                    xalign 0.5

                    spacing gui.page_spacing

                    textbutton _("<") action FilePagePrevious()

                    if config.has_autosave:
                        textbutton _("{#auto_page}A") action FilePage("auto")

                    if config.has_quicksave:
                        textbutton _("{#quick_page}Q") action FilePage("quick")

                    ## range(1, 10) donne les nombres de 1 à 9.
                    for page in range(1, 10):
                        textbutton "[page]" action FilePage(page)

                    textbutton _(">") action FilePageNext()

                if config.has_sync:
                    if CurrentScreenName() == "save":
                        textbutton _("Uploader Sync"):
                            action UploadSync()
                            xalign 0.5
                    else:
                        textbutton _("Télécharger Sync"):
                            action DownloadSync()
                            xalign 0.5


style page_label is gui_label
style page_label_text is gui_label_text
style page_button is gui_button
style page_button_text is gui_button_text

style slot_button is gui_button
style slot_button_text is gui_button_text
style slot_time_text is slot_button_text
style slot_name_text is slot_button_text

style page_label:
    xpadding 75
    ypadding 5

style page_label_text:
    textalign 0.5
    layout "subtitle"
    hover_color gui.hover_color

style page_button:
    properties gui.button_properties("page_button")

style page_button_text:
    properties gui.text_properties("page_button")

style slot_button:
    properties gui.button_properties("slot_button")

style slot_button_text:
    properties gui.text_properties("slot_button")


## Écran des préférences #######################################################
##
## L’écran de préférences permet au joueur de configurer le jeu pour mieux
## correspondre à ses attentes.
##
## https://www.renpy.org/doc/html/screen_special.html#preferences

screen screen_language:
    style_prefix "window"
    frame:
        xalign 0.5
        yalign 0.5
        vbox:
            spacing 45  
            label _("Choisissez une langue")
            textbutton "Français" action Language (None),Return()
            textbutton "English" action Language ("english"),Return()
            #spacing 150

screen preferences():

    tag menu

    use game_menu(_("Options"), scroll="viewport"):

        vbox:

            hbox:
                box_wrap True

                if renpy.variant("pc") or renpy.variant("web"):

                    vbox:
                        style_prefix "radio"
                        label _("Affichage")
                        textbutton _("Fenêtre") action Preference("display", "window")
                        textbutton _("Plein écran") action Preference("display", "fullscreen")

                vbox:
                    style_prefix "check"
                    label _("Avance rapide")
                    textbutton _("Texte non lu") action Preference("skip", "toggle")
                    textbutton _("Après les choix") action Preference("after choices", "toggle")
                    textbutton _("Transitions") action InvertSelected(Preference("transitions", "toggle"))

                ## Des boites vbox additionnelles de type "radio_pref" ou
                ## "check_pref" peuvent être ajoutées ici pour ajouter des
                ## préférences définies par le créateur du jeu.

                vbox:
                    style_prefix "radio"
                    label _("language")
                    textbutton _("Français") text_font "DejaVuSans.ttf" action Language(None)
                    textbutton _("English") text_font "DejaVuSans.ttf" action Language("english")

            null height (4 * gui.pref_spacing)

            hbox:
                style_prefix "slider"
                box_wrap True

                vbox:

                    label _("Vitesse du texte")

                    bar value Preference("text speed")

                    label _("Avance automatique")

                    bar value Preference("auto-forward time")



                vbox:

                    if config.has_music:
                        label _("Volume de la musique")

                        hbox:
                            bar value Preference("music volume")

                    if config.has_sound:

                        label _("Volume des sons")

                        hbox:
                            bar value Preference("sound volume")

                            if config.sample_sound:
                                textbutton _("Test") action Play("sound", config.sample_sound)


                    if config.has_voice:
                        label _("Volume des voix")

                        hbox:
                            bar value Preference("voice volume")

                            if config.sample_voice:
                                textbutton _("Test") action Play("voice", config.sample_voice)

                    if config.has_music or config.has_sound or config.has_voice:
                        null height gui.pref_spacing

                        textbutton _("Couper tous les sons"):
                            action Preference("all mute", "toggle")
                            style "mute_all_button"


style pref_label is gui_label
style pref_label_text is gui_label_text
style pref_vbox is vbox

style radio_label is pref_label
style radio_label_text is pref_label_text
style radio_button is gui_button
style radio_button_text is gui_button_text
style radio_vbox is pref_vbox

style check_label is pref_label
style check_label_text is pref_label_text
style check_button is gui_button
style check_button_text is gui_button_text
style check_vbox is pref_vbox

style slider_label is pref_label
style slider_label_text is pref_label_text
style slider_slider is gui_slider
style slider_button is gui_button
style slider_button_text is gui_button_text
style slider_pref_vbox is pref_vbox

style mute_all_button is check_button
style mute_all_button_text is check_button_text

style pref_label:
    top_margin gui.pref_spacing
    bottom_margin 3

style pref_label_text:
    yalign 1.0

style pref_vbox:
    xsize 338

style radio_vbox:
    spacing gui.pref_button_spacing

style radio_button:
    properties gui.button_properties("radio_button")
    foreground "gui/button/radio_[prefix_]foreground.png"

style radio_button_text:
    properties gui.text_properties("radio_button")

style check_vbox:
    spacing gui.pref_button_spacing

style check_button:
    properties gui.button_properties("check_button")
    foreground "gui/button/check_[prefix_]foreground.png"

style check_button_text:
    properties gui.text_properties("check_button")

style slider_slider:
    xsize 525

style slider_button:
    properties gui.button_properties("slider_button")
    yalign 0.5
    left_margin 15

style slider_button_text:
    properties gui.text_properties("slider_button")

style slider_vbox:
    xsize 675


## Écran de l'historique #######################################################
##
## Il s’agit d’un écran qui affiche l’historique des dialogues au joueur. Bien
## qu’il n'y ait rien de spécial sur cet écran, il doit accéder à l’historique
## de dialogue stocké dans _history_list.
##
## https://www.renpy.org/doc/html/history.html

screen history():

    tag menu

    ## Cette instruction permet d’éviter de prédire cet écran, car il peut être
    ## très large
    predict False

    use game_menu(_("Historique"), scroll=("vpgrid" if gui.history_height else "viewport"), yinitial=1.0, spacing=gui.history_spacing):

        style_prefix "history"

        for h in _history_list:

            window:

                ## Cela positionne correctement l'écran si history_height est
                ## initialisé à None.
                has fixed:
                    yfit True

                if h.who:

                    label h.who:
                        style "history_name"
                        substitute False

                        ## Utilise pour la couleur du texte, la couleur par
                        ## défaut des dialogues du personnage si elle a été
                        ## initialisée.
                        if "color" in h.who_args:
                            text_color h.who_args["color"]

                $ what = renpy.filter_text_tags(h.what, allow=gui.history_allow_tags)
                text what:
                    substitute False

        if not _history_list:
            label _("L'historique des dialogues est vide.")


## Ceci détermine quels tags peuvent être affichés sur le screen de
## l'historique.

define gui.history_allow_tags = { "alt", "noalt", "rt", "rb", "art" }


style history_window is empty

style history_name is gui_label
style history_name_text is gui_label_text
style history_text is gui_text

style history_label is gui_label
style history_label_text is gui_label_text

style history_window:
    xfill True
    ysize gui.history_height

style history_name:
    xpos gui.history_name_xpos
    xanchor gui.history_name_xalign
    ypos gui.history_name_ypos
    xsize gui.history_name_width

style history_name_text:
    min_width gui.history_name_width
    textalign gui.history_name_xalign

style history_text:
    xpos gui.history_text_xpos
    ypos gui.history_text_ypos
    xanchor gui.history_text_xalign
    xsize gui.history_text_width
    min_width gui.history_text_width
    textalign gui.history_text_xalign
    layout ("subtitle" if gui.history_text_xalign else "tex")

style history_label:
    xfill True

style history_label_text:
    xalign 0.5


## Écran d'aide ################################################################
##
## Cet écran fournit des informations sur les touches et les boutons de souris.
## En interne, il utilise d’autres écrans (keyboard_help, mouse_help et
## gamepad_help) pour afficher une aide dédiée.

screen help():

    tag menu

    default device = "keyboard"

    use game_menu(_("Aide"), scroll="viewport"):

        style_prefix "help"

        vbox:
            spacing 23

            hbox:

                textbutton _("Clavier") action SetScreenVariable("device", "keyboard")
                textbutton _("Souris") action SetScreenVariable("device", "mouse")

                if GamepadExists():
                    textbutton _("Manette") action SetScreenVariable("device", "gamepad")

            if device == "keyboard":
                use keyboard_help
            elif device == "mouse":
                use mouse_help
            elif device == "gamepad":
                use gamepad_help


screen keyboard_help():

    hbox:
        label _("Entrée")
        text _("Avance dans les dialogues et active l’interface (effectue un choix).")

    hbox:
        label _("Espace")
        text _("Avance dans les dialogues sans effectuer de choix.")

    hbox:
        label _("Flèches directionnelles")
        text _("Permet de se déplacer dans l’interface.")

    hbox:
        label _("Echap.")
        text _("Ouvre le menu du jeu.")

    hbox:
        label _("Ctrl")
        text _("Fait défiler les dialogues tant que la touche est pressée.")

    hbox:
        label _("Tab")
        text _("Active ou désactive les «sauts des dialogues».")

    hbox:
        label _("Page Haut")
        text _("Retourne au précédent dialogue.")

    hbox:
        label _("Page Bas")
        text _("Avance jusqu'au prochain dialogue.")

    hbox:
        label "H"
        text _("Cache l’interface utilisateur.")

    hbox:
        label "S"
        text _("Prend une capture d’écran.")

    hbox:
        label "V"
        text _("Active la {a=https://www.renpy.org/l/voicing}{size=24}vocalisation automatique{/size}{/a}.")

    hbox:
        label "Shift+A"
        text _("Ouvre le menu d'accessibilité.")


screen mouse_help():

    hbox:
        label _("Bouton gauche")
        text _("Avance dans les dialogues et active l’interface (effectue un choix).")

    hbox:
        label _("Bouton central")
        text _("Cache l’interface utilisateur.")

    hbox:
        label _("Bouton droit")
        text _("Ouvre le menu du jeu.")

    hbox:
        label _("Molette vers le haut")
        text _("Retourne au précédent dialogue.")

    hbox:
        label _("Molette vers le bas")
        text _("Avance jusqu'au prochain dialogue.")


screen gamepad_help():

    hbox:
        label _("Bouton R1\nA/Bouton du bas")
        text _("Avance dans les dialogues et active l’interface (effectue un choix).")

    hbox:
        label _("Gâchettes gauche")
        text _("Retourne au précédent dialogue.")

    hbox:
        label _("Bouton R1")
        text _("Avance jusqu'au prochain dialogue.")

    hbox:
        label _("Boutons directionnels, stick gauche")
        text _("Permet de se déplacer dans l’interface.")

    hbox:
        label _("Start, Guide, B/Right Button")
        text _("Ouvre le menu du jeu.")

    hbox:
        label _("Y/Bouton du haut")
        text _("Cache l’interface utilisateur.")

    textbutton _("Calibrage") action GamepadCalibrate()


style help_button is gui_button
style help_button_text is gui_button_text
style help_label is gui_label
style help_label_text is gui_label_text
style help_text is gui_text

style help_button:
    properties gui.button_properties("help_button")
    xmargin 12

style help_button_text:
    properties gui.text_properties("help_button")

style help_label:
    xsize 375
    right_padding 30

style help_label_text:
    size gui.text_size
    xalign 1.0
    textalign 1.0



################################################################################
## Écrans additionnels
################################################################################


## Écran de confirmation #######################################################
##
## Cet écran est appelé quand Ren'Py souhaite poser une question au joueur dont
## la réponse est oui ou non.
##
## https://www.renpy.org/doc/html/screen_special.html#confirm

screen confirm(message, yes_action, no_action):

    ## Cette instruction s’assure que les autres écrans resteront en arrière
    ## plan tant que cet écran sera affiché.
    modal True

    zorder 200

    style_prefix "confirm"

    add "gui/overlay/confirm.png"

    frame:

        vbox:
            xalign .5
            yalign .5
            spacing 45

            label _(message):
                style "confirm_prompt"
                xalign 0.5

            hbox:
                xalign 0.5
                spacing 150

                textbutton _("Oui") action yes_action
                textbutton _("Non") action no_action

    ## Le clic bouton droit et la touche Echap. correspondent à la réponse
    ## "non".
    key "game_menu" action no_action


style confirm_frame is gui_frame
style confirm_prompt is gui_prompt
style confirm_prompt_text is gui_prompt_text
style confirm_button is gui_medium_button
style confirm_button_text is gui_medium_button_text

style confirm_frame:
    background Frame([ "gui/confirm_frame.png", "gui/frame.png"], gui.confirm_frame_borders, tile=gui.frame_tile)
    padding gui.confirm_frame_borders.padding
    xalign .5
    yalign .5

style confirm_prompt_text:
    textalign 0.5
    layout "subtitle"

style confirm_button:
    properties gui.button_properties("confirm_button")

style confirm_button_text:
    properties gui.text_properties("confirm_button")


## Écran de l’indicateur d'avance rapide #######################################
##
## L’écran skip_indicator est affiché pour indiquer qu’une avance rapide est en
## cours.
##
## https://www.renpy.org/doc/html/screen_special.html#skip-indicator

screen skip_indicator():

    zorder 100
    style_prefix "skip"

    frame:

        hbox:
            spacing 9

            text _("Avance rapide")

            text "▸" at delayed_blink(0.0, 1.0) style "skip_triangle"
            text "▸" at delayed_blink(0.2, 1.0) style "skip_triangle"
            text "▸" at delayed_blink(0.4, 1.0) style "skip_triangle"


## Cette transformation est utilisé pour faire clignoter les flèches l’une après
## l’autre.
transform delayed_blink(delay, cycle):
    alpha .5

    pause delay

    block:
        linear .2 alpha 1.0
        pause .2
        linear .2 alpha 0.5
        pause (cycle - .4)
        repeat


style skip_frame is empty
style skip_text is gui_text
style skip_triangle is skip_text

style skip_frame:
    ypos gui.skip_ypos
    background Frame("gui/skip.png", gui.skip_frame_borders, tile=gui.frame_tile)
    padding gui.skip_frame_borders.padding

style skip_text:
    size gui.notify_text_size

style skip_triangle:
    ## Nous devons utiliser une police qui a le glyphe BLACK RIGHT-POINTING
    ## SMALL TRIANGLE.
    font "DejaVuSans.ttf"


## Écran de notification #######################################################
##
## Cet écran est utilisé pour affiché un message au joueur. (Par exemple, quand
## une sauvegarde rapide a eu lieu ou quand une capture d’écran vient d’être
## réalisée.)
##
## https://www.renpy.org/doc/html/screen_special.html#notify-screen

screen notify(message):

    zorder 100
    style_prefix "notify"

    frame at notify_appear:
        text "[message!tq]"

    timer 3.25 action Hide('notify')


transform notify_appear:
    on show:
        alpha 0
        linear .25 alpha 1.0
    on hide:
        linear .5 alpha 0.0


style notify_frame is empty
style notify_text is gui_text

style notify_frame:
    ypos gui.notify_ypos

    background Frame("gui/notify.png", gui.notify_frame_borders, tile=gui.frame_tile)
    padding gui.notify_frame_borders.padding

style notify_text:
    properties gui.text_properties("notify")

## Écran NVL ###################################################################
##
## Cet écran est utilisé pour les dialogues et les menus en mode NVL.
##
## https://www.renpy.org/doc/html/screen_special.html#nvl


screen nvl(dialogue, items=None):

    window:
        style "nvl_window"

        has vbox:
            spacing gui.nvl_spacing

        ## Les dialogues sont affichés soit dans une vpgrid soit dans une vbox.
        if gui.nvl_height:

            vpgrid:
                cols 1
                yinitial 1.0

                use nvl_dialogue(dialogue)

        else:

            use nvl_dialogue(dialogue)

        ## Si fourni, affiche le menu. Le menu peut s’afficher de manière
        ## incorrecte si config.narrator_menu est initialisé à True.
        for i in items:

            textbutton i.caption:
                action i.action
                style "nvl_button"

    add SideImage() xalign 0.0 yalign 1.0


screen nvl_dialogue(dialogue):

    for d in dialogue:

        window:
            id d.window_id

            fixed:
                yfit gui.nvl_height is None

                if d.who is not None:

                    text d.who:
                        id d.who_id

                text d.what:
                    id d.what_id


## Ce paramètre contrôle le maximum d’entrée dans le mode NVL qui peuvent être
## affichée simultanément.
define config.nvl_list_length = gui.nvl_list_length

style nvl_window is default
style nvl_entry is default

style nvl_label is say_label
style nvl_dialogue is say_dialogue

style nvl_button is button
style nvl_button_text is button_text

style nvl_window:
    xfill True
    yfill True

    background "gui/nvl.png"
    padding gui.nvl_borders.padding

style nvl_entry:
    xfill True
    ysize gui.nvl_height

style nvl_label:
    xpos gui.nvl_name_xpos
    xanchor gui.nvl_name_xalign
    ypos gui.nvl_name_ypos
    yanchor 0.0
    xsize gui.nvl_name_width
    min_width gui.nvl_name_width
    textalign gui.nvl_name_xalign

style nvl_dialogue:
    xpos gui.nvl_text_xpos
    xanchor gui.nvl_text_xalign
    ypos gui.nvl_text_ypos
    xsize gui.nvl_text_width
    min_width gui.nvl_text_width
    textalign gui.nvl_text_xalign
    layout ("subtitle" if gui.nvl_text_xalign else "tex")

style nvl_thought:
    xpos gui.nvl_thought_xpos
    xanchor gui.nvl_thought_xalign
    ypos gui.nvl_thought_ypos
    xsize gui.nvl_thought_width
    min_width gui.nvl_thought_width
    textalign gui.nvl_thought_xalign
    layout ("subtitle" if gui.nvl_text_xalign else "tex")

style nvl_button:
    properties gui.button_properties("nvl_button")
    xpos gui.nvl_button_xpos
    xanchor gui.nvl_button_xalign

style nvl_button_text:
    properties gui.text_properties("nvl_button")


## Screen des bulles ###########################################################
##
## Le screen des bulles est utilisé pour afficher des dialogues en utilisant des
## bulles de dialogue. Ce screen prend les mêmes paramètres que le screen say,
## doit prévoir un displayable avec l'id "what", et peut créer des displayables
## avec les ids "namebox", "who", et "window".
##
## https://www.renpy.org/doc/html/bubble.html#bubble-screen

screen bubble(who, what):
    style_prefix "bubble"

    window:
        id "window"

        if who is not None:

            window:
                id "namebox"
                style "bubble_namebox"

                text who:
                    id "who"

        text what:
            id "what"

style bubble_window is empty
style bubble_namebox is empty
style bubble_who is default
style bubble_what is default

style bubble_window:
    xpadding 30
    top_padding 5
    bottom_padding 5

style bubble_namebox:
    xalign 0.5

style bubble_who:
    xalign 0.5
    textalign 0.5
    color "#000"

style bubble_what:
    align (0.5, 0.5)
    text_align 0.5
    layout "subtitle"
    color "#000"

define bubble.frame = Frame("gui/bubble.png", 55, 55, 55, 95)
define bubble.thoughtframe = Frame("gui/thoughtbubble.png", 55, 55, 55, 55)

define bubble.properties = {
    "bottom_left" : {
        "window_background" : Transform(bubble.frame, xzoom=1, yzoom=1),
        "window_bottom_padding" : 27,
    },

    "bottom_right" : {
        "window_background" : Transform(bubble.frame, xzoom=-1, yzoom=1),
        "window_bottom_padding" : 27,
    },

    "top_left" : {
        "window_background" : Transform(bubble.frame, xzoom=1, yzoom=-1),
        "window_top_padding" : 27,
    },

    "top_right" : {
        "window_background" : Transform(bubble.frame, xzoom=-1, yzoom=-1),
        "window_top_padding" : 27,
    },

    "thought" : {
        "window_background" : bubble.thoughtframe,
    }
}

define bubble.expand_area = {
    "bottom_left" : (0, 0, 0, 22),
    "bottom_right" : (0, 0, 0, 22),
    "top_left" : (0, 22, 0, 0),
    "top_right" : (0, 22, 0, 0),
    "thought" : (0, 0, 0, 0),
}



################################################################################
## Variantes pour les mobiles
################################################################################

style pref_vbox:
    variant "medium"
    xsize 675

## Comme la souris peut ne pas être présente, nous remplaçons le menu rapide
## avec une version qui utilise des boutons plus gros et qui sont plus faciles à
## toucher du doigt.
screen quick_menu():
    variant "touch"

    zorder 100

    if quick_menu:

        hbox:
            style_prefix "quick"

            xalign 0.5
            yalign 0.98

            textbutton _("Historique") action ShowMenu('history')
            textbutton _("Avance rapide") action Skip() alternate Skip(fast=True, confirm=True)
            textbutton _("Auto") action Preference("auto-forward", "toggle")
            textbutton _("Sauvegarder") action ShowMenu('save')
            textbutton _("Charger") action QuickLoad()
            textbutton _("option") action ShowMenu('preferences')


style window:
    variant "small"
    background "gui/phone/textbox.png"

style radio_button:
    variant "small"
    foreground "gui/phone/button/radio_[prefix_]foreground.png"

style check_button:
    variant "small"
    foreground "gui/phone/button/check_[prefix_]foreground.png"

style nvl_window:
    variant "small"
    background "gui/phone/nvl.png"

style main_menu_frame:
    variant "small"
    background "gui/phone/overlay/main_menu.png"

style game_menu_outer_frame:
    variant "small"
    background "gui/phone/overlay/game_menu.png"

style game_menu_navigation_frame:
    variant "small"
    xsize 510

style game_menu_content_frame:
    variant "small"
    top_margin 0

style pref_vbox:
    variant "small"
    xsize 600

style bar:
    variant "small"
    ysize gui.bar_size
    left_bar Frame("gui/phone/bar/left.png", gui.bar_borders, tile=gui.bar_tile)
    right_bar Frame("gui/phone/bar/right.png", gui.bar_borders, tile=gui.bar_tile)

style vbar:
    variant "small"
    xsize gui.bar_size
    top_bar Frame("gui/phone/bar/top.png", gui.vbar_borders, tile=gui.bar_tile)
    bottom_bar Frame("gui/phone/bar/bottom.png", gui.vbar_borders, tile=gui.bar_tile)

style scrollbar:
    variant "small"
    ysize gui.scrollbar_size
    base_bar Frame("gui/phone/scrollbar/horizontal_[prefix_]bar.png", gui.scrollbar_borders, tile=gui.scrollbar_tile)
    thumb Frame("gui/phone/scrollbar/horizontal_[prefix_]thumb.png", gui.scrollbar_borders, tile=gui.scrollbar_tile)

style vscrollbar:
    variant "small"
    xsize gui.scrollbar_size
    base_bar Frame("gui/phone/scrollbar/vertical_[prefix_]bar.png", gui.vscrollbar_borders, tile=gui.scrollbar_tile)
    thumb Frame("gui/phone/scrollbar/vertical_[prefix_]thumb.png", gui.vscrollbar_borders, tile=gui.scrollbar_tile)

style slider:
    variant "small"
    ysize gui.slider_size
    base_bar Frame("gui/phone/slider/horizontal_[prefix_]bar.png", gui.slider_borders, tile=gui.slider_tile)
    thumb "gui/phone/slider/horizontal_[prefix_]thumb.png"

style vslider:
    variant "small"
    xsize gui.slider_size
    base_bar Frame("gui/phone/slider/vertical_[prefix_]bar.png", gui.vslider_borders, tile=gui.slider_tile)
    thumb "gui/phone/slider/vertical_[prefix_]thumb.png"

style slider_vbox:
    variant "small"
    xsize None

style slider_slider:
    variant "small"
    xsize 900
