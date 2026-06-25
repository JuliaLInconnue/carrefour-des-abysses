init offset = -1












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
    left_bar Frame("gui/bar/left.webp", gui.bar_borders, tile=gui.bar_tile)
    right_bar Frame("gui/bar/right.webp", gui.bar_borders, tile=gui.bar_tile)

style vbar:
    xsize gui.bar_size
    top_bar Frame("gui/bar/top.webp", gui.vbar_borders, tile=gui.bar_tile)
    bottom_bar Frame("gui/bar/bottom.webp", gui.vbar_borders, tile=gui.bar_tile)

style scrollbar:
    ysize gui.scrollbar_size
    base_bar Frame("gui/scrollbar/horizontal_[prefix_]bar.webp", gui.scrollbar_borders, tile=gui.scrollbar_tile)
    thumb Frame("gui/scrollbar/horizontal_[prefix_]thumb.webp", gui.scrollbar_borders, tile=gui.scrollbar_tile)

style vscrollbar:
    xsize gui.scrollbar_size
    base_bar Frame("gui/scrollbar/vertical_[prefix_]bar.webp", gui.vscrollbar_borders, tile=gui.scrollbar_tile)
    thumb Frame("gui/scrollbar/vertical_[prefix_]thumb.webp", gui.vscrollbar_borders, tile=gui.scrollbar_tile)

style slider:
    ysize gui.slider_size
    base_bar Frame("gui/slider/horizontal_[prefix_]bar.webp", gui.slider_borders, tile=gui.slider_tile)
    thumb "gui/slider/horizontal_[prefix_]thumb.webp"

style vslider:
    xsize gui.slider_size
    base_bar Frame("gui/slider/vertical_[prefix_]bar.webp", gui.vslider_borders, tile=gui.slider_tile)
    thumb "gui/slider/vertical_[prefix_]thumb.webp"


style frame:
    padding gui.frame_borders.padding
    background Frame("gui/frame.webp", gui.frame_borders, tile=gui.frame_tile)

style terminal_frame:
    padding gui.frame_borders.padding
    background Frame("gui/terminal_frame.webp", gui.frame_borders, tile=gui.frame_tile)

style window_terminal is window:
    background Image("gui/terminal_frame.webp", xalign=0.5, yalign=1.0)





















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




    if not renpy.variant("small"):
        add SideImage() xalign 0.0 yalign 1.0



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

    background Image("gui/textbox.webp", xalign=0.5, yalign=1.0)

style namebox:
    xpos gui.name_xpos
    xanchor gui.name_xalign
    xsize gui.namebox_width
    ypos gui.name_ypos
    ysize gui.namebox_height

    background Frame("gui/namebox.webp", gui.namebox_borders, tile=gui.namebox_tile, xalign=gui.name_xalign)
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











screen input(prompt):
    style_prefix "input"

    window:

        has vbox
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










screen choice(items):
    style_prefix "choice"

    vbox:
        for i in items:
            hbox:
                if i.chosen == True:
                    $ i.caption = i.caption + " ✓"
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







screen quick_menu():


    zorder 100

    if quick_menu:

        frame:
            xalign 0.5
            yalign 0.9999
            has hbox
            style_prefix "quick"

            xalign 0.5
            yalign 0.9999


            textbutton _("Historique") action ShowMenu('history')
            textbutton _("Avance rapide") action Skip() alternate Skip(fast=True, confirm=True)
            textbutton _("Auto") action Preference("auto-forward", "toggle")
            textbutton _("Sauvegarder") action ShowMenu('save')
            textbutton _("Charger") action ShowMenu('load')
            textbutton _("option") action ShowMenu('preferences')





init python:
    config.overlay_screens.append("quick_menu")

default quick_menu = True

style quick_button is default
style quick_button_text is button_text

style quick_button:
    properties gui.button_properties("quick_button")

style quick_button_text:
    properties gui.text_properties("quick_button")











image logomin = "logomin.webp"

screen navigation():

    vbox:
        style_prefix "navigation"

        xpos 0
        yalign 0.65

        spacing gui.navigation_spacing

        if main_menu:

            textbutton _("{b}{size=34}Nouvelle partie") action Start()

        else:

            textbutton _("Historique") action ShowMenu("history")

            textbutton _("Sauvegarde") action ShowMenu("save")

        textbutton _("{b}Charger") action ShowMenu("load")

        textbutton _("Options") action ShowMenu("preferences")

        if _in_replay:

            textbutton _("Fin de la rediffusion") action EndReplay(confirm=True)

        elif not main_menu:

            textbutton _("Menu principal") action MainMenu()

        if main_menu:

            frame:
                textbutton _("{b}Histoire Multiple \n sur Google Play Livre !") action OpenURL ("https://play.google.com/store/books/details?id=5xxpEQAAQBAJ")

            textbutton _("Extra") action ShowMenu("about")



        if renpy.variant("pc") or (renpy.variant("web") and not renpy.variant("mobile")):



            textbutton _("Aide") action ShowMenu("help")

        if renpy.variant("pc"):



            textbutton _("Quitter") action Quit(confirm=not main_menu)


style navigation_button is gui_button
style navigation_button_text is gui_button_text

style navigation_button:
    size_group "navigation"
    properties gui.button_properties("navigation_button")

style navigation_button_text:
    properties gui.text_properties("navigation_button")








screen main_menu():
    tag menu



    add gui.main_menu_background

    frame:
        style "main_menu_frame"



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

    background "gui/overlay/main_menu_[oversplash].webp"

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












screen game_menu(title, scroll=None, yinitial=0.0, spacing=0):

    style_prefix "game_menu"

    if main_menu:
        add gui.main_menu_background
    else:
        add gui.game_menu_background

    frame:
        style "game_menu_outer_frame"

        has hbox


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

                    has vbox
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

    background "gui/overlay/game_menu.webp"

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










screen about():
    tag menu




    use game_menu(_("Extra"), scroll="viewport"):
        style_prefix "extra"
        frame:
            xpadding 50
            ypadding 50
            has vbox
            textbutton _("Crédits") action ShowMenu('generique')
            textbutton _("Galerie") action ShowMenu('galerie')
            textbutton _("Changelog") action ShowMenu("Changelog")
            textbutton _('Succès') action ShowMenu("achievement_menu")
            textbutton _('Des mêmes Créateurices') action ShowMenu("Other")

    python:
        style.extra = Style(style.default)
        style.extra_button.background = None
        style.extra_button_text.color = "#190030"
        style.extra_button_text.hover_color = "#718effff"
        style.extra_button_text.selected_color = "#86f1ff"
        style.extra_button_text.size = 90

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




    use game_menu(_("Extra"), scroll="viewport"):
        style_prefix "about"

        vbox:

            label "[config.name!t]":
                background Solid('#ffffff')
            text _("Version [config.version!t]\n"):
                outlines [ (absolute(2), "#000000", absolute(0), absolute(0)) ]



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
            label _("Modèles utilisés")
            text _("Principes généraux - fairedesjeux.fr")
            text _("Succès - Angel Seraph")
            text _("Inventaire - insipid- sur reddit")
            label _("Scénario")
            text _("Julia l'inconnue \n Charasime \m Powart")
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
        add "sp/achievementbg.webp" at Position(xpos=0.85, ypos=0.1, xanchor=0.5, yanchor=0.5)
        text _("{size=22}Nouveau succès débloqué:\n") + achievetext + "{/size}" id "achievetext" at Position(xpos=0.85, ypos=0.1, xanchor=0.5, yanchor=0.5) xmaximum 290 ymaximum 90
    timer 3.0 action Hide("gain_achieve")

init python:


    g = Gallery()
    g.transition = fade
    g.navigation = True






    g.button("decors")
    g.unlock_image("anifond","fond ecole")
    g.unlock_image("fonddroite2","fond droite")
    g.unlock_image("projecteur1","fond gauche")
    g.unlock_image("projecteur2","fond gauche")
    g.unlock_image("fond reboot")
    g.unlock_image("fond Void_room")
    g.unlock_image("anifond 2","fond trans")
    g.unlock_image("anifond","fond ecole fake")
    g.unlock_image("fond reboot fake")
    g.unlock_image("anifond")
    g.unlock_image("anifond 2")
    g.unlock_image("pacrel_nuit")
    g.unlock_image("fondcafecreaB", "fondcafecreaF")
    g.unlock_image("fondcafecreaB N", "fondcafecreaF")
    g.unlock_image("Pic_ombre_ch1joa")
    g.unlock_image("fond prison_LJDV")
    g.unlock_image("Fond prison_LJDV_barre")

    g.button("personnages")
    g.unlock_image("ju splain")
    g.unlock_image("ju wu")
    g.unlock_image("ju plexe")
    g.unlock_image("ju plexe_C")
    g.image("ju plexe_C2")
    g.unlock_image("ju sad")
    g.unlock_image("ju re")
    g.unlock_image("ju fear")
    g.unlock_image("ju ink")
    g.unlock_image("juposteur happy")
    g.unlock_image("joassis marche")
    g.unlock_image("joassis")
    g.unlock_image("ajaiassis marche")
    g.unlock_image("ajaiassis")
    g.unlock_image("joa C")
    g.unlock_image("joa P")
    g.unlock_image("joa R")
    g.unlock_image("Charasime Eery")
    g.unlock_image("Charasime psycho")
    g.image("Charasime deter")
    g.image("Charasime deter_R")
    g.image("Charasime damn")
    g.image("Charasime blush")
    g.image("Charasime cry")
    g.image("Charasime fear")
    g.image("Charasime happy")

    g.button("memes")
    g.unlock_image("Logo2")
    g.image("buff vap")

    g.button("cutscenes")
    g.image("Unfinished")


    g.transition = dissolve


screen galerie:
    tag menu




    add "fond Void_room"
    style_prefix "about"


    label _("{b}{color=#FFFFFF}{size=100}Galerie") xalign 0.5 yalign 0.1:
        background Solid('#000000d4')
    grid 2 2:

        xfill True
        yfill True


        add g.make_button("decors", "UI/galerie/underground.webp", xalign=0.5, yalign=0.5)
        add g.make_button("personnages", "UI/galerie/Edwin.webp", xalign=0.5, yalign=0.5)

        add g.make_button("memes", "UI/galerie/klarpear.webp", xalign=0.5, yalign=0.5)
        add g.make_button("cutscenes", "UI/galerie/cutscene.webp", xalign=0.5, yalign=0.5)




    frame:
        xalign 0.5
        yalign 0.55
        textbutton _("Retour") action Return()

screen Other():
    tag menu

    use game_menu(_("Extra"), scroll="viewport"):
        style_prefix "about"

        label _("Julia L'Inconnue") xalign 0.5 yalign 0.4
        textbutton _("Youtube") action OpenURL ("https://www.youtube.com/@julienlinconnu") xalign 0.3 yalign 0.5
        textbutton _("Instagram") action OpenURL ("https://www.instagram.com/julienlinconnu/") xalign 0.3 yalign 0.5
        textbutton _("Google Livre") action OpenURL ("https://play.google.com/store/books/details?id=5xxpEQAAQBAJ") xalign 0.3 yalign 0.5
        label _("PoWarT_") xalign 0.3 yalign 0.6
        textbutton _("Instagram") action OpenURL("https://www.instagram.com/po0wpowar/") xalign 0.3 yalign 0.7
        label _("Charasime") xalign 0.3 yalign 0.8
        textbutton _("Youtube") action OpenURL("https://www.youtube.com/channel/UC3DDibM0MkPNR8Gaxqa13Mw") xalign 0.3 yalign 0.9
        textbutton _("Instagram") action OpenURL("https://www.instagram.com/charasime/") xalign 0.3 yalign 0.9

        frame:
            xalign 0.5
            yalign 0.9
            textbutton _("Retour") action Return()



init python:
    splashtexts = {
    1 : {"texth" : "{color=#ffffff}You got absolutely no bitches", "textb" : "{color=#ffffff}Not a single maiden"},
    2 : {"texth" : "{color=#ffffff}Top text", "textb" : "{color=#ffffff}Bottom text"},
    3 : {"texth" : "{color=#ffffff}Un principe de texte d'intro", "textb" : "{color=#ffffff}honteusement dérobé à la funkin team"},
    4 : {"texth" : "{color=#ffffff}Tu as détruit ton monde.", "textb" : "{color=#ffffff}Nous ne pouvons pas te laisser impuni."},
    5 : {"texth" : "{color=#ffffff}The grievous lady may not have a face", "textb" : "{color=#ffffff}but she sees everything"},
    6 : {"texth" : "{color=#ffffff}Crazy?", "textb" : "{color=#ffffff}I was crazy once !"},
    7 : {"texth" : "{color=#ffffff}Si ce jeu est fini un jour,", "textb" : "{color=#ffffff}je pense que pas grand monde y jouera"},
    8 : {"texth" : "{color=#ffffff}La perfection n'est pas atteignable", "textb" : "{color=#ffffff}mais Charasime a un cheat code"},
    9 : {"texth" : "{color=#ffffff}J'ai peur et j'ai froid...", "textb" : "{color=#ffffff}La solitude me dévaste..."},
    10 : {"texth" : "{color=#ffffff}S'il ne répond pas à nos attentes,", "textb" : "{color=#ffffff}nous reprendrons la main"},
    11 : {"texth" : "{color=#ffffff}La malveillance est max", "textb" : "{color=#ffffff}mais le skill est min"},
    12 : {"texth" : "{color=#ffffff}Entre l'antagoniste et l'écrivain,", "textb" : "{color=#ffffff}qui est vraiment responsable de la fin du monde?"},
    13 : {"texth" : "{color=#ffffff} \"Non désolée :emoji_décu_pointant_le_ciel:\"", "textb" : "{color=#ffffff}- LaJoieDeVivre"},
    14 : {"texth" : "{color=#ffffff}La raclette va au placard à couvert", "textb" : "{color=#ffffff}et les couverts dans le four à micro-ondes"},
    15 : {"texth" : "{color=#ffffff}Ce splash screen", "textb" : "{color=#ffffff}m'as pris beaucoup trop de temps"},
    16 : {"texth" : "{color=#ffffff}Des fois,", "textb" : "{color=#ffffff}je pense"},
    17 : {"texth" : "{color=#ffffff}Stop posting about Among Us", "textb" : "{color=#ffffff}I'm tired of seeing it"},
    18 : {"texth" : "{color=#ffffff}Kasane Teto supremacy", "textb" : "{color=#ffffff}Pearto mass destruction weapon"},
    19 : {"texth" : "{color=#ffffff}hey guys", "textb" : "{color=#ffffff}did you know that in term of male human and fem-"},
    20 : {"texth" : "{color=#ffffff}Edmes a beau avoir formatté à tour de bras,", "textb" : "{color=#ffffff}il n'a jamais tué personne."},
    21 : {"texth" : "{color=#ffffff}Mieux que Garten of BanBan", "textb" : "{color=#ffffff}depuis l'old alpha 1.0"},
    22 : {"texth" : "{color=#ffffff}We are so back", "textb" : "{color=#ffffff}We are getting this game"},
    23 : {"texth" : "{color=#ffffff}Y a plus besoin de soutenir Meurice", "textb" : "{color=#ffffff}Il est à Nova maintenant"},
    24 : {"texth" : "{color=#ffffff}Attention aux rhinocéros", "textb" : "{color=#ffffff}Ils se propagent vite ces cons"},
    25 : {"texth" : "{color=#ffffff}I like thigh highs", "textb" : "{color=#ffffff}especially when I'm wearing them"},
    26 : {"texth" : "{color=#ffffff}Tout est politique", "textb" : "{color=#ffffff}Même dire l'inverse"},
    27 : {"texth" : "{color=#ffffff}Faire tout brûler", "textb" : "{color=#ffffff}faire tout péter"},
    28 : {"texth" : "{color=#ffffff}Méééé euh... puisque je vous dis que je savais pas", "textb" : "{color=#ffffff}C'est pas ma faute si à Betharram y avait des enfants et des prêtres."},
    29 : {"texth" : "{color=#ffffff}I'll make you say", "textb" : "{color=#ffffff}How proud you are of me"},
    30 : {"texth" : "{color=#ffffff}MGED en bikini", "textb" : "{color=#ffffff}Charasime ravie et Joa terrifiée"},
    31 : {"texth" : "{color=#ffffff}Bourré, Jules écrit", "textb" : "{color=#ffffff}tout son code en une ligne"},
    32 : {"texth" : "{color=#ffffff}Faites des poutous", "textb" : "{color=#ffffff}Votou Poutez"},
    33 : {"texth" : "{color=#ffffff}Une biologiste dessinatrice ? Et puis quoi encore ?", "textb" : "{color=#ffffff}Une biologiste programmeuse ?"},
    34 : {"texth" : "{color=#ffffff}Notre accord avec ce dieu sera grandiose !", "textb" : "{color=#ffffff}Qu'est ce qui pourrait mal se passer ?"},
    35 : {"texth" : "{color=#ffffff}Les GB dominent le monde", "textb" : "{color=#ffffff}Et les EIPI dominent le shitpost"},
    36 : {"texth" : "{color=#ffffff}All the singles furries", "textb" : "{color=#ffffff}All the singles furries"},
    37 : {"texth" : "{color=#ffffff}Shikanoko nokonoko", "textb" : "{color=#ffffff}Koshitantan"},
    38 : {"texth" : "Bizarre, un peu", "textb" : "les leaks de Pokemon"},
    39 : {"texth" : "{color=#ffffff}Imagine prendre plus de 2 ans à comprendre", "textb" : "{color=#ffffff}comment faire fonctionner la présentation de texte correctement"},
    40 : {"texth" : "Connection terminated", "textb" : "I'm sorry to interrupt you Elizabeth"},
    41 : {"texth" : "Cranking it", "textb" : "All the way"},
    42 : {"texth" : "{color=#ffffff}J'ai enlevé les spagettis", "textb" : "{color=#ffffff}Le code est désormais un peu plus propre"},
    43 : {"texth" : "{color=#ffffff}Tellement de lignes ici", "textb" : "{color=#ffffff}ont perdu leur contexte"},
}




screen mainUI:
    imagebutton auto "aventure %s":
        focus_mask True
        xpos 0.07
        ypos 0.73
        action Jump("aventure")
    imagebutton auto "discuter %s":
        focus_mask True
        xpos 0.3
        ypos 0.73
        action Jump("menu1")
    imagebutton auto "explorer %s":
        focus_mask True
        xpos 0.6
        ypos 0.73
        action Jump("menu111face")
    imagebutton auto "coden %s":
        focus_mask True
        xpos 0.83
        ypos 0.73
        action Jump("menu2")
    imagebutton auto "exit %s":
        focus_mask True
        xpos 0.83
        ypos 0.05
        action Jump("menu3")

screen whiteUI:
    imagebutton auto "discuter %s":
        focus_mask True
        xpos 0.3
        ypos 0.73
        action Jump("inverted1")
    imagebutton auto "exit %s":
        focus_mask True
        xpos 0.6
        ypos 0.73
        action Jump("whiteexit")

screen blackUI:
    imagebutton auto "discuter %s":
        focus_mask True
        xpos 0.3
        ypos 0.73
        action Jump("offlinemenu1")
    imagebutton auto "exit %s":
        focus_mask True
        xpos 0.6
        ypos 0.73
        action Jump("blackexit")

screen arcade_borne:
    imagebutton auto "arcade %s":
        focus_mask True
        sensitive choc
        xpos 0.38
        ypos 0.3
        if tupin:
            action [ToggleScreen("arcade"), Hide (screen = None), Hide ("inventory")]
        else:
            action Jump ("err_borne")
    if tupin:
        imagebutton auto "chr/Statisticien/statisticien_arcade_%s.webp":
            focus_mask True
            xpos 0.5691
            ypos 0.43
            sensitive floscreenswitch
            action [Hide (screen = None), Jump ("flo_rep")]

style terminal_button:
    color "#00ff26"
    size 50
    font "gui/DigitTech16-Regular.ttf"

screen flotrain:
    imagebutton auto "chr/Statisticien/statisticien_train_%s.webp":
        focus_mask True
        sensitive choc
        xpos 0.129
        ypos 0.362
        action [Hide (screen = None), Jump("flotrain")]

screen arcade:
    add "arcade_terminal"
    textbutton "> Tetris (sDextra)":
        xpos 0.3
        ypos 0.3
        background '#011400'
        hover_background '#004303'
        text_style "terminal_button"
        action [Hide (screen = None), Jump("tetris_start")]
    textbutton "> Solitaire (Susan The Cat)":
        xpos 0.3
        ypos 0.4
        background '#011400'
        hover_background '#004303'
        text_style "terminal_button"
        action [Hide (screen = None), Jump("newgame_solitaire")]
    textbutton "> Minesweeper (Andredron)":
        xpos 0.3
        ypos 0.5
        background '#011400'
        hover_background '#004303'
        text_style "terminal_button"
        action [Hide (screen = None), Jump("minesweeper_start")]
    textbutton "> Retour":
        xpos 0.3
        ypos 0.85
        text_style "terminal_button"
        background '#011400'
        hover_background '#004303'
        action [Hide (screen = None), Jump("menu111droite"), Call("inventory")]



screen aventure:
    add "Miclordes_trans"
    add "Miclordes"

    imagebutton auto "aventureprincipale %s":
        focus_mask True
        xpos 0.05
        ypos 0.05
        action [ToggleScreen("aventure_P"), Hide (screen = None), Play("music", "audio/A day in the unknown.ogg", loop=True, fadein=3)]
    imagebutton auto "UI/Aventure/RPG %s.webp":
        focus_mask True
        xpos 0.05
        ypos 0.35
        action [ToggleScreen("RPG"), Hide (screen = None), Play("music", "audio/A day in the unknown.ogg", loop=True, fadein=3)]
    imagebutton auto "UI/Aventure/romance %s.webp":
        focus_mask True
        xpos 0.28
        ypos 0.37
        action [ToggleScreen("romance"), Hide (screen = None), Play("music", "audio/A day in the unknown.ogg", loop=True, fadein=3)]
    imagebutton auto "UI/Aventure/tribunal %s.webp":
        focus_mask True
        xpos 0.50
        ypos 0.37
        action [ToggleScreen("tribunal"), Hide (screen = None), Play("music", "audio/A day in the unknown.ogg", loop=True, fadein=3)]
    imagebutton auto "UI/Aventure/world %s.webp":
        focus_mask True
        xpos 0.72
        ypos 0.35
        action [ToggleScreen("world"), Hide (screen = None), Play("music", "audio/A day in the unknown.ogg", loop=True, fadein=3)]
    frame:
        xalign 0.5
        yalign 0.95
        textbutton _("Retour") action [Play("music", "audio/A day in the unknown.ogg", loop=True, fadein=3), Jump ("menu0")]

screen aventure_P:
    add "Aventure AP"

    imagebutton auto "UI/Aventure/porte1 %s.webp":
        xpos 0.10
        ypos 0.198
        action [ToggleScreen("aventure_P_perso"), Hide (screen = None)]
    imagebutton auto "UI/Aventure/porte2 %s.webp":
        xpos 0.55
        ypos 0.198
        action [ToggleScreen("aventure_P_crea"), Hide (screen = None)]
    frame:
        xalign 0.5
        yalign 0.95
        textbutton _("Retour") action [ToggleScreen ("aventure"), Hide (screen = None), Play("music", "audio/Miclordes.ogg", loop=True, fadein=3)]

init python:
    import subprocess

screen RPG:
    add "UI/RPG/RPG_intro.webp"
    $ rpg_path = rpg_path.replace("\\\\","/")

    text "{size=200}{color=#000000}R.P.G":
        xpos 0.05
        ypos 0.1

    if renpy.variant("pc") and os.path.exists (rpg_path):
        textbutton _("{size=100}Jouer") action Jump ("RPG"):
            xpos 0.1
            ypos 0.5
    elif renpy.variant("pc"):
        textbutton _("{size=100}Jouer") action [Notify (_("Quelque chose manque pour que ça fonctionne ! Pensez à ajouter le plugin RPG aux fichiers !")), Confirm(_("Souhaitez vous être redirigé vers la page du module correspondant ?"), OpenURL("https://julialinconnue.itch.io/carrefour-des-abysses-rpg"), Notify ("Quelque chose manque pour que ça fonctionne ! Pensez à ajouter le plugin RPG aux fichiers !"))]:
            xpos 0.1
            ypos 0.5
    else:
        text _("Le lien au logiciel RPG n'est"):
            xpos 0
            ypos 0.35
        text _("pas établissable à partir de"):
            xpos 0
            ypos 0.40
        text _("lui même sur cette"):
            xpos 0
            ypos 0.45
        text _("plateforme :("):
            xpos 0
            ypos 0.50

    textbutton _("{size=100}Retour") action [ToggleScreen ("aventure"), Hide (screen = None), Play("music", "audio/Miclordes.ogg", loop=True, fadein=3)]:
        xpos 0.075
        ypos 0.7

screen romance:
    add "UI/Romance/Romance_intro.webp"
    text "{size=200}{color=#000000}Romance":
        xpos 0.27
        ypos -0.02
    frame:
        xalign 0.5
        yalign 0.95
        textbutton _("Retour") action [ToggleScreen ("aventure"), Hide (screen = None), Play("music", "audio/Miclordes.ogg", loop=True, fadein=3)]

screen tribunal:
    add "UI/Tribunal/Tribunal_intro.webp"
    text "{size=200}{color=#000000}Tribunal":
        xpos 0.27
        ypos -0.02
    frame:
        xalign 0.5
        yalign 0.95
        textbutton _("Retour") action [ToggleScreen ("aventure"), Hide (screen = None), Play("music", "audio/Miclordes.ogg", loop=True, fadein=3)]

screen world:
    add "UI/World/World_intro.webp"
    text "{size=150}{color=#000000}World":
        xpos 0.75
        ypos 0.2
    textbutton _("{size=60}Prendre un billet") action Jump ("world"):
        xpos 0.73
        ypos 0.5
    frame:
        xalign 0.9
        yalign 0.95
        textbutton _("Retour") action [ToggleScreen ("aventure"), Hide (screen = None), Play("music", "audio/Miclordes.ogg", loop=True, fadein=3)]

screen aventure_P_perso:
    add "Aventure HP"
    viewport id "aventure_P":
        scrollbars "horizontal"
        mousewheel "horizontal"
        draggable True
        area (0,0,1920,840)
        child_size (10010, 1000)

        imagebutton auto "Aventure_P %s":
            focus_mask True
            xpos 10
            ypos 0
            action [ToggleScreen("pacrel"), Hide (screen = None)]
        imagebutton auto "Aventure_Null %s":
            focus_mask True
            xpos 510
            ypos 0
            action Notify(_("Cette section n'est pas encore disponible"))
        imagebutton auto "Aventure_Null %s":
            focus_mask True
            xpos 1010
            ypos 0
            action Notify(_("Cette section n'est pas encore disponible"))
        imagebutton auto "Aventure_Null %s":
            focus_mask True
            xpos 1510
            ypos 0
            action Notify(_("Cette section n'est pas encore disponible"))
        imagebutton auto "Aventure_Null %s":
            focus_mask True
            xpos 2010
            ypos 0
            action Notify(_("Cette section n'est pas encore disponible"))
        imagebutton auto "Aventure_Null %s":
            focus_mask True
            xpos 2510
            ypos 0
            action Notify(_("Cette section n'est pas encore disponible"))
        imagebutton auto "Aventure_Null %s":
            focus_mask True
            xpos 3010
            ypos 0
            action Notify(_("Cette section n'est pas encore disponible"))
        imagebutton auto "Aventure_Null %s":
            focus_mask True
            xpos 3510
            ypos 0
            action Notify(_("Cette section n'est pas encore disponible"))
        imagebutton auto "Aventure_Null %s":
            focus_mask True
            xpos 4010
            ypos 0
            action Notify(_("Cette section n'est pas encore disponible"))
        imagebutton auto "Aventure_Null %s":
            focus_mask True
            xpos 4510
            ypos 0
            action Notify(_("Cette section n'est pas encore disponible"))
        imagebutton auto "Aventure_Null %s":
            focus_mask True
            xpos 5010
            ypos 0
            action Notify(_("Cette section n'est pas encore disponible"))
        imagebutton auto "Aventure_Null %s":
            focus_mask True
            xpos 5510
            ypos 0
            action Notify(_("Cette section n'est pas encore disponible"))
        imagebutton auto "Aventure_Null %s":
            focus_mask True
            xpos 6010
            ypos 0
            action Notify(_("Cette section n'est pas encore disponible"))
        imagebutton auto "Aventure_Null %s":
            focus_mask True
            xpos 6510
            ypos 0
            action Notify(_("Cette section n'est pas encore disponible"))
        imagebutton auto "Aventure_Null %s":
            focus_mask True
            xpos 7010
            ypos 0
            action Notify(_("Cette section n'est pas encore disponible"))
        imagebutton auto "Aventure_Null %s":
            focus_mask True
            xpos 7510
            ypos 0
            action Notify(_("Cette section n'est pas encore disponible"))
        imagebutton auto "Aventure_Null %s":
            focus_mask True
            xpos 8010
            ypos 0
            action Notify(_("Cette section n'est pas encore disponible"))
        imagebutton auto "Aventure_Null %s":
            focus_mask True
            xpos 8510
            ypos 0
            action Notify(_("Cette section n'est pas encore disponible"))
        imagebutton auto "Aventure_Null %s":
            focus_mask True
            xpos 9010
            ypos 0
            action Notify(_("Cette section n'est pas encore disponible"))
        imagebutton auto "Aventure_Null %s":
            focus_mask True
            xpos 9510
            ypos 0
            action Notify(_("Cette section n'est pas encore disponible"))
    frame:
        xalign 0.5
        yalign 0.95
        textbutton _("Retour") action [ToggleScreen ("aventure_P"), Hide (screen = None)]



screen aventure_P_crea:
    add "Aventure HP"

    viewport:
        scrollbars "horizontal"
        spacing 5
        mousewheel "horizontal"
        draggable True
        area (0,0,1920,840)
        child_size (6010, 1000)

        imagebutton auto "Aventure_LJDV %s":
            focus_mask True
            xpos 10
            ypos 0
            action [ToggleScreen("LJDV"), Hide (screen = None)]
        imagebutton auto "Aventure_Ajai %s":
            focus_mask True
            xpos 510
            ypos 0
            action [ToggleScreen("Powart"), Hide (screen = None)]
        imagebutton auto "Aventure_Null %s":
            focus_mask True
            xpos 1010
            ypos 0
            action Notify(_("Cette section n'est pas encore disponible"))
        imagebutton auto "Aventure_Null %s":
            focus_mask True
            xpos 1510
            ypos 0
            action Notify(_("Cette section n'est pas encore disponible"))
        imagebutton auto "Aventure_Null %s":
            focus_mask True
            xpos 2010
            ypos 0
            action Notify(_("Cette section n'est pas encore disponible"))
        imagebutton auto "Aventure_Null %s":
            focus_mask True
            xpos 2510
            ypos 0
            action Notify(_("Cette section n'est pas encore disponible"))
        imagebutton auto "Aventure_Null %s":
            focus_mask True
            xpos 3010
            ypos 0
            action Notify(_("Cette section n'est pas encore disponible"))
        imagebutton auto "Aventure_Null %s":
            focus_mask True
            xpos 3510
            ypos 0
            action Notify(_("Cette section n'est pas encore disponible"))
        imagebutton auto "Aventure_Null %s":
            focus_mask True
            xpos 4010
            ypos 0
            action Notify(_("Cette section n'est pas encore disponible"))
        imagebutton auto "Aventure_Null %s":
            focus_mask True
            xpos 4510
            ypos 0
            action Notify(_("Cette section n'est pas encore disponible"))
        imagebutton auto "Aventure_Null %s":
            focus_mask True
            xpos 5010
            ypos 0
            action Notify(_("Cette section n'est pas encore disponible"))
        imagebutton auto "Aventure_Null %s":
            focus_mask True
            xpos 5510
            ypos 0
            action Notify(_("Cette section n'est pas encore disponible"))
    frame:
        xalign 0.5
        yalign 0.95
        textbutton _("Retour") action [ToggleScreen ("aventure_P"), Hide (screen = None)]



screen pacrel:
    style_prefix "aventurep"
    add "Aventure_fond pacrel"

    vbox:
        xalign 0.1
        yalign 0.7
        textbutton _("Prologue") action [Jump("prologue_pacrel"), Hide (screen = None)]
        if persistent.p0:
            if expé:
                textbutton _("Chapitre 1 early access") action [Jump("Ch1_pacrel"), Hide (screen = None)]
            else:
                textbutton _("Chapitre 1") action Notify(_("Cette section n'est pas encore disponible"))
        if persistent.p1:
            textbutton _("Chapitre 2") action Notify(_("Cette section n'est pas encore disponible"))
        if persistent.p2:
            textbutton _("Chapitre 3") action Notify(_("Cette section n'est pas encore disponible"))
        if persistent.p3:
            textbutton _("Chapitre 4") action Notify(_("Cette section n'est pas encore disponible"))
        if persistent.p4:
            textbutton _("Epilogue") action Notify(_("Cette section n'est pas encore disponible"))
        textbutton _("Retour") action [ToggleScreen ("aventure_P_perso"), Hide (screen = None)]

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
        if persistent.LJDV0:
            textbutton _("Chapitre 1") action [Jump("Ch1_LJDV"), Hide (screen = None)]
        if persistent.LJDV1:
            textbutton _("Chapitre 2") action Notify(_("Cette section n'est pas encore disponible"))
        textbutton _("Retour") action [ToggleScreen ("aventure_P_crea"), Hide (screen = None)]

    python:
        style.aventurej = Style(style.default)
        style.aventurej_button.background = None
        style.aventurej_button_text.color = "#ff0000"
        style.aventurej_button_text.hover_color = "#ff9100ff"
        style.aventurej_button_text.selected_color = "#d4ff00"
        style.aventurej_button_text.size = 80    

screen event_config:
    frame:
        xalign 0.41
        yalign 0.59
        has vbox
        textbutton _("{size=30}Nouvel An(inactif)") action [SetVariable("today_event", "_NY"), Hide (screen = None)]
        textbutton _("{size=30}Saint-Valentin(inactif)") action [SetVariable("today_event", "_keur"), Hide (screen = None)]
        textbutton _("{size=30}Printemps(inactif)") action [SetVariable("today_event", "_egg"), Hide (screen = None)]
        textbutton _("{size=30}Premier avril(inactif)") action [SetVariable("today_event", "_pwasson"), Hide (screen = None)]
        textbutton _("{size=30}Premier mai(inactif)") action [SetVariable("today_event", "_komrad"), Hide (screen = None)]
        textbutton _("{size=30}Halloween") action [SetVariable("today_event", "_halloween"), Hide (screen = None)]
        textbutton _("{size=30}Noël(inactif)") action [SetVariable("today_event", "_Krima"), Hide (screen = None)]
        textbutton _("{size=30}autre") action [SetVariable("today_event", ""), Hide (screen = None)]

screen Powart:
    style_prefix "aventurePowart"
    add "Aventure_fond Powart"

    vbox:
        xalign 0.1
        yalign 0.5
        textbutton _("Prologue") action [Jump("prologue_Powart"), Hide (screen = None)]
        if persistent.Powart0:
            textbutton _("Chapitre 1") action Notify(_("Cette section n'est pas encore disponible"))
        textbutton _("Retour") action [ToggleScreen ("aventure_P_crea"), Hide (screen = None)]

    python:
        style.aventurePowart = Style(style.default)
        style.aventurePowart_button.background = None
        style.aventurePowart_button_text.color = "#050049"
        style.aventurePowart_button_text.hover_color = "#3c00ffff"
        style.aventurePowart_button_text.selected_color = "#00593e"
        style.aventurePowart_button_text.size = 80




init python:
    def label_callback(name, abnormal):
        store.last_label = name

    config.label_callback = label_callback

screen inventory:
    zorder 200
    frame:
        background "#99ff9900"
        xalign 0.01
        yalign 0.02

        imagebutton auto "inventory %s":
            focus_mask True
            xpos 0.01
            ypos 0.02
            action ToggleScreen("inventory_item_description")

    on "hide" action Hide("inventory_item_description")

default item_descriptions = {
    _("Trilogie Histoire Multiple") : _("Trois bouquins sur un mec random qui se bat pour sauver sa créatrice de son alter-ego et de dieux"),
    _("Rapport OFAC 105") : _("Une annonce d'un accord entre des dieux et l'OFAC contre un créateur")}
default inventory_items = []
default item_description = ""

style inv_button is frame:
    xsize 200
    ysize 100

style inv_button_text:
    xalign 0.5
    yalign 0.5

screen inventory_item_description:

    modal True
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

        has hbox
        box_wrap True
        box_wrap_spacing 10
        spacing 10
        xoffset 20
        yoffset 20
        style_prefix "inv"
        for item in inventory_items:
            imagebutton:
                idle ("UI/" + item + " idle.webp")
                hover ("UI/" +item + " hover.webp")
                action SetVariable("item_description", item_descriptions.get(item))
                selected False


    on "hide" action SetVariable("item_description", "")

init python:
    clickcount = 0
    requiredclicks = 10
    timelimit = 60
    bon_timer = ""
    mistimed = ""
    fin = False
    def addclick(bon_timer, requiredclicks):
        if store.clickcount < requiredclicks:
            store.clickcount += 1
        else:
            store.clickcount = 0
            renpy.jump(bon_timer)
            renpy.hide_screen("quicktimebar")

screen quicktimebar(bon_timer, requiredclicks=20, qte_title="Cliquez jusqu'au remplissage de la barre !", fin=False, mistimed="", timelimit=60):
    tag quicktimebar
    frame:
        background None
        xpos 100
        ypos 10
        vbox:
            text "{b}" + str(qte_title):
                size 50
                color "#000000"
                xalign 0.5
            bar value AnimatedValue(value=store.clickcount, range=requiredclicks, delay=1.0, old_value=store.clickcount):
                xsize 1700
                ysize 10
            frame:
                xalign 0.5
                ypos 500
                textbutton _("{color=#2b0000}{size=50}Cliquez ici"):
                    action [Function(addclick, bon_timer,requiredclicks)]

        if fin:
            timer store.timelimit action [SetVariable("clickcount", 0), Jump (mistimed), PauseAudio(channel='music', value=True)]
        else:
            timer store.timelimit action NullAction()



screen directions(gauche=False, dirgauche="", droite=False, dirdroite="", arriere=False, dirarriere="", avant=False, diravant=""):
    if gauche:
        imagebutton auto "droite %s":
            focus_mask True
            at xflip
            xpos 0
            ypos 0.37
            action [Hide (screen = None), Jump(dirgauche)]
    if droite:
        imagebutton auto "droite %s":
            focus_mask True
            xpos 0.79
            ypos 0.37
            action [Hide (screen = None), Jump(dirdroite)]
    if arriere:
        imagebutton auto "back %s":
            focus_mask True
            xpos 0.4
            ypos 0.6
            action [Hide (screen = None), Jump(dirarriere)]
    if avant:
        imagebutton auto "droite %s":
            focus_mask True
            at uppies
            xpos 0.355
            ypos 0.25
            action [Hide (screen = None), Jump(diravant)]

screen Felementjulia:
    imagemap:
        ground "none"
        hotspot (492, 613, 109, 81) action Jump("menu0bis")
        hotspot (709, 396, 497, 296) action Jump("whiteout")
        hotspot (1582, 972, 123, 94) action [Hide ("directions"), Hide ("window"), Show("OFAC1")]
        hotspot (417, 373, 192, 64) action Jump("HMlib")
        hotspot (1296, 375, 211, 59) action Jump("capital")
        hotspot (98, 767, 115, 120) action OpenURL("https://youtu.be/BW78t48Zcq8?si=WMnGnrbIKB_4xMDv")

screen directionsFbis:
    imagemap:
        ground "none"
        hotspot (500, 408, 102, 43) action Jump("menu0")



screen Arret_urgence:
    imagemap:
        ground "BAU"
        hotspot (811, 438, 216, 219) action Jump("menu111bouton")
    imagemap:
        ground "fond reboot"
        hotspot (368, 122, 355, 747) action [Hide (screen = None), Jump ("Gare_Monde_J")]
        hotspot (1127, 127, 354, 757) action [Hide (screen = None), Jump ("Gare_Monde_J")]

screen gare_monde(monde="", affichage=""):
    imagemap:
        ground "gare_monde"
        hotspot (368, 122, 355, 747) action [Hide (screen = None), Jump (monde)]
        hotspot (1127, 127, 354, 757) action [Hide (screen = None), Jump (monde)]
    vbox:
        xalign 0.5
        ypos 0
        text _(affichage)




screen to_inverted():
    vbox:
        xalign 0.5
        yalign 0.5
        textbutton _("{color=#FF0000}{size=100}Résister au vide") action Jump("inverted")

    timer 3.0 action Jump("finwhite")


screen OFAC1():
    frame:
        xsize 1400
        ysize 1080
        background "Rapport_OFAC"
        style_prefix "about"
        has vbox
        xpos 200
        ypos 150

        label _("{b}{size=+2}{color=#000000}Rapport de l'OFAC #105 : Accord avec Dieu")
        text _("{size=-10}Mesdames, Messieurs,\nAprès consultation du bureau d'affaire et du comité permanent de l'OFAC, je suis au plaisir de vous annoncer que nous commençerons dès aujourd'hui un contrat avec Bodias, dieu tout puissant, pour nous assister dans nos tâches. Avec un peu de chance, nous pourrons enfin finir cette affaire Pacrel une fois pour toute ! Il nous a prévenu et demandé la plus grande confidentialité, le prospect de l'existence d'un dieu pouvant créer le chaos et attirer de l'attention sur nos opérations. Plus que jamais, il vous faudra donc détruire ce document dès que consulté. \nUn rendez-vous en personne nous a également permis d'établir que notre existence était sous le couvert d'une autre entité et en danger par cette dernière. Il nous faudra alors sans doute combattre également dans ce cadre cette entité maléfique. \nCordialement, \nFRAQUES Jean, Directeur général de coordination")
        textbutton _("Fermer") action [ Hide ("OFAC1") , Jump ("ofac1")]










screen Changelog():
    tag menu




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



            order_reverse True



            button:
                style "page_label"

                key_events True
                xalign 0.5
                action page_name_value.Toggle()

                input:
                    style "page_label_text"
                    value page_name_value


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









screen screen_language:
    style_prefix "window"
    frame:
        xalign 0.5
        yalign 0.5
        xpadding 50
        ypadding 50
        has vbox
        spacing 45
        label _("{size=90}{space=30}Choisissez une langue")
        vpgrid:
            cols 2
            spacing 500
            textbutton "{size=70}Français" action Language (None),Return()
            textbutton "{size=70}English" action Language ("english"),Return()

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





                vbox:
                    style_prefix "radio"
                    label _("language")
                    textbutton _("Français") text_font "DejaVuSans.ttf" action Language(None)
                    textbutton _("English") text_font "DejaVuSans.ttf" action Language("english")
                vbox:
                    style_prefix "radio"
                    label _("Fonctions admin")
                    textbutton _("Formatage"):
                        action Confirm(_("Tous tes progrès seront supprimés (incluant la galerie et les succès) définitivement (C'est très très long). Es-tu sûr.e ?"), Confirm (_("Tu es vraiment sûr.e de toi ?"),persistent._clear, Return()), Return())
                    textbutton _("Evénement custom") action Show ("event_config")

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
    foreground "gui/button/radio_[prefix_]foreground.webp"

style radio_button_text:
    properties gui.text_properties("radio_button")

style check_vbox:
    spacing gui.pref_button_spacing

style check_button:
    properties gui.button_properties("check_button")
    foreground "gui/button/check_[prefix_]foreground.webp"

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










screen history():
    tag menu




    predict False

    use game_menu(_("Historique"), scroll=("vpgrid" if gui.history_height else "viewport"), yinitial=1.0, spacing=gui.history_spacing):

        style_prefix "history"

        for h in _history_list:

            window:



                has fixed
                yfit True

                if h.who:

                    label h.who:
                        style "history_name"
                        substitute False




                        if "color" in h.who_args:
                            text_color h.who_args["color"]

                $ what = renpy.filter_text_tags(h.what, allow=gui.history_allow_tags)
                text what:
                    substitute False

        if not _history_list:
            label _("L'historique des dialogues est vide.")





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














default frame_conf = "gui/frame.webp"

screen confirm(message, yes_action, no_action, frame_conf="gui/frame.webp"):



    modal True

    zorder 200

    style_prefix "confirm"

    add "gui/overlay/confirm.webp"

    frame:
        background Frame([frame_conf])
        has vbox
        xalign .5
        yalign .5
        spacing 45

        label _(message):
            style "confirm_prompt"
            if frame_conf == "gui/terminal_frame.webp":
                text_style "terminal_button"
            xalign 0.5

        hbox:
            xalign 0.5
            spacing 150
            textbutton _("Oui") action yes_action:
                if frame_conf == "gui/terminal_frame.webp":
                    text_style "terminal_button"
            textbutton _("Non") action no_action:
                if frame_conf == "gui/terminal_frame.webp":
                    text_style "terminal_button"



    key "game_menu" action no_action


style confirm_frame is gui_frame
style confirm_prompt is gui_prompt
style confirm_prompt_text is gui_prompt_text
style confirm_button is gui_medium_button
style confirm_button_text is gui_medium_button_text

style confirm_frame:
    background Frame([ "gui/confirm_frame.webp", "gui/frame.webp"], gui.confirm_frame_borders, tile=gui.frame_tile)
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









screen skip_indicator():

    zorder 100
    style_prefix "skip"

    frame:

        has hbox
        spacing 9

        text _("Avance rapide")

        text "▸" at delayed_blink(0.0, 1.0) style "skip_triangle"
        text "▸" at delayed_blink(0.2, 1.0) style "skip_triangle"
        text "▸" at delayed_blink(0.4, 1.0) style "skip_triangle"




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
    background Frame("gui/skip.webp", gui.skip_frame_borders, tile=gui.frame_tile)
    padding gui.skip_frame_borders.padding

style skip_text:
    size gui.notify_text_size

style skip_triangle:


    font "DejaVuSans.ttf"










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

    background Frame("gui/notify.webp", gui.notify_frame_borders, tile=gui.frame_tile)
    padding gui.notify_frame_borders.padding

style notify_text:
    properties gui.text_properties("notify")








screen nvl(dialogue, items=None):

    window:
        style "nvl_window"

        has vbox
        spacing gui.nvl_spacing


        if gui.nvl_height:

            vpgrid:
                cols 1
                yinitial 1.0

                use nvl_dialogue(dialogue)

        else:

            use nvl_dialogue(dialogue)



        for i in items:

            textbutton i.caption:
                action i.action
                style "nvl_button"

    add SideImage() xalign 0.0 yalign 1.0


screen nvl_dialogue(dialogue):

    for d in dialogue:

        window:
            id d.window_id

            has fixed
            yfit gui.nvl_height is None

            if d.who is not None:

                text d.who:
                    id d.who_id

            text d.what:
                id d.what_id




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

    background "gui/nvl.webp"
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

define bubble.frame = Frame("gui/bubble.webp", 55, 55, 55, 95)
define bubble.thoughtframe = Frame("gui/thoughtbubble.webp", 55, 55, 55, 55)

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







style pref_vbox:
    variant "medium"
    xsize 675




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
    background "gui/phone/textbox.webp"

style radio_button:
    variant "small"
    foreground "gui/phone/button/radio_[prefix_]foreground.webp"

style check_button:
    variant "small"
    foreground "gui/phone/button/check_[prefix_]foreground.webp"

style nvl_window:
    variant "small"
    background "gui/phone/nvl.webp"

style main_menu_frame:
    variant "small"
    background "gui/phone/overlay/main_menu.webp"

style game_menu_outer_frame:
    variant "small"
    background "gui/phone/overlay/game_menu.webp"

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
    left_bar Frame("gui/phone/bar/left.webp", gui.bar_borders, tile=gui.bar_tile)
    right_bar Frame("gui/phone/bar/right.webp", gui.bar_borders, tile=gui.bar_tile)

style vbar:
    variant "small"
    xsize gui.bar_size
    top_bar Frame("gui/phone/bar/top.webp", gui.vbar_borders, tile=gui.bar_tile)
    bottom_bar Frame("gui/phone/bar/bottom.webp", gui.vbar_borders, tile=gui.bar_tile)

style scrollbar:
    variant "small"
    ysize gui.scrollbar_size
    base_bar Frame("gui/phone/scrollbar/horizontal_[prefix_]bar.webp", gui.scrollbar_borders, tile=gui.scrollbar_tile)
    thumb Frame("gui/phone/scrollbar/horizontal_[prefix_]thumb.webp", gui.scrollbar_borders, tile=gui.scrollbar_tile)

style vscrollbar:
    variant "small"
    xsize gui.scrollbar_size
    base_bar Frame("gui/phone/scrollbar/vertical_[prefix_]bar.webp", gui.vscrollbar_borders, tile=gui.scrollbar_tile)
    thumb Frame("gui/phone/scrollbar/vertical_[prefix_]thumb.webp", gui.vscrollbar_borders, tile=gui.scrollbar_tile)

style slider:
    variant "small"
    ysize gui.slider_size
    base_bar Frame("gui/phone/slider/horizontal_[prefix_]bar.webp", gui.slider_borders, tile=gui.slider_tile)
    thumb "gui/phone/slider/horizontal_[prefix_]thumb.webp"

style vslider:
    variant "small"
    xsize gui.slider_size
    base_bar Frame("gui/phone/slider/vertical_[prefix_]bar.webp", gui.vslider_borders, tile=gui.slider_tile)
    thumb "gui/phone/slider/vertical_[prefix_]thumb.webp"

style slider_vbox:
    variant "small"
    xsize None

style slider_slider:
    variant "small"
    xsize 900
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
