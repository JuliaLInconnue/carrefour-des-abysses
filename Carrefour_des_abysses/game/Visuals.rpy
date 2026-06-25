
  

# Déclarez sous cette ligne les images, avec l'instruction 'image'
$ Halloween = Event (31, 10, True)

    ### Couleurs solides
image white = Solid("#ffffff")

    ### Vidéos
        ## Decors
image anifond = Movie(play="images/Decor/video/fondanim.webm")
image anifond 2 = Movie(play="images/Decor/video/Fond_trans.webm")
image projecteur2 = Movie(play="images/Decor/video/Projecteur/projecteur2.webm")
        ## Personnages
image Miclordes = Movie(play="images/chr/Miclordes/Miclordes.webm")
image Miclordes T = Movie(play="images/chr/Miclordes/Miclordes_T.webm")
image Miclordes H = Movie(play="images/chr/Miclordes/Miclordes_H.webm")
image Miclordes H_T = Movie(play="images/chr/Miclordes/Miclordes_H_T.webm")
image joa_spike = Movie(play="images/chr/joa/joa_spike.webm")

    ### Images
        ## UI
                #Julia
image presplash = AnImage("UI/presplash[today_event].webp")
image cadenasT = AnImage("UI/cadenas[today_event].webp") 
image cadenasL = AnImage("UI/cadenas[today_event].webp")
image cadenasR = AnImage("UI/cadenas[today_event].webp")
image chaine = AnImage("UI/chaine[today_event].webp")
image orga = AnImage("UI/orga_crea[today_event].webp")
image logo2 = AnImage("UI/Logo2[today_event].webp")
image logo = AnImage("UI/logo_2[today_event].webp")
image linconnue = AnImage("UI/l'inconnue pdp[today_event].webp")
image TS_Logo = AnImage("UI/TS_Logo[today_event].webp")
image projecteur1 = AnImage("UI/Projecteur/projecteur1[today_event].webp")
image inventory idle = AnImage("UI/inventory idle[today_event].webp")
image inventory hover = AnImage("UI/inventory hover[today_event].webp")
image Inventaire = AnImage("UI/Inventaire[today_event].webp")
image none = AnImage("UI/none[today_event].webp")
image BAU = AnImage("UI/BAU[today_event].webp")
image Rapport_OFAC = AnImage("UI/Rapport_OFAC[today_event].webp")
image droite idle = At(AnImage("UI/direction idle[today_event].webp"),xflip)
image droite hover = At(AnImage("UI/direction hover[today_event].webp"),xflip)
image back idle = AnImage("UI/back idle[today_event].webp")
image back hover = AnImage("UI/back hover[today_event].webp")
image aventure idle = AnImage("UI/aventure idle[today_event].webp")
image aventure hover = AnImage("UI/aventure hover[today_event].webp")
image discuter idle = AnImage("UI/discuter idle[today_event].webp")
image discuter hover = AnImage("UI/discuter hover[today_event].webp")
image explorer idle = AnImage("UI/explorer idle[today_event].webp")
image explorer hover = AnImage("UI/explorer hover[today_event].webp")
image coden idle = AnImage("UI/code idle[today_event].webp")
image coden hover = AnImage("UI/code hover[today_event].webp")
image exit idle = AnImage("UI/exit idle[today_event].webp")
image exit hover = AnImage("UI/exit hover[today_event].webp")
image arcade_terminal = AnImage("UI/arcade/arcade_terminal[today_event].webp")
image fond_tetris = AnImage('UI/arcade/Tetris/fond_tetris[today_event].jpg')
            #Aventure
image aventure_annexe = AnImage("UI/Aventure/aventure annexe[today_event].webp")
image aventureprincipale idle = AnImage("UI/Aventure/aventureprincipale idle[today_event].webp")
image aventureprincipale hover = AnImage("UI/Aventure/aventureprincipale hover[today_event].webp")
image Aventure HP = AnImage("UI/Aventure/HP[today_event].webp")
image Aventure AP = AnImage("UI/Aventure/AP[today_event].webp")
image Aventure_P idle = AnImage("UI/Aventure/P idle[today_event].webp")
image Aventure_P hover = AnImage("UI/Aventure/P hover[today_event].webp")
image Aventure_LJDV idle = AnImage("UI/Aventure/LJDV idle[today_event].webp")
image Aventure_LJDV hover = AnImage("UI/Aventure/LJDV hover[today_event].webp")
image Aventure_Ajai idle = AnImage("UI/Aventure/Powart idle[today_event].webp")
image Aventure_Ajai hover = AnImage("UI/Aventure/Powart hover[today_event].webp")
image Aventure_Null idle = AnImage("UI/Aventure/Null idle[today_event].webp")
image Aventure_Null hover = AnImage("UI/Aventure/Null hover[today_event].webp")
image porte1 idle = AnImage("UI/Aventure/porte1 idle[today_event].webp")
image porte1 hover = AnImage("UI/Aventure/porte1 hover[today_event].webp")
image porte2 idle = AnImage("UI/Aventure/porte2 idle[today_event].webp")
image porte2 hover = AnImage("UI/Aventure/porte2 hover[today_event].webp")
image arcade idle = AnImage("UI/arcade/arcade idle[today_event].webp")
image arcade hover = AnImage("UI/arcade/arcade hover[today_event].webp")
image Aventure_fond pacrel = AnImage("UI/Aventure/fond_pacrel[today_event].webp")
image Aventure_fond LJDV = AnImage("UI/Aventure/fond_LJDV[today_event].webp")
image Aventure_fond Powart = AnImage("UI/Aventure/fond_Powart[today_event].webp")
            #others
image buff vap = "Fichier source/buff vap.webp"
image Unfinished = "Unfinished.webp"
        ## Personnages
image default_chr = AnImage("chr/default_chr[today_event].webp")
image garde = AnImage("chr/Agent_Conseil[today_event].webp")
            #Julia
image ju splain = DynamicDisplayable(_lipsync,"I",
    None,                                                
    AnImage("chr/unknown/jusplain[today_event].webp"),
    AnImage("chr/unknown/jusplain_T[today_event].webp"),
)
image ju plexe = DynamicDisplayable(_lipsync,"I",
    None,                                                
    AnImage("chr/unknown/juplexe[today_event].webp"),
    AnImage("chr/unknown/juplexe_T[today_event].webp"),
)
image ju plexe_C = AnImage("chr/unknown/juplexe_C[today_event].webp")
image ju plexe_C2 = AnImage("chr/unknown/juplexe_C2[today_event].webp")
image ju fear = DynamicDisplayable(_lipsync,"I",
    None,                                                
    AnImage("chr/unknown/fear[today_event].webp"),
    AnImage("chr/unknown/fear_T[today_event].webp"),
)
image ju ink = DynamicDisplayable(_lipsync,"IIG",
    None,                                                
    AnImage("chr/unknown/juink[today_event].webp"),
    AnImage("chr/unknown/juink_T[today_event].webp"),
)
image ju re = DynamicDisplayable(_lipsync,"I",
    None,                                                
    AnImage("chr/unknown/jure[today_event].webp"),
    AnImage("chr/unknown/jure_T[today_event].webp"),
)
image ju wu = DynamicDisplayable(_lipsync,"I",
    None,                                                
    AnImage("chr/unknown/juwu[today_event].webp"),
    AnImage("chr/unknown/juwu_T[today_event].webp"),
)
image ju sad = DynamicDisplayable(_lipsync,"I",
    None,                                                
    AnImage("chr/unknown/jusad[today_event].webp"),
    AnImage("chr/unknown/jusad_T[today_event].webp"),
)
image XY splain = DynamicDisplayable(_lipsync,"IXY",
    None,                                                
    AnImage("chr/unknown/XY_splain[today_event].webp"),
    AnImage("chr/unknown/XY_splain_T[today_event].webp"),
)
            #Edmes
image juposteur fhappy = AnImage("chr/Juposteur/juposteur joie crame[today_event].webp")
image juposteur happy = AnImage("chr/Juposteur/juposteur joie[today_event].webp")
image edmes splain = DynamicDisplayable(_lipsync,"Edmes",
    None,                                                
    AnImage("chr/unknown/edmes_splain[today_event].webp"),
    AnImage("chr/unknown/edmes_splain_T[today_event].webp"),
)
            #Ajai
image ajaiassis = DynamicDisplayable(_lipsync,"Ajai",
    None,                                                
    AnImage("chr/ajai/ajaiassis[today_event].webp"),
    AnImage("chr/ajai/ajaiassis_T[today_event].webp"),
)
image ajaiassis marche = AnImage("chr/ajai/ajaiassis_W[today_event].webp")
image ajai think = DynamicDisplayable(_lipsync,"Ajai",
    None,                                                
    AnImage("chr/ajai/ajai_think[today_event].webp"),
    AnImage("chr/ajai/ajai_think_T[today_event].webp"),
)
image ajai fear = DynamicDisplayable(_lipsync,"Ajai",
    None,                                                
    AnImage("chr/ajai/ajai_fear[today_event].webp"),
    AnImage("chr/ajai/ajai_fear_T[today_event].webp"),
)
image ajai assu = DynamicDisplayable(_lipsync,"Ajai",
    None,                                                
    AnImage("chr/ajai/ajai_assu[today_event].webp"),
    AnImage("chr/ajai/ajai_assu_T[today_event].webp"),
)
image ajai rage = DynamicDisplayable(_lipsync,"Ajai",
    None,                                                
    AnImage("chr/ajai/ajai_rage[today_event].webp"),
    AnImage("chr/ajai/ajai_rage_T[today_event].webp"),
)
            #Téa
image joassis = DynamicDisplayable(_lipsync,"LJDV",
    None,                                                
    AnImage("chr/joa/joassis[today_event].webp"),
    AnImage("chr/joa/joassis_T[today_event].webp"),
)
image joassis marche = "chr/joa/joassis_w.webp"
image joa R = DynamicDisplayable(_lipsync,"LJDV",
    None,                                                
    AnImage("chr/joa/joa rage[today_event].webp"),
    AnImage("chr/joa/joa rage_T[today_event].webp"),
)
image joa P = DynamicDisplayable(_lipsync,"LJDV",
    None,                                                
    AnImage("chr/joa/joa avoid[today_event].webp"),
    AnImage("chr/joa/joa avoid_T[today_event].webp"),
)
image joa C = DynamicDisplayable(_lipsync,"LJDV",
    None,                                                
    AnImage("chr/joa/joa assu[today_event].webp"),
    AnImage("chr/joa/joa assu_T[today_event].webp"),
)
image joa fear = DynamicDisplayable(_lipsync,"LJDV",
    None,                                                
    AnImage("chr/joa/joa fear[today_event].webp"),
    AnImage("chr/joa/joa fear_T[today_event].webp"),
)
            #Miclordes
image Miclordes_trans = AnImage("chr/Miclordes/Miclordes[today_event].jpg")
            #Charasime
#F = front ; WS = weird smile ; D = Determinated ; T = Talk ; DE = Dead eyes
image Charasime psycho = DynamicDisplayable(_lipsync,"clem",
    AnImage("chr/Charasime/Charasime 28[today_event].webp"),                                                
    AnImage("chr/Charasime/Charasime 3[today_event].webp"),
    AnImage("chr/Charasime/Charasime 2[today_event].webp"),
)
image Charasime deter = DynamicDisplayable(_lipsync,"clem",
    AnImage("chr/Charasime/Charasime 29[today_event].webp"),                                                
    AnImage("chr/Charasime/Charasime 15[today_event].webp"),
    AnImage("chr/Charasime/Charasime 1[today_event].webp"),
)
image Charasime damn = DynamicDisplayable(_lipsync,"clem",
    AnImage("chr/Charasime/Charasime 11[today_event].webp"),                                                
    AnImage("chr/Charasime/Charasime 16[today_event].webp"),
    AnImage("chr/Charasime/Charasime 4[today_event].webp"),
    AnImage("chr/Charasime/Charasime 26[today_event].webp"),
)
image Charasime deter_R = DynamicDisplayable(_lipsync,"clem",
    AnImage("chr/Charasime/Charasime 11[today_event].webp"),                                                
    AnImage("chr/Charasime/Charasime 26[today_event].webp"),
    AnImage("chr/Charasime/Charasime 30[today_event].webp"),
)
image Charasime fear = DynamicDisplayable(_lipsync,"clem",
    AnImage("chr/Charasime/Charasime 29[today_event].webp"),                                                
    AnImage("chr/Charasime/Charasime 3[today_event].webp"),
    AnImage("chr/Charasime/Charasime 35[today_event].webp"),
)
image Charasime happy = DynamicDisplayable(_lipsync,"clem",
    AnImage("chr/Charasime/Charasime 25[today_event].webp"),                                                
    AnImage("chr/Charasime/Charasime 15[today_event].webp"),
    AnImage("chr/Charasime/Charasime 39[today_event].webp"),
)
image Charasime Eery = "chr/Charasime/Charasime 17.webp"
image Charasime cry = "chr/Charasime/Charasime 19.webp"
image Charasime blush = "chr/Charasime/Charasime 20.webp"
                ### Z
image Z penche = DynamicDisplayable(_lipsync,"Z",
    None,                                                
    AnImage("chr/Z/z_penche_T[today_event].webp"),
    AnImage("chr/Z/z_penche[today_event].webp"),
)
                ### Statisticien
image flo stare = AnImage("chr/Statisticien/statisticien_stare[today_event].webp")
image flo happy = AnImage("chr/Statisticien/statisticien_happy[today_event].webp")
                ### Kyono
image kyono idle = DynamicDisplayable(_lipsync,"kyo",
    None,                                                
    AnImage("chr/kyono/kyono_idle_T[today_event].webp"),
    AnImage("chr/kyono/kyono_idle[today_event].webp"),
)
image kyono fear = DynamicDisplayable(_lipsync,"kyo",
    None,                                                
    AnImage("chr/kyono/kyono_fear_T[today_event].webp"),
    AnImage("chr/kyono/kyono_fear[today_event].webp"),
)
image kyono cry = DynamicDisplayable(_lipsync,"kyo",
    None,                                                
    AnImage("chr/kyono/kyono_cry_T[today_event].webp"),
    AnImage("chr/kyono/kyono_cry[today_event].webp"),
)
image kyono toj = DynamicDisplayable(_lipsync,"kyo",
    None,                                                
    AnImage("chr/kyono/kyono_toj_T[today_event].webp"),
    AnImage("chr/kyono/kyono_toj[today_event].webp"),
)
image kyono bow = DynamicDisplayable(_lipsync,"kyo",
    None,                                                
    AnImage("chr/kyono/kyono_bow_T[today_event].webp"),
    AnImage("chr/kyono/kyono_bow[today_event].webp"),
)
                ### Juge
image juge marteau :
        "chr/juge/juge_marteau.webp"
        0.5
        "chr/juge/juge_marteau_F.webp"
image juge marteau3 :
        "chr/juge/juge_marteau.webp"
        0.2
        "chr/juge/juge_marteau_F.webp"
        repeat 3
image juge focus = DynamicDisplayable(_lipsync,"juge",
    None,                                                
    AnImage("chr/juge/juge_focus_T[today_event].webp"),
    AnImage("chr/juge/juge_focus[today_event].webp"),
)
image juge surpris = DynamicDisplayable(_lipsync,"juge",
    None,                                                
    AnImage("chr/juge/juge_surpris_T[today_event].webp"),
    AnImage("chr/juge/juge_surpris[today_event].webp"),
)
image juge angy = DynamicDisplayable(_lipsync,"juge",
    None,                                                
    AnImage("chr/juge/juge_angy_T[today_event].webp"),
    AnImage("chr/juge/juge_angy[today_event].webp"),
)
image juge idle = DynamicDisplayable(_lipsync,"juge",
    None,                                                
    AnImage("chr/juge/juge_idle_T[today_event].webp"),
    AnImage("chr/juge/juge_idle[today_event].webp"),
)
                ### Eight
image eight panique = DynamicDisplayable(_lipsync,"eight",
    None,                                                
    AnImage("chr/eight/eight_panique_T[today_event].webp"),
    AnImage("chr/eight/eight_panique[today_event].webp"),
)
image eight joie = DynamicDisplayable(_lipsync,"eight",
    None,                                                
    AnImage("chr/eight/eight_joie_T[today_event].webp"),
    AnImage("chr/eight/eight_joie[today_event].webp"),
)
image eight think = DynamicDisplayable(_lipsync,"eight",
    None,                                                
    AnImage("chr/eight/eight_think_T[today_event].webp"),
    AnImage("chr/eight/eight_think[today_event].webp"),
)
image eight colere = DynamicDisplayable(_lipsync,"eight",
    None,                                                
    AnImage("chr/eight/eight_colere_T[today_event].webp"),
    AnImage("chr/eight/eight_colere[today_event].webp"),
)
image eight pris = DynamicDisplayable(_lipsync,"eight",
    None,                                                
    AnImage("chr/eight/eight_pris_T[today_event].webp"),
    AnImage("chr/eight/eight_pris[today_event].webp"),
)
image eight defeat = AnImage("chr/eight/eight_defeat[today_event].webp")
                ### Fraques
image jf hurt = DynamicDisplayable(_lipsync,"jf",
    None,                                                
    AnImage("chr/Fraques/jf_hurt_T[today_event].webp"),
    AnImage("chr/Fraques/jf_hurt[today_event].webp"),
)
image jf evidence = DynamicDisplayable(_lipsync,"jf",
    None,                                                
    AnImage("chr/Fraques/jf_evidence_T[today_event].webp"),
    AnImage("chr/Fraques/jf_evidence[today_event].webp"),
)
image jf obj = DynamicDisplayable(_lipsync,"jf",
    None,                                                
    AnImage("chr/Fraques/jf_obj_T[today_event].webp"),
    AnImage("chr/Fraques/jf_obj[today_event].webp"),
)
image jf doute = DynamicDisplayable(_lipsync,"jf",
    None,                                                
    AnImage("chr/Fraques/jf_doute_T[today_event].webp"),
    AnImage("chr/Fraques/jf_doute[today_event].webp"),
)
image jf haine = DynamicDisplayable(_lipsync,"jf",
    None,                                                
    AnImage("chr/Fraques/jf_haine_T[today_event].webp"),
    AnImage("chr/Fraques/jf_haine[today_event].webp"),
)
image jf hurt = DynamicDisplayable(_lipsync,"jf",
    None,                                                
    AnImage("chr/Fraques/jf_hurt_T[today_event].webp"),
    AnImage("chr/Fraques/jf_hurt[today_event].webp"),
)
image jf hide_joy = DynamicDisplayable(_lipsync,"jf",
    None,                                                
    AnImage("chr/Fraques/jf_hide_joy_T[today_event].webp"),
    AnImage("chr/Fraques/jf_hide_joy[today_event].webp"),
)
image jf hide_fear = DynamicDisplayable(_lipsync,"jf",
    None,                                                
    AnImage("chr/Fraques/jf_hide_fear_T[today_event].webp"),
    AnImage("chr/Fraques/jf_hide_fear[today_event].webp"),
)
                ### Archiviste
image archiviste bluff = DynamicDisplayable(_lipsync,"p",
    None,                                                
    AnImage("chr/archiviste/archiviste_bluff_T[today_event].webp"),
    AnImage("chr/archiviste/archiviste_bluff[today_event].webp"),
)
image archiviste fier = DynamicDisplayable(_lipsync,"p",
    None,                                                
    AnImage("chr/archiviste/archiviste_fier_T[today_event].webp"),
    AnImage("chr/archiviste/archiviste_fier[today_event].webp"),
)
image archiviste corner = DynamicDisplayable(_lipsync,"p",
    None,                                                
    AnImage("chr/archiviste/archiviste_objection_T[today_event].webp"),
    AnImage("chr/archiviste/archiviste_objection[today_event].webp"),
)
image archiviste objection = DynamicDisplayable(_lipsync,"p",
    None,                                                
    AnImage("chr/archiviste/archiviste_obj_T[today_event].webp"),
    AnImage("chr/archiviste/archiviste_obj[today_event].webp"),
)
image archiviste embarras = DynamicDisplayable(_lipsync,"p",
    None,                                                
    AnImage("chr/archiviste/archiviste_embarras_T[today_event].webp"),
    AnImage("chr/archiviste/archiviste_embarras[today_event].webp"),
)
image archiviste evidence = DynamicDisplayable(_lipsync,"p",
    None,                                                
    AnImage("chr/archiviste/archiviste_evidence_T[today_event].webp"),
    AnImage("chr/archiviste/archiviste_evidence[today_event].webp"),
)
image archiviste disaster = DynamicDisplayable(_lipsync,"p",
    None,                                                
    AnImage("chr/archiviste/archiviste_disaster_T[today_event].webp"),
    AnImage("chr/archiviste/archiviste_disaster[today_event].webp"),
)
                ### Doubt
image doubt idle = DynamicDisplayable(_lipsync,"doubt",
    None,                                                
    AnImage("chr/doubt/doubt_idle_T[today_event].webp"),
    AnImage("chr/doubt/doubt_idle[today_event].webp"),
)
image doubt happy = DynamicDisplayable(_lipsync,"doubt",
    None,                                                
    AnImage("chr/doubt/doubt_happy_T[today_event].webp"),
    AnImage("chr/doubt/doubt_happy[today_event].webp"),
)
                ### Bodias
image bodias juge = DynamicDisplayable(_lipsync,"bodias",
    None,                                                
    AnImage("chr/klarsen/klarsen_fiere_T[today_event].webp"),
    AnImage("chr/klarsen/klarsen_fiere[today_event].webp"),
)
                ### Pacrel
                ### Klarsen
image klarsen fiere = DynamicDisplayable(_lipsync,"klarsen",
    None,                                                
    AnImage("chr/klarsen/klarsen_fiere_T[today_event].webp"),
    AnImage("chr/klarsen/klarsen_fiere[today_event].webp"),
)
image klarsen fiere_d = DynamicDisplayable(_lipsync,"klarsen",
    None,                                                
    AnImage("chr/klarsen/klarsen_fiere_D_T[today_event].webp"),
    AnImage("chr/klarsen/klarsen_fiere_D[today_event].webp"),
)
        ## Decors
image projecteur1 = AnImage("Decor/photo/projecteur1[today_event].webp")
image fond Void_room = AnImage('Decor/photo/Void_room[today_event].webp')
image fond droite = AnImage("Decor/photo/fonddroite[today_event].webp")
image fonddroite2 = AnImage("Decor/photo/fonddroite2[today_event].webp")
image fond gauche = AnImage("Decor/photo/fondgauche[today_event].webp")
image fond reboot = AnImage("Decor/photo/fondreboot[today_event].webp")
image gare_monde = AnImage("Decor/photo/gare_monde[today_event].webp")
image fond ecole = AnImage("Decor/photo/fond hdi 3.1[today_event].webp")
image fond trans = AnImage("Decor/photo/fondtranscendental[today_event].webp")
image fond ecole fake = AnImage("Decor/photo/fond ecole fake[today_event].webp")
image fond reboot fake = AnImage("Decor/photo/fond reboot fake[today_event].webp")
image pacrel_nuit = AnImage("Decor/photo/pacrel_nuit[today_event].webp")
image fondcafecreaF = AnImage("Decor/photo/cafe_crea_F[today_event].webp")
image fondcafecreaB = AnImage("Decor/photo/cafe_crea_B[today_event].webp")
image fondcafecreaB N = AnImage("Decor/photo/cafe_crea_B_N[today_event].webp")
image Pic_ombre_ch1joa = AnImage("Decor/photo/Pic_ombre_ch1joa[today_event].webp")
image fond prison_LJDV = AnImage("Decor/photo/fond prison[today_event].webp")
image fond prison_LJDV_barre = AnImage("Decor/photo/fond prison barre[today_event].webp")
image train ext = AnImage("Decor/photo/train_ext[today_event].webp")
image train int = AnImage("Decor/photo/train_int[today_event].webp")
image capedmes = AnImage("Decor/photo/capedmes[today_event].webp")
image powart_prologue = AnImage("Decor/photo/prologue powart[today_event].webp")
image gopic 1 = AnImage("Decor/photo/gopic_ljdv_1[today_event].webp")
image gopic 2 = AnImage("Decor/photo/gopic_ljdv_2[today_event].webp")
image arcade_terminal = AnImage("UI/arcade/arcade_terminal[today_event].webp")
image grillage_1930 = AnImage("Decor/photo/grillage[today_event].webp")
image grillage_1930 trou = AnImage("Decor/photo/grillage_trou[today_event].webp")
image fond ssback = AnImage("Decor/photo/sweep_back[today_event].webp")
        ## Jumpscare
image I_Know = "jumpscare/I_Know.jpg"
image YOU = "jumpscare/YOU.jpg"
image Edmes closeup = "jumpscare/Edmes closeup.webp"
