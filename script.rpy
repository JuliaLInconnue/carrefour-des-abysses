# Vous pouvez placer le script de votre jeu dans ce fichier.
init:

    python:
    
        import math

        class Shaker(object):
        
            anchors = {
                'top' : 0.0,
                'center' : 0.5,
                'bottom' : 1.0,
                'left' : 0.0,
                'right' : 1.0,
                }
        
            def __init__(self, start, child, dist):
                if start is None:
                    start = child.get_placement()
                #
                self.start = [ self.anchors.get(i, i) for i in start ]  # central position
                self.dist = dist    # maximum distance, in pixels, from the starting point
                self.child = child
                
            def __call__(self, t, sizes):
                # Float to integer... turns floating point numbers to
                # integers.                
                def fti(x, r):
                    if x is None:
                        x = 0
                    if isinstance(x, float):
                        return int(x * r)
                    else:
                        return x

                xpos, ypos, xanchor, yanchor = [ fti(a, b) for a, b in zip(self.start, sizes) ]

                xpos = xpos - xanchor
                ypos = ypos - yanchor
                
                nx = xpos + (1.0-t) * self.dist * (renpy.random.random()*2-1)
                ny = ypos + (1.0-t) * self.dist * (renpy.random.random()*2-1)

                return (int(nx), int(ny), 0, 0)
        
        def _Shake(start, time, child=None, dist=100.0, **properties):

            move = Shaker(start, child, dist=dist)
        
            return renpy.display.layout.Motion(move,
                time,
                child,
                add_sizes=True,
                **properties)

        Shake = renpy.curry(_Shake)
    #

init:
    transform flip:
        yzoom -1.0

#phrase d'intro

define fun = renpy.random.randint(1,41) 
default projecteur = 1

# Ecran précédant le menu principal
label splashscreen:
  play music "audio/Weirdness ensues.ogg"
  scene black
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

  show text _("{color=#ffffff}Un jeu de Julia L'Inconnue (ft charasime)") at Position(xpos=0.5,xanchor=0.5,ypos=0.9,yanchor=0.9) with dissolve
  show linconnue at Position(xpos=0.5,xanchor=0.5,ypos=0.5,yanchor=0.5,) with dissolve
  with Pause (1)
  hide text with dissolve
  hide linconnue with dissolve
  with Pause (0.5)

  if fun >= 2:
    show text "{color=#ffffff}CW : Disturbing imagery and themes" with dissolve
  else:
    show text "CW : no bitches :("
  with Pause (5)
  hide text with dissolve
  with Pause (1)
  #texte d'intro
  if fun == 1:
    show text "{color=#ffffff}You got absolutely no bitches" at Position (ypos=0.4) as text1
    pause 1.0
    show text "{color=#ffffff}Not a single maiden" at Position (ypos=0.6) as text2
    $ Achievement.add(achievement_name['nobitches'])
  elif fun == 2:
    show text "{color=#ffffff}Top text" at Position (ypos=0.4) as text1
    pause 1.0
    show text "{color=#ffffff}Bottom text" at Position (ypos=0.6) as text2
  elif fun == 3:
    show text _("{color=#ffffff}Un principe de texte d'intro") at Position (ypos=0.4) as text1
    pause 1.0
    show text _("{color=#ffffff}honteusement dérobé à la funkin team") at Position (ypos=0.6) as text2
  elif fun == 4:
    show text _("{color=#ffffff}Tu as détruit ton monde.") at Position (ypos=0.4) as text1
    pause 1.0
    show text _("{color=#ffffff}Nous ne pouvons pas te laisser impuni.") at Position (ypos=0.6) as text2
  elif fun == 5:
    show text "{color=#ffffff}The grievous lady may not have a face" at Position (ypos=0.4) as text1
    pause 1.0
    show text "{color=#ffffff}but she sees everything" at Position (ypos=0.6) as text2
  elif fun == 6:
    show text "{color=#ffffff}Crazy?" at Position (ypos=0.4) as text1
    pause 1.0
    show text "{color=#ffffff}I was crazy once !" at Position (ypos=0.6) as text2
  elif fun == 7:
    show text _("{color=#ffffff}Si ce jeu est fini un jour,") at Position (ypos=0.4) as text1
    pause 1.0
    show text _("{color=#ffffff}je pense que pas grand monde y jouera") at Position (ypos=0.6) as text2
  elif fun == 8:
    show text _("{color=#ffffff}La perfection n'est pas atteignable") at Position (ypos=0.4) as text1
    pause 1.0
    show text _("{color=#ffffff}mais Charasime a un cheat code") at Position (ypos=0.6) as text2
  elif fun == 9:
    show text _("{color=#ffffff}J'ai peur et j'ai froid...") at Position (ypos=0.4) as text1
    pause 1.0
    show text _("{color=#ffffff}La solitude me dévaste...") at Position (ypos=0.6) as text2
  elif fun == 10:
    show text _("{color=#ffffff}Si il n'est pas satisfaisant pour nos attentes,") at Position (ypos=0.4) as text1
    pause 1.0
    show text _("{color=#ffffff}nous reprendrons la main") at Position (ypos=0.6) as text2
  elif fun == 11:
    show text _("{color=#ffffff}La malveillance est max") at Position (ypos=0.4) as text1
    pause 1.0
    show text _("{color=#ffffff}mais le skill est min") at Position (ypos=0.6) as text2
  elif fun == 12:
    show text _("{color=#ffffff}Entre l'antagoniste et l'écrivain,") at Position (ypos=0.4) as text1
    pause 1.0
    show text _("{color=#ffffff}qui est vraiment responsable de la fin du monde?") at Position (ypos=0.6) as text2
  elif fun == 13:
    show text '{color=#ffffff} \"Non désolée :emoji_décu_pointant_le_ciel:\"' at Position (ypos=0.4) as text1
    pause 1.0
    show text "{color=#ffffff}- LaJoieDeVivre" at Position (ypos=0.6) as text2
  elif fun == 14:
    show text _("{color=#ffffff}La raclette va au placard à couvert") at Position (ypos=0.4) as text1
    pause 1.0
    show text _("{color=#ffffff}et les couverts dans le four à micro-ondes") at Position (ypos=0.6) as text2
  elif fun == 15:
    show text _("{color=#ffffff}Ce splash screen") at Position (ypos=0.4) as text1
    pause 1.0
    show text _("{color=#ffffff}m'as pris beaucoup trop de temps") at Position (ypos=0.6) as text2
  elif fun == 16:
    show text _("{color=#ffffff}Des fois") at Position (ypos=0.4) as text1
    pause 1.0
    show text _("{color=#ffffff}je pense") at Position (ypos=0.6) as text2
  elif fun == 17:
    show text "{color=#ffffff}Stop posting about Among Us" at Position (ypos=0.4) as text1
    pause 1.0
    show text "{color=#ffffff}I'm tired of seeing it" at Position (ypos=0.6) as text2
  elif fun == 18:
    show text "{color=#ffffff}Kasane Teto supremacy" at Position (ypos=0.4) as text1
    pause 1.0
    show text "{color=#ffffff}Pearto mass destruction weapon" at Position (ypos=0.6) as text2
  elif fun == 19:
    show text "{color=#ffffff}hey guys" at Position (ypos=0.4) as text1
    pause 1.0
    show text "{color=#ffffff}did you know that in term of male human and fem-" at Position (ypos=0.6) as text2
  elif fun == 20:
    show text _("{color=#ffffff}Edmes a beau avoir formatté à tour de bras,") at Position (ypos=0.4) as text1
    pause 1.0
    show text _("{color=#ffffff}il n'a jamais tué personne.") at Position (ypos=0.6) as text2
  elif fun == 21:
    show text _("{color=#ffffff}Mieux que Garten of BanBan") at Position (ypos=0.4) as text1
    pause 1.0
    show text _("{color=#ffffff}depuis l'old alpha 1.0") at Position (ypos=0.6) as text2
  elif fun == 22:
    show text "{color=#ffffff}We are so back" at Position (ypos=0.4) as text1
    pause 1.0
    show text "{color=#ffffff}We are getting this game" at Position (ypos=0.6) as text2
  elif fun == 23:
    show text "{color=#ffffff}Soutien à Meurice" at Position (ypos=0.4) as text1
    pause 1.0
    show text "{color=#ffffff}Un humour à défendre" at Position (ypos=0.6) as text2
  elif fun == 24:
    show text _("{color=#ffffff}Attention aux rhinocéros") at Position (ypos=0.4) as text1
    pause 1.0
    show text _("{color=#ffffff}Ils se propagent vite ces cons") at Position (ypos=0.6) as text2
  elif fun == 25:
    show text "{color=#ffffff}I like thigh highs" at Position (ypos=0.4) as text1
    pause 1.0
    show text "{color=#ffffff}especially when I'm wearing them" at Position (ypos=0.6) as text2
  elif fun == 26:
    show text _("{color=#ffffff}Tout est politique") at Position (ypos=0.4) as text1
    pause 1.0
    show text _("{color=#ffffff}Même dire l'inverse") at Position (ypos=0.6) as text2
  elif fun == 27:
    show text _("{color=#ffffff}Faire tout brûler") at Position (ypos=0.4) as text1
    pause 1.0
    show text _("{color=#ffffff}faire tout péter") at Position (ypos=0.6) as text2
  elif fun == 28:
    show text _("{color=#ffffff}Méééé euh... puisque je vous dis que je savais pas") at Position (ypos=0.4) as text1
    pause 1.0
    show text _("{color=#ffffff}C'est pas ma faute si à Betharram y avait des enfants et des prêtres.") at Position (ypos=0.6) as text2
  elif fun == 29:
    show text "{color=#ffffff}I'll make you say" at Position (ypos=0.4) as text1
    pause 1.0
    show text "{color=#ffffff}How proud you are of me" at Position (ypos=0.6) as text2
  elif fun == 30:
    show text _("{color=#ffffff}MGED en bikini") at Position (ypos=0.4) as text1
    pause 1.0
    show text _("{color=#ffffff}Charasime ravie et Joa terrifiée") at Position (ypos=0.6) as text2
  elif fun == 31:
    show text _("{color=#ffffff}Bourré, Jules écrit") at Position (ypos=0.4) as text1
    pause 1.0
    show text _("{color=#ffffff}tout son code en une ligne") at Position (ypos=0.6) as text2
  elif fun == 32:
    show text _("{color=#ffffff}Faites des poutous") at Position (ypos=0.4) as text1
    pause 1.0
    show text _("{color=#ffffff}Votou Poutez") at Position (ypos=0.6) as text2
  elif fun == 33:
    show text _("{color=#ffffff}Une biologiste dessinatrice ? Et puis quoi encore ?") at Position (ypos=0.4) as text1
    pause 1.0
    show text _("{color=#ffffff}Une biologiste programmeuse ?") at Position (ypos=0.6) as text2
  elif fun == 34 :
    show text _("{color=#ffffff}Notre accord avec ce dieu sera grandiose !") at Position (ypos=0.4) as text1
    pause 1.0
    show text _("{color=#ffffff}Qu'est ce qui pourrait mal se passer ?") at Position (ypos=0.6) as text2
  elif fun == 35 :
    show text "{color=#ffffff}Les GB dominent le monde" at Position (ypos=0.4) as text1
    pause 1.0
    show text "{color=#ffffff}Et les EIPI dominent le shitpost" at Position (ypos=0.6) as text2
  elif fun == 36 :
    show text "{color=#ffffff}All the single furries" at Position (ypos=0.4) as text1
    pause 1.0
    show text "{color=#ffffff}All the singles furries" at Position (ypos=0.6) as text2
  elif fun == 37 :
    show text "{color=#ffffff}Shikanoko nokonoko" at Position (ypos=0.4) as text1
    pause 1.0
    show text "{color=#ffffff}Koshitantan" at Position (ypos=0.6) as text2
  elif fun == 38 :
    show text "{color=#ffffff}Typhlosion" at Position (ypos=0.2) as text1
    pause 0.5
    show text "{color=#ffffff}Vaporeon" at Position (ypos=0.4) as text2
    pause 0.5
    show text "{color=#ffffff}Gardevoire" at Position (ypos=0.6) as text3
  elif fun == 39 :
    show text "{color=#ffffff}Imagine prendre plus de 8 semaines à comprendre" at Position (ypos=0.4) as text1
    pause 1.0
    show text "{color=#ffffff}comment faire fonctionner la présentation de texte correctement" at Position (ypos=0.6) as text2
  elif fun == 40 :
    show text "{color=#ffffff}Ce jeu contient une grande quantité de" at Position (ypos=0.4) as text1
    pause 1.0
    show text "{color=#ffffff}fun" at Position (ypos=0.6) as text2
    pause 0.95
    show text "{color=#ffffff}fun" at Position (ypos=0.625,xpos=0.525) as text25
    pause 0.9
    show text "{color=#ffffff}fun" at Position (ypos=0.65,xpos=0.55) as text3
    pause 0.85
    show text "{color=#ffffff}fun" at Position (ypos=0.675,xpos=0.575) as text35
    pause 0.8
    show text "{color=#ffffff}fun" at Position (ypos=0.7,xpos=0.6) as text4
    pause 0.75
    show text "{color=#ffffff}fun" at Position (ypos=0.725,xpos=0.625) as text45
    pause 0.7
    show text "{color=#ffffff}fun" at Position (ypos=0.75,xpos=0.65) as text5
    pause 0.65
    show text "{color=#ffffff}fun" at Position (ypos=0.775,xpos=0.675) as text55
    pause 0.6
    show text "{color=#ffffff}fun" at Position (ypos=0.8,xpos=0.7) as text6
    pause 0.55
    show text "{color=#ffffff}fun" at Position (ypos=0.825,xpos=0.725) as text65
    pause 0.5
    show text "{color=#ffffff}fun" at Position (ypos=0.85,xpos=0.75) as text7
    pause 0.45
    show text "{color=#ffffff}fun" at Position (ypos=0.875,xpos=0.775) as text75
    pause 0.4
    show text "{color=#ffffff}fun" at Position (ypos=0.9,xpos=0.8) as text8
    pause 0.35
    show text "{color=#ffffff}fun" at Position (ypos=0.925,xpos=0.825) as text85
    pause 0.3
    show text "{color=#ffffff}fun" at Position (ypos=0.95,xpos=0.85) as text9
    pause 0.25
    show text "{color=#ffffff}fun" at Position (ypos=0.975,xpos=0.875) as text95
    pause 0.2
    show text "{color=#ffffff}fun" at Position (ypos=1,xpos=0.9) as text10
    $ Achievement.add(achievement_name['fnaf 6'])
  elif fun == 41 :
    show text "{color=#ffffff}My name is Edwin." at Position (ypos=0.3) as text1
    pause 1.0
    show text "{color=#ffffff}I made the mimic." at Position (ypos=0.5) as text2
    pause 1.0
    show text "{color=#ffffff}It was difficult to put the pieces together." at Position (ypos=0.7) as text3
  with Pause (1)
  hide text
  return

##introduction / Arc Inconnu
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
    show ju splain_T
    I "Ah, me voilà!"
    show ju fear_T
    I "Qu'est ce que ?"
    show ju plexe_T
    I "Excusez-moi mais qui êtes vous?"
    show ju plexe
    python:
     name = renpy.input(_("Entrez votre nom ou pseudonyme"))
     name = name.strip() or "XDDCC"
    show ju splain
    jump menu00
       
label menu00:
 show ju splain_T
 if name=="Julia" or name=="L'Inconnue":
   I "Ahah!"
   I "Ah..."
   show ju re_T
   I "Je vois que j'ai affaire à un.e petit.e rigolo.tte..."
   I "Pas vrai, [currentuser]?"
   $ Achievement.add(achievement_name['doxxed'])
   $ name=currentuser
   I "Fais gaffe à ce que tu pourrais dire ici."
   I "Tu sais quoi? J'utiliserais ton nom jusqu'à nouvel ordre, [name]"
   show ju splain
   jump menu0
 elif name == "Créa" or name == "Téa" or name == "Joa" or name == "lajoiedevivre":
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
   show ju plexe_T
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
  I "shimishimi yay shimi yay shimi ya"
  I "drank, swalalala"
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
   show ju splain_T
   I "Bon retour !"
   I "Tu m'as presque manqué, comment ça va?"
   show ju splain
   menu:
      "Plutôt bien !":
       show ju splain_T
       I "Oh bah parfait !"
       show ju splain
       jump menu0
      "Plutôt mal...":
       show ju fear
       pause (1)
       show ju fear_T
       I "Oh..."
       I "Tu veux en parler?"
       show ju fear
       menu:
         "Un peu...":
           show ju wu_T
           I "je suis à l'écoute, dis moi tout ce qui te fais mal."
           show ju wu
           "Elle écoutera rien du tout, il n'y a ni enregistrement ni adaptation au texte."
           show ju fear
           pause (0.5)
           show ju fear_T
           I "Hey ! D'où tu me grille comme ça?"
           I "Le logiciel a raison, j'ai aucun moyen de répondre efficacement..."
           I "Mais c'est un peu pareil dans la vraie vie. Le mieux serait d'aller voir un psy."
           show ju wu_T
           I "Quoi qu'il en soit, donc, je te laisse un espace de discussion."
           show ju wu
           python:
             so6 = renpy.input("")
             so6 = 1
           show ju wu_T
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
           show ju splain_T
           I "Ok, très bien."
           show ju wu_T
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
   show ju splain_T
   I "Je n'ai jamais entendu parlé de toi."
   I "Que fais tu ici, [name]? T'es perdu.e? Tu me dis vraiment rien..."
   I "Ou du moins, ton visage ne me dit rien pour l'instant..."
   I "J'ai quand même un... mmmh..."
   show ju splain
   I "\{Pourquoi son visage me dit tout de même quelque chose?\}"
   jump menu0

label menu0:
 
 $ persistent.visite = True
 hide anifond
 hide anifond 2
 hide ju fear
 hide screen Arret_urgence
 hide screen directionsD
 hide screen directionsG
 hide screen directionsB
 hide screen directionsF
 hide screen aventure
 hide fond ecole
 hide ju splain
 hide image "Miclordes/Miclordes.jpg"
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
   p "\{Ce n'est clairement pas Julia...\}"
   p "Non, merci, je vais partir très vite, je n'ai pas besoin de tout ça."
   hide juposteur
   show fond reboot fake
   play music "audio/Heartbeat.ogg"
   call screen quicktimebaredmes()
 else:
   show fond ecole
   show ju splain_T
   show anifond behind fond
   I "Alors, dis moi [name], qu'est ce que tu viens faire là?"
   show ju splain
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
 show ju fear_T at flip
 I "Oulah ! Qu'est ce que t'as foutu ?!"
 p "Il va falloir que je règle ça vite !"
 show ju fear at flip
 window hide 
 show screen directionsFbis
 $ ui.interact()
         
label menu1:
  hide screen mainUI
  show ju splain
  menu:
     "Qui êtes-vous?":
       show ju splain_T
       I "Moi? Je m'appelle Julia mais aux yeux des autres créateurices je suis l'Inconnue. Je suis la maîtresse et créatrice de ces lieux."
       show ju splain
       p "C'est quand même un peu vide, non?"
       show ju plexe_T
       I "C'est vrai que c'est pas immense pour l'instant..."
       I "Mais c'est un début ! C'est encore temporaire !"
       show ju plexe
       p "Mouais..."
       p "\{Bref, ça m'a donné d'autres idées de questions...\}"
       p "\{Peut-être que je devrais lui demander...\}"
       show ju splain
       jump menu11
     "Où sommes nous?":
       show ju splain_T
       I "Tu te trouves actuellement à la naissance d'un nouveau monde, ce que nous appelons le quatrième glitch."
       I "C'est basiquement comme une base contenant les éléments les plus simple de tout monde."
       I "J'imagine qu'on peut un peu estimer que ça pourrait correspondre à un modèle ou à une game engine."
       I "Pour l'instant, on se retrouve dans une petite pièce à l'écart de tout ça que j'ai créée en vitesse."
       show ju splain
       p "C'est pas mal pour un début."
       show ju wu_T
       I "Merci, ça me flâte !"
       show ju splain_T
       I "Mais j'ai plus vraiment de mérite."
       I "En général, la première fois est compliquée mais les fois suivantes sont plus simples."
       show ju splain
       p "\{Est ce qu'il sous-entends qu'il y en a déjà eu avant?\}"
       p "\{Peut-être que je devrais lui poser la question...\}"
       jump menu12
     "Quid de Julien L'Inconnu ?" if inconnu == 1:
       show ju splain_T
       I "Julien L'Inconnu était mon ancien nom !"
       show ju splain
       p "C'était donc pour ça qu'il ne te connaissais pas !"
       show ju re_T
       I "attends une minute..."
       show ju re
       p "*gulp* \{ pas encore... \}"
       "Vous sentez de lourdes chaînes métalliques se serrer à vos poignets jusqu'à ce que retentisse un \"clic\" métallique."
       "Le froid et la pression des menottes vous brûle les poignets."
       jump menu13
     "Qui est Edmes ?" if inconnu == 5 :
       show ju plexe_T
       I "Edmes ?"
       show ju plexe
       p "Oui, tu l'avais mentionné un peu plus tôt de l'autre côté. Qui est-il ?"
       show ju plexe_T
       I "C'était un des personnages de mon deuxième univers."
       I "Plus précisément, c'était un Executeur."
       show ju plexe
       p "Un Executeur ? C'est encore un type de hierarchie?"
       show ju plexe_T
       I "Non, c'est un système que j'avais implanté pour éviter tout problème similaire à la fin de mon premier univers."
       I "Le principe étant que tout personnage vivant est sous ma supervision, j'ai décidé de créer des Executeurs pour tuer des personnages et ainsi exploiter une faille pour les rendre plus puissant."
       show ju plexe
       p "C'est pas ultra clair comme truc..."
       show ju plexe_T
       I "En gros, j'ai utilisé des persos pour tuer d'autres persos pour avoir des assistants non subordonnés à moi."
       show ju plexe
       p "Je sais pas pourquoi mais ça sent la mauvaise idée..."
       show ju plexe_T
       I "Tu ne pourrait pas être plus juste."
       I "Pour éviter le danger de la prise de pouvoir des Exécuteurs, j'avais prévu leur disparition une fois les personnages ciblés morts."
       I "Edmes était le second. Il était différent. Il avait la connaissance du temps et il voulait se venger à tout prix..."
       show ju plexe
       p "C'est donc pour ça que tu as fini corrompu fut un temps ?"
       show ju plexe_T
       I "Oui et c'est aussi la cause principale de l'affaire Pacrel."
       show ju plexe
       if inconnu == 5:
         $ inconnu = inconnu + 1
       jump menu1
     "Qu'est ce que l'affaire Pacrel ?" if inconnu == 6 :
       show ju splain_T
       I "L'affaire Pacrel est une affaire entamée autour d'Edmes et de Julien Pacrel."
       I "Il aurait dû être un Illustrateur, un de mes bras droit. Edmes a cependant compris la supercherie et, bien qu'il soit attaché comme une ombre à Pacrel, il a causé d'énormes problèmes."
       show ju splain
       p "C'est donc de là que vienne les personnages corrompus..."
       show ju splain_T
       I "Les Ink Guys, exactement. Edmes dépendant de la survie de Pacrel pour la sienne, il l'a gardé en souffrance tout juste en vie."
       I "Ce qui a créé de nombreuses rumeurs sur ses proches et beaucoup de questionnement médicaux autour de son cas."
       I "Mais rien de tout cela n'aurait jamais existé si il était réellement random."
       I "Julien Pacrel était un orphelin et avait passé ses jours à squatter des lieux abandonnés jusqu'en 1930 en groupe."
       I "C'était ce qui lui semblait le plus simple mais qui le mettait également beaucoup en danger quand il revenait en terrain confidentiel."
       I "Ses nombreux larcins de survie l'avait rendu connu aux yeux de toute la région et donc, en addition de circonstance, l'histoire fut très relayée."
       I "Et pour la fin de cette affaire, je ne saurais plus vraiment partir en détail."
       show ju splain
       p "Très bien, j'ai compris, je retourne le voir."
       if inconnu == 6:
         $ inconnu = inconnu + 1
       jump menu1
     "Retour":
       show ju splain_T
       I "Ok, on peut repousser ça à plus tard."
       show ju splain
       jump menu0

label menu11:
  menu:
    "Des Créateurices? Quesaquo?":
      show ju splain_T
      I "C'est en quelque sorte quelqu'un de normal."
      show ju splain
      p "Quelqu'un de normal? Je serais aussi un.e Créateur.ice?"
      show ju splain_T
      I "En quelque sorte..."
      I "Enfin, je crois? Tu as un monde, toi?"
      show ju splain
      p "Je sais pas vraiment..."
      show ju splain_T
      I "Est-ce que tu as déjà créé quelque chose?"
      I "De manière artistique quelconque, en dessinant, chantant, écrivant, sculptant, jouant de la musique, faisant un sport en synchro, programmant, gravant, modelant ou tout autre manipulation de matière?"
      show ju splain
      p "Je... J'imagine?"
      show ju splain_T
      I "alors tu en est un.e, c'est aussi simple que ça."
      show ju splain
      p "Et du coup, ce qui nous entoure..."
      show ju splain_T
      I "Est une projection de ces différents types d'art."
      I "De plus, n'importe qui du monde réel peut être Créteurice."
      I "Pas besoin d'être connu, professionnel ou même d'avoir étudié l'art."
      show ju plexe_T
      I "Même si c'est vrai que des fois ça peut aider..."
      show ju splain
      jump menu11
    "Existe-il des influences inter-Créateurices?":
      show ju splain_T
      I "Y'en a pas mal, yep !" 
      I "En soit, comme pour tout, c'est difficile voire impossible de partir de rien et tout ou presque a déjà été fait."
      I "Donc quoi qu'il arrive et quoi qu'on fasse, on se base toujours sur le travail d'autrui."
      I "Des fois, on peut penser qu'un travail est tout à fait original mais il ne faut pas oublier que ce n'est plus ou moins qu'un mélange de très nombreuses sources."
      I "Regarde la salle par exemple !"
      hide ju splain_T
      window hide
      pause (3)
      window show
      show ju splain
      p "Et si on sort de ça, est ce qu'il y a des relations de pouvoirs?"
      show ju splain_T
      I "Ahahah !"
      show ju plexe_T
      I "Ah..."
      I "C'est vrai qu'il y a ça aussi..."
      show ju plexe
      p "Eh bien?"
      show ju re_T
      I "Yep, Y'en a."
      I "Je sais pas si j'ai le droit d'en dire plus, le conseil m'écoute sans doute."
      show ju re
      p "C'est à dire?"
      I "..."
      p "\{On dirait que si je veux aller plus loin, il va falloir que je lui force un peu la main...\}"
      p "\{Je prends des risques par contre... Je sais pas comment elle réagira...\}"
      p "\{Je devrais peut-être prendre des pincettes...\}"
      jump menu111
    "retour":
      show ju splain_T
      I "Si tu veux en reposer, je suis encore là."
      show ju splain
      jump menu1

label menu111:
  menu:
    "Je fais parti.e du conseil, tu peux tout me dire !":
      stop music fadeout 1
      show ju re_T
      I "Ah?"
      I "C'est ... Vrai?"
      hide ju re_T
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
      p "\{Peut être que ça serait pas mal que je vérifie les alentours avant de prendre des décisions...\}"
      p "\{Je ne sais juste pas vraiment où commencer\}"
      show ju splain
      jump menu11

label menu111face:
 hide projecteur1
 hide projecteur2
 hide fonddroite2
 hide screen mainUI
 hide ju splain
 hide screen directionsD
 hide screen directionsG
 show anifond
 show fond ecole
 show screen directionsF
 $ ui.interact()

label HMlib:
  hide screen directionsF
  hide screen window
  p "\{Des bouquins sur un gars random et ses deux associés devenus immortels qui se bat contre son alter-ego pour sauver son créateur et des dieux qui observent la destruction comme un spectacle\}"
  if "Trilogie Histoire Multiple" in inventory_items:
    p "Je les ai déjà, ça ne servirait à rien de les reprendre."
    jump menu111face
  else:
    $ inventory_items.append("Trilogie Histoire Multiple")
    "A obtenu la trilogie Histoire Multiple ! Elle semble incomplète ..."
    p "\{Je me demande ce qu'ils font là et pourquoi ils sont mis en importance à ce point\}"
  jump menu111face

label ofac1:
  hide screen directionsF
  hide screen window
  if "Rapport OFAC 105" in inventory_items:
   p "toujours intéressant de se relir."
   jump menu111face
  else:
   $ inventory_items.append("Rapport OFAC 105")
   "A obtenu le rapport ofac n°105 ! Qui ça pourrait bien être ?"
   p "\{Je ne sais pas si j'ai le droit de fouiller dans ses affaires \}"
  jump menu111face

label capital:
  hide screen directionsF
  hide screen window
  p "\{Des gros et vieux bouquins poussiéreux écrits en tout petit.\}"
  p "\{Si la couverture du premier a bien vécue, on dirait que les deux autres sont presques neufs.\}"
  p "\{C'est bien mais je vais peut-être pas prendre ça...\}"
  jump menu111face

label whiteout:
  hide screen directionsF
  hide screen inventory
  show white with dissolve
  play music "audio/Void_Seeker.ogg"
  show text _('{color=#000000}Tu as cassé tes menottes, [name]...')
  pause 2.0
  hide text
  pause 1.0
  show text _('{color=#000000}Tu as transcendé ta condition humaine vers quelque chose de nouveau.')
  pause 2.0
  hide text
  pause 1.0
  show text _('{color=#000000}Mais tu dois survivre, [name].')
  pause 2.0
  hide text
  pause 1.0
  show text _('{color=#000000}Tiens bon...')
  pause 2.0
  hide text
  pause 1.0
  play music "audio/Heartbeat.ogg"
  call screen quicktimebarwhite()
  
label menu111droite:
 hide screen directionsB
 hide screen directionsF
 hide screen fenetre
 hide screen Arret_urgence
 show fond droite
 show fonddroite2 behind fond
 call screen directionsD

label menu111gauche:
 $ projecteur = renpy.random.randint(1,2)
 show projecteur1 behind fond
 if projecteur == 2 :
   show projecteur2 behind fond
   hide screen directionsB
 show fond gauche
 hide screen directionsF
 hide screen fenetre
 hide screen Arret_urgence
 call screen directionsG

label menu111arriere:
 hide screen directionsD
 hide screen directionsG
 hide fonddroite2
 hide projecteur1
 hide projecteur2
 show fond reboot
 show screen Arret_urgence
 show screen directionsB
 $ ui.interact()
 
label inverted:
  play music "audio/Void_Seeker.ogg"
  hide screen to_inverted
  hide white
  show screen inventory
  show fond trans
  show anifond 2
  if inconnu == 5:
    show ju ink_T
    IIG "Quelle créature pathétique tu fais."
    show ju ink
    p "Comment ?"
    show ju ink_T
    IIG "Tu essayes de retrouver les traces d'un passé à tout jamais révolu, enfermé avec une vision de toi-même."
    show ju ink
    p "Tu ne semble plus le même..."
    show ju ink_T
    IIG "Je t'anéhantirais dans ta recherche d'informations avant que tu ne puisse trouver quoi que ce soit !"
    show ju ink
    p "Je ferais mieux de partir d'ici avant de me faire buter !"
    show ju ink_T
    IIG "Tu fais encore confiance à ces inconnus alors que tu sais pertinemment qu'iels te mentent !"
    show ju ink
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
   show ju ink_T
   HUH "Bien le bonjour !"
   show ju ink
   p "Uargh !"
   show ju ink_T
   HUH "Je t'ai vraiment fait peur ?"
   show ju ink
   p "Je dirais plutôt surpris.e..."
   p "Tu as l'air bizarre par rapport à tout à l'heure..."
   show ju ink_T
   HUH "Sous cet état, je suis toujours bizarre !"
   HUH "Par contre ma mémoire me fait un peu défaut donc je pourrais pas dire que je me souviens de tout à l'heure !"
   HUH "Tu as l'air de me fixer attentivement comme si tu voulais quelque chose de moi."
   show ju ink
   p "Qui êtes-vous ?"
   show ju ink_T
   HUH "Moi ? Je suis l'Inconnu !"
   IIG "Ou du moins je penses que je l'ai été un jour..."
   IIG "Et toi ?"
   show ju ink
   p "Moi ? Je suis [name]."
   show ju ink_T
   IIG "Oh enchanté, [name] ! Merci de venir me passer le bonjour !"
   show ju ink
   $ inverted = True
  else:
    p "\{Décidément, ça fait mal à la tête...\}"
    show ju ink_T
    IIG "Bon retour, hum... Attends..."
    IIG "Comment tu t'appelles, déjà ?"
    show ju ink
    p "C'est pas important, t'inquiètes pas."
  jump inverted05

label inverted05:
  p "\{Même si il a l'air troublé, je pourrais peut-être lui poser des questions...\}"
  show screen whiteUI
  $ ui.interact()

label inverted1:
  hide screen whiteUI
  p "Est ce que je pourrais te poser une question ?"
  menu:
    "Qui est Julia l'Inconnue ?":
      show ju ink_T
      IIG "Ju-qui?"
      IIG "Désolé mais ça ne me dit pas grand chose..."
      IIG "Après tout, je suis le seul à avoir cette dénomination."
      show ju ink
      p "Vraiment ?"
      show ju ink_T
      IIG "Oui vraiment, chaque créateurice a son dénominateur et est appelé par celui-là, les prénoms sont peu utilisés."
      show ju ink
      p "Je devrais peut-être lui poser la question..."
      show ju ink_T
      IIG "Me poser quelle question ?"
      show ju ink
      p "Non, rien ! J'ai pensé.e à voix haute !"
      if inconnu == 0:
       $ inconnu = inconnu + 1
      jump inverted1
    "Pourquoi tu souris tout le temps?":
      show ju ink_T
      IIG "Drôle de question !"
      IIG "C'est à dire que je ne peux pas vraiment faire autrement, mon visage est bloqué comme ça !"
      show ju ink
      p "Bloqué ?"
      show ju ink_T
      IIG "Les joies d'être un Ink Guy !"
      show ju ink
      jump inverted1
    "Comment s'est terminé l'affaire Pacrel?" if inconnu == 7:
      show ju ink_T
      IIG "Wow, tu as l'air d'avoir une sacrée tête d'enterré ! Tout va bien ?"
      show ju ink
      p "Je crois avoir appris plus que je n'aurais voulu apprendre un jour..."
      show ju ink_T
      IIG "Ce monde est bien perturbé, mon ami ! Tu n'es qu'au début de tes peines !"
      IIG "Sinon, j'ai oublié la majorité de ce qui s'est passé avant que je ne me retrouve ici !"
      show ju ink
      p "Tu n'aurais même pas de miettes de souvenirs ?"
      show ju ink_T
      IIG "Si, je me souviens de sa mort, de la mort de Pacrel et de quand j'ai été possédé !"
      show ju ink
      p "Wow, trop enthousiaste..."
      show ju ink_T
      IIG "Je ne peux pas me contrôler, mon pote ! Cette forme m'y oblige !"
      show ju ink
      p "Ah..."
      p "Attends un instant... La mort de Pacrel ?"
      show ju ink_T
      IIG "C'est plus tout à fait clair mais oui ! Il s'est interposé pour essayer de me sauver et s'est fait transpercé par un...hum...pic d'ombre !"
      show ju ink
      p "\{Il y a quelque chose qui ne convient pas ici... Je crois que je vais devoir réassembler ses souvenirs si je veux en tirer quoi que ce soit...\}"
      show ju ink_T
      IIG "Qu'est-ce qui te trouble ?"
      show ju ink
      p "De ce que j'ai pu comprendre, la mort de Pacrel causerait..."
      menu :
        "La mort de l'Inconnu":
          p "Je suis ultrasûr."
          show ju ink_T
          IIG "Je crois que j'ai perdu le fil..."
          show ju ink
          p "Merde..."
          jump inverted1
        "La mort d'Edmes":
          p "Une petite voix m'a expliquée que la mort de l'un menait à la mort de l'autre."
          p "Hors, ceci est arrivé et tu es toujours corrompu."
          p "Comment est-ce possible ?"
          show ju ink_T
          IIG "Mmmmh... C'est vrai, ça !"
          show ju ink
          p "Ce qui veut donc dire qu'il n'a pas pu mourir."
          show ju ink_T
          IIG "Mais je l'ai pourtant vu se faire transperser de bout en bout devant mes yeux !"
          show ju ink
          p "Par un pic d'ombre ?"
          show ju ink_T
          IIG "Oui, tout juste avant que je ne m'en prenne plusieurs moi-même !"
          IIG "Ces trucs font extrêmement mal !"
          show ju ink
          p "Mais tu as tout de même survécu, ce qui veut dire que ces pics ne tuent pas !"
          show ju ink_T
          IIG "C'est vrai, ça ! T'es vachement perspicace !"
          show ju ink
          p "Cependant, ils ont tout de même un effet sur leurs cibles."
          show ju ink_T
          IIG "Quel type d'effet?"
          show ju ink
          menu:
            "L'effet spoiler":
             show ju ink_T
             IIG "Ok Bad Mulch."
             IIG "Je sais qu'on a perdu et qu'on aurait pu gagner au second tour si la gauche était unie pais là c'est pas le sujet."
             show ju ink
             p "Merde..."
             $ Achievement.add(achievement_name['Bad Mulch'])
             jump inverted1
            "La perte du soi":
              p "Tu as perdu tes couleurs et tes souvenirs après ces évènements."
              p "Si tu es toujours corrompu, le vieux Pacrel est sans doute seulement corrompu sans ses souvenirs !"
              show ju ink_T
              IIG "On pourrait donc le retrouver !"
              show ju ink
              p "Je sais pas si ça pourrait être tout à fait utile..."
              show ju ink_T
              IIG "Etant donné que sa simple présence casse la fabrique des ordres."
              IIG "Sa mention est quasiment un signe d'instabilité !"
              show ju ink
              show fond trans at Shake((0, 0, 0, 0), 5.0, dist=20)
              show ju ink_T
              IIG "En parlant d'instabilité, on dirait bien que ça commence à trembler par ici !"
              IIG "Les liens avec ton monde sont instables, va voir si tout va bien là-bas !"
              show ju ink
              p "Mais..."
              show ju ink_T
              IIG "On se reverra, je te le prommets."
              IIG "De toute façon, je ne pourrais pas aller bien plus loin !"
              show ju ink
              if inconnu == 7:
               $ inconnu = inconnu + 1
              jump whiteexit
            "La perte de couleur":
             p "Je suis ultrasûr."
             show ju ink_T
             IIG "Je crois que j'ai perdu le fil... On parlait de joueurs LOL qui voient pas le soleil ou du Sénat ?"
             show ju ink
             p "Merde..."
             jump inverted1 
        "La mort de Jean Fraques":
          p "Je suis ultrasûr."
          show ju ink_T
          IIG "Je crois que j'ai perdu le fil..."
          show ju ink
          p "Merde..."
          jump inverted1
    "Retour":
      jump inverted05
   
label whiteexit:
  hide screen whiteUI
  show ju ink_T
  IIG "Penses juste à venir me revoir ! On se sent seul quand enfermé avec soi-même."
  show ju ink
  pause 0.25
  play music "audio/A day in the unknown.ogg"
  jump menu0

label menu111bouton:
  if off == True:
    jump offlinetransition
  else:
    hide screen directionsB
    p "\{ Un bouton d'arrêt d'urgence? Mmmmh...\}"
    p "\{Peut-être que je pourrais...\}"
    stop music
    show ju re onlayer overlay
    p "Uwa !"
    show ju re_T onlayer overlay
    I "N'y pense \nmême pas."
    hide screen Arret_urgence
    show fond ecole
    show ju re
    p "Je n'allais rien faire !"
    show ju re_T
    I "Fais gaffe à ce que tu fais ici, ne touche pas à ce que tu ne dois pas toucher."
    show ju re
    p "Mais..."
    show ju re_T
    I "Suis mes conseils et tout se passera bien, compris ?"
    show ju re
    menu:
      "Nuh-uh !":
        hide ju re
        show fond reboot
        "*clic !*"
        "..."
        
        show ju plexe_T
        I "Qu'est ce que tu as fait?!"
        I "ARREE.EE...EEEEEE"
        show ju plexe_C
        "{color=#000000}EEEEEEEEEEEEEEEEEEEEEEEEE"
        "{color=#000000}RESET SYSTEM, PLEASE STAND BY"
        "{color=#000000}DELETING JULIA.CHR"
        hide ju plexe_C
        "{color=#000000}DELETING ASSETS"
        window hide
        show text"{color=#ffffff}DELETING BACKGROUND.PNG"
        hide fond reboot
        show black
        hide anifond
        play music "audio/Void_Seeker.ogg"
        show text"{color=#ffffff}RESET SUCCESSFUL, DO YOU WANT TO RESTART?"
        $ Achievement.add(achievement_name['Disconnected'])
        menu:
          "YES":
            jump offlinedialogue
          "NO":
            jump finreset
      "Oui capitaine...":
        show ju re_T
        I "C'est bien, tu as compris."
        play music "audio/A day in the unknown.ogg"
        show ju splain
        jump menu0

label offlinedialogue:
  show text"{color=#ffffff}RESTORING FILES, RECONNECTION MAY TAKE SEVERAL MINUTES"
  window show
  I "..."
  window hide
  pause (1)
  show ju plexe
  window show
  show ju plexe_T
  I "Qu'est-ce..."
  I "Qu'est-ce que tu as fait?"
  show ju plexe
  p "Je crois que j'ai fait ce qu'il fallait."
  show ju plexe_T
  I "Qu'est ce que tu dis? Tu as supprimé ce monde !"
  I "C'est l'équivalent de sauter par la fenêtre pour voir ce que tu trouveras derrière !"
  show ju plexe
  p "Mmmmh... je devrais peut-être"
  show ju re_T
  I "N'y penses même pas ! tu as déjà effacé ce monde !"
  show ju plexe
  p "Temporairement..."
  show ju plexe_T
  I "Hein? Comment ça?"
  show ju plexe
  p "Tu n'as pas entendue la voix?"
  show ju plexe_T
  I "Quelle voix?"
  show ju plexe
  p "Rien, laisse tomber, on a pas beaucoup de temps avant que tout revienne."
  show ju plexe_T
  I  "Tout va revenir?"
  show ju plexe
  p "Oui mais je crois qu'on est déconnecté des serveurs."
  show ju plexe_T
  I "Donc ça voudrait dire... "
  show ju plexe
  p "...Que plus personne ne nous écoute."
  p "Le conseil ne peut plus vous écouter pour l'instant."
  show ju plexe_T
  I "On dirait vraiment que tu avais envie de me poser ces questions..."
  show ju plexe
  show fond Void_room behind ju with dissolve
  show ju splain_T
  I "J'apprécie ta dédication mais si tu pouvais éviter de pousser ce monde à ses limites par le futur, ça serait bien !"
  show ju splain
  jump offlinemenu0

label offlinetransition:
  hide screen Arret_urgence
  hide screen directionsB
  show ju plexe_T
  I "C'est reparti pour un tour?"
  I "Très bien, fais comme tu le souhaite mais fait vite..."
  hide ju plexe_T
  show fond reboot
  "clic !"
  "{color=#000000}RESET SYSTEM, PLEASE STAND BY"
  "{color=#000000}DELETING JULIA.CHR"
  "{color=#000000}DELETING ASSETS"
  window hide
  show text"{color=#ffffff}DELETING BACKGROUND.PNG"
  hide fond reboot
  show black
  hide anifond
  play music "audio/Void_Seeker.ogg"
  show text"{color=#ffffff}RESET SUCCESSFUL, DO YOU WANT TO RESTART?"
  menu:
    "YES":
      show text"{color=#ffffff}RESTORING FILES, RECONNECTION MAY TAKE SEVERAL MINUTES"
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
  show text"{color=#ffffff}DELETING BACKGROUND.PNG"
  hide fond reboot fake
  show black
  hide anifond
  stop music
  play music "audio/Void_Seeker.ogg"
  show text"{color=#ffffff}RESET SUCCESSFUL, DO YOU WANT TO RESTART?"
  menu:
    "YES":
      show text"{color=#ffffff}RESTORING FILES, RECONNECTION MAY TAKE SEVERAL MINUTES"
      show ju fear_T
      I "AAAAAAAAAAAh !"
      show ju fear
      p "Hey, tout va bien, tout à été reset."
      show ju plexe_T
      I "AAaaah... Ah ?"
      show ju plexe
      show fond Void_room behind ju with dissolve
      show ju plexe_T
      I "Tu as eu un sacré réflexe, [name]..."
      show ju plexe
      p "Je penses qu'après tout ça, il me reste juste une seule question..."
      show ju plexe_T
      I "Oh... Très bien. Je t'avouerais que j'ai le cerveau un peu retourné mais je tenterais de répondre."
      show ju plexe
      jump offlinemenu1
    "NO":
      jump finreset

label offlinemenu0:
  $ off=True
  show ju splain
  show fond Void_room behind ju with dissolve
  show ju splain_T
  I "Allez, on est seul.e.s face à face, pose moi donc tes questions pour lesquelles tu as tant travaillé.e !"
  show ju splain
  window hide
  show screen blackUI
  $ ui.interact()

label offlinemenu1:
  hide screen blackUI
  menu:
    "Du coup, ces hierarchies?":
      show ju splain_T
      I "Ah oui, c'etait ça !"
      I "Eh bien, on décompose notre organisation, comme dans notre vrai monde, en échelles hierarchiques."
      show orga
      I "Plus une personne se trouve bas dans cette organisation, plus elle aura des personnes au dessus d'elle ayant un contrôle sur elle."
      show ju splain
      p "Donc chaque rang a créé le rang inférieur?"
      show ju splain_T
      I "Pas forcément non plus, ça dépend vraiment des rangs."
      show ju splain
      hide orga with dissolve 
      show ju splain_T
      I "Tu voulais que je commence par un certain rang?"
      show ju splain
      jump offlinemenu11
    "Pourquoi y a t'il ce bouton?":
      show ju re
      I "..."
      p "Alors?"
      show ju re_T
      I "Tu m'as fait souffrir avec le bouton pour savoir ce que fait le bouton...?"
      show ju re
      p "Je voulais savoir et tu m'as pas dit, après tout."
      show ju re_T
      I "Je n'ai même pas envie d'élaborer."
      show ju re
      p "petite joueuse, va."
      I "..."
      show ju splain
      jump offlinemenu1
    "Qu'est ce qui a pu t'arriver ?" if inconnu >= 2:
      show ju plexe_T
      I "C'est... compliqué..."
      I "J'ai eu des problèmes avec mes univers. Des problèmes qui m'ont coûté mon premier univers et quasiment ma vie."
      I "Mais si on parle essentiellement de ce que tu as vu, je dirais que c'était ma période corrompue."
      show ju plexe
      p "Ta période corrompue ? Que s'est-il passé ?"
      show ju plexe_T
      play music "audio/Tears of the past.ogg"
      I "Je n'étais... Pas prête à sa mort."
      show ju sad_T
      I "Je pensais qu'elle ne viendrait pas..."
      I "Je pensais que j'aurais pu la protéger..."
      I "Je pensais pouvoir y arriver seule..."
      I "J'avais tort..."
      show ju sad
      p "Tout va bien?"
      show ju sad_T
      I "Oui... J'ai juste besoin d'un peu de temps..."
      show ju sad
      pause 2
      if complique == False:
        $ inconnu = inconnu + 1
      show ju splain
      $ complique = True
      play music "audio/Void_Seeker.ogg"
      jump offlinemenu1
    "Qui est le réel antagoniste de cette histoire ?" if inconnu >= 8:
      show ju splain_T
      I "C'est une sacré question !"
      I "Après le peu qu'on a traversé ici et la quantité que tu verras plus loin, la question est legit compliquée à répondre."
      I "On peut citer le Conseil, Edmes, l'OFAC, des tas et des tas d'autres antagonistes dont on parle depuis tout à l'heure..."
      I "Mais j'ai toujours pensé à un truc."
      I "Aussi machiavélique qu'un antagoniste soit, il restera toujours limité à la plume de son auteur dans ses actes et dans leurs violences."
      I "Les véritables antagonistes de cet univers sont donc l'auteur et celleux qui l'encadre."
      I "J'imagine du coup que si on suit cette logique et que si on ignore le Conseil, je suis le véritable antagoniste de l'histoire."
      show ju splain
      p "Et pourtant, Edmes me semblait plus dangereux."
      show ju splain_T
      I "J'imagine que c'est une question de point de vue."
      I "Te voici arrivé à la fin de nos discussions !"
      show ju splain
      p "Déjà ? Mais qu'est ce que je peux faire maintenant ?"
      show ju splain_T
      I "De ce que j'ai pu entendre, il y aurait deux-trois trucs qui ont commencé à changer"
      I "J'imagine que tu peux encore faire un tour pour observer les allentours si tu n'a pas eu le temps de tout voir !"
      I "Et si tu veux partir, j'imagine que je te reverrais la prochaine fois !"
      show ju splain
      if inconnu == 8:
       $ inconnu = inconnu + 1
      $ Inconnu = True
      show text _("{color=#ffffff} Fin de l'Inconnu.e") with dissolve
      $ Achievement.add(achievement_name['Inconnu'])
      pause 3.0
      hide text with dissolve
      menu:
        "Continuer":
           show ju splain_T
           I "Parfait ! Je serais toujours là si tu as besoin de quoi que ce soit !"
           show ju splain
           jump offlinemenu1
        "Partir":
           jump menu3
    "retour" if inconnu !=8:
      jump offlinemenu0
   
label blackexit:
  hide screen blackUI
  show ju plexe_T
  I "Vraiment? Tu as fait tout ça juste pour ça?"
  hide text
  I "Tu sais que ça me détruit la tête à chaque fois?"
  show ju plexe
  "FULLY RESTORED"
  show ju plexe_T
  I "Tout ça pour ça..."
  show ju plexe
  $ Achievement.add(achievement_name['techdimanche'])
  stop music
  hide text
  show anifond with dissolve
  show fond ecole
  hide fond Void_room with dissolve   
  play music "audio/A day in the unknown.ogg"
  show ju splain_T
  I "Bon, passons à autre chose !"
  show ju splain
  jump menu0

label offlinemenu11:
 menu:
   "Le Conseil" if conseil == 0:
     show ju plexe
     I "..."
     p "Qu'est ce qu'il se passe? Tu ne veux toujours pas me dire?"
     show ju plexe_T
     I "C'est à dire que..."
     show ju wu_T
     I "Il n'y a simplement rien à dire !"
     show ju wu
     p "À d'autres mais pas à moi !"
     show ju plexe_T
     I "Argh..."
     show ju plexe
     p "\{Elle a vraiment du mal à en parler...\}"
     p "\{Si je compte en savoir plus un de ces jours, il va falloir que je lui force la main...\}"
     show ju wu_T
     I "Et puis c'est pas comme si c'était intéressant !"
     I "Iels font que de la paperasse de toute façon !"
     show ju wu
     p "Iels t'ont fait quelque chose?"
     show ju fear_T
     I "Iirk !"
     show ju wu_T
     I "R...Rien du tout !" 
     show ju wu 
     hide text with dissolve 
     show chaine behind ju at Shake((0, 0, 0, 0), 4.0, dist=20) 
     pause 5
     show cadenasR behind ju at Position(xpos=0.9,xanchor=0.9,ypos=0.5,yanchor=0.5) 
     pause 0.2
     show cadenasL behind ju at Position(xpos=0.1,xanchor = 0.1, ypos=0.5, yanchor=0.5) 
     pause 0.2
     show cadenasT behind ju at Position(xpos=0.5,xanchor = 0.5, ypos=0.1, yanchor=0.1) 
     p "\{C'est quoi ces trucs? On dirait une mauvaise reférence à Ace Attorney !\}"
     if "Trilogie Histoire Multiple" in inventory_items  and "Rapport OFAC 105" in inventory_items:
       p "J'ai trouvé des bouquins qui trainaient en hauteur dans les étagères."
       show ju re_T
       I "C... Comment? qu'est ce que tu es allé cherché ça dans mes affaires?"
       show ju re
       jump offlinemenu111
     else:
       p "\{Peut-être que je pourrais essayer d'explorer les alentours pour trouver de quoi déverouiller ces cadenas\}"
       hide cadenasR
       hide cadenasT
       hide cadenasL
       hide chaine
       show ju splain
       jump offlinemenu11
   "L'accord OFAC - conseil" if conseil == 1 and inconnu == 1:
     show ju plexe_T
     I "Tu es prêt.e à tout pour me mettre dans tous mes états, hein ?"
     show ju plexe
     p "Je pense qu'il y a quelque chose de plus poussé derrière ces simples questions."
     p "Et je ne penses très honnètement pas que tu tenterais tant que ça de ne pas le divulguer si tout allait bien."
     show ju plexe_T
     I "C'est... vrai..."
     I "Il faut aussi dire que je m'attendais pas à ce que les choses se déroulent comme ça..."
     I "Après tout, les deux organismes me méprisent..."
     show ju plexe
     p "Du coup, j'ai bien compris que le conseil était tes patrons mais qui est l'OFAC ?"
     show ju plexe_T
     I "L'OFAC, ou Office Factieuse Anti Corruption, est une association internationale de l'un de mes anciens mondes."
     I "C'est un réseau totalement factieux de gens peu scrupuleux fondé en 1930 à Appaos à la suite des évènements de l'affaire Pacrel dans les locaux de leur ancienne structure."
     show ju plexe
     p "C'est moi ou ça sent le maxi complotisme, cette histoire ?"
     show ju plexe_T
     I "C'est vraiment pas toi pour le coup, cette association est totalement complotiste."
     I "Et vu que mes mondes sont très paranormaux, il y avait toute les chances pour qu'ils surgissent."
     I "Ils pensent que je suis leur ennemi principal et ils ont donc réussi, d'une manière ou d'une autre malgré leur totale incompétence, à contacter mes supérieurs."
     I "Ils ne savent juste pas encore qu'ils ne seront que des pions et qu'ils finiront par être jetés."
     I "Ni même que la cause de tout ces désordres a déjà pactisée avec le Conseil, contre moi."
     p "\{Contre elle ? je devrais peut-être lui demander pourquoi ici avant de continuer dans les hierarchies\}"
     show ju splain
     if inconnu == 1:
       $ inconnu = inconnu + 1
     jump offlinemenu11
   "Les Administrateurices et Modérateurices":
     show ju re_T
     I "Ah... Eux..."
     show ju re
     p "Iels ont quelque chose de spécial ?"
     show ju re_T
     I "Iels sont ce qu'on peut considérer comme cadres et cadres supérieurs..."
     show ju re
     p "Ah donc c'est un peu tes supérieurs."
     show ju re_T
     I "...Ou comme milice du conseil."
     I "Après tout, iels y sont directement reliés."
     show ju re
     p "Vraiment ?"
     show ju re_T
     I "Oui, c'est une milice du système, même si elle ne s'en rend pas toujours compte."
     I "Ce sont les étudiants en art et les artistes professionnels de notre monde."
     I "Iels relayent ce qui est défini comme correct, bien qu'avec moins d'influence que le conseil."
     show ju splain
     jump offlinemenu11
   "Les Créateurices confirmés":
     show ju splain_T
     I "C'est plus ou moins la base de la base de la hierarchie."
     I "Cette catégorie rassemble l'ensemble des personnes qui ont déjà créé quoi que ce soit,"
     I "Qu'iels en soient conscient.es ou non."
     I "Ça s'applique donc également à toi j'imagine."
     I "Sans quoi tu ne serais sans doute pas là."
     show ju fear_T
     I "Cependant, c'est les moins importants de la chaîne des confirmés. Iels sont à la merci des envies de leurs supérieurs."
     show ju fear
     p "Et il y en aurait d'autre que des confirmés ?"
     show ju fear_T
     I "Il y a celleux qui sont en dehors de ce système..."
     I "Entre ma première arrivée parmis les confirmé.es et aujourd'hui, je suis passé par ces filets."
     show ju fear
     $ puni=True
     jump offlinemenu11
   "Les Créateurices OOB" if oob and inconnu >=4:
     show ju splain_T
     I "Nous voici à la fin de nos affaires !"
     I "Les Créateurices OOB ou Créateurices Out Of Bound sont les Créateurices Exilées du système."
     I "Iels n'y sont souvent pas à cause du Conseil mais par simple conviction personnelle ou par instabilité excessive."
     I "Ces Créateurices sont la plupart du temps plus puissants que les plus hauts d'entre elleux."
     I "Et iels sont également assez fréquemment passé par la case sanction ou corruption, ces évènements menant à de grands gains de puissances instables."
     I "À part ça, même si j'en ai fait partie, je ne suis plus vraiment dans ces cases."
     show ju splain
     if inconnu == 4:
       $ inconnu = inconnu + 1
     jump offlinemenu11
   "Les Créateurices Sanctionné.es" if puni and inconnu >= 3:
     show ju splain_T
     I "Si des problèmes sont observés dans un univers..."
     I "Ou... Si ils ne sont pas au goût du conseil..."
     I "Un.e Créateurice peut se retrouver sanctionné.e par le conseil."
     I "Cette sanction peut souvent se traduire par une surveillance accrue, une destruction des mondes créés auparavant, une interdiction d'en créer de nouveaux et j'en passe."
     I "le Conseil ne se limite cependant pas à ces sanctions."
     show ju splain
     p "J'imagine que c'est la raison pour laquelle tu rechignes à parler du conseil."
     show ju re_T
     I "Bingo..."
     I "Le Conseil a un côté plus obscure qui ne pourrait être connu que par un.e sanctionné.e..."
     show ju re
     p "Tu as donc été sanctionnée. Ton renouveau et ta paranoïa semblent pointer dans ce sens."
     show ju re_T
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
     show ju splain_T
     I "En effet, ce n'est pas vraiment une partie de la pyramide, comme les Créateur.ices OOB."
     I "Je suis l'une des personnes à l'origine de cette dernière."
     I "Les Créateurices corrompues sont des Créateurices ayant été corrompues par Edmes, l'un de mes personnages."
     I "Au même titre que leurs homologues personnages, ces Créateurices, ont une puissance décuplée."
     I "En échange de cette puissance, cependant, iels perdent leurs couleurs et leur libre arbitre."
     show ju splain
     if name == "Valentin" or name == "valentin":
       p "Sauf si on considère que le libre arbitre n'a jamais réellement existé."
       show ju splain_T
       I "Comme les oiseaux bleu ?"
       show ju splain
       p "Outch, Touché."
       $ Achievement.add(achievement_name['Oiseau bleu'])
     show ju splain_T
     I "On les reconnait à leur grand sourire et à leur teinte monochrome."
     I "Je n'ai pas vraiment de crainte autour de la mention d'Edmes donc une fois que tu en auras fini ici, penses à me demander dans le monde normal."
     I "Rien que le fait que nous vivions dans les ombres ici me mets mal à l'aise..."
     I "Plus qu'une catégorie de Créateurice, lance-le donc !"
     show ju splain
     $ oob = True
     jump offlinemenu11
   "retour":
      jump offlinemenu1

label offlinemenu111:
  p "Je pense que la partie de ces livres qui explique ton silence est..."
  menu:
    "Le personnage principal":
      show ju splain_T
      I "Je vois pas de lien dans cette association."
      show ju splain
      p "Argh... si j'avais sû..."
      jump offlinemenu1
    "Les dieux":
      show ju fear_T
      I "Iirk !"
      show ju fear
      hide cadenasL
      p "C'était donc ça. tu essayez de te protéger du regard de divinités."
      show ju re_T
      I "Sois raisonnable, je n'ai rien à me reprocher ici. Les divinités n'aurait pas à me surveiller."
      show ju re
      p "Donc tu me confirme que des divinités existent ici, tu n'es pas assez attentive."
      show ju re_T
      I "Espèce de..."
      show ju re
      jump offlinemenu112
    "La trame verte et bleue":
      show ju splain_T
      I "Je vois pas de lien dans cette association."
      show ju splain
      p "Argh... si j'avais sû..."
      jump offlinemenu1
    "Le fait qu'ils soient 3":
      show ju splain_T
      I "Je vois pas de lien dans cette association."
      show ju splain
      p "Argh... si j'avais sû..."
      jump offlinemenu1

label offlinemenu112:
  p "Et si je me permets, je pense savoir ce qu'ils font par ici mais avant ça..."
  show ju re_T
  I "Ne tente pas quelque chose que tu pourrais regretter."
  show ju re
  p "j'ai trouvé un autre document. Pour être plus précis, un rapport d'une organisation appellée OFAC."
  show ju re_T
  I "Oû est ce que tu l'as trouvée ?"
  show ju re
  p "Elle traînait par terre."
  show ju re_T
  I "Merde... J'étais presque sûre de l'avoir rangé..."
  show ju re
  p "Et je pense que l'important ici est..."
  menu:
    
    "L'OFAC":
      show ju splain_T
      I "Je vois pas de lien dans cette association."
      show ju splain
      p "Argh... si j'avais sû..."
      jump offlinemenu1
    "La destruction du document":
      show ju splain_T
      I "Je vois pas de lien dans cette association."
      show ju splain
      p "Argh... si j'avais sû..."
      jump offlinemenu1
    "L'association de personnages avec des dieux":
      show ju fear_T
      I "ARGH!"
      hide cadenasR
      show ju fear
      p "Encore touché ! J'ai tout ce qui me faut désormais !"
      show ju re_T
      I "Ah vraiment? Et pourquoi donc ?"
      show ju re
      p "Parce qu'il y a un lien entre ces deux pièces qui représentent les dynamismes de ce monde."
      show ju re_T
      I "Et quel est ce lien ?"
      show ju re
      jump offlinemenu113
    "Jean Fraques":
      show ju splain_T
      I "Je vois pas de lien dans cette association."
      show ju splain
      p "Argh... si j'avais sû..."
      jump offlinemenu1

label offlinemenu113:
  p "Je pense que ce lien est..."
  menu:
    "le fait que tous ces documents soient en papier":
      show ju splain_T
      I "Je vois pas de lien dans cette association."
      show ju splain
      p "Argh... si j'avais sû..."
      jump offlinemenu1
    "Le grand dieu":
      show ju splain_T
      I "Je vois pas de lien dans cette association."
      show ju splain
      p "Argh... si j'avais sû..."
      jump offlinemenu1
    "Le mec random":
      show ju splain_T
      I "Je vois pas de lien dans cette association."
      show ju splain
      p "Argh... si j'avais sû..."
      jump offlinemenu1
    "Toi":
      p "Je pense que tu es le créateur entre les personnages et le dieu."
      show ju plexe_T
      I "Je..."
      show ju plexe
      p "De plus, je pense que tu as peur de l'affaire qui tourne autour de ces personnages."
      show ju plexe_T
      I "J..."
      show ju plexe
      p "Si quelqu'un se rendait compte que tu étais à l'origine de l'affaire ou que tu ne la maitrisais pas, tu risquerais beaucoup."
      show ju plexe_T
      I "Non, non..."
      show ju plexe
      p "Ce dieu, ou ce membre du conseil, est donc ton supérieur hyérarchique et tu es totalement sous sa tutelle !"
      show ju fear
      pause 2.0
      hide cadenasT
      pause 2.0
      hide chaine
      show ju fear_T
      I "AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAARGH !"
      I "POURQUOIIIIIIIIII ?! POURQUOI ES-TU SI INSUPPORTABLE ?!"
      $ Achievement.add(achievement_name['Jubreakdownadmin'])
      show ju sad
      play music "audio/Tears of the past.ogg"
      pause (1)
      show ju sad_T
      I "Je... Je..."
      pause 1
      I "J'imagine que tu a fini.e par trouver... Par toi même..."
      show ju sad
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
      show ju splain_T
      I "C'est comme tu veux, chef.fe !"
      show ju splain
      jump menu1

label menu13:
  show ju re_T
  I "Qui est ce 'il' qui t'a parlé de ça ?"
  show ju re
  "vous sentez les chaînes se reserrer un peu plus."
  menu:
    "Je préfère garder mes sources anonymes." if integrité < 1:
       show ju re_T
       I "Tu sembles oublier ta situation actuelle."
       show ju re
       p "J'ai de l'intégrité journalistique"
       $ integrité = 1
       show ju re_T
       I "On verra si tu veux vraiment rester sur tes positions."
       show ju re
       jump menu13
    "Je tiendrais mot" if integrité >= 1 and integrité <5:
       show ju re_T
       I "Ton respect d'autrui ne te mênera nulle part."
       I "Balance-le donc maintenant, ça va faire [integrité] fois que tu refuses"
       show ju re
       $ integrité = integrité + 1
       jump menu13
    "Je suis pas un collabo." if integrité == 5:
       show ju re_T
       I "Tu sais quoi ? J'en ai ma claque !"
       I "Je te laisse plus le choix, maintenant ! Réponds !"
       show ju re
       $ integrité = integrité + 1
       $ Achievement.add(achievement_name['Integrité Journalistique'])
       jump menu13
    "Oui... Bon... Ok... C'est toi.":
       show ju re_T
       I "M..."
       show ju fear_T
       I "Moi ?... Qu'est-ce que tu entends par moi ?"
       show ju fear
       p "Eh bien d'une façon ou d'une autre je l'ai rencontré.e en personne."
       show ju fear_T
       I "Comment est-ce que ça pourrait même être possible ?"
       show ju fear
       p "Aucune idée mais il a l'air plus prompt à répondre à mes questions."
       show ju fear_T
       I "Je te rapellerais que si tu veux plus d'infos, tu peux toujours me les poser de l'autre côté."
       show ju fear
       p "Et je compte bien le faire."
       $ inconnu = inconnu + 1
       jump menu0

label menu2:
 hide screen mainUI
 show ju splain_T
 I "Vraiment? Montre le moi donc ! "
 show ju splain
 python:
   codeg = renpy.input("Entrez le code")
 if code in codeg:
   show ju re_T
   $ Achievement.add(achievement_name['codedate'])
   I "Oh, je vois que tu as fait quelques recherches..."
   show ju re
   p "C'est censé correspondre à quoi?"
   show ju re_T
   I "C'est la date de fin et de début de mon deuxième univers."
   #à compléter plus tard
   show ju splain
   jump menu0
 elif codeg == "Th3_4rch1v1st":
   A "{color=#000000} Ce jeu cache plus que tu ne peux l'imaginer. \n Elle même n'en sait rien."
   pause 3.0
   hide text
   A "{color=#000000} Nous resterons en contact, ne m'oublie pas. \n Je te parlerais à travers ces codes."
   pause 3.0
   hide text
   show ju splain_T
   I "Tu pensais à quelque chose?"
   show ju splain
   p "Non ! Non... Rien..."
   show ju plexe_T
   I "Mmmmh..."
   show ju plexe
   jump menu0
 elif codeg == "PZHXJGVFS":
   $ joaearly = True
   "partie La Joie de Vivre déverouillée"
   jump menu0
 else:
   show ju splain_T
   I "Jamais entendu parlé."
   show ju splain
   jump menu0

label aventure:
  scene
  show image "Miclordes/Miclordes.jpg"
  show Miclordes
  play music "audio/Miclordes.ogg"
  hide screen mainUI
  hide screen inventory
  pause 2
  if persistent.av :
    show Miclordes H_T
    Miclordes "Rebonjour et rebonsoir, [name] !"
    Miclordes "Besoin d'un rappel sur ta mission ?"
    show Miclordes H
    menu : 
      "J'ai besoin d'un rappel.":
        show Miclordes H_T
        Miclordes "Bon bah pars pour un petit récap' !"
        Miclordes "Tu dois trouver et rassembler les histoires en réparant ce que tu vois brisé, autant en vrai qu'en versions alternatives."
        Miclordes 'Ton toi du futur m\'a demandé de te dire "Si tu te retrouve bloqué, trouve un moyen de passer entre les lignes et tu pourrais y trouver des routes alternatives."'
        Miclordes "Bonne visite à travers les univers ! J'espère que tu trouvera ce que tu veux et doit trouver !"
        show Miclordes
        $ persistent.av = True
        show screen aventure
        pause 2
        hide Miclordes
        hide image "Miclordes/Miclordes.jpg"
        $ ui.interact()
      "C'est tout bon !":
        show Miclordes H_T
        Miclordes "Ok !"
        show Miclordes
        show screen aventure
        pause 2
        hide Miclordes
        hide image "Miclordes/Miclordes.jpg"
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
    Miclordes '"Si tu te retrouve bloqué, trouve un moyen de passer entre les lignes et tu pourrais y trouver des routes alternatives."'
    Miclordes "C'est rien d'incroyable mais bon, j'imagine que ça pourraît peut-être t'être utile."
    show Miclordes H_T
    Miclordes "Bonne visite à travers les univers ! J'espère que tu trouvera ce que tu veux et doit trouver !"
    show Miclordes
    $ persistent.av = True
    show screen aventure
    pause 2
    hide Miclordes
    hide image "Miclordes/Miclordes.jpg"
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

label prologue_LJDV:
 hide screen LJDV
 show fondcafecreaB
 show fondcafecreaF
 "Créa, aka Joie, aka LaJoieDeVivre, est une Créatrice confirmée."
 "Tout comme ses paires, elle possède son monde dans lequel elle édicte ses règles."
 "Cependant, en opposition à ses paires, elle a tendance à voyager de dimension en dimension telle une exploratrice, à la recherche des trésors immatériels de ces univers."
 "Ses personnages étant attachés, métaphoriquement et littéralement, à elle, iels se retrouvent régulièrement à des endroits où iels ne devraient pas être."
 "Son sens de l'orientation, tout au moins questionnable, la mène souvent à se perdre dans des recoins d'univers qu'elle n'avait semblablement pas l'intention d'explorer."
 show joa R_T with dissolve
 LJDV "Hé ! Tu sais que je t'entends ?!"
 show joa R
 "Elle finit ainsi relativement fréquemment dans des situations compromettantes dans lesquelles elle essaye de paraître au plus hors de contrôle et d'appâter le danger loin des personnages pour annihiler le problème en bonne et due forme sans casser la \"magie\" des univers qu'elle parcourt."
 "Son arme principale est le feu orangé, duquel elle fait transitionner les composés pour créer avec les cendres du passé."
 "LaJoieDeVivre est une Créatrice hors paire, capable de voir le beau dans chaque chose et d'en faire quelque chose d'exceptionnel."
 hide joa with dissolve
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
  show joassis W behind fondcafecreaF with dissolve at left
  pause 0.5
  show joassis behind fondcafecreaF with dissolve at left
  LJDV "\{Il fait définitivement pas aussi froid qu'iels l'avaient annoncé aujourd'hui. On se croirait plus en mai qu'à la veille du nouvel an.\}"
  LJDV "\{Après, je vais pas me plaindre. J'ai juste à discuter un peu avec Ajai de ce qu'il s'est passé cette année.\}"
  LJDV "\{C'est bizarre, il est toujours là en avance d'habitude. Cette journée s'annonce vraiment étrange\}"
  show ajaiassis W behind fondcafecreaF with dissolve at right
  pause 0.5
  show ajaiassis behind fondcafecreaF with dissolve at right
  show ajaiassis T behind fondcafecreaF at right
  Ajai "Désolé du retard, j'ai eu un petit contretemps."
  show joassis T behind fondcafecreaF at left
  show ajaiassis behind fondcafecreaF at right
  LJDV "Ma foi si c'est qu'une fois par année !"
  show joassis behind fondcafecreaF at left
  show ajaiassis T behind fondcafecreaF at right
  Ajai "On se voit qu'une fois par année d'habitude..."
  show joassis T behind fondcafecreaF at left
  show ajaiassis behind fondcafecreaF at right
  LJDV "Des détails, tout ça !"
  LJDV "Comment ça va depuis l'année dernière ?"
  show joassis behind fondcafecreaF at left
  show ajaiassis T behind fondcafecreaF at right
  Ajai "C'est un peu le bazar comme d'habitude, à tel point que je vois plus passer les jours."
  show joassis T behind fondcafecreaF at left
  show ajaiassis behind fondcafecreaF at right
  LJDV "Ah bah ne m'en parle même pas !"
  show joassis behind fondcafecreaF at left
  show ajaiassis T behind fondcafecreaF at right
  Ajai "Il s'est passé quoi de ton côté ?"
  show ajaiassis behind fondcafecreaF at left
  hide joassis
  hide ajaiassis
  show joa C_T
  LJDV "Eh ben, il y a quelques heures, Samwy est rentré. Je l'avais plus revu depuis plusieurs années et, apparemment, je l'avais oublié dans l'univers de Julien."
  LJDV "Le pauvre était tellement perdu qu'il commençait à halluciner en pensant qu'il était en 2012 et que les murs pouvaient s'ouvrir !"
  show joa c
  Ajai "Tu l'as oublié depuis 2012 ?!"
  show joa P_T 
  LJDV "Peut-être bien mais au moins il est encore vivant, non ?"
  show joa p
  Ajai "Si tu continue à faire n'importe quoi et tu risqueras de te brûler, le Conseil avait pas apprécié l'échec de Julien."
  show joa R
  Ajai "Whoa ! Calme toi !"
  show joa R_T
  LJDV "Tu sais très bien qu'il ne méritait pas ce qui lui est arrivé, et les autres non plus."
  show joa R
  Ajai "On a tenté ce qu'on pouvait à l'époque mais rien n'a fait."
  Ajai "Au moins, on peut pour l'instant dire que cette sanction n'a pas l'air d'avoir d'effets sur lui. C'était peut-être juste un bon prototype."
  show joa R_T
  LJDV "J'en doute, certains ont tendance à prendre du temps avant de montrer leurs effets."
  show joa R
  menu :
    Ajai "On devrait peut-être parler d'autre chose non ? J'ai peur que quelqu'un nous entende ici :
      "Plutôt crever que de me censurer !":
        show joa R_T 
        LJDV "Tu penses que c'est ce qu'iels auraient voulu ? Qu'on les abandonnent comme ça et qu'on accepte que ce soit normal ?!
        LJDV "C'est pas normal qu'on soit muselé comme ça ! On devrait pouvoir dire ce qui se passe sans risquer notre existence face à ces fraudes !" 
        show joa R
        Ajai "Stop ! On va nous entendre !"
        show joa R_T
        LJDV "J'en ai plus rien à foutre ! Qu'ils viennent m'arrêter si ils ont les couilles ! Les gens du Conseil sont pathétiques et ceux à leurs bottes sont stupides !"
        show joa R
        Administrateur "Vous me flattez."
        show joa P_T
        LJDV "Ah... Bonjour monsieur l'agent. Comment allez-vous ?"
        jump go_prison LJDV
      "Revenir sur mon monde":


  show screen LJDV
  $ ui.interact()


label finreset:
 show text"{color=#ffffff}VERY WELL"
 pause(2)
 hide text
 pause (1)
 show text _("{color=#ffffff} F IN  RE SET _I NCO MPLET") with dissolve
 $ Achievement.add(achievement_name['delete'])
 pause (3)
 return

label finwhite:
  stop music
  hide screen to_inverted
  window show
  p "{color=#ffffff}Non ! Pas si tôt !"
  pause (1)
  show text _("{color=#000000} Fin Perte de soi")
  $ Achievement.add(achievement_name['white'])
  pause (3)
  return

label finEdmes:
  stop music
  hide fond reboot fake
  hide animfond
  show Edmes closeup
  Edmes "Tu pensais vraiment que je te laisserais partir ?"
  show text _("{color=#ffffff} Fin Tué dans l'Oeuf") with dissolve
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
  show text _("{color=#ff0000} Bonne fin any% noclip ultra-antifa") with dissolve
  $ Achievement.add(achievement_name['antifa'])
  pause (3)
  return

label menu3:
 hide screen mainUI
 show ju plexe_T
 I "C'est compréhensible. Je vais te sortir du quatrième glitch."
 show ju splain_T
 I "Adieu ou à bientôt j'imagine. Passe un bon reste de journée !"
 I "Si tu change d'avis, je reste là. C'est pas vraiment comme si j'avais le choix !"
 I "Ahahahahahahah...Ah"
 I "Save me Save me Save me Save me Save me Save me Save me Save me Save me Save me Save me Save me Save me Save me Save me Save me Save me Save me Save me Save me Save me Save me Save me Save me Save me Save me Save me Save me Save me Save me Save me Save me Save me Save me Save me Save me Save me Save me Save me Save me Save me Save me Save me Save me Save me Save me Save me Save me Save me Save me Save me Save me Save me Save me Save me Save me Save me Save me Save me Save me Save me Save me"
 show ju plexe_C
 "{color=#000000}Session ending"
 "{color=#000000}Closing simulation"
 "{color=#000000}Return to main menu"
 return

return