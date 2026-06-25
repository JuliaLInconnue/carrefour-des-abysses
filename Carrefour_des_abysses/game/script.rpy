
init:
    transform flip:
        yzoom -1.0
    transform xflip:
        xzoom -1.0
    transform uppies:
        rotate 270
    transform panzoom:
        linear 2 xzoom 2 yzoom 2
    transform AMV:
        linear 0.4 xoffset -50
        linear 0.4 xoffset +50
        repeat
    transform imprimante:
        linear 0.1 xoffset -500
        linear 0.1 xoffset +500
        repeat
    transform Cleugran8:
        linear 0.1 xoffset -50
        linear 0.1 xoffset +50
        repeat
    transform AMH:
        linear 0.4 yoffset -50
        linear 0.4 yoffset +20
        repeat
    transform shake:
        linear 0.04 xoffset -10
        linear 0.04 xoffset +10
        linear 0.04 yoffset -10
        linear 0.04 yoffset +10
        repeat 10


label splashscreen:
    play music "audio/Weirdness ensues.ogg"
    show black
    show presplash
    call screen screen_language 
    with Pause (1)
    if fun==1:
        show logo2 at Position(xpos=0.5,xanchor=0.5,ypos=0.5,yanchor=0.5,) with dissolve
        with Pause (0.5)
        hide logo2 with dissolve
        with Pause (0.5)
    else:
        show logo at Position(xpos=0.5,xanchor=0.5,ypos=0.5,yanchor=0.5,) with dissolve
        with Pause (0.5)
        hide logo with dissolve
        with Pause (0.5)

    show text _ ("{color=#ffffff}Un jeu de la Team Sweep") at Position(xpos=0.5,xanchor=0.5,ypos=0.9,yanchor=0.9) with dissolve
    show TS_Logo at Position(xpos=0.5,xanchor=0.5,ypos=0.5,yanchor=0.5,) with dissolve
    with Pause (1)
    hide text with dissolve
    hide TS_Logo with dissolve
    with Pause (0.5)
    call screen confirm(message=_("Ce jeu peut déplaire à certaines personnes. Souhaitez vous voir les avertissements de contenu ?"), yes_action = [SetVariable ("TriggerWarning",True), Return()], no_action = [SetVariable ("TriggerWarning",False), Return()])
    if TriggerWarning:
        if fun >= 2:
            show text _ ("{color=#ffffff}CW : Thèmes et images perturbantes \n violence, langage grossier, peur") with dissolve
        else:
            show text "CW : no bitches :("
        with Pause (5)
        hide text with dissolve
        with Pause (1)


    show text splashtexts [fun]["texth"] as text1 at Position (ypos=0.4)
    pause 1.0
    show text splashtexts [fun]["textb"] as text2 at Position (ypos=0.6)

    if fun == 1:
        $ Achievement.add(achievement_name['nobitches'])
    elif fun == 38:
        show text "{color=#ffffff}Typhlosion" as text1 at Position (ypos=0.2)
        pause 0.5
        show text "{color=#ffffff}Vaporeon" as text2 at Position (ypos=0.4)
        pause 0.5
        show text "{color=#ffffff}Gardevoire" as text3 at Position (ypos=0.6)
    elif fun == 40:
        pause 1
        hide text1
        hide text2
        pause 1
        show text "{color=#ffffff}Ce jeu contient une grande quantité de" as text1 at Position (ypos=0.4)
        pause 1.0
        $ feddyt = 0.95
        $ feddytxt = 2
        $ feddyx = 0.675
        $ feddyy = 0.382
        while feddyy <1:
            $ renpy.show("presplash text", what = Text ("{color=#ffffff}fun,"), at_list = [Transform(ypos=feddyy, xpos = feddyx)], tag = "text" + str(feddytxt))

            pause feddyt
            python:
                renpy.sound.queue("beeps.ogg")
                feddytxt += 1
                feddyt -= 0.03
                feddyx += 0.035
                if feddyx > 1:
                  feddyx = 0
                  feddyy += 0.025
        $ Achievement.add(achievement_name['fnaf 6'])
    elif fun == 41:
        hide text
        show text "{color=#ffffff}My name is Edwin." as text1 at Position (ypos=0.3)
        pause 1.0
        show text "{color=#ffffff}I made the mimic." as text2 at Position (ypos=0.5)
        pause 1.0
        show text "{color=#ffffff}It was difficult to put the pieces together." as text3 at Position (ypos=0.7)
    with Pause (1)
    hide text
    return


label start:
    stop music
    python:
        if os.name == 'nt': 
          import os
          for name in ('LOGNAME', 'USER', 'LNAME', 'USERNAME'):
            currentuser = os.environ.get(name)
        elif os.name == 'posix':
          import os
          for user in ('LOGNAME', 'USER', 'LNAME', 'USERNAME'):
            currentuser = os.environ.get('USER')
    HUH "Pas mal pour un début."
    play music "audio/A day in the unknown.ogg"
    HUH "Si seulement le conseil savait tout le travail que je mettais là dedans, iels m'auraient peut-être plus pris au sérieux..."
    HUH "Tout ce travail jeté à la poubelle..."
    HUH "\"Julia, je ve suis pas sûre que ce soit une bonne idée\", \" Vous nous décevez une fois de plus, madame l'Inconnue\"... je leur donnerais tort..."
    I "Mais je sais toujours pas comment apparaître dans mon propre monde."
    "Un claquement raisonna dans toute la pièce, suivi promptement par un bruit de moteur."
    "La lumière clignotta puis inonda la pièce en se stabilisant."
    show fond ecole
    show anifond behind fond
    show ju splain
    pause (1)
    I "Ah, me voilà!"
    show ju fear
    I "Qu'est ce que ?"
    show ju plexe
    I "Excusez-moi mais qui êtes vous?"
    python:
        name = renpy.input(_("Entrez votre nom ou pseudonyme"))
        name = name.strip() or "XDDCC"
    jump menu00

label menu00:
    show ju splain
    if name=="Julia" or name=="L'Inconnue":
        I "Ahah!"
        I "Ah..."
        show ju re
        I "Je vois que j'ai affaire à un.e petit.e rigolo.tte..."
        I "Pas vrai, [currentuser]?"
        $ Achievement.add(achievement_name['doxxed'])
        $ name=currentuser
        I "Fais gaffe à ce que tu pourrais dire ici."
        I "Tu sais quoi? J'utiliserais ton nom jusqu'à nouvel ordre, [name]"
        show ju splain
        jump menu0
    elif name == "Créa" or name == "Téa" or name == "Joa" or name == "lajoiedevivre" or name == "lahainedevivre":
        I "Joa qui revient gérer la fougère, une fois de plus à ce que je vois."
        I "C'est sympa de venir me rendre visite de temps en temps dans mon temple de lore !"
        I "Et ... Merci..."
        I "Merci encore d'être restée quand tout le monde est parti..."
        $ Achievement.add(achievement_name['TeamSweep'])
        I "J'ai recook deux-trois trucs, j'espère que ça va te plaire !"
        I "Il était comment ce bouquin?"
        I "Naaah, je rigole !"
        jump menu0
    elif name == "Powar_t" or name == "Ajai":
        I "Le cocréateur d'Emilie la lapine et professeur de création d'oc en personne !"
        I "Et ... Merci..."
        I "Merci encore d'être resté quand tout le monde est parti..."
        $ Achievement.add(achievement_name['TeamSweep'])
        I "J'ai recook deux-trois trucs, j'espère que ça va te plaire !"
        I "On les aura, ces fachos !"
        show ju plexe
        I "Et j'espère que ça sera avant que ça ne soit trop tard, j'ai pas envie de te perdre..."
        show ju splain
        jump menu0
    elif name == "so6" or name == "cho7":
        I "Wow, tu te fais plus tout.e jeune, hein ?"
        I "C'était une sacré époque et, si je suis heureuse de l'avoir traversée, je suis heureuse d'avoir changée."
        I "Des fois je repense au progrès et il faut bien avouer qu'il y avait du chemin à faire !"
        $ Achievement.add(achievement_name['vétéran'])
        jump menu0
    elif name == "Charasime" or name == "Clémentine":
        I "Clé...Clémentine? c'est vraiment toi?"
        I "Shimmi shimmi yay shimmi yay shimmi ya"
        I "Drank, swalalala"
        I "O Cholera, czy to freddy five bears?"
        I "Hurhurhurhurhurhurhur hurhurhur"
        I "hey guys, did you know th..."
        p "Je pense que ça suffit, Julia"
        I "Bon ok..."
        $ Achievement.add(achievement_name['brainrot'])
        jump menu0
    elif name == "Bodias":
        jump finrhinoceros
    elif persistent.visite:
        show ju splain
        I "Bon retour !"
        I "Tu m'as presque manqué, comment ça va?"
        menu:
            "Plutôt bien !":
                show ju splain
                I "Oh bah parfait !"
                jump menu0
            "Plutôt mal...":
                show ju fear
                pause (1)
                I "Oh..."
                I "Tu veux en parler?"
                menu:
                    "Un peu...":
                        show ju wu
                        I "je suis à l'écoute, dis moi tout ce qui te fais mal."
                        "Elle écoutera rien du tout, il n'y a ni enregistrement ni adaptation au texte."
                        show ju fear
                        pause (0.5)
                        I "Hey ! D'où tu me grille comme ça?"
                        I "Le logiciel a raison, j'ai aucun moyen de répondre efficacement..."
                        I "Mais c'est un peu pareil dans la vraie vie. Le mieux serait d'aller voir un psy."
                        show ju wu
                        I "Quoi qu'il en soit, donc, je te laisse un espace de discussion."
                        python:
                            so6 = renpy.input("")
                            so6 = ""
                        I "Alors? Ca va mieux?"
                        I "Si c'est pas encore le cas, dis toi que ça ira mieux demain et parles-en à tes proches."
                        I "Saches que quoi qu'il arrive, même si ça ne le semble pas,"
                        I "Il y a énormément de personnes qui tiennent à toi dans ce monde."
                        I "Quant à moi, même si je ne suis rien de plus qu'un personnage dans un jeu vidéo créé par une personne random,"
                        I "Je pense tout de même que tu fais du mieux que tu peux."
                        I "C'est pas parfait, hein...{w=0.5} Mais c'est mieux que ça le soit pas !"
                        I "Imagine à quel point la vie serait ennuyeuse si on réussissait tout et qu'on faisait jamais aucune faute !"
                        I "Et à quel point tout serait fade si il n'y aurait aucun obstacle."
                        I "Quoi que tu traverse en ce moment, je suis fière de toi camarade !"
                        I "Je suis vraiment, vraiment très fière de toi. Ne l'oublie pas, ok?"
                        show ju splain
                        jump menu0
                    "Pas vraiment...":
                        show ju splain
                        I "Ok, très bien."
                        show ju wu
                        I "Des fois c'est aussi bien de garder certains trucs et de ne pas les dire à un inconnu."
                        I "Saches que quoi qu'il arrive, même si ça ne le semble pas,"
                        I "Il y a énormément de personnes qui tiennent à toi dans ce monde."
                        I "Quant à moi, même si je ne suis rien de plus qu'un personnage dans un jeu vidéo créé par une personne random,"
                        I "Je pense tout de même que tu fais du mieux que tu peux"
                        I "C'est pas parfait, hein...{w=1} Mais c'est mieux que ça le soit pas !"
                        I "Imagine à quel point la vie serait ennuyeuse si on réussissait tout et qu'on faisait jamais aucune faute !"
                        I "Et à quel point tout serait fade si il n'y aurait aucun obstacle."
                        I "Quoi que tu traverse en ce moment, je suis fière de toi camarade !"
                        I "Je suis vraiment, vraiment très fière de toi. Ne l'oublie pas, ok?"
                        show ju splain
                        jump menu0
    else:

        show ju splain
        I "Je n'ai jamais entendu parlé de toi."
        I "Que fais tu ici, [name]? T'es perdu.e? Tu me dis vraiment rien..."
        I "Ou du moins, ton visage ne me dit rien pour l'instant..."
        I "J'ai quand même un... mmmh..."
        I "{{Pourquoi son visage me dit tout de même quelque chose?}"
        jump menu0

label menu0:

    $ persistent.visite = True
    hide anifond
    hide anifond 2
    hide ju fear
    hide screen Arret_urgence
    hide screen directions
    hide screen arcade_borne
    hide screen aventure
    hide fond ecole
    hide ju splain
    hide expression "Miclordes/Miclordes.jpg"
    if inconnu == 8:
        play music "audio/Dissonant vision.ogg"
        show fond ecole fake
        show anifond behind fond
        p "Qu'est ce qu'il s'est passé ici ? tout allait pourtant..."
        show juposteur fhappy
        pause 0.1
        show juposteur happy
        p "Wow ! Qu'est ce que ?"
        HUH "Bon retour, cher ami !"
        HUH "Tu m'as presque manqué !"
        p "Qui es-tu ?"
        show juposteur fhappy
        pause 0.2
        show juposteur happy
        HUH "Moi ? Je suis l'Inconnu, enfin !"
        p "Quel inconnu ?"
        HUH "Le seul qui existe, pourquoi ?"
        show juposteur fhappy
        pause 0.2
        show juposteur happy
        pause 0.1
        show juposteur fhappy
        pause 0.2
        show juposteur happy
        pause 0.1
        show juposteur fhappy
        pause 0.4
        show juposteur happy
        p "{{Ce n'est clairement pas Julia...}"
        p "Non, merci, je vais partir très vite, je n'ai pas besoin de tout ça."
        hide juposteur
        show fond reboot fake
        play music "audio/Heartbeat.ogg"
        call screen quicktimebar("timeskip", 150, __("Force ton chemin vers l'arrêt d'urgence !"), True, "finEdmes")
    else:
        hide screen Felementjulia
        show fond ecole
        show ju splain
        show anifond behind fond
        I "Alors, dis moi [name], qu'est ce que tu viens faire là?"
        window hide 
        show screen mainUI
        show screen inventory
        $ ui.interact()

label menu0bis:
    hide screen Arret_urgence
    hide screen directionsD
    hide screen directionsG
    hide screen directionsB
    hide screen directionsF
    $ Achievement.add(achievement_name['Inception'])
    show anifond at flip
    show fond ecole at flip
    show ju fear at flip
    I "Oulah ! Qu'est ce que t'as foutu ?!"
    p "Il va falloir que je règle ça vite !"
    window hide 
    show screen directionsFbis
    $ ui.interact()

label menu1:
    hide screen mainUI
    show ju splain
    menu:
        "Qui êtes-vous?":
            show ju splain
            I "Moi? Je m'appelle Julia mais aux yeux des autres créateurices je suis l'Inconnue. Je suis la maîtresse et créatrice de ces lieux."
            p "C'est quand même un peu vide, non?"
            show ju plexe
            I "C'est vrai que c'est pas immense pour l'instant..."
            I "Mais c'est un début ! C'est encore temporaire !"
            p "Mouais..."
            p "{{Bref, ça m'a donné d'autres idées de questions...}"
            p "{{Peut-être que je devrais lui demander...}"
            show ju splain
            jump menu11
        "Où sommes nous?":
            show ju splain
            I "Tu te trouves actuellement à la naissance d'un nouveau monde, ce que nous appelons le quatrième glitch."
            I "C'est basiquement comme une base contenant les éléments les plus simple de tout monde."
            I "J'imagine qu'on peut un peu estimer que ça pourrait correspondre à un modèle ou à une game engine."
            I "Pour l'instant, on se retrouve dans une petite pièce à l'écart de tout ça que j'ai créée en vitesse."
            p "C'est pas mal pour un début."
            show ju wu
            I "Merci, ça me flâte !"
            show ju splain
            I "Mais j'ai plus vraiment de mérite."
            I "En général, la première fois est compliquée mais les fois suivantes sont plus simples."
            p "{{Est ce qu'il sous-entends qu'il y en a déjà eu avant?}"
            p "{{Peut-être que je devrais lui poser la question...}"
            jump menu12
        "Quid de Julien L'Inconnu ?" if inconnu == 1:
            show ju splain
            I "Julien L'Inconnu était mon ancien nom !"
            p "C'était donc pour ça qu'il ne te connaissais pas !"
            show ju re
            I "attends une minute..."
            p "*gulp* {{ pas encore... }"
            "Vous sentez de lourdes chaînes métalliques se serrer à vos poignets jusqu'à ce que retentisse un \"clic\" métallique."
            "Le froid et la pression des menottes vous brûle les poignets."
            jump menu13
        "Qui est Edmes ?" if inconnu == 5:
            show ju plexe
            I "Edmes ?"
            p "Oui, tu l'avais mentionné un peu plus tôt de l'autre côté. Qui est-il ?"
            I "C'était un des personnages de mon deuxième univers."
            I "Plus précisément, c'était un Executeur."
            p "Un Executeur ? C'est encore un type de hierarchie?"
            I "Non, c'est un système que j'avais implanté pour éviter tout problème similaire à la fin de mon premier univers."
            I "Le principe étant que tout personnage vivant est sous ma supervision, j'ai décidé de créer des Executeurs pour tuer des personnages et ainsi exploiter une faille pour les rendre plus puissant."
            p "C'est pas ultra clair comme truc..."
            I "En gros, j'ai utilisé des persos pour tuer d'autres persos pour avoir des assistants non subordonnés à moi."
            p "Je sais pas pourquoi mais ça sent la mauvaise idée..."
            I "Tu ne pourrait pas être plus juste."
            I "Pour éviter le danger de la prise de pouvoir des Exécuteurs, j'avais prévu leur disparition une fois les personnages ciblés morts."
            I "Edmes était le second. Il était différent. Il avait la connaissance du temps et il voulait se venger à tout prix..."
            p "C'est donc pour ça que tu as fini corrompu fut un temps ?"
            I "Oui et c'est aussi la cause principale de l'affaire Pacrel."
            if inconnu == 5:
                $ inconnu = inconnu + 1
            jump menu1
        "Qu'est ce que l'affaire Pacrel ?" if inconnu == 6:
            show ju splain
            I "L'affaire Pacrel est une affaire entamée autour d'Edmes et de Julien Pacrel."
            I "Il aurait dû être un Illustrateur, un de mes bras droit. Edmes a cependant compris la supercherie et, bien qu'il soit attaché comme une ombre à Pacrel, il a causé d'énormes problèmes."
            p "C'est donc de là que vienne les personnages corrompus..."
            I "Les Ink Guys, exactement. Edmes dépendant de la survie de Pacrel pour la sienne, il l'a gardé en souffrance tout juste en vie."
            I "Ce qui a créé de nombreuses rumeurs sur ses proches et beaucoup de questionnement médicaux autour de son cas."
            I "Mais rien de tout cela n'aurait jamais existé si il était réellement random."
            I "Julien Pacrel était un orphelin et avait passé ses jours à squatter des lieux abandonnés jusqu'en 1930 en groupe."
            I "C'était ce qui lui semblait le plus simple mais qui le mettait également beaucoup en danger quand il revenait en terrain confidentiel."
            I "Ses nombreux larcins de survie l'avait rendu connu aux yeux de toute la région et donc, en addition de circonstance, l'histoire fut très relayée."
            I "Et pour la fin de cette affaire, je ne saurais plus vraiment partir en détail."
            p "Très bien, j'ai compris, je retourne le voir."
            if inconnu == 6:
                $ inconnu = inconnu + 1
            jump menu1
        "Retour":
            show ju splain
            I "Ok, on peut repousser ça à plus tard."
            jump menu0

label menu11:
    menu:
        "Des Créateurices? Quesaquo?":
            show ju splain
            I "C'est en quelque sorte quelqu'un de normal."
            p "Quelqu'un de normal? Je serais aussi un.e Créateur.ice?"
            I "En quelque sorte..."
            I "Enfin, je crois? Tu as un monde, toi?"
            p "Je sais pas vraiment..."
            I "Est-ce que tu as déjà créé quelque chose?"
            I "De manière artistique quelconque, en dessinant, chantant, écrivant, sculptant, jouant de la musique, faisant un sport en synchro, programmant, gravant, modelant ou tout autre manipulation de matière?"
            p "Je... J'imagine?"
            I "alors tu en est un.e, c'est aussi simple que ça."
            p "Et du coup, ce qui nous entoure..."
            I "Est une projection de ces différents types d'art."
            I "De plus, n'importe qui du monde réel peut être Créteurice."
            I "Pas besoin d'être connu, professionnel ou même d'avoir étudié l'art."
            show ju plexe
            I "Même si c'est vrai que des fois ça peut aider..."
            show ju splain
            jump menu11
        "Existe-il des influences inter-Créateurices?":
            show ju splain
            I "Y'en a pas mal, yep !"
            I "En soit, comme pour tout, c'est difficile voire impossible de partir de rien et tout ou presque a déjà été fait."
            I "Donc quoi qu'il arrive et quoi qu'on fasse, on se base toujours sur le travail d'autrui."
            I "Des fois, on peut penser qu'un travail est tout à fait original mais il ne faut pas oublier que ce n'est plus ou moins qu'un mélange de très nombreuses sources."
            I "Regarde la salle par exemple !"
            hide ju splain
            window hide
            pause (3)
            window show
            show ju splain
            p "Et si on sort de ça, est ce qu'il y a des relations de pouvoirs?"
            I "Ahahah !"
            show ju plexe
            I "Ah..."
            I "C'est vrai qu'il y a ça aussi..."
            p "Eh bien?"
            show ju re
            I "Yep, Y'en a."
            I "Je sais pas si j'ai le droit d'en dire plus, le conseil m'écoute sans doute."
            p "C'est à dire?"
            I "..."
            p "{{On dirait que si je veux aller plus loin, il va falloir que je lui force un peu la main...}"
            p "{{Je prends des risques par contre... Je sais pas comment elle réagira...}"
            p "{{Je devrais peut-être prendre des pincettes...}"
            jump menu111
        "retour":
            show ju splain
            I "Si tu veux en reposer, je suis encore là."
            jump menu1

label menu111:
    menu:
        "Je fais parti.e du conseil, tu peux tout me dire !":
            stop music fadeout 1
            show ju re
            I "Ah?"
            I "C'est ... Vrai?"
            scene black
            hide fond ecole
            I "Quel plaisir de rencontrer quelqu'un de ton gabarit !"
            I "Tu faisais donc parti de celleux qui m'ont exilés."
            p "Hein?"
            show I_Know
            play sound "audio/see.ogg" fadein 1
            I "C'était tellement simple, tellement banal."
            I "Vous n'y avez même pas réfléchi plus de 10 minutes !"
            I "Mais maintenant..."
            I "Ahaha..."
            I "Maintenant, l'un d'entre vous est là et je peux enfin prendre ma vengeance !"
            I "Ne crie pas, personne ne t'entendra d'ici..."
            I "Que dis-je? Après tout, tu le sais déjà!"
            hide I_Know
            window hide
            show YOU
            pause 2.0
            show text "{color=#ffffff}I SEE YOU"
            pause 2.0
            hide text
            show text "{color=#ffffff}IT WILL BE OVER SOON"
            pause 2.0
            hide text
            show text "{color=#ffffff}AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH AH "
            pause 2.0
            hide YOU
            hide text
            stop sound
            pause 2.0
            show text "Fin Sacrifice du Conseil" with dissolve
            $ Achievement.add(achievement_name['sheep'])
            pause 4.0
            hide text with dissolve
            pause 1.0
            return
        "Finalement, rien !":
            I "..."
            p "{{Peut être que ça serait pas mal que je vérifie les alentours avant de prendre des décisions...}"
            p "{{Je ne sais juste pas vraiment où commencer}"
            show ju splain
            jump menu11

label menu111face:
    scene
    hide screen mainUI
    hide screen directions
    hide screen arcade_borne
    show anifond
    show fond ecole
    show screen Felementjulia
    call screen directions (True, "menu111gauche", True, "menu111droite", True, "menu0")
    $ ui.interact()

label HMlib:
    hide screen directions
    hide screen window
    p "{{Des bouquins sur un gars random et ses deux associés devenus immortels qui se bat contre son alter-ego pour sauver son créateur et des dieux qui observent la destruction comme un spectacle}"
    if "Trilogie Histoire Multiple" in inventory_items:
        p "Je les ai déjà, ça ne servirait à rien de les reprendre."
        jump menu111face
    else:
        $ inventory_items.append("Trilogie Histoire Multiple")
        "A obtenu la trilogie Histoire Multiple ! Elle semble incomplète ..."
        p "{{Je me demande ce qu'ils font là et pourquoi ils sont mis en importance à ce point}"
    jump menu111face

label ofac1:
    hide screen directions
    hide screen window
    if "Rapport OFAC 105" in inventory_items:
        p "toujours intéressant de se relir."
        jump menu111face
    else:
        $ inventory_items.append("Rapport OFAC 105")
        "A obtenu le rapport ofac n°105 ! Qui ça pourrait bien être ?"
        p "{{Je ne sais pas si j'ai le droit de fouiller dans ses affaires }"
    jump menu111face

label capital:
    hide screen directions
    hide screen window
    p "{{Des gros et vieux bouquins poussiéreux écrits en tout petit.}"
    p "{{Si la couverture du premier a bien vécue, on dirait que les deux autres sont presques neufs.}"
    p "{{C'est bien mais je vais peut-être pas prendre ça...}"
    jump menu111face

label whiteout:
    hide screen directions
    hide screen inventory
    hide screen Felementjulia
    show fond:
        xcenter 0.5 ycenter 0.5
        linear 2 zoom 20
    show white with dissolve
    play music "audio/Void_Seeker.ogg"
    show text _ ('{color=#000000}Tu as cassé tes menottes, [name]...')
    pause 2.0
    hide text
    pause 1.0
    show text _ ('{color=#000000}Tu as transcendé ta condition humaine vers quelque chose de nouveau.')
    pause 2.0
    hide text
    pause 1.0
    show text _ ('{color=#000000}Mais tu dois survivre, [name].')
    pause 2.0
    hide text
    pause 1.0
    show text _ ('{color=#000000}Tiens bon...')
    pause 2.0
    hide text
    pause 1.0
    play music "audio/Heartbeat.ogg"
    call screen quicktimebar("inverted", 20, __("Résiste au vide !"), True, "finwhite", 60)

label menu111droite:
    hide screen directions
    hide screen fenetre
    hide screen Arret_urgence
    hide screen Felementjulia
    hide arcade_terminal
    show fond droite
    show anifond behind fond
    show fonddroite2 behind fond
    $ choc = True
    show screen inventory
    show screen arcade_borne
    call screen directions (True, "menu111face", True, "menu111arriere", True, "menu0")
    $ ui.interact()

label err_borne:
    $ choc = False
    "bip...bzzzz!"
    p "Outch ! Je me suis pris un coup de jus !"
    p "{{Cette machine semble ancienne... Il pourrait être pertinent de trouver quelqu'un pour la réparer avant de l'essayer à nouveau...}"
    $ borne_noticed = True
    p "{{Pas sûr d'en trouver dans le coin, par contre... Pas grand monde ne semble circuler par ici.}"
    $ choc = True
    jump menu111droite

label flo_rep:
    hide screen directions
    show flo happy
    $ floscreenswitch = False
    $ choc = False
    flo "Et voici une bonne chôse de faite, elle devrait fonctionner comme neuve maintenant !"
    p "Oh merci !"
    flo "De rien, c'est naturel, Je reste dans le coin si jamais d'autres évènements venaient à arriver ici !"
    flo "Peut-être même que je pourrais t'apprendre deux trois trucs une fois que tu auras retrouvé la mémoire."
    hide flo
    $ choc = True
    jump menu111droite

label menu111gauche:
    $ projecteur = renpy.random.randint(1,2)
    hide screen Felementjulia
    show projecteur1 behind fond
    if projecteur == 2:
        show projecteur2 behind fond
    show fond gauche
    hide screen directions
    hide screen fenetre
    hide screen Arret_urgence
    call screen directions (True, "menu111arriere", True, "menu111face", True, "menu0")

label menu111arriere:
    hide screen directions
    hide screen arcade_borne
    scene
    show fond reboot
    show screen Arret_urgence
    call screen directions (True, "menu111droite", True, "menu111gauche", True, "menu0")
    $ ui.interact()

label inverted:
    scene
    play music "audio/Void_Seeker.ogg"
    hide screen to_inverted
    hide white
    show screen inventory
    show fond trans
    show anifond 2 behind fond
    if inconnu == 5:
        show ju ink
        IIG "Quelle créature pathétique tu fais."
        p "Comment ?"
        IIG "Tu essayes de retrouver les traces d'un passé à tout jamais révolu, enfermé avec une vision de toi-même."
        p "Tu ne semble plus le même..."
        IIG "Je t'anéhantirais dans ta recherche d'informations avant que tu ne puisse trouver quoi que ce soit !"
        p "Je ferais mieux de partir d'ici avant de me faire buter !"
        IIG "Tu fais encore confiance à ces inconnus alors que tu sais pertinemment qu'iels te mentent !"
        hide screen whiteUI
        pause 0.25
        jump menu0
    elif not inverted:
        pause (2)
        p "Décidément..."
        p "Qu'est ce que cet endroit cache encore ?"
        show ju ink
        $ persistent.ink = True
        pause(0.5)
        IIGHUH "Bien le bonjour !"
        p "Uargh !"
        IIGHUH "Je t'ai vraiment fait peur ?"
        p "Je dirais plutôt surpris·e..."
        p "Tu as l'air bizarre par rapport à tout à l'heure..."
        IIGHUH "Sous cet état, je suis toujours bizarre !"
        IIGHUH "Par contre ma mémoire me fait un peu défaut donc je pourrais pas dire que je me souviens de tout à l'heure !"
        IIGHUH "Tu as l'air de me fixer attentivement comme si tu voulais quelque chose de moi."
        p "Qui êtes-vous ?"
        IIGHUH "Moi ? Je suis l'Inconnu !"
        IIG "Ou du moins je penses que je l'ai été un jour..."
        IIG "Et toi ?"
        p "Moi ? Je suis [name]."
        IIG "Oh enchanté, [name] ! Merci de venir me passer le bonjour !"
        $ inverted = True
    else:
        p "{{Décidément, ça fait mal à la tête...}"
        show ju ink
        IIG "Bon retour, hum... Attends..."
        IIG "Comment tu t'appelles, déjà ?"
        p "C'est pas important, t'inquiètes pas."
    p "{{Même si il a l'air troublé, je pourrais peut-être lui poser des questions...}"
    show screen whiteUI
    $ ui.interact()

label inverted1:
    hide screen whiteUI
    p "Est ce que je pourrais te poser une question ?"
    menu:
        "Qui est Julia l'Inconnue ?":
            show ju ink
            IIG "Ju-qui?"
            IIG "Désolé mais ça ne me dit pas grand chose..."
            IIG "Après tout, je suis le seul à avoir cette dénomination."
            p "Vraiment ?"
            IIG "Oui vraiment, chaque créateurice a son dénominateur et est appelé par celui-là, les prénoms sont peu utilisés."
            p "Je devrais peut-être lui poser la question..."
            IIG "Me poser quelle question ?"
            p "Non, rien ! J'ai pensé.e à voix haute !"
            if inconnu == 0:
                $ inconnu = inconnu + 1
            jump inverted1
        "Pourquoi tu souris tout le temps?":
            show ju ink
            IIG "Drôle de question !"
            IIG "C'est à dire que je ne peux pas vraiment faire autrement, mon visage est bloqué comme ça !"
            p "Bloqué ?"
            IIG "Les joies d'être un Ink Guy !"
            jump inverted1
        "Comment s'est terminé l'affaire Pacrel?" if inconnu == 7:
            show ju ink
            IIG "Wow, tu as l'air d'avoir une sacrée tête d'enterré ! Tout va bien ?"
            p "Je crois avoir appris plus que je n'aurais voulu apprendre un jour..."
            IIG "Ce monde est bien perturbé, mon ami ! Tu n'es qu'au début de tes peines !"
            IIG "Sinon, j'ai oublié la majorité de ce qui s'est passé avant que je ne me retrouve ici !"
            p "Tu n'aurais même pas de miettes de souvenirs ?"
            IIG "Si, je me souviens de sa mort, de la mort de Pacrel et de quand j'ai été possédé !"
            p "Wow, trop enthousiaste..."
            IIG "Je ne peux pas me contrôler, mon pote ! Cette forme m'y oblige !"
            p "Ah..."
            p "Attends un instant... La mort de Pacrel ?"
            IIG "C'est plus tout à fait clair mais oui ! Il s'est interposé pour essayer de me sauver et s'est fait transpercé par un...hum...pic d'ombre !"
            p "{{Il y a quelque chose qui ne convient pas ici... Je crois que je vais devoir réassembler ses souvenirs si je veux en tirer quoi que ce soit...}"
            IIG "Qu'est-ce qui te trouble ?"
            p "De ce que j'ai pu comprendre, la mort de Pacrel causerait..."
            menu:
                "La mort de l'Inconnu":
                    p "Je suis ultrasûr."
                    IIG "Je crois que j'ai perdu le fil..."
                    p "Merde..."
                    jump inverted1
                "La mort d'Edmes":
                    p "Une petite voix m'a expliquée que la mort de l'un menait à la mort de l'autre."
                    p "Hors, ceci est arrivé et tu es toujours corrompu."
                    p "Comment est-ce possible ?"
                    IIG "Mmmmh... C'est vrai, ça !"
                    p "Ce qui veut donc dire qu'il n'a pas pu mourir."
                    IIG "Mais je l'ai pourtant vu se faire transperser de bout en bout devant mes yeux !"
                    p "Par un pic d'ombre ?"
                    IIG "Oui, tout juste avant que je ne m'en prenne plusieurs moi-même !"
                    IIG "Ces trucs font extrêmement mal !"
                    p "Mais tu as tout de même survécu, ce qui veut dire que ces pics ne tuent pas !"
                    IIG "C'est vrai, ça ! T'es vachement perspicace !"
                    p "Cependant, ils ont tout de même un effet sur leurs cibles."
                    IIG "Quel type d'effet?"
                    menu:
                        "L'effet spoiler":
                            IIG "Ok Bad Mulch."
                            IIG "Je sais qu'on a perdu et qu'on aurait pu gagner au second tour si la gauche était unie pais là c'est pas le sujet."
                            p "Merde..."
                            $ Achievement.add(achievement_name['Bad Mulch'])
                            jump inverted1
                        "La perte du soi":
                            p "Tu as perdu tes couleurs et tes souvenirs après ces évènements."
                            p "Si tu es toujours corrompu, le vieux Pacrel est sans doute seulement corrompu sans ses souvenirs !"
                            IIG "On pourrait donc le retrouver !"
                            p "Je sais pas si ça pourrait être tout à fait utile..."
                            IIG "Etant donné que sa simple présence casse la fabrique des ordres."
                            IIG "Sa mention est quasiment un signe d'instabilité !"
                            show fond trans at shake
                            IIG "En parlant d'instabilité, on dirait bien que ça commence à trembler par ici !"
                            IIG "Les liens avec ton monde sont instables, va voir si tout va bien là-bas !"
                            p "Mais..."
                            IIG "On se reverra, je te le promets."
                            IIG "De toute façon, je ne pourrais pas aller bien plus loin !"
                            if inconnu == 7:
                                $ inconnu = inconnu + 1
                            jump whiteexit
                        "La perte de couleur":
                            p "Je suis ultrasûr."
                            IIG "Je crois que j'ai perdu le fil... On parlait de joueurs LOL qui voient pas le soleil ou du Sénat ?"
                            p "Merde..."
                            jump inverted1
                "La mort de Jean Fraques":
                    p "Je suis ultrasûr."
                    IIG "Je crois que j'ai perdu le fil..."
                    p "Merde..."
                    jump inverted1
        "Retour":
            jump inverted05

label whiteexit:
    hide screen whiteUI
    show ju ink
    IIG "Penses juste à venir me revoir ! On se sent seul quand enfermé avec soi-même."
    pause 0.25
    play music "audio/A day in the unknown.ogg"
    jump menu0

label menu111bouton:
    if off == True:
        jump offlinetransition
    else:
        hide screen directionsB
        p "{{ Un bouton d'arrêt d'urgence? Mmmmh...}"
        p "{{Peut-être que je pourrais...}"
        stop music
        show ju re onlayer overlay
        p "Uwa !"
        show ju re onlayer overlay
        I "N'y pense \nmême pas."
        hide screen Arret_urgence
        show fond ecole
        show ju re
        p "Je n'allais rien faire !"
        I "Fais gaffe à ce que tu fais ici, ne touche pas à ce que tu ne dois pas toucher."
        p "Mais..."
        I "Suis mes conseils et tout se passera bien, compris ?"
        menu:
            "Nuh-uh !":
                hide ju re
                show fond reboot
                "*clic !*"
                "..."

                show ju plexe
                I "Qu'est ce que tu as fait?!"
                I "ARREE.EE...EEEEEE"
                show ju plexe_C
                "{color=#000000}EEEEEEEEEEEEEEEEEEEEEEEEE"
                "{color=#000000}RESET SYSTEM, PLEASE STAND BY"
                "{color=#000000}DELETING JULIA.CHR"
                hide ju plexe_C
                "{color=#000000}DELETING ASSETS"
                window hide
                show text "{color=#ffffff}DELETING BACKGROUND.webp"
                hide fond reboot
                show black
                hide anifond
                play music "audio/Void_Seeker.ogg"
                show text "{color=#ffffff}RESET SUCCESSFUL, DO YOU WANT TO RESTART?"
                $ Achievement.add(achievement_name['Disconnected'])
                menu:
                    "YES":
                        jump offlinedialogue
                    "NO":
                        jump finreset
            "Oui capitaine...":
                show ju re
                I "C'est bien, tu as compris."
                play music "audio/A day in the unknown.ogg"
                show ju splain
                jump menu0

label offlinedialogue:
    show text "{color=#ffffff}RESTORING FILES, RECONNECTION MAY TAKE SEVERAL MINUTES"
    window show
    I "..."
    window hide
    pause (1)
    show ju plexe
    window show
    I "Qu'est-ce..."
    I "Qu'est-ce que tu as fait?"
    p "Je crois que j'ai fait ce qu'il fallait."
    I "Qu'est ce que tu dis? Tu as supprimé ce monde !"
    I "C'est l'équivalent de sauter par la fenêtre pour voir ce que tu trouveras derrière !"
    p "Mmmmh... je devrais peut-être..."
    show ju re
    I "N'y penses même pas ! tu as déjà effacé ce monde !"
    show ju plexe
    p "Temporairement..."
    I "Hein? Comment ça?"
    p "Tu n'as pas entendue la voix?"
    I "Quelle voix?"
    p "Rien, laisse tomber, on a pas beaucoup de temps avant que tout revienne."
    I "Tout va revenir?"
    p "Oui mais je crois qu'on est déconnecté des serveurs."
    I "Donc ça voudrait dire... "
    p "...Que plus personne ne nous écoute."
    p "Le conseil ne peut plus vous écouter pour l'instant."
    I "On dirait vraiment que tu avais envie de me poser ces questions..."
    show fond Void_room behind ju with dissolve
    show ju splain
    I "J'apprécie ta dédication mais si tu pouvais éviter de pousser ce monde à ses limites par le futur, ça serait bien !"
    jump offlinemenu0

label offlinetransition:
    hide screen Arret_urgence
    hide screen directionsB
    show ju plexe
    I "C'est reparti pour un tour?"
    I "Très bien, fais comme tu le souhaite mais fait vite..."
    hide ju plexe
    show fond reboot
    "clic !"
    "{color=#000000}RESET SYSTEM, PLEASE STAND BY"
    "{color=#000000}DELETING JULIA.CHR"
    "{color=#000000}DELETING ASSETS"
    window hide
    show text "{color=#ffffff}DELETING BACKGROUND.webp"
    hide fond reboot
    show black
    hide anifond
    play music "audio/Void_Seeker.ogg"
    show text "{color=#ffffff}RESET SUCCESSFUL, DO YOU WANT TO RESTART?"
    menu:
        "YES":
            show text "{color=#ffffff}RESTORING FILES, RECONNECTION MAY TAKE SEVERAL MINUTES"
            show ju splain
            jump offlinemenu0
        "NO":
            jump finreset

label offlinetransition2:
    "clic !"
    Edmes "Penses à demander à ta nouvelle amie qui est le réel antagoniste de cette histoire !"
    "{color=#000000}RESET SYSTEM, PLEASE STAND BY"
    "{color=#000000}DELETING JULIA.CHR"
    "{color=#000000}DELETING ASSETS"
    window hide
    show text "{color=#ffffff}DELETING BACKGROUND.webp"
    hide fond reboot fake
    show black
    hide anifond
    stop music
    play music "audio/Void_Seeker.ogg"
    show text "{color=#ffffff}RESET SUCCESSFUL, DO YOU WANT TO RESTART?"
    menu:
        "YES":
            show text "{color=#ffffff}RESTORING FILES, RECONNECTION MAY TAKE SEVERAL MINUTES"
            show ju fear
            I "AAAAAAAAAAAh !"
            p "Hey, tout va bien, tout à été reset."
            show ju plexe
            I "AAaaah... Ah ?"
            show fond Void_room behind ju with dissolve
            I "Tu as eu un sacré réflexe, [name]..."
            p "Je penses qu'après tout ça, il me reste juste une seule question..."
            I "Oh... Très bien. Je t'avouerais que j'ai le cerveau un peu retourné mais je tenterais de répondre."
            jump offlinemenu1
        "NO":
            jump finreset

label offlinemenu0:
    $ off=True
    show ju splain
    show fond Void_room behind ju with dissolve
    show ju splain
    I "Allez, on est seul.e.s face à face, pose moi donc tes questions pour lesquelles tu as tant travaillé.e !"
    window hide
    show screen blackUI
    $ ui.interact()

label offlinemenu1:
    hide screen blackUI
    menu:
        "Du coup, ces hierarchies?":
            show ju splain
            I "Ah oui, c'etait ça !"
            I "Eh bien, on décompose notre organisation, comme dans notre vrai monde, en échelles hierarchiques."
            show orga
            I "Plus une personne se trouve bas dans cette organisation, plus elle aura des personnes au dessus d'elle ayant un contrôle sur elle."
            p "Donc chaque rang a créé le rang inférieur?"
            I "Pas forcément non plus, ça dépend vraiment des rangs."
            hide orga with dissolve
            I "Tu voulais que je commence par un certain rang?"
            jump offlinemenu11
        "Pourquoi y a t'il ce bouton?":
            show ju re
            I "..."
            p "Alors?"
            I "Tu m'as fait souffrir avec le bouton pour savoir ce que fait le bouton...?"
            p "Je voulais savoir et tu m'as pas dit, après tout."
            I "Je n'ai même pas envie d'élaborer."
            p "petite joueuse, va."
            I "..."
            show ju splain
            jump offlinemenu1
        "Qu'est ce qui a pu t'arriver ?" if inconnu >= 2:
            show ju plexe
            I "C'est... compliqué..."
            I "J'ai eu des problèmes avec mes univers. Des problèmes qui m'ont coûté mon premier univers et quasiment ma vie."
            I "Mais si on parle essentiellement de ce que tu as vu, je dirais que c'était ma période corrompue."
            p "Ta période corrompue ? Que s'est-il passé ?"
            play music "audio/Tears of the past.ogg"
            I "Je n'étais... Pas prête à sa mort."
            show ju sad
            I "Je pensais qu'elle ne viendrait pas..."
            I "Je pensais que j'aurais pu la protéger..."
            I "Je pensais pouvoir y arriver seule..."
            I "J'avais tort..."
            p "Tout va bien?"
            I "Oui... J'ai juste besoin d'un peu de temps..."
            pause 2
            if complique == False:
                $ inconnu = inconnu + 1
            show ju splain
            $ complique = True
            play music "audio/Void_Seeker.ogg"
            jump offlinemenu1
        "Qui est le réel antagoniste de cette histoire ?" if inconnu >= 8:
            show ju splain
            I "C'est une sacré question !"
            I "Après le peu qu'on a traversé ici et la quantité que tu verras plus loin, la question est legit compliquée à répondre."
            I "On peut citer le Conseil, Edmes, l'OFAC, des tas et des tas d'autres antagonistes dont on parle depuis tout à l'heure..."
            I "Mais j'ai toujours pensé à un truc."
            I "Aussi machiavélique qu'un antagoniste soit, il restera toujours limité à la plume de son auteur dans ses actes et dans leurs violences."
            I "Les véritables antagonistes de cet univers sont donc l'auteur et celleux qui l'encadre."
            I "J'imagine du coup que si on suit cette logique et que si on ignore le Conseil, je suis le véritable antagoniste de l'histoire."
            p "Et pourtant, Edmes me semblait plus dangereux."
            I "J'imagine que c'est une question de point de vue."
            I "Te voici arrivé à la fin de nos discussions !"
            p "Déjà ? Mais qu'est ce que je peux faire maintenant ?"
            I "De ce que j'ai pu entendre, il y aurait deux-trois trucs qui ont commencé à changer"
            I "J'imagine que tu peux encore faire un tour pour observer les alentours si tu n'a pas eu le temps de tout voir !"
            I "Et si tu veux partir, j'imagine que je te reverrais la prochaine fois !"
            if inconnu == 8:
                $ inconnu = inconnu + 1
            $ Inconnu = True
            show text _ ("{color=#ffffff} Fin de l'Inconnu.e") with dissolve
            $ Achievement.add(achievement_name['Inconnu'])
            pause 3.0
            hide text with dissolve
            menu:
                "Continuer":
                    show ju splain
                    I "Parfait ! Je serais toujours là si tu as besoin de quoi que ce soit !"
                    jump offlinemenu1
                "Partir":
                    jump menu3
        "retour" if inconnu !=8:
            jump offlinemenu0

label blackexit:
    hide screen blackUI
    show ju plexe
    I "Vraiment? Tu as fait tout ça juste pour ça?"
    hide text
    I "Tu sais que ça me détruit la tête à chaque fois?"
    "FULLY RESTORED"
    I "Tout ça pour ça..."
    $ Achievement.add(achievement_name['techdimanche'])
    stop music
    hide text
    show anifond with dissolve
    show fond ecole
    hide fond Void_room with dissolve
    play music "audio/A day in the unknown.ogg"
    show ju splain
    I "Bon, passons à autre chose !"
    jump menu0

label offlinemenu11:
    menu:
        "Le Conseil" if conseil == 0:
            show ju plexe
            I "..."
            p "Qu'est ce qu'il se passe? Tu ne veux toujours pas me dire?"
            I "C'est à dire que..."
            show ju wu
            I "Il n'y a simplement rien à dire !"
            p "À d'autres mais pas à moi !"
            show ju plexe
            I "Argh..."
            p "{{Elle a vraiment du mal à en parler...}"
            p "{{Si je compte en savoir plus un de ces jours, il va falloir que je lui force la main...}"
            show ju wu
            I "Et puis c'est pas comme si c'était intéressant !"
            I "Iels font que de la paperasse de toute façon !"
            p "Iels t'ont fait quelque chose?"
            show ju fear
            I "Iirk !"
            show ju wu
            I "R...Rien du tout !"
            hide text with dissolve
            show chaine behind ju at shake
            pause 2
            show cadenasR behind ju at Position(xpos=0.9,xanchor=0.9,ypos=0.5,yanchor=0.5)
            pause 0.2
            show cadenasL behind ju at Position(xpos=0.1,xanchor = 0.1, ypos=0.5, yanchor=0.5)
            pause 0.2
            show cadenasT behind ju at Position(xpos=0.5,xanchor = 0.5, ypos=0.1, yanchor=0.1)
            p "{{C'est quoi ces trucs? On dirait une mauvaise reférence à Ace Attorney !}"
            if "Trilogie Histoire Multiple" in inventory_items  and "Rapport OFAC 105" in inventory_items:
                p "J'ai trouvé des bouquins qui trainaient en hauteur dans les étagères."
                show ju re
                I "C... Comment? qu'est ce que tu es allé cherché ça dans mes affaires?"
                jump offlinemenu111
            else:
                p "{{Peut-être que je pourrais essayer d'explorer les alentours pour trouver de quoi déverouiller ces cadenas}"
                hide cadenasR with dissolve
                hide cadenasT with dissolve
                hide cadenasL with dissolve
                hide chaine with dissolve
                show ju splain
                jump offlinemenu11
        "L'accord OFAC - conseil" if conseil == 1 and inconnu == 1:
            show ju plexe
            I "Tu es prêt.e à tout pour me mettre dans tous mes états, hein ?"
            p "Je pense qu'il y a quelque chose de plus poussé derrière ces simples questions."
            p "Et je ne penses très honnètement pas que tu tenterais tant que ça de ne pas le divulguer si tout allait bien."
            I "C'est... vrai..."
            I "Il faut aussi dire que je m'attendais pas à ce que les choses se déroulent comme ça..."
            I "Après tout, les deux organismes me méprisent..."
            p "Du coup, j'ai bien compris que le conseil était tes patrons mais qui est l'OFAC ?"
            I "L'OFAC, ou Office Factieuse Anti Corruption, est une association internationale de l'un de mes anciens mondes."
            I "C'est un réseau totalement factieux de gens peu scrupuleux fondé en 1930 à Appaos à la suite des évènements de l'affaire Pacrel dans les locaux de leur ancienne structure."
            p "C'est moi ou ça sent le maxi complotisme, cette histoire ?"
            I "C'est vraiment pas toi pour le coup, cette association est totalement complotiste."
            I "Et vu que mes mondes sont très paranormaux, il y avait toute les chances pour qu'ils surgissent."
            I "Ils pensent que je suis leur ennemi principal et ils ont donc réussi, d'une manière ou d'une autre malgré leur totale incompétence, à contacter mes supérieurs."
            I "Ils ne savent juste pas encore qu'ils ne seront que des pions et qu'ils finiront par être jetés."
            I "Ni même que la cause de tout ces désordres a déjà pactisée avec le Conseil, contre moi."
            p "{{Contre elle ? je devrais peut-être lui demander pourquoi ici avant de continuer dans les hierarchies}"
            show ju splain
            if inconnu == 1:
                $ inconnu = inconnu + 1
            jump offlinemenu11
        "Les Administrateurices et Modérateurices":
            show ju re
            I "Ah... Eux..."
            p "Iels ont quelque chose de spécial ?"
            I "Iels sont ce qu'on peut considérer comme cadres et cadres supérieurs..."
            p "Ah donc c'est un peu tes supérieurs."
            I "...Ou comme milice du conseil."
            I "Après tout, iels y sont directement reliés."
            p "Vraiment ?"
            I "Oui, c'est une milice du système, même si elle ne s'en rend pas toujours compte."
            I "Ce sont les étudiants en art et les artistes professionnels de notre monde."
            I "Iels relayent ce qui est défini comme correct, bien qu'avec moins d'influence que le conseil."
            show ju splain
            jump offlinemenu11
        "Les Créateurices confirmés":
            show ju splain
            I "C'est plus ou moins la base de la base de la hierarchie."
            I "Cette catégorie rassemble l'ensemble des personnes qui ont déjà créé quoi que ce soit,"
            I "Qu'iels en soient conscient.es ou non."
            I "Ça s'applique donc également à toi j'imagine."
            I "Sans quoi tu ne serais sans doute pas là."
            show ju fear
            I "Cependant, c'est les moins importants de la chaîne des confirmés. Iels sont à la merci des envies de leurs supérieurs."
            p "Et il y en aurait d'autre que des confirmés ?"
            I "Il y a celleux qui sont en dehors de ce système..."
            I "Entre ma première arrivée parmis les confirmé.es et aujourd'hui, je suis passé par ces filets."
            $ puni=True
            show ju splain
            jump offlinemenu11
        "Les Créateurices OOB" if oob and inconnu >=4:
            show ju splain
            I "Nous voici à la fin de nos affaires !"
            I "Les Créateurices OOB ou Créateurices Out Of Bound sont les Créateurices Exilées du système."
            I "Iels n'y sont souvent pas à cause du Conseil mais par simple conviction personnelle ou par instabilité excessive."
            I "Ces Créateurices sont la plupart du temps plus puissants que les plus hauts d'entre elleux."
            I "Et iels sont également assez fréquemment passé par la case sanction ou corruption, ces évènements menant à de grands gains de puissances instables."
            I "À part ça, même si j'en ai fait partie, je ne suis plus vraiment dans ces cases."
            if inconnu == 4:
                $ inconnu = inconnu + 1
            jump offlinemenu11
        "Les Créateurices Sanctionné.es" if puni and inconnu >= 3:
            show ju splain
            I "Si des problèmes sont observés dans un univers..."
            I "Ou... Si ils ne sont pas au goût du conseil..."
            I "Un.e Créateurice peut se retrouver sanctionné.e par le conseil."
            I "Cette sanction peut souvent se traduire par une surveillance accrue, une destruction des mondes créés auparavant, une interdiction d'en créer de nouveaux et j'en passe."
            I "le Conseil ne se limite cependant pas à ces sanctions."
            p "J'imagine que c'est la raison pour laquelle tu rechignes à parler du conseil."
            show ju re
            I "Bingo..."
            I "Le Conseil a un côté plus obscure qui ne pourrait être connu que par un.e sanctionné.e..."
            p "Tu as donc été sanctionnée. Ton renouveau et ta paranoïa semblent pointer dans ce sens."
            I "Pas tout à fait... Je suis la sanction..."
            I "Mais j'en reparlerais peut-être un jour, une fois que tu auras tout vu puis que tu auras reparlé avec lui."
            I "Le conseil a tendance à faire des experiences très peu éthiques sur les sanctionné.es puis à les faire taire."
            I "Mais il y a pire que tout ça... Les créateurices corrompu.es."
            show ju splain
            $ corrupt = True
            if inconnu == 3:
                $ inconnu = inconnu + 1
            jump offlinemenu11
        "Les Créateurices corrompu.es" if corrupt:
            p "Je n'ai pas vu ça dans la pyramide que tu m'as montré pourtant."
            show ju splain
            I "En effet, ce n'est pas vraiment une partie de la pyramide, comme les Créateur.ices OOB."
            I "Je suis l'une des personnes à l'origine de cette dernière."
            I "Les Créateurices corrompues sont des Créateurices ayant été corrompues par Edmes, l'un de mes personnages."
            I "Au même titre que leurs homologues personnages, ces Créateurices, ont une puissance décuplée."
            I "En échange de cette puissance, cependant, iels perdent leurs couleurs et leur libre arbitre."
            if name == "Valentin" or name == "valentin":
                p "Sauf si on considère que le libre arbitre n'a jamais réellement existé."
                I "Comme les oiseaux bleu ?"
                p "Outch, Touché."
                $ Achievement.add(achievement_name['Oiseau bleu'])
            I "On les reconnait à leur grand sourire et à leur teinte monochrome."
            I "Je n'ai pas vraiment de crainte autour de la mention d'Edmes donc une fois que tu en auras fini ici, penses à me demander dans le monde normal."
            I "Rien que le fait que nous vivions dans les ombres ici me mets mal à l'aise..."
            I "Plus qu'une catégorie de Créateurice, lance-le donc !"
            $ oob = True
            jump offlinemenu11
        "retour":
            jump offlinemenu1

label offlinemenu111:
    p "Je pense que la partie de ces livres qui explique ton silence est..."
    menu:
        "Le personnage principal":
            show ju splain
            I "Je vois pas de lien dans cette association."
            p "Argh... si j'avais sû..."
            jump offlinemenu1
        "Les dieux":
            show ju fear
            I "Iirk !"
            hide cadenasL
            p "C'était donc ça. tu essayez de te protéger du regard de divinités."
            show ju re
            I "Sois raisonnable, je n'ai rien à me reprocher ici. Les divinités n'aurait pas à me surveiller."
            p "Donc tu me confirme que des divinités existent ici, tu n'es pas assez attentive."
            I "Espèce de..."
            jump offlinemenu112
        "La trame verte et bleue":
            show ju splain
            I "Je vois pas de lien dans cette association."
            p "Argh... si j'avais sû..."
            jump offlinemenu1
        "Le fait qu'ils soient 3":
            show ju splain
            I "Je vois pas de lien dans cette association."
            p "Argh... si j'avais sû..."
            jump offlinemenu1

label offlinemenu112:
    p "Et si je me permets, je pense savoir ce qu'ils font par ici mais avant ça..."
    show ju re
    I "Ne tente pas quelque chose que tu pourrais regretter."
    p "j'ai trouvé un autre document. Pour être plus précis, un rapport d'une organisation appellée OFAC."
    I "Oû est ce que tu l'as trouvée ?"
    p "Elle traînait par terre."
    I "Merde... J'étais presque sûre de l'avoir rangé..."
    p "Et je pense que l'important ici est..."
    menu:
        "L'OFAC":

            show ju splain
            I "Je vois pas de lien dans cette association."
            p "Argh... si j'avais sû..."
            jump offlinemenu1
        "La destruction du document":
            show ju splain
            I "Je vois pas de lien dans cette association."
            p "Argh... si j'avais sû..."
            jump offlinemenu1
        "L'association de personnages avec des dieux":
            show ju fear
            I "ARGH!"
            hide cadenasR
            p "Encore touché ! J'ai tout ce qui me faut désormais !"
            show ju re
            I "Ah vraiment? Et pourquoi donc ?"
            p "Parce qu'il y a un lien entre ces deux pièces qui représentent les dynamismes de ce monde."
            I "Et quel est ce lien ?"
            jump offlinemenu113
        "Jean Fraques":
            show ju splain
            I "Je vois pas de lien dans cette association."
            p "Argh... si j'avais sû..."
            jump offlinemenu1

label offlinemenu113:
    p "Je pense que ce lien est..."
    menu:
        "le fait que tous ces documents soient en papier":
            show ju splain
            I "Je vois pas de lien dans cette association."
            p "Argh... si j'avais sû..."
            jump offlinemenu1
        "Le grand dieu":
            show ju splain
            I "Je vois pas de lien dans cette association."
            p "Argh... si j'avais sû..."
            jump offlinemenu1
        "Le mec random":
            show ju splain
            I "Je vois pas de lien dans cette association."
            p "Argh... si j'avais sû..."
            jump offlinemenu1
        "Toi":
            p "Je pense que tu es le créateur entre les personnages et le dieu."
            show ju plexe
            I "Je..."
            p "De plus, je pense que tu as peur de l'affaire qui tourne autour de ces personnages."
            I "J..."
            p "Si quelqu'un se rendait compte que tu étais à l'origine de l'affaire ou que tu ne la maitrisais pas, tu risquerais beaucoup."
            I "Non, non..."
            p "Ce dieu, ou ce membre du conseil, est donc ton supérieur hyérarchique et tu es totalement sous sa tutelle !"
            show ju fear
            pause 2.0
            hide cadenasT
            pause 2.0
            hide chaine
            I "AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAARGH !"
            I "POURQUOIIIIIIIIII ?! POURQUOI ES-TU SI INSUPPORTABLE ?!"
            $ Achievement.add(achievement_name['Jubreakdownadmin'])
            show ju sad
            play music "audio/Tears of the past.ogg"
            pause (1)
            I "Je... Je..."
            pause 1
            I "J'imagine que tu a fini.e par trouver... Par toi même..."
            $ conseil = 1
            pause 2
            play music "audio/Void_Seeker.ogg"
            jump offlinemenu11

label timeskip:
    if inconnu == 8:
        jump offlinetransition2
    else:
        jump inverted

label menu12:
    menu:
        "retour":
            show ju splain
            I "C'est comme tu veux, chef.fe !"
            jump menu1

label menu13:
    show ju re
    I "Qui est ce 'il' qui t'a parlé de ça ?"
    "vous sentez les chaînes se reserrer un peu plus."
    menu:
        "Je préfère garder mes sources anonymes." if integrité < 1:
            I "Tu sembles oublier ta situation actuelle."
            p "J'ai de l'intégrité journalistique"
            $ integrité = 1
            I "On verra si tu veux vraiment rester sur tes positions."
            jump menu13
        "Je tiendrais mot" if integrité >= 1 and integrité <5:
            I "Ton respect d'autrui ne te mênera nulle part."
            I "Balance-le donc maintenant, ça va faire [integrité] fois que tu refuses"
            $ integrité = integrité + 1
            jump menu13
        "Je suis pas un collabo." if integrité == 5:
            I "Tu sais quoi ? J'en ai ma claque !"
            I "Je te laisse plus le choix, maintenant ! Réponds !"
            $ integrité = integrité + 1
            $ Achievement.add(achievement_name['Integrité Journalistique'])
            jump menu13
        "Oui... Bon... Ok... C'est toi.":
            show ju re
            I "M..."
            show ju fear
            I "Moi ?... Qu'est-ce que tu entends par moi ?"
            p "Eh bien d'une façon ou d'une autre je l'ai rencontré.e en personne."
            I "Comment est-ce que ça pourrait même être possible ?"
            p "Aucune idée mais il a l'air plus prompt à répondre à mes questions."
            I "Je te rapellerais que si tu veux plus d'infos, tu peux toujours me les poser de l'autre côté."
            p "Et je compte bien le faire."
            $ inconnu = inconnu + 1
            jump menu0

label menu2:
    hide screen mainUI
    show ju splain
    I "Vraiment? Montre le moi donc ! "
    python:
        codeg = renpy.input("Entrez le code")
    if code in codeg:
        show ju re
        $ Achievement.add(achievement_name['codedate'])
        I "Oh, je vois que tu as fait quelques recherches..."
        p "C'est censé correspondre à quoi?"
        I "C'est la date de fin et de début de mon deuxième univers."
        I "Y a pas grand chose d'autre à dire."
        I "Il a été reformaté récemment, d'où le fait que je mets un peu de temps à tout remettre en place."
        show ju splain
        jump menu0
    elif codeg == "Th3_4rch1v1st":
        A "{color=#000000} Ce jeu cache plus que tu ne peux l'imaginer. \n Elle même n'en sait rien."
        pause 3.0
        hide text
        A "{color=#000000} Nous resterons en contact, ne m'oublie pas. \n Je te parlerais à travers ces codes."
        pause 3.0
        hide text
        show ju splain
        I "Tu pensais à quelque chose?"
        p "Non ! Non... Rien..."
        show ju plexe
        I "Mmmmh..."
        jump menu0
    elif codeg == "PZHXJGVFS":
        $ expé = True
        "partie expérimentale déverouillée"
        jump menu0
    else:
        show ju splain
        I "Jamais entendu parlé."
        jump menu0

label menu3:
    hide screen mainUI
    show ju plexe
    I "C'est compréhensible. Je vais te sortir du quatrième glitch."
    show ju splain
    I "Adieu ou à bientôt j'imagine. Passe un bon reste de journée !"
    I "Si tu change d'avis, je reste là. C'est pas vraiment comme si j'avais le choix !"
    I "Ahahahahahahah...Ah"
    I "Save me Save me Save me Save me Save me Save me Save me Save me Save me Save me Save me Save me Save me Save me Save me Save me Save me Save me Save me Save me Save me Save me Save me Save me Save me Save me Save me Save me Save me Save me Save me Save me Save me Save me Save me Save me Save me Save me Save me Save me Save me Save me Save me Save me Save me Save me Save me Save me Save me Save me Save me Save me Save me Save me Save me Save me Save me Save me Save me Save me Save me Save me"
    show ju plexe_C
    "{color=#000000}Session ending"
    "{color=#000000}Closing simulation"
    "{color=#000000}Return to main menu"
    return



label finreset:
    show text "{color=#ffffff}VERY WELL"
    pause(2)
    hide text
    pause (1)
    show text _ ("{color=#ffffff} F IN  RE SET _I NCO MPLET") with dissolve
    $ Achievement.add(achievement_name['delete'])
    pause (3)
    return

label finwhite:
    stop music
    hide screen to_inverted
    window show
    p "{color=#ffffff}Non ! Pas si tôt !"
    pause (1)
    show text _ ("{color=#000000} Fin Perte de soi")
    $ Achievement.add(achievement_name['white'])
    pause (3)
    return

label finEdmes:
    stop music
    hide fond reboot fake
    hide animfond
    show Edmes closeup
    Edmes "Tu pensais vraiment que je te laisserais partir ?"
    show text _ ("{color=#ffffff} Fin Tué dans l'Oeuf") with dissolve
    $ Achievement.add(achievement_name['tuedansloeuf'])
    pause 3.0
    return

label finrhinoceros:
    stop music
    show YOU
    I "Oh mais je vous connais !"
    I "Je vous savais Autoritaire mais je ne pensais pas que vous seriez si idiot."
    I "Assez idiot pour casser votre couverture et vous jeter dans mes griffes !"
    I "Les légendes étaient donc vraies, vous êtes totalement incompétent !"
    I "Je ne vous tuerais pas tout de suite, je suis une bonne personne après tout, je ne peux pas vous laisser partir sans payer pour le mal que vous avez causé."
    show text _ ("{color=#ff0000} Bonne fin any% noclip ultra-antifa") with dissolve
    $ Achievement.add(achievement_name['antifa'])
    pause (3)
    return



label aventure:
    scene
    show Miclordes_trans
    show Miclordes
    play music "audio/Miclordes.ogg"
    hide screen mainUI
    hide screen inventory
    pause 2
    if persistent.av:
        show Miclordes H_T
        Miclordes "Rebonjour et rebonsoir, [name] !"
        Miclordes "Besoin d'un rappel sur ta mission ?"
        show Miclordes H
        menu:
            "J'ai besoin d'un rappel.":
                show Miclordes H_T
                Miclordes "Bon bah pars pour un petit récap' !"
                Miclordes "Tu dois trouver et rassembler les histoires en réparant ce que tu vois brisé, autant en vrai qu'en versions alternatives."
                Miclordes "Ton toi du futur m'a demandé de te dire \"Si tu te retrouve bloqué, trouve un moyen de passer entre les lignes et tu pourrais y trouver des routes alternatives.\""
                Miclordes "Bonne visite à travers les univers ! J'espère que tu trouvera ce que tu veux et doit trouver !"
                show Miclordes
                $ persistent.av = True
                show screen aventure
                pause 2
                hide Miclordes
                hide Miclordes_trans
                $ ui.interact()
            "C'est tout bon !":
                show Miclordes H_T
                Miclordes "Ok !"
                show Miclordes
                show screen aventure
                pause 2
                hide Miclordes
                hide Miclordes_trans
                $ ui.interact()
    else:
        show Miclordes T
        HUH "Bonjour, [name]."
        HUH "Tu sembles égaré mais également savoir où tu compte aller."
        show Miclordes
        p "Hein ? Qui êtes-vous ? Où suis-je ?"
        p "Comment connaissez-vous mon nom ?"
        show Miclordes T
        HUH "Je sais bien plus que ton nom, [name]."
        HUH "Je suis Miclordes, l'une des trois bras droit de l'Inconnue et la première Illustratrice."
        Miclordes "Je maitrise les déplacements dans le temps et l'espace, ce qui fait que je serais ton guide dans cet univers pour remplir ta mission."
        Miclordes "Nous sommes en ce moment même en train de voyager à grande vitesse à travers l'espace-temps."
        show Miclordes
        p "Comment ça ? Quelle mission ?"
        show Miclordes H_T
        Miclordes "Décidément, tu en poses des questions !"
        Miclordes "Tu me ferais presque penser à Ilona !"
        show Miclordes H
        p "Ilo-qui ?"
        show Miclordes T
        Miclordes "Attends au moins que je te réponde à ta question précédente avant de l'en poser une autre..."
        show Miclordes
        p "Désolé.e..."
        show Miclordes T
        Miclordes "Tu es l'ar... Peut-être que je devrais pas te le dire tout de suite."
        Miclordes "Tu es quelqu'un de spécial, [name]."
        Miclordes "ta mission ici est de rassembler tous les souvenirs et toutes les histoires afin de les réparer et d'en tirer quelque chose."
        show Miclordes
        p "Quelque chose ? Quel quelque chose ?"
        show Miclordes T
        Miclordes "Je ne peux pas le savoir, tu ne me l'as jamais dit."
        Miclordes "Mais l'un des futurs toi m'a dit de te dire quelque chose."
        Miclordes "\"Si tu te retrouve bloqué, trouve un moyen de passer entre les lignes et tu pourrais y trouver des routes alternatives.\""
        Miclordes "C'est rien d'incroyable mais bon, j'imagine que ça pourraît peut-être t'être utile."
        show Miclordes H_T
        Miclordes "Bonne visite à travers les univers ! J'espère que tu trouvera ce que tu veux et doit trouver !"
        show Miclordes
        $ persistent.av = True
        show screen aventure
        pause 2
        hide Miclordes
        hide expression "Miclordes/Miclordes.jpg"
        $ ui.interact()



label prologue_pacrel:
    hide screen pacrel
    show pacrel_nuit
    "Julien Pacrel est une âme errante de son monde."
    "Orphelin tôt dans son enfance à la suite d'un accident tragique, il fût contraint à vivre dans les ombres de la capitale d'Istelle, Appaos."
    "Survivant au jour le jour, squattant les bâtiments abandonnés, il est coincé dans un état d'apathie à se morfondre pour des évènements qu'il ne pourrait pas contrôler."
    "Il a échappé de peu à la grande guerre mais les tensions montent à nouveau désormais en 1925, ou du moins c'est ce que disent les journaux jetés par terre."
    "Lui comme les autres orphelins de la ville ont été abandonné.es et repoussé.es, jugé.es comme nuisibles et comme profiteurices du système."
    "Julien Pacrel ne comprend cependant pas vraiment ces critiques, d'autant plus que ces derniers ont désormais choisi un chemin de 'repentance' envers eux."
    "Dans la naissance de l'animation, iels se sont tous associé.es et organisé.es afin de former les studios sweep et de montrer de quoi iels sont réellement capables."
    "Iels utiliseront alors des locaux abandonnés de l'organisme de renseignement national, isolé par des grillages dans un quartier relativement peu fréquenté."
    "Ces derniers leur furent empruntés car considéré trop dangereux pour les riverains en l'échange d'une dette colossale qui leur sera demandée pour 1930 au plus tard."
    "Julien Pacrel est une âme promise à la mort depuis sa naissance mais sa détermination de survivre pour les autres pourrait bien le rendre immortel"
    $ Achievement.add(achievement_name['pacrel'])
    $ persistent.p0 = True
    show screen pacrel
    hide pacrel_nuit
    $ ui.interact()

label Ch1_pacrel:
    hide screen pacrel
    show pacrel_nuit
    "Studios sweep, Appaos \n 20 juillet 1929, 21h30"
    "Le soleil se couche une fois de plus sur la ville d'Appaos, métropole du sud-est de l'Istelle coincée au milieu des montagnes."
    "Vous vous dirigez discrètement une enième fois autour des barbelés du bâtiment abandonné par l'organisme de défense interterritorial."
    "les journées se suivent et se ressemblent. Les passants vous lancent toujours ces regards glaçants."
    hide pacrel_nuit
    jump Ch1_pacrel_F

label Ch1_pacrel_G:
    scene
    show white
    show grillage_1930
    show text "gauche"
    hide screen direction
    call screen directions (True, "Ch1_pacrel_B", True, "Ch1_pacrel_F")

label Ch1_pacrel_D:
    scene
    hide screen direction
    show white
    show grillage_1930
    show text "droite"
    call screen directions (True, "Ch1_pacrel_F", True, "Ch1_pacrel_B", True, "Ch1_pacrel_partir")

label Ch1_pacrel_F:
    scene
    hide screen direction
    show white
    show grillage_1930
    show text "avant"
    call screen directions (True, "Ch1_pacrel_G", True, "Ch1_pacrel_D")

label Ch1_pacrel_B:
    scene
    hide screen direction
    show fond ssback
    show grillage_1930 trou
    show text "arriere"
    call screen directions (True, "Ch1_pacrel_D", True, "Ch1_pacrel_G", avant = True, diravant = "Ch1_pacrel_rentrer")

label Ch1_pacrel_partir:
    scene
    hide screen direction
    Pacrel "Je pourrais faire un tour ailleurs avant, je n'ai pas envie de rentrer tout de suite..."
    menu:
        "Déambuler dans les rues":
            jump Ch1_pacrel_rue
        "Aller au magasin le plus proche":
            jump Ch1_pacrel_magasin

label Ch1_pacrel_rue:
    $ froid = froid+1
    if froid <=5:
        call screen directions (True, "Ch1_pacrel_rue", True, "Ch1_pacrel_rue", True, "Ch1_pacrel_rue", True, "Ch1_pacrel_rue")
    else:
        jump Ch1_pacrel_Game_over_perdu

label Ch1_pacrel_Game_over_perdu:
    "Peu"
    show black with dissolve
    "{color=#ffffff}Game Over \n Perdu dans le froid"
    show screen pacrel

label Ch1_pacrel_rentrer:
    scene
    hide screen direction
    "Vous écartez le trou dans le grillage et tentez de vous introduire, comme à votre habitude, dans l'enceinte de la zone confidentielle."
    call screen quicktimebar("Ch1_pacrel_rentré",20, __("Traversez les barbelés !"), True, "Ch1_pacrel_Game_over_tetanos")

label Ch1_pacrel_Game_over_tetanos:
    pause 2 
    "Votre habitude est si naturelle pour vous que vous ne faîtes plus attention à vos alentours."
    "Ce manque de prudence vous est cependant défavorable cette fois. Vos mains glissent sur le grillage."
    "Le grillage rouillé découpé vous transperce le dos et les mains."
    Pacrel "Argh ! Putain !"
    "Vous réussissez à vous en extirper et vous ne semblez pas tant saigner que ça."
    "Relativement irrité par votre erreur, vous vous glissez hâtivement à travers le grillage sans vous blesser davantage en grognant."
    Pacrel "{{Encore une journée qui sera tout au plus médiocre, hein ?}"
    "Vous traversez accroupi rapidement le côté nord de la zone à accès restreint le long de ses murs."
    "Une douleur soudaine vous traverse alors, vous faisant tomber à quatre pattes au sol."
    "Vous criez, vous appelez à l'aide, mais personne ne vint."
    "En essayant de vous relever, vos jambes sont saisies soudainement de spasmes et vous renvoit directement au sol."
    "Vous criez à l'aide d'autant plus."
    "Les passants vous lancent des regards méprisants lorsqu'iels ne tentent pas de vous éviter du regard."
    "Peu à peu, vos membres sont secoués de spasmes avant de s'immobiliser définitivement."
    "Vos cris deviennent de plus en plus troubles et faibles."
    "Vous finissez par vous immobiliser définitivement au milieu des hautes herbes."
    "Personne ne vous recherchera."
    show black with dissolve
    "{color=#ffffff}Game Over \n Succombe au tétanos"
    show screen pacrel
    $ ui.interact()

label Ch1_pacrel_rentré:
    pause 2
    "Vous réussissez à vous faufiler dans l'enceinte extérieur du bâtiment que vous occupez, comme chaque soir."
    "Vous traversez accroupi rapidement le côté nord de la zone à accès restreint le long de ses murs."
    "Loin du regard des autres, vous finissez par vous retrouver devant la porte du bâtiment dans lequel vous animez avec vos camarades."
    Pacrel "Et d'une journée de plus. On y arrivera cette fois."
    Pacrel "Ce soir, tout changera."
    jump Ch1_pacrel_porte

label Ch1_pacrel_porte:
    menu:
        "Enfoncer la porte d'un coup de pied":
            call screen quicktimebar ("Ch1_pacrel_bureau", 10, __("Enfonce cette porte !"), True, "Ch1_pacrel_porte",5)
            jump Ch1_pacrel_bureau
        "Pousser la poignée":
            $ Douceur = Douceur + 1
            "La porte résiste et ne s'ouvre pas. Elle semble rouillée sur place."
            if Douceur == 10:
                $ Achievement.add(achievement_name['Douceur'])
                "Il faudrait sans doute changer de tactique. Le respect des locaux ne semble plus très efficace après plusieurs siècles sans entretien. "
            jump Ch1_pacrel_porte

label Ch1_pacrel_bureau:
    pause 2
    "La porte s'ouvre violemment dans un grinçement strident et frappe le mur à pleine puissance."
    "Le bruit résonne dans l'ensemble du bâtiment et les couloirs s'emplissent de poussière."
    "Vous entrez dans le bâtiment avec assurance dans un silence complet."
    "Chacun de vos pas mettent en suspension dans l'air l'épaisse couche de poussière recouvrant le sol."
    "Le bois ancien recouvrant les murs imbibe l'air d'odeurs boisées partiellement putréfiée."
    "Le parquet grince et craque à chacun de vos pas. Vous vous dirigez avec assurance jusqu'à votre bureau."
    "Vous voyez de la lumière dans les différents bureaux et quelques personnes traverser de temps en temps les couloirs en passant d'un bureau à l'autre."
    "Vous voici en face de votre propre bureau. Vous soupirez un instant puis enfoncez la porte de ce dernier."
    "Vous avancez jusqu'à votre table de travail, en faites le tour par la droite et vous dirigez vers l'armoire métallique pour y prendre des feuilles."
    call screen quicktimebar("Ch1_pacrel_fin", 100, __("Récupère assez de copies blanches pour la prochaine heure"))

label Ch1_pacrel_fin:
    pause 2
    "Vous vous dirigez vers votre chaise et vous asseyez dans un silence assourdissant."
    show text _ ("{color=#ffffff}Fin du chapitre 1")
    pause 3
    $ persistent.p1 = True
    show screen pacrel
    scene
    hide text
    $ ui.interact()

label Ch2_pacrel:

label Ch3_pacrel:

label Ch4_pacrel:

label epilogue_pacrel:



label prologue_LJDV:
    hide screen LJDV
    show fondcafecreaB
    show fondcafecreaF
    "Créa, aka Joie, aka LaJoieDeVivre, est une Créatrice confirmée."
    "Tout comme ses paires, elle possède son monde dans lequel elle édicte ses règles."
    "Cependant, en opposition à ses paires, elle a tendance à voyager de dimension en dimension telle une exploratrice, à la recherche des trésors immatériels de ces univers."
    "Ses personnages étant attachés, métaphoriquement et littéralement, à elle, iels se retrouvent régulièrement à des endroits où iels ne devraient pas être."
    "Son sens de l'orientation, tout au moins questionnable, la mène souvent à se perdre dans des recoins d'univers qu'elle n'avait semblablement pas l'intention d'explorer."
    show joa R with dissolve
    LJDV "Hé ! Tu sais que je t'entends ?!"
    show joa R
    "Elle finit ainsi relativement fréquemment dans des situations compromettantes dans lesquelles elle essaye de paraître au plus hors de contrôle et d'appâter le danger loin des personnages,"
    "pour annihiler le problème en bonne et due forme sans casser la \"magie\" des univers qu'elle parcourt."
    "Son arme principale est le feu orangé, duquel elle fait transitionner les composés pour créer avec les cendres du passé."
    "LaJoieDeVivre est une Créatrice hors paire, capable de voir le beau dans chaque chose et d'en faire quelque chose d'exceptionnel."
    hide joa with dissolve
    $ persistent.LJDV0 = True
    show screen LJDV
    hide joa_prologue
    $ ui.interact()

label Ch1_LJDV:
    hide screen LJDV
    show fondcafecreaB
    show fondcafecreaF
    "31/12/2034 - 10h00 \n Café de la Cité des Créateurices"
    "Quelque chose de terrible va se passer aujourd'hui. Personne ici ne le sait encore. La chute va être brutale."
    "H-13 avant la fin du monde."
    show joassis marche behind fondcafecreaF at left with dissolve
    pause 0.5
    show joassis behind fondcafecreaF at left with dissolve
    LJDV "{{Il fait définitivement pas aussi froid qu'iels l'avaient annoncé aujourd'hui. On se croirait plus en mai qu'à la veille du nouvel an.}"
    LJDV "{{Après, je vais pas me plaindre. J'ai juste à discuter un peu avec Ajai de ce qu'il s'est passé cette année.}"
    LJDV "{{C'est bizarre, il est toujours là en avance d'habitude. Cette journée s'annonce vraiment étrange}"
    show ajaiassis marche behind fondcafecreaF at right with dissolve
    pause 0.5
    show ajaiassis behind fondcafecreaF at right with dissolve
    show ajaiassis behind fondcafecreaF at right
    Ajai "Désolé du retard, j'ai eu un petit contretemps."
    show joassis behind fondcafecreaF at left
    show ajaiassis behind fondcafecreaF at right
    LJDV "Ma foi si c'est qu'une fois par année !"
    show joassis behind fondcafecreaF at left
    show ajaiassis behind fondcafecreaF at right
    Ajai "On se voit qu'une fois par année d'habitude..."
    show joassis behind fondcafecreaF at left
    show ajaiassis behind fondcafecreaF at right
    LJDV "Des détails, tout ça !"
    LJDV "Comment ça va depuis l'année dernière ?"
    show joassis behind fondcafecreaF at left
    show ajaiassis behind fondcafecreaF at right
    Ajai "C'est un peu le bazar comme d'habitude, à tel point que je vois plus passer les jours."
    show joassis behind fondcafecreaF at left
    show ajaiassis behind fondcafecreaF at right
    LJDV "Ah bah ne m'en parle même pas !"
    show joassis behind fondcafecreaF at left
    show ajaiassis behind fondcafecreaF at right
    Ajai "Il s'est passé quoi de ton côté ?"
    show ajaiassis behind fondcafecreaF at left
    hide joassis
    hide ajaiassis
    show joa C at left
    show ajai think at right
    LJDV "Eh ben, il y a quelques heures, Samwy est rentré. Je l'avais plus revu depuis plusieurs années et, apparemment, je l'avais oublié dans l'univers de Julien."
    LJDV "Le pauvre était tellement perdu qu'il commençait à halluciner en pensant qu'il était en 2012 et que les murs pouvaient s'ouvrir !"
    show joa at left
    show ajai fear at right
    Ajai "Tu l'as oublié depuis 2012 ?!"
    show joa P at left
    show ajai fear at right
    LJDV "Peut-être bien mais au moins il est encore vivant, non ?"
    show joa P at left
    show ajai fear at right
    Ajai "Si tu continue à faire n'importe quoi, tu risqueras de te brûler. Le Conseil avait pas apprécié l'échec de Julien."
    show joa R at left
    Ajai "Whoa ! Calme toi !"
    show joa R at left
    show ajai fear at right
    LJDV "Tu sais très bien qu'il ne méritait pas ce qui lui est arrivé, et les autres non plus."
    show joa R at left
    show ajai fear at right
    Ajai "On a tenté ce qu'on pouvait à l'époque mais rien n'a fait."
    show ajai think at right
    Ajai "Au moins, on peut pour l'instant dire que cette sanction n'a pas l'air d'avoir d'effets sur lui. C'était peut-être juste un bon prototype."
    show joa R at left
    show ajai think at right
    LJDV "J'en doute, certains ont tendance à prendre du temps avant de montrer leurs effets."
    show joa R at left
    show ajai think at right
    menu:
        Ajai "On devrait peut-être parler d'autre chose non ? J'ai peur que quelqu'un nous entende ici."
        "Plutôt crever que de me censurer !":
            show ajai fear at right
            show joa R at left
            LJDV "Tu penses que c'est ce qu'iels auraient voulu ? Qu'on les abandonnent comme ça et qu'on accepte que ce soit normal ?!"
            LJDV "C'est pas normal qu'on soit muselé comme ça ! On devrait pouvoir dire ce qui se passe sans risquer notre existence face à ces fraudes !"
            show joa R at left
            show ajai fear at right
            Ajai "Stop ! On va nous entendre !"
            show joa R at left
            show ajai fear at right
            LJDV "J'en ai plus rien à foutre ! Qu'ils viennent m'arrêter si ils ont les couilles ! Les gens du Conseil sont pathétiques et ceux à leurs bottes sont stupides !"
            show joa R at left
            show garde
            Administrateur "Vous me flattez."
            show joa fear at left
            pause 0.5
            show joa P at left
            LJDV "Ah... Bonjour monsieur l'agent. Comment allez-vous ?"
            show joa P at left
            Administrateur "Très bien, tellement bien que je me sens d'humeur à vous faire visiter les locaux à accès restreint dans lesquels je travaille."
            show joa C at left
            LJDV "Vous m'en verrez flattée mais je ne puis malheureusement pas répondre à votre requête."
            show joa C at left
            Administrateur "Oh mais je ne vous laisse pas le choix. J'emmènerais également votre ami avec vous, juste au cas où."
            show joa R at left
            LJDV "Sous quel motif ?"
            show joa R at left
            show ajai fear at right
            Ajai "Pourquoi est-ce que je suis mis aussi dans le paquet ?"
            show ajai fear at right
            Administrateur "Outrage à agent et complicité. Vous vous expliquerez devant le tribunal."
            hide garde with dissolve
            show black with dissolve
            jump ch1_prison_LJDV
        "Revenir sur mon monde":
            show joa C at left
            show ajai think at right
            LJDV "Tu as sans doute raison, on peut pas vraiment faire confiance aux gens par ici. Ils ont des yeux de partout."
            LJDV "Eh bien, pour reprendre la discussion sur mon retour, j'ai assisté à des scènes particulièrement drôles."
            show joa C at left
            show ajai think at right
            Ajai "Ah vraiment ? Il faudrait que j'y fasse un tour un de ces jours !"
            show joa C at left
            show ajai think at right
            LJDV "Et comment ! Mais il faudra que tu fasses gaffe au chaos là bas."
            LJDV "Rien qu'en reprenant le cas de Samwy, je pourrais te parler du fait que, peu après être revenu, il a réemménagé avec scratch."
            LJDV "À peine rassemblés, ils sont redevenus aussi chaotique. Je ne pourrais même pas dire si c'était tout à fait conscient."
            show joa C at left
            show ajai fear at right
            Ajai "J'espère pour toi que ce n'est pas ingérable."
            show joa C at left
            show ajai think at right
            LJDV "Ingérable ? Loin de là ! C'est toujours un magnifique spectacle !"
            LJDV "Il y a de cela bientôt deux heures, ils se sont mis à l'idée de se mettre à la cuisine pour la première fois en essayant de faire un oeuf au plat."
            LJDV "Samwy n'avait cependant pas imaginé que garder sa bouteille de cognac à la main à proximité du feu et sa réserve derrière lui."
            show joa C at left
            show ajai think at right
            Ajai "C'est juste moi ou ça sent la catastrophe ?"
            show joa C at left
            show ajai think at right
            LJDV "Ah ça sent pas juste la catastrophe, c'est quasiment de la maladresse prémeditée !"
            LJDV "Sans surprise, Samwy en a versé un peu par accident sur le gaz, créant de grandes flammes bleues."
            LJDV "Et, pris dans la panique, il a décidé de répondre en fonction de ses connaissances."
            show joa C at left
            show ajai fear at right
            Ajai "C'est à dire ?"
            show joa C at left
            show ajai fear at right
            LJDV "Eh bien l'eau peut servir à éteindre un feu, pas vrai ?"
            show joa C at left
            show ajai think at right
            Ajai "Si elle est utilisée à bon escient j'imagine que oui mais tout dépent sur quoi et en quelle quantité."
            Ajai "Ils n'auraient pas pu simplement couper le gaz et attendre un instant ?"
            show joa C at left
            show ajai think at right
            LJDV "Oh tu en attends beaucoup d'eux là, mon pauvre !"
            show ajai fear at right
            LJDV "Eh bien, en continuant sur ce raisonnement, l'eau est un liquide, pas vrai ?"
            show joa C at left
            show ajai fear at right
            Ajai "Ne me dit pas que..."
            show joa C at left
            show ajai fear at right
            LJDV "Le cognac aussi est un liquide, pas vrai ?"
            show joa C at left
            show ajai fear at right
            Ajai "Je refuse de contracter."
            show joa C at left
            show ajai fear at right
            LJDV "Donc il devrait éteindre le feu !"
            show joa C at left
            show ajai fear at right
            Ajai "J'ai dit que je refusais d'y croire."
            show joa C at left
            show ajai fear at right
            LJDV "Sans surprise, donc, Samwy n'a même pas réfléchi et a versé l'intégralité du contenu de sa bouteille sur le feu !"
            LJDV "Que pourrait-il mal se passer ! Ahaha !"
            show joa C at left
            show ajai fear at right
            Ajai "Alors là..."
            show joa C at left
            show ajai fear at right
            LJDV "La pièce fut rapidement alors englouti par des flammes bleues, suivi par l'entièreté de l'appartement."
            show joa C at left
            show ajai fear at right
            Ajai "Aïe..."
            show joa C at left
            show ajai fear at right
            LJDV "Puis de tout l'immeuble !"
            show joa C at left
            show ajai fear at right
            Ajai "Double aïe..."
            show joa at left
            show ajai fear at right
            LJDV "Ils ont tenté de s'enfuir aussi vite qu'ils le pouvaient mais leurs voisins n'ont visiblement pas apprécié leur représentation pyrotechnique."
            LJDV "Ils se sont fait rapidement rattrapés et ont passé ce qu'on pourrait qualifier de sale quart d'heure."
            show joa C at left
            show ajai think at right
            Ajai "Je sais pas pourquoi mais ça ne m'étonne même plus. Tu n'as rien fait pour empêcher tout ça de dégénérer ?"
            show joa C at left
            show ajai think at right
            LJDV "Pourquoi donc ? Je savais qu'il ne risquait rien à long terme et c'était bien trop drôle de tout voir se dérouler."
            LJDV "J'aurais tout gâcher si j'avais essayé d'intervenir !"
            show joa at left
            show ajai think at right
            Ajai "J'imagine que tu n'as pas tord. Et les autres ? Iels vont bien ?"
            show joa C at left
            show ajai think at right
            LJDV "Plutôt bien oui, rien qui change de l'ordinaire."
            LJDV "À la limite il y aurait peut-être Rose et Hélios qui avait l'air de se déplacer un peu bizarrement à des endroits hors de ma portée."
            LJDV "Mais bon, je leur fais confiance et j'ai pas envie d'empiéter sur leur vie privée donc je les laisse faire ce qu'iels veulent !"
            LJDV "Je les ai vu trainer avec Samwy et certains personnages d'autres univers dont certains de Julien et de toi mais bon, rien de quoi s'inquiéter."
            show joa C at left
            show ajai think at right
            Ajai "Mes personnages ne sortent jamais de mon univers. Iels n'en ont ni la possibilité ni la motivation."
            show joa fear at left
            show ajai think at right
            LJDV "C... Comment ? Mais pourtant..."
            hide joa
            "Les heures passèrent alors à toute vitesse sans même que vous ne vous en rendiez compte."
            show fondcafecreaB N
            "Toute l'année écoulée se déroulait à nouveau en cet instant entre vous."
            "Et, sans même que vous ne le remarquiez dans un premier temps, celui qui mettrait fin à l'histoire était présent parmis vous."
            show joa R at left
            show ajai think at right
            "Vous sentez une pression à proximité. Quelque chose ne semble pas normal."
            show ajai think at right
            Ajai "Donc tu le ressens aussi ?"
            show joa C at left
            show ajai think at right
            LJDV "J'en ai bien l'impression."
            LJDV "Qu'est ce qu'il pourrait bien se passer pour que l'ambiance soit aussi lourde soudainement ?"
            show joa C at left
            show ajai think at right
            Ajai "Je pense que ça vient de ce gars."
            hide joa
            hide ajai
            hide window
            show capedmes
            LJDV "Qui peut bien être ce guignol ?"
            Ajai "Y a quelque chose qui cloche avec lui mais personne ne semble réagir..."
            LJDV "Etrange que les gardes ne réagissent pas à sa présence. Est ce que ça voudrait dire qu'il a été demandé par le conseil ?"
            hide capedmes
            show joa R at left
            show ajai think at right
            Ajai "C'est définitivement pas impossible"
            show ajai think at right
            "Une explosion retentit alors au loin, suivie par une autre, et encore une autre, et encore, et encore."
            show Pic_ombre_ch1joa
            "Un pic sombre sortit du sol, suivit par un autre, détruisant tout sur leur passage."
            show joa R at left
            LJDV "Des pics d'ombre !"
            hide Pic_ombre_ch1joa
            show joa R at left
            show ajai fear at right
            Ajai "Tu sais ce que c'est ?"
            show joa R at left
            show ajai fear at right
            LJDV "C'est l'arme principale d'Edmes ! Qu'est ce que ces trucs font là ?!"
            show joa_spike
            LJDV "Ecarte toi de là !"
            hide screen window
            play music "audio/Heartbeat.ogg"
            call screen quicktimebar("succes_picombre", 400, __("Résiste au pic d'ombre !"), True, "ch1_GO_Picombre", 60)

label succes_picombre:
    $ Achievement.add(achievement_name['Picombre'])
    jump ch1_GO_Picombre

label ch1_GO_Picombre:
    stop music
    hide joa_spike
    scene
    show black
    LJDV "J... J'ai réussi ?"
    LJDV "Ajai ? Tout va b.."
    LJDV "Argh !"
    show gopic 1
    "Vous sentez un pic d'ombre vous traverser, vous brûlant simultanément de froid et de chaud."
    "Votre vision se trouble de plus en plus. vos idées fusent dans tous les sens et disparaissent peu à peu."
    "Ajai, transpercé à vos côtés, semblent devenir de plus en plus terne, bien que vous ne sachiez plus distiguer le réel du fictif."
    "Vous ne reconnaissez plus la personne à vos côtés ni comment la situation a pu autant dégénérer, bien que vous en ayez un souvenir lointain"
    show gopic 2
    "Qui êtes-vous ? Où êtes-vous ? Qu'êtes-vous ?"
    "Vous ne le saurez sans doute jamais plus. Votre corps entier vous lâche."
    hide screen window
    show text _ ("{color=#ffffff}Game Over \n Transpercé par un pic d'ombre")
    pause 4
    show screen LJDV
    scene
    $ ui.interact()

label ch1_prison_LJDV:
    scene
    show fond prison_LJDV
    "..."
    show ajai think at right
    Ajai "Eh beh, on est pas dans le pétrin..."
    show ajai think at right
    show joa fear at left
    LJDV "Fallait s'y attendre en même temps..."
    show joa fear at left
    "Un bruit sourd retentit à la surface, suivi par plusieurs autres et des cris."
    show joa fear at left
    LJDV "Je sais pas ce qu'il se passe là haut mais j'aimerais pas être à leur place."
    hide joa with dissolve
    hide ajai with dissolve
    show fond prison_LJDV_barre
    show Charasime Eery
    pause 2.0
    show Charasime psycho
    HUH "Ils m'ont causé pas mal de problèmes là-haut mais maintenant je vais pouvoir m'occuper de votre cas."
    hide Charasime
    show fond prison_LJDV
    show ajai fear at right
    show joa fear at left
    LJDV "Eh beh on est pas dans le pétrin..."
    show joa fear
    hide screen window
    show text _ ("{color=#ffffff}Fin du chapitre 1")
    pause 3
    $ persistent.LJDV1 = True
    show screen LJDV
    scene
    hide text
    $ ui.interact()



label prologue_Powart:
    hide screen Powart
    show powart_prologue
    "Ajai, aka Powart, aka Le Poisson, est un Créateur confirmé."
    "Tout comme ses paires, il possède son monde dans lequel il édicte ses règles."
    "De nature casanière, il a tendance à ne quitter son monde pour la cité des Créateurices que très rarement."
    "Maître incontesté des eaux, il veille sur le géant bleu."
    "Il canalise ses sauts d'humeur et assure son sommeil tout en conservant son équilibre."
    "Ses personnages sont partagés entre deux tribus d'origine différentes, une de la mer et une de la terre."
    "Le second contrôle le premier, ou du moins c'est ce qu'ils s'aiment à imaginer."
    "Il règne par l'ignorance et l'exploitation de l'autre, sans même comprendre que leur vie dépend de leur existence."
    show ajai think
    Ajai "Tu as pris des libertés sur le lore. C'est pas très précis tout ça."
    show ajai think
    "Ces turbulences ont beau être aussi forte qu'elles puissent l'être, Powart les garde toujours entièrement sous contrôle."
    "Son arme principale est un trident et son élément de création est l'eau."
    "Ces dernières lui permettent de briser, de rogner et d'accumuler la matière pour modifier les paysages."
    "Powart est un Créateur hors paire, capable d'identifier les sources d'instabilités et de remodeler les fondations."
    $ persistent.Powart0 = True
    show screen Powart
    scene
    $ ui.interact()



label RPG:
    python:
        rpg_path = rpg_path.replace("\\\\","/")
        subprocess.Popen (rpg_path)
    call screen RPG



label world:
    hide screen world
    show train ext
    show Z penche with dissolve
    pause 1
    show Z penche
    z "Envie de faire un tour à bord de l'Interdimmentionnel Express ? Tous à bord !"
    z "Rangez vos bagages et installez vous confortablement ! Ce train démarera sous peu en direction de qui-sait-où !"
    show black with fade
    hide Z penche
    $ worldpick = renpy.random.randint(1,5)
    hide black
    hide train ext
    show train int onlayer bg
    if tupin == False:
        show screen flotrain onlayer under
    $ renpy.jump("world" + str(worldpick))

label flotrain:
    scene
    show screen flotrain
    $ choc = False
    show train int
    p "{{Depuis tout à l'heure, il me regarde comme si il attendait quelque chose de moi. Peut-être que je devrais me présenter ?}"
    p "Bonjour, monsieur. Comment allez-vous ? Me reconnaissez-vous de quelque part?"
    hide screen flotrain
    show flo happy

    flo "Oh, bonjour ! Désolé, je ne voulais pas te déranger. Je suis florian, j'aurais cru que tu saurais encore qui je suis."
    p "Ah... Euh... Vous me connaissez, donc ?"
    show flo stare
    flo "Oui mais de manière assez étrange, on dirait qu'ils m'ont complètement effacé de ta mémoire."
    p "Qu... Quoi ?"
    show flo happy
    flo "C'est pas important, te casse pas trop la tête. J'ai encore des trucs à préparer avant de te remettre au jus mais je te promets que je te réexpliquerais tout une fois que ça sera fait."
    flo "Pour l'instant, tout ce que tu dois savoir, c'est que tu peux me tutoyer et que si tu dois réparer des vieilles machines je suis ton homme !"
    if borne_noticed:
        p "Ah, justement ! J'ai trouvé une borne d'arcade cassée dans un monde pas loin de celui-là. Est ce que tu pourrais la réparer ?"
        flo "Mmmh... Je pense que je peux essayer ! Je ne garantis rien sur la réussite par contre !"
        p "Merci beaucoup !"
        flo "C'est rien. C'est dans quel monde ?"
        p "C'est dans l'univers de L'Inconnue."
        flo "Outch, tu t'es aventuré·e en territoire dangereux. C'est une zone ultra surveillée et tout juste assez stable pour ne pas s'effondrer sur elle-même."
        p "Si ça te dérange, ça n'en vaut sans doute pas la peine."
        flo "Ne t'inquiète pas, je m'en occupe. J'en profiterais pour essayer de désactiver quelques-uns de ces systèmes sur mon passage. Je t'attendrais là-bas, ok ?"
        p "Ok, à tout à l'heure"
        $ tupin = True
        "La borne d'arcade du hub principal est désormais en réparation."
        scene
        call screen world
    p "Merci ! J'essaierais d'y penser !"
    flo "Tu n'as rien en tête pour l'instant ?"
    p "Rien du tout, malheureusement."
    flo "Eh bien j'attendrais ici autant de temps qu'il le faudra. À la prochaine, ami·e amnésique !"
    hide flo
    $ choc = True
    hide screen flotrain
    $ renpy.jump("world" + str(worldpick))

label world1:
    show ju splain
    p "Oh rebonjour !"
    show ju splain
    I "Ceci est un test."
    show ju splain
    menu:
        "Faire une mauvaise blague":
            p "icule"
            show ju re
            pause 2.0
            p "Amaird..."
            show ju re
            I "I know where you live."
            $ Achievement.add(achievement_name['deez'])
            $ renpy.run(OpenURL('https://fr.wikipedia.org/wiki/Terre'))
            $ renpy.quit()
        "Approuver":
            "Elle semble satisfaite de son travail."
            scene
            hide screen flotrain
            call screen world

label world2:
    show joa C
    p "I had a... pretty interesting day..."
    show joa R
    LJDV "Are you sure ?"
    show joa C
    p "I..."
    show joa P
    LJDV "Are you sure ?"
    LJDV "Are you sure ?"
    LJDV "Are you sure ?"
    LJDV "Are you sure ?"
    LJDV "Are you sure ?"
    LJDV "Are you sure ?"
    LJDV "When you can't even say..."
    LJDV "My name..."
    scene
    hide screen flotrain
    call screen world

label world3:
    show Charasime Eery
    clem "......................................"
    p "....................................."
    clem "......................................"
    p "....................................."
    clem "......................................"
    p "....................................."
    clem "......................................"
    p "....................................."
    clem "......................................"
    p "....................................."
    clem "......................................"
    p "....................................."
    clem "......................................"
    p "....................................."
    show Charasime deter
    clem "Shimmi shimmi yay shimmi yay shimmi yaaaa"
    if name == "Charasime" or name == "Clémentine":
        p "Drank"
        clem "Swalla la la"
        p "Drank"
        clem "Swalla la la"
        p "Swalla la la"
        clem "Swalla la la"
    scene
    hide screen flotrain
    call screen world

label world4:
    show ju splain
    pause 2 
    show ju splain
    I "Oh bonjour !"
    I "Tu as déjà vu une imprimante humaine ?"
    show ju splain
    p "Hum... Non ?"
    show ju splain
    I "Maintenant, oui !"
    show ju splain at imprimante
    pause 5
    scene
    hide screen flotrain
    call screen world

label world5:
    show ju splain at right
    show Charasime psycho at left
    "..."
    "Il sembleraient qu'elles te fixent du regard."
    "Veux-tu tenter de fermer les yeux ?"
    menu:
        "Oui":
            show black with dissolve
            hide ju splain
            pause 2
            hide black
            show Charasime Eery:
                yalign 0.1
                zoom 3.

            pause 1 
            show Charasime deter:
                yalign 0.1
                zoom 3.

            clem "Do you have games on your phone ?"
            scene
            call screen world
        "Non, je préfère attendre (Le trajet peut être long et ne peut pas être skippé)":
            "Comme tu le voudras."
            "Il reste juste une heure de trajet."
            call screen quicktimebar ("world5_end", 500, __("Regarder l'horloge"))
            $ renpy.pause(60, hard=True)
            "Et une minute de passée."
            "J'imagine que tu ne regrette rien."
            $ renpy.pause(520, hard=True)
            "Dix minutes, tu tiens quand même bien le coup !"
            "Tu aurais pu partir ou faire autre chose simultanément mais tu n'avais rien sur toi."
            $ renpy.pause(1180, hard=True)
            "Et la demi-heure ! Tu es persévérant-e !"
            "Pourquoi il n'y a pas de timer ? Tu vas pas non plus me demander la lune après avoir regretté ton choix, si ?"
            $ renpy.pause(1800, hard=True)
            $ Achievement.add(achievement_name['idle'])
            "Peut-être qu'un de ces jours je mettrais vraiment une horloge, qui sait !"
            "Bah, de qui je me moque ? Ces sections dans le train ne sont pas canons."
            "Même le concept de la chôse n'est pas totalement implémenté ! Le but final serait, à la manière de pjsk, de se déplacer dans les décors d'histoire multiple."
            "Il serait alors possible de voir ces discussions un peu partout !"
            scene
            hide screen flotrain
            call screen world

label world5_end:
    $ Achievement.add(achievement_name['idle'])
    "Tu as réussi à fuir."
    scene
    hide screen flotrain
    call screen world


label Gare_Monde_J:
    scene
    show gare_monde
    show fond ecole:
        zoom 0.69
        xalign 0.5
        ypos 0.1
    show screen gare_monde ("menu111face", "{size=100}{color=#00d9ff}Julia L'Inconnue")
    call screen directions (True, "Gare_Monde_A", True, "Gare_Monde_T")
label Gare_Monde_A:
    scene
    show gare_monde
    show screen gare_monde ("menu111face", "{size=100}{color=#ffffff}PowarT")
    call screen directions (True, "Gare_Monde_C", True, "Gare_Monde_J")

label Gare_Monde_C:
    scene
    show gare_monde
    show screen gare_monde ("menu111face", "{size=100}{color=#ffffff}Charasime")
    call screen directions (True, "Gare_Monde_OWO", True, "Gare_Monde_A")

label Gare_Monde_OWO:
    scene
    show gare_monde
    show screen gare_monde ("menu111face", "{size=70}{color=#ffffff}OwOIWonderWhatsThis")
    call screen directions (True, "Gare_Monde_T", True, "Gare_Monde_C")

label Gare_Monde_T:
    scene
    show gare_monde
    show screen gare_monde ("menu111face", "{size=100}{color=#ffffff}LaJoieDeVivre")
    call screen directions (True, "Gare_Monde_J", True, "Gare_Monde_OWO")



label epilogue:
    A "Nous voici donc à la fin de la route."
    p "C'est passé si vite..."
    A "Et pourtant, ça a été si long."
    A "Une fois de plus, nous nous rencontrons ici. C'est si étrange que je... Enfin, que tu termine ici."
    A "Nous avons vu tout ce que nous avions à voir et collecté tout ce que nous pouvions."
    p "Je n'aurais même pas le droit à un dernier affrontement épique contre le grand personnage mystérieux de ce monde ?"
    p "Je me sens presque trahi sur la marchandise !"
    A "Heh, moi aussi !"
    p "En même temps, nous sommes la même personne."
    A "Mais, d'un autre côté, nous combattre à mort nous tuera ultimement nous deux."
    p "C'est vrai que ça serait pas ultra malin..."
    A "Et puis il s'est passé tant de choses, nous avons archivé tant de vies. Je pense qu'on mérite une petite pause."
    p "Tu n'as pas tort."
    pause 2.0
    ".{pause=1.0}.{pause=1.0}.{pause=1.0}.{pause=1.0}.{pause=1.0}"
    p "Il n'y a plus rien."
    A "Comment ?"
    p "Tout est silencieux maintenant, il n'y a plus rien ni personne."
    A "Tu as peur ?"
    p "Pas vraiment... C'est surtout que"

return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
