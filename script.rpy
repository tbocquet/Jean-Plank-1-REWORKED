#Scenes
image mainmenujp2 = "main_menujp2.jpg"

#Personnages
define jp = Character('Jean Plank', color="#c8ffc8")
define urgo = Character('Urgo, dit \"le Boucher\"', color="#c8ffc8")
define lucienintro = Character('Lucien, mais ses amis l\'appellent Jean-François', color="#c8ffc8")
define lucien = Character('Lucien le Magicien Marabout', color="#c8ffc8")
define sj = Character('Saint Gède', color="#c8ffc8")
define mf = Character ('Miss Fourtout', color="#c8ffc8")
define odin = Character ('ODIN, DIEU DES DIEUX', color="#c8ffc8")

label start:

scene mainmenujp2

$ potion = 0
$ censure = 0

menu:
    "Jouer à la version tout public":
        $ censure = 1

    "Jouer à la version non censurée ":
        $ censure = 0


#############################################################################################################################
#                                                                                                                           #
#                                                        SCENE 1                                                            #
#                                                                                                                           #
#############################################################################################################################

scene jp_arrive

play music "music/jp_theme.ogg"
"Jean Plank était content."
"Après un périlleux voyage de plusieurs semaines, il avait enfin réussi à regagner Bill's Water."
"Cerise sur le gâteau, son navire était presque aussi intact que les cinq moussaillons qui avaient survécu à cette aventure."
"Ce qui était suffisamment rare pour mériter d'être souligné."

show introjp1
"Sourire aux lèvres, Jean Plank se tourna vers son nouveau compagnon."

voice "doublages_jp1/scene1/scene1_jp1.ogg"
jp "Hé ! Quel était ton nom déjà ?"

#Adoujimadisempala
voice "doublages_jp1/scene1/scene1_lucien1.ogg"
lucienintro "Lucien, mais mes amis m'appellent Jean-François."

voice "doublages_jp1/scene1/scene1_jp2.ogg"
jp "Et bien Lucien, bienvenue au bercail !"

"Pour la petite histoire, Jean-François était un indigène ayant rejoint l'équipage de notre bienheureux capitaine il y a peu."

show village_lucien
"Un beau matin, Jean Plank avait débarqué dans son village pour le piller et tout saccager."
"Son méfait accompli, il y avait ensuite mis le feu pour finir en beauté."
"Jean-François avait assisté à la catastrophe, totalement impuissant."

show lucien_pirate
"Mais c'est en regardant les flammes qui dévoraient son foyer qu'il avait trouvé une raison de vivre !"
"Il allait devenir pirate !"
"A son manque de jugeote évident, Jean Plank avait reconnu en lui un véritable potentiel et l'avait pris sous son aile afin de lui enseigner les ficelles du métier."
"Enfin en théorie parce que jusqu'à présent la seule chose que Jean-François avait appris, c'est que tout le monde devait payer."
"De là à savoir si Jean connaissait réellement les ficelles du métier..."

hide village_lucien
hide lucien_pirate
"Mais revenons à notre histoire."

show emeute
"Jean Plank posa pied à terre et salua triomphalement les nombreux villageois qui étaient venus l'accueillir."
"Il avait cependant beaucoup trop à faire pour pouvoir s'amuser avec la plèbe."
"Il fallait organiser les préparatifs pour son prochain voyage et ravitailler son navire."
"Pour résumer : trêve de mondanités, Jean Plank devait faire les courses."

voice "doublages_jp1/scene1/scene1_jp3.ogg"
jp "OK Lucien ! Allons chez Urgo !"


#############################################################################################################################
#                                                                                                                           #
#                                                        SCENE 2                                                            #
#                                                                                                                           #
#############################################################################################################################

scene boucherie

play music "music/boucherie.ogg"
"Urgo, dit \"Le Boucher\" était une vieille connaissance de notre bien aimé capitaine."
"Ayant eu quelques problèmes avec la justice pour infractions majeures sur mineurs de plus de 18 ans, il avait déménagé dans un coin reculé."
"Jean Plank poussa la porte de l'établissement et entra en hurlant."

show urgo
play sound "sound/violent_open_door.ogg"
voice "doublages_jp1/scene2/scene2_jp1.ogg"
jp "Haha !"

voice "doublages_jp1/scene2/scene2_urgo1.ogg"
urgo "Jean Plank ?! Ça alors, quelle surprise ! Je ne t'ai pas revu depuis ce jour où tu voulais éviter de payer et où j'ai consenti à te laisser fuir lâchement."

voice "doublages_jp1/scene2/scene2_jp2.ogg"
jp "Inutile de ressasser le passé, j'ai bien changé depuis cette époque."

voice "doublages_jp1/scene2/scene2_urgo2.ogg"
urgo "Effectivement, si tu es enfin revenu me régler ta dette."

voice "doublages_jp1/scene2/scene2_jp3.ogg"
jp "Oulah, quand même pas à ce point !"

voice "doublages_jp1/scene2/scene2_urgo3.ogg"
urgo "Allons Jean Plank... Comme tu le dis si souvent : \"Tout le monde doit payer\"."

show jpcrayonurgo

$renpy.sound.set_volume(0.00, delay=0, channel='music')
play alder "music/Crayon.ogg"

voice "doublages_jp1/scene2/scene2_jp4.ogg"
jp "Urgo..."

show urgocrayon
voice "doublages_jp1/scene2/scene2_urgo4.ogg"
urgo "Oui, Jean Plank ?"

hide urgocrayon
voice "doublages_jp1/scene2/scene2_jp5.ogg"
jp "C'est pas comme ça que ça marche."

$renpy.sound.set_volume(1.00, delay=0, channel='music')
stop alder

hide jpcrayonurgo
voice "doublages_jp1/scene2/scene2_urgo5.ogg"
urgo "Si tu n'es pas revenu pour me payer, alors pourquoi est tu là ?"

voice "doublages_jp1/scene2/scene2_jp6.ogg"
jp "Pour remplir mon bateau à moindre frais."

label fight_urgo:

scene couperet
play music "music/fighturgo.ogg"
"L'instinct surdéveloppé d'Urgo lui indiqua qu'il était sur le point de se faire dépouiller."
"Pris d'un excès de rage, il prit son couperet et le lança sur notre capitaine."

menu:
    "Esquiver":
        show urgo_dodge
        "Le lancer fut évité aisément par une gracieuse rotation du bassin de notre héros."
        show urgo_dodge2
        "Lucien en revanche ne savait pas faire ce genre de mouvements et prit le couperet dans les côtes, ce qui lui arracha un cri de douleur."
        show urgo_dodge3
        "Jean Plank le regarda d'un air dédaigneux puis décida de prendre son rôle de mentor au sérieux en montrant à Lucien \"Comment qu'on fait\"."
    "Réfléchir":
        show urgo_reflexion
        "Jean Plank prit un air songeur."
        "Malheureusement, ce n'était vraiment pas le bon moment pour ça."
        show urgo_reflexion1
        "Le couperet fila droit et alla se planter entre les deux yeux vitreux du capitaine."
        show urgo_reflexion2
        "Il s'écroula au sol, misérable."
        "Et hop, vous venez d'assister à votre première défaite."
        show ecran_game_over
        play music "music/music_mort.ogg"
        window hide
        pause
        hide ecran_game_over
        stop music
        jump fight_urgo
        

show commentquonfait
voice "doublages_jp1/scene2/scene2_jp7.ogg"
jp "Regarde, c'est comme ça qu'on fait !"

show lucien_focus
voice "doublages_jp1/scene2/scene2_lucien1.ogg"
lucienintro "Concentre toi plutôt sur ton combat-là !"

show jp_insulte_urgo
"Inspiré par la volonté de combattre de Lucien, notre capitaine retourna à sa rixe."
"Duelliste de renom, il n'eut aucun mal à acculer Urgo, qui venait de lancer son arme."
"En guise de punition, notre capitaine lui envoya quelques cinglantes répliques dont il avait le secret."

voice "doublages_jp1/scene2/scene2_jp8.ogg"
jp "Gibier de potence !"

show bras
"Puis il lui trancha le bras gauche d'un grand coup de sabre."

voice "doublages_jp1/scene2/scene2_jp9.ogg" #jp "Ce ne sont pas de simples oranges !"
"Et oui, Jean Plank était aussi sanguinaire que les oranges qu'il consomme."

show jp_sort_urgo
voice "doublages_jp1/scene2/scene2_jp10.ogg"
jp "Aller, à la prochaine !"
jp "Avait-il dit en partant fièrement."


#############################################################################################################################
#                                                                                                                           #
#                                                        SCENE 3                                                            #
#                                                                                                                           #
#############################################################################################################################

scene lucien_blessure
play music "music/lucien_rituel.ogg"

"En retournant vers la ville, Jean Plank remarqua alors que son comparse avait du mal à suivre."
"A son teint livide pour une personne de sa couleur de peau ainsi qu'à la mare de sang qu'il laissait derrière lui, Jean Plank se dit qu'il allait peut-être devoir jeter un œil à la blessure de son ami."
"Effectivement, la plaie était profonde et sans un médecin compétent, Lucien risquait d'y passer."
"Mais Jean Plank n'était pas n'importe qui ! Il avait acquis, au cours de ses voyages dans le Grand Nord, de nombreuses connaissances en médecine viking."
"Il regarda Lucien et lui dit avec assurance :"

show jp_degueu
voice "doublages_jp1/scene3/scene3_jp1.ogg"
jp "Lucien, t'inquiète frère, je vais te cautériser !"

"A ces mots, Lucien, qui avait toute confiance, refusa néanmoins poliment."

show lucien_non
voice "doublages_jp1/scene3/scene3_lucien1.ogg"
lucienintro "Toi, tu ne t'approches pas de moi avec tes techniques de charlatan !"

show jp_attache_lucien
"Il fit alors s'allonger paisiblement Lucien."

voice "doublages_jp1/scene3/scene3_lucien2.ogg"
lucienintro "Lâche moi ! Je te dis, lâche moi !"

show lucien_rituel
"Il l'attacha solidement afin de pouvoir se concentrer sur le rituel puis disposa ses douze derniers tonneaux de poudre en cercle autour de son ami."
"Il prit également grand soin d'en répandre sur le corps de Lucien."

play sound "sound/meche_on_fire.ogg"
"Il installa une mèche et puis mit le feu à l'aide du chien de son pistolet en entonnant des chants traditionnels Viking."

show lucien_rituel2
"Enfin, il courut de toutes ses forces se cacher derrière un arbre."

scene ecran_noir
play sound "sound/explosion_poudre.ogg"
pause

play music "music/lucien_transformation.ogg"
show lucien_fumee

"Une épaisse fumée violette entourait notre capitaine préféré."
"On n'y voyait pas à trois pieds, mais Jean Plank percevait une douce mélodie provenant de cet épais nuage."

show lucien_fumee2
"Peu à peu, le brouillard surnaturel se leva."
"Jean Plank put alors constater que Lucien était devenu..."

show lucien_transform
"UN MAGICIEN !"


play music "music/jp_theme.ogg"
show lucien_magie

voice "doublages_jp1/scene3/scene3_lucien3.ogg"
lucien "Pourquoi, es-tu surpris ?"

voice "doublages_jp1/scene3/scene3_jp2.ogg"
jp "Qu'est ce donc là que ce subterfuge ?!"

voice "doublages_jp1/scene3/scene3_lucien4.ogg"
lucien "Un subterfuge ? Sache jeune blanc-bec, que ça ce n'est pas un subterfuge, ça c'est la Magie. La Magie qui remplit les esprits, la Magie qui fait tourner le monde."

"Jean Plank le regardait perplexe."

voice "doublages_jp1/scene3/scene3_lucien5.ogg"
lucien "C'est une légende de mon village. Celle que Maman elle me racontait le soir devant le feu. Elle disait : la Magie noire c'est le vaudou c'est le mal, mais le feu, lui, il est là pour t'éclairer. "

"Jean Plank ainsi convaincu, il était temps d'aller chercher de la poudre."



#############################################################################################################################
#                                                                                                                           #
#                                                        SCENE 4                                                            #
#                                                                                                                           #
#############################################################################################################################


scene exterieur_entrepot
"Quelques minutes plus tard, nos deux compères entraient chez le fournisseur habituel de Jean Plank."
"Comme à son habitude, ce dernier hurla."

show entrepot
play music "music/religieux_shop.ogg"
voice "doublages_jp1/scene4/scene4_jp1.ogg"
play sound "sound/violent_open_door.ogg"
jp "Haha !"
"Mais personne ne daigna venir l'accueillir."

$renpy.sound.play("sound/sonnette.ogg", loop=True)
show jp_cloche
"Vexé, il entreprit de martyriser la petite cloche accrochée au comptoir."
"Après une attente qui, bien que courte, parut interminable aux oreilles de Lucien, quelqu'un arriva pour s'occuper de notre fougueux duo."

show singedjp1
stop sound
voice "doublages_jp1/scene4/scene4_sj1.ogg"
sj "Jean Plank, mon vieil ami !"

voice "doublages_jp1/scene4/scene4_jp2.ogg"
jp "Il nous faut plus de poudre."

voice "doublages_jp1/scene4/scene4_sj2.ogg"
sj "Toujours à l'essentiel à ce que je vois. Et désolé pour l'attente, j'avais une expérimentation sur le feu."

voice "doublages_jp1/scene4/scene4_lucien1.ogg"
lucien "Une expérimentation ?"

voice "doublages_jp1/scene4/scene4_sj3.ogg"
sj "Oui mon jeune ami érudit ! Une expérience révolutionnaire ! Si mes travaux portent leurs fruits, cela bouleversera totalement notre vision du monde !"
"Il allait proposer à Lucien de visiter son laboratoire, mais en voyant l'air impatient du capitaine, il se ravisa."

voice "doublages_jp1/scene4/scene4_sj4.ogg"
sj "Plus de poudre donc... Je te remets la spéciale viking ?"

voice "doublages_jp1/scene4/scene4_jp3.ogg"
jp "Plutôt la \"Carnage et Brûlures\". Dans sa version portable, bien sûr."

voice "doublages_jp1/scene4/scene4_sj5.ogg"
sj "Fort bien."

show singed_poudre
"Saint Gède descendit à la cave puis revint avec deux énormes tonneaux de poudre dans les bras."
"Il les disposa sur le comptoir."

voice "doublages_jp1/scene4/scene4_sj6.ogg"
sj "Et voilà ! Portable, comme convenu. Cela fera 500 serpents d'argent."

voice "doublages_jp1/scene4/scene4_jp4.ogg"
$renpy.sound.set_volume(0.00, delay=0, channel='music')
play sound "sound/scratch.ogg"
play alder "music/sj_choix.ogg"
jp "Comment ?"

show singed_regard
"Les yeux pénétrants de Saint Gède se plongèrent dans le regard bovin de Jean Plank."

voice "doublages_jp1/scene4/scene4_sj7.ogg"
sj "500 serpents d'argent."

menu:
    "Voler cet idiot":
        show singed_vol
        stop alder
        $renpy.sound.set_volume(1.00, delay=0, channel='music')
        "Rusé comme une huître, Jean Plank prit un air de surprise en pointant du doigt un bidule derrière Saint Gède."

        voice "doublages_jp1/scene4/scene4_jp5.ogg"
        jp "Attention, t'as une potion qui crame !"

        play sound "sound/metalgear.ogg"
        show singed_vol2
        "Réflexe de conservation oblige, notre Saint vendeur se retourna puis se remémora que son laboratoire n'était pas à cet étage."
        "Mais c'était trop tard."

        show singed_vol3
        "Se tournant de nouveau vers son comptoir, il put alors voir Jean Plank s'enfuir, les bras remplis de la précieuse poudre."

        show singed_vol4
        "Son regard croisa celui de Lucien qui haussa les épaules avant d'emboîter la course au capitaine."

        show singed_vol5
        "Saint Gède se massa les yeux, fatigué."
        "Il aurait pu les poursuivre et leur fracasser le crâne, mais il était magnanime. Son temps était précieux, il avait beaucoup de travail et la rancœur l'empêcherait d'être pleinement concentré."
        "Il choisit donc de pardonner à Jean Plank. Après tout qu'est-ce que quelques tonneaux de poudre ? Si son projet aboutissait, tout cela n'aurait plus d'importance."

        show taverne1
        play music "music/taverne.ogg"
        "Du côté de Plank - Jean de son prénom - la satisfaction d'avoir fait une bonne affaire le poussa vers la taverne pour une soirée de beuverie et de débauche."

        show taverne2
        "Très fier de son audacieux casse, il s'écroula ivre mort sur la table au bout de la quatrième bouteille de Rhum."

    "Payer ce grand prince":
        $ potion = 1

        show jp_paye1
        stop alder
        $renpy.sound.set_volume(1.00, delay=0, channel='music')
        "Un peu à l'encontre de ses principes, Jean Plank se résolut à lâcher une bourse à Saint Gède."
        "Ce dernier, très surpris par l'action du capitaine, le remercia chaleureusement."
        "Il allait raccompagner à la porte à nos deux complices lorsque Jean Plank s'exclama :"

        show jp_paye2
        voice "doublages_jp1/scene4/scene4_jp6.ogg"
        jp "Et c'est tout ?"

        show jp_paye3
        voice "doublages_jp1/scene4/scene4_sj8.ogg"
        sj "Comment ça, tout ?"

        hide jp_paye3
        "Jean Plank ne comprenait pas, il venait de payer et il n'était pas récompensé pour ça."
        "Devant l'incrédulité de son ami, Saint Gède, grand humaniste, ne put s'empêcher de faire un geste."

        show jp_paye4
        voice "doublages_jp1/scene4/scene4_sj9.ogg"
        sj"Bon tiens, si tu le désires, j'ai là une potion d'invincibilité expérimentale."

        hide jp_paye4
        voice "doublages_jp1/scene4/scene4_jp7.ogg"
        jp "D'invincibilité ?"

        show jp_paye4
        voice "doublages_jp1/scene4/scene4_sj10.ogg"
        sj "Expérimentale !"

        sound "doublages_jp1/scene4/scene4_jp7.ogg"
        "C'était véritablement un chouette objet."
        "Voici qui concluait les taches de ravitaillement de notre héros."

        show taverne2
        play music "music/jp_ivre.ogg"
        "N'ayant rien d'autre à faire, il se dirigea vers le bar où, comme à son habitude, il descendit quatre bouteilles de Rhum avant de s'écrouler ivre mort."

#############################################################################################################################
#                                                                                                                           #
#                                                        SCENE 5                                                            #
#                                                                                                                           #
#############################################################################################################################

play music "music/sunset.ogg"
scene jardin_mf
"Jean Plank se réveilla quelques heures plus tard."
"Son regard était rivé sur le ciel obscurci du crépuscule."
"Il était dans son jardin, allongé dans l'herbe."
"Son magicien l'avait probablement traîné jusqu'ici après son aventure alcoolisée."
"Juste au-dessus, un visage aussi plaisant que familier le toisait d'un regard condescendant."

voice "doublages_jp1/scene5/scene5_mf0.ogg"
mf "Et voilà. Encore une fois, je te retrouve ivre mort. Ce serait mentir que de dire que je ne suis pas habituée."

show jardin_mf2
"Jean Plank se leva, non sans difficulté, et se dressa de sa stature imposante devant ce nouvel adversaire. Il lui fallait rapidement une réponse efficace qui couperait court à toute répartie possible."

voice "doublages_jp1/scene5/scene5_jp1.ogg"
jp "Ha ha !"

voice "doublages_jp1/scene5/scene5_mf1.ogg"
mf "Tu es rentré quand ?"

voice "doublages_jp1/scene5/scene5_jp2.ogg"
jp "C'est important ?"

show jardin_mf3
voice "doublages_jp1/scene5/scene5_mf2.ogg"
mf "Et puis j'ai trouvé ça."

voice "doublages_jp1/scene5/scene5_jp3.ogg"
jp "Et alors ?"

voice "doublages_jp1/scene5/scene5_mf3.ogg"
mf "Elle n'est pas à moi."

voice "doublages_jp1/scene5/scene5_jp4.ogg"
jp "Évidemment, puisqu'elle est à moi."

voice "doublages_jp1/scene5/scene5_mf4.ogg"
mf "Ah ouais ? Dans ce cas, comment tu expliques qu'elle soit propre ?"

"Le ton montait toujours très vite entre Jean et sa compagne, mais même un aveugle ne pouvait nier la complicité plus qu'évidente qu'ils avaient."
"Jean Plank savait qu'il devait passer à l'offensive sans quoi il ne pourrait garder la face."

voice "doublages_jp1/scene5/scene5_jp5.ogg"
jp "Il ne me semble pas t'avoir vu sur les quais quand je suis rentré ce mat..."
"Il chercha du regard Lucien qui acquiesça d'un signe de tête."

voice "doublages_jp1/scene5/scene5_jp6.ogg"
jp "Ouais, ce matin !"

voice "doublages_jp1/scene5/scene5_mf5.ogg"
mf "Tu détournes le sujet."

voice "doublages_jp1/scene5/scene5_jp7.ogg"
jp "Et bien je ne vois qu'une seule façon de régler ce conflit !"

voice "doublages_jp1/scene5/scene5_mf6.ogg"
mf "Très bien ! On va régler ça à l'épée !"

voice "doublages_jp1/scene5/scene5_jp8.ogg"
jp "Tu oses me défier ?"

voice "doublages_jp1/scene5/scene5_mf7.ogg"
mf "Ouais j'ose, ouais !"

show FIAK
"N'écoutant que leurs instincts les plus primaires, nos deux amants se lancèrent alors à corps perdu dans leur confrontation."

show couple
"Dix minutes plus tard, le combat était terminé."
"On ne savait pas trop qui avait finalement gagné, mais Lucien avait pu prendre beaucoup de notes."

play music "music/meteore.ogg"
"Tout semblait aller pour le mieux quand tout à coup, un vacarme assourdissant se fit entendre."

show meteore1
"Ils se rhabillèrent en catastrophe puis sortirent dehors pour voir de quoi il retournait."

show meteore2
"Levant les yeux au ciel, ils découvrirent alors avec stupeur l'origine du boucan infâme."
"Un météore gigantesque se dirigeait droit sur eux !"

voice "doublages_jp1/scene5/scene5_mf8.ogg"
mf "Oh mon Dieu, il fonce droit sur nous !"

voice "doublages_jp1/scene5/scene5_jp9.ogg"
jp "Hum, c'est vrai !"
"Miss Fourtout regarda le capitaine qui avait visiblement du mal à connecter et ordonna la retraite."

show mf_fuite
voice "doublages_jp1/scene5/scene5_mf9.ogg"
mf "Fuyons !"

show jp_retient_mf
voice "doublages_jp1/scene5/scene5_jp10.ogg"
jp "Pas si vite ! Où crois-tu aller ? Personne n'abandonne le navire !"

voice "doublages_jp1/scene5/scene5_mf10.ogg"
mf "On est sur la terre ferme !"
#Scene crayon

show meteore_zoom
voice "doublages_jp1/scene5/scene5_jp11.ogg"
jp "Fourtout..."

voice "doublages_jp1/scene5/scene5_jp12.ogg"
jp "Le navire est une métaphore..."

hide meteore_zoom
voice "doublages_jp1/scene5/scene5_mf11.ogg"
mf "Mais je n'en ai rien à faire moi ! On va crever bordel !"
show lucien_chill
"En vision périphérique, elle remarqua alors Lucien qui s'était tranquillement assis sur un rocher."

voice "doublages_jp1/scene5/scene5_mf12.ogg"
mf "Mais, dis-lui toi !"

voice "doublages_jp1/scene5/scene5_lucien1.ogg"
lucien "Hé là, je refuse de me mêler de vos histoires de couple !"

voice "doublages_jp1/scene5/scene5_mf13.ogg"
mf "Mais toi aussi, tu vas mourir !"

voice "doublages_jp1/scene5/scene5_lucien2.ogg"
lucien "Ne t'inquiète pas pour moi, j'utiliserais ma magie pour résister au cataclysme."

voice "doublages_jp1/scene5/scene5_mf14.ogg"
mf "Et nous, alors ?"

voice "doublages_jp1/scene5/scene5_lucien3.ogg"
lucien "Eh bien, tu n'avais qu'à devenir magicienne !"

hide lucien_chill
voice "doublages_jp1/scene5/scene5_jp13.ogg"
jp "Bien dit !"

voice "doublages_jp1/scene5/scene5_mf15.ogg"
mf "Mais lâche moi abruti, lâche moi !"

show jp_retient_mf2
"Toujours en retenant sa fuyarde de femme, Jean Plank réalisa alors que c'était la fin."

if potion == 0:
    jump scene_valhala

show potion
"Tomba alors de sa poche la potion que lui avait précédemment refourgué Saint Gède."
"L'espoir renaissait."

show potion2
"Notre charismatique personnage principal lâcha Miss Fourtout et ramassa la fiole, la buvant d'un trait."
"Il sentit alors tout son corps se remplir d'une puissance nouvelle."
"Une vague de chaleur remonta de son ventre, lui brûlant la gorge avant d'irradier tout son être."
"Il lui semblait que son corps allait se déchirer."

show jp_cri
"Jean Plank se mit à hurler."
"Non pas car il avait mal, mais parce qu'il trouvait ça stylé."
"Il n'avait plus le temps."
"La peur, si tant est qu'elle l'eut un jour gagné, venait de le quitter."
"Il savait quoi faire désormais."

show meteore_jp2
"D'un mouvement superbe, il se lança corps et âme dans son combat épique contre le caillou cosmique."

window hide
stop music
play sound "sound/impact.ogg"
show ecran_noir
pause


#############################################################################################################################
#                                                                                                                           #
#                                                        SCENE 6                                                            #
#                                                                                                                           #
#############################################################################################################################

play music "music/ruines.ogg"
show ruines1
"Jean Plank regarda autour de lui :"
"Il ne restait que des ruines."

show ruines_lucien
"Lucien avait effectivement survécu et se tenait au milieu des décombres, immaculé."

hide ruines_lucien
"Le trésor de Jean Plank avait disparu avec sa demeure. Tout avait été pulvérisé par la chaleur de l'explosion."
"Miss Fourtout aussi avait disparu, elle aussi probablement désintégrée dans l'explosion malgré tous les efforts du capitaine pour la protéger."
"Mais le pire était à venir pour Jean Plank."
# "Lorsqu'il voulut remettre son tricorne, il ne le trouva point."
"Pour la première fois depuis des années, il sentit la brise marin caresser son crâne."

show lucien_degout
"Lucien s'approcha alors de lui, un air de dégoût fixé sur son visage ébène."

voice "doublages_jp1/scene6/scene6_lucien1.ogg"
lucien "Je ne trouve pas les mots." #nan vraiment je n'ai pas de réplique mais Sacha aura sûrement une idée

"Une sueur glacée glissa le long du dos du capitaine."

show miroir
"Jean Plank se précipita alors vers un morceau de miroir qui traînait par terre..."
"Le prit..."

show miroir2
"Et paniqué, il regarda."
"Mais ce ne fut pas son visage qu'il y vit."
"C'était celui de Saint Gède !"
"Saint Gède lui avait volé son visage !"

play sound "jp_singed_unhuman_scream"
"Le cri que Jean Plank poussa ne pourrait être décrit."
"Une sonorité à la limite de l'inhumain, traduisant la haine qui rongeait son cœur et l'infinie tristesse qui l'envahissait."
"Il se dépêcha d'aller ramasser son tricorne, mais rien n'effacerait ce qu'il ressentait actuellement."
"Il était amer de regrets, de regrets de ne pas avoir compris ce qui était réellement important durant toutes ces années."
"La faible voix de Miss Fourtout se fit alors entendre."

show ruines_mf
voice "doublages_jp1/scene6/scene6_mf1.ogg"
mf "Jean.."
"Elle n'était pas morte, simplement ensevelie sous des décombres."

show ruines_mf2
"Avec l'aide de Lucien, ils parvinrent à la dégager."

show ruines_mf_vomi
"Elle ouvrit les yeux et voyant le nouveau visage de celui-ci, elle se crispa de dégoût avant de se tourner tant bien que mal sur le côté pour vomir du sang."
"Elle était visiblement très mal en point."
#"Jean lui prit la main."

show ruines_mf3
voice "doublages_jp1/scene6/scene6_mf2.ogg"
mf "Je pense que c'est la fin, Jean..."

voice "doublages_jp1/scene6/scene6_jp1.ogg"
jp "Mais non, tu vas t'en sortir ! Il te reste tellement à vivre."

voice "doublages_jp1/scene6/scene6_mf3.ogg"
mf "Si c'est pour voir ta gueule tous les jours, ça ne vaut vraiment pas le coup !"
"Apaisée, elle ferma les yeux et mourut paisiblement sous le regard impuissant de Jean Plank."


"Jean Plank avait désormais tout perdu."



scene jp_larmes
play music "music/kill_la_kill_ost.ogg"
"Pour la première fois de sa vie, des larmes (mais des larmes d'homme) coulèrent de ses yeux."
"La rage l'inonda, lui faisant oublier la douleur."
"Oui! Il était désormais prêt à perdre bien plus encore !"
"Qui donc était responsable ?"
"Comment Saint-Gède avait-il osé ?!"
"Ce forban..."
"Tout n'était que complot."
"Oui !"
"Un complot infâme fomenté par quelqu'un qui existe, mais qu'on ne sait pas encore qui c'est !"
"Mais peu importe qui était ce scélérat, il allait le regretter."
"Il allait payer !"
"L'heure de la vengeance a sonné."

jump credits

#############################################################################################################################
#                                                                                                                           #
#                                                        SCENE 7                                                            #
#                                                                                                                           #
#############################################################################################################################

label scene_valhala:

show ecran_noir
stop music
play sound "sound/impact.ogg"
pause

hide ecran_noir
show jp_perdu

voice "doublages_jp1/scene7/scene7_jp1.ogg"
jp "Où... Où suis-je ?"

play music "music/valhalla.ogg"
show discover_valhalla
pause
"Jean Plank se rappela alors de la formule interdite impie apprise lors de son voyage."
"Il hurla de toutes ses forces : "

voice "doublages_jp1/scene7/scene7_jp2.ogg"
jp "KOKO WA DOKO ?! TIENMEN JDONC SECIÉ RAISTE DENTARA JEGRIMALKIN !"


show valhalla1
voice "doublages_jp1/scene7/scene7_odin1.ogg"
odin "Jean Plank, fils de fils de pute, bienvenue à Asgaard ! "

show valhalla2
"Au son de cette voix Jean Plank se retourna d'un coup."

voice "doublages_jp1/scene7/scene7_jp3.ogg"
jp "Qu'est-ce donc là que cette duperie ?"

voice "doublages_jp1/scene7/scene7_jp4.ogg"
jp "Vous tentez de jouer de malice pour spolier mon trésor ?!"

voice "doublages_jp1/scene7/scene7_odin2.ogg"
odin "Quel blasphème oses-tu proférer contre moi, Odin, Dieu des Dieux ?!"

show ecran_noir
$renpy.sound.set_volume(0.00, delay=0, channel='music')
play sound "sound/tonnerre.ogg"
"Le tonnerre gronda et Jean Plank fut foudroyé."

$renpy.sound.set_volume(1.00, delay=0, channel='music')

stop sound
show valhalla3
"Jean Plank se réveilla le lendemain."
"Au vu des événements récents, il comprit qu'il était mort."
"Il avait été tué."
"Une seule personne était capable de cette ignominie."
"Son plus grand rival, celui avec qui il avait tout appris : le Capitaine des Docks."

show valhalla4
voice "doublages_jp1/scene7/scene7_odin3.ogg"
odin "Jean Plank, te voilà revenu aux portes du Valhalla."

"Jean Plank songea à un plan de vengeance."
"Ce \"Odin\" allait peut-être lui être utile."

voice "doublages_jp1/scene7/scene7_odin4.ogg"
odin "Si tu es disposé à m'écouter, j'aimerais beaucoup que tu restes en notre compagnie. Nous aimons les valeureux combattants, tu te plairas ici !"

$renpy.sound.set_volume(0.00, delay=0, channel='music')
play alder "music/Crayon.ogg"
show jp_crayon_valhalla
voice "doublages_jp1/scene7/scene7_jp5.ogg"
jp "Odin, j'ai une vengeance à accomplir."

show odin_crayon

voice "doublages_jp1/scene7/scene7_odin5.ogg"
odin "Mais tu es mort Jean Plank, il t'est désormais impossible de retourner dans le monde des vivants."
hide odin_crayon

voice "doublages_jp1/scene7/scene7_jp6.ogg"
jp "Mais il suffirait que tu me donnes tes pouvoirs."

show odin_crayon

odin "Jean, je ne peux... Mes responsabilités..."
hide odin_crayon

voice "doublages_jp1/scene7/scene7_jp7.ogg"
jp "Ne t'en fais pas, je ferais de toi un gueux."

show odin_crayon

odin "Mais Jean..."
hide odin_crayon

voice "doublages_jp1/scene7/scene7_jp8.ogg"
jp "Od', c'est un sacrifice nécessaire."

show odin_crayon

odin "Nécessaire ?"
hide odin_crayon

voice "doublages_jp1/scene7/scene7_jp9.ogg"
jp "Oui, Od'. Pour notre gloire éternelle."

show odin_crayon

odin "Je comprends Jean. Quelqu'un doit le faire."

stop alder
$renpy.sound.set_volume(1.00, delay=0, channel='music')

show odin_pouvoirs
stop music
play sound "music/transfusion_power.ogg"
"Alors Odin donna l'intégralité de ses pouvoirs à Jean Plank."
window hide
pause
stop sound
show odin_gueux
"Conformément à sa promesse, Jean fit d'Odin un simple mortel avant de l'envoyer sur Terre dans une VIEILLE FERME DE MERDE."
# play sound "demerde.ogg"
window hide
pause

play music "music/kill_la_kill_ost.ogg"

scene jp_odin
"Du haut du Valhalla, Jean Plank était prêt."
"Il avait perdu son trésor, il avait perdu sa femme, il avait perdu son magicien."
"Il avait perdu la vie."
"Plus rien à perdre, tout à reprendre."
"L'heure de la vengeance est arrivée !"



#############################################################################################################################
#                                                                                                                           #
#                                                        CREDITS                                                            #
#                                                                                                                           #
#############################################################################################################################

label credits:

"Crédits :"
"Scénariste : Shiroi Maô\nConseiller scénaristique : Styrale"
"Réalisation : Monsieur Shiroi Maô\nCo-réalisateur : Monsieur Styrale\n"
"Montage : Le Sublime Shiroi Maô\nAssistant montage : L'astucieux Monsieur Styrale\n"
"Directeur de recherche : Le très estimé Lucas HAMMERER\nAssistant chercheur : Thomas BOCQUET"
"Directeur artistique : Séphultura \nConseiller artistique : LucianAteMyKFC"
"Digital Painteur presque de qualité : ShiroiMaô\nDirecteurs Audio : Jean-Eudes PATRÉCHER et Gontran PEUCOUTEUX\n"
"Doublage :"
"MissFourtout : La très généreuse génitrice de Monsieur Styrale\nJeanPlank, Lucien le magicien : ShiroiMaô qui en reste sans voix\n"
"Urgo, Saint Gède et Odin : Monsieur Styrale qui a donc acquis une expérience professionelle dans le doublage"
"Remerciements à la famille de Monsieur Lucas pour avoir le soutien moral et les studios"
"Remerciement à Monsieur Simon comme catalyseur de haine et surtout pour NE PAS AVOIR ÉTÉ LÀ !"
"Jeu réalisé avec le moteur Renpy"
pause
"FUCK ME PLEASE !"
pause
menu:
    "Revenir au menu principal":
        stop sound
        return
