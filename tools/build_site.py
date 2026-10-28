# Génère index.html (FR) et en/index.html (EN) — à lancer depuis n'importe où : python3 tools/build_site.py
# Les textes, photos, jours et prix se modifient ICI, puis on régénère (les pages sont écrasées).
import json, os, html, datetime
HERE = os.path.dirname(os.path.abspath(__file__))
R = os.path.dirname(HERE)
B = 'https://lhassa-katmandou.com'
PROFILE = open(os.path.join(HERE, 'profile.svg'), encoding='utf-8').read()
esc = html.escape

ALT = {
 'fr': {1:"Le groupe de cyclistes devant le palais du Potala, à Lhassa",2:"Le groupe à vélo dans une rue de Lhassa",3:"Le groupe devant un monastère de Lhassa",4:"Le lac Yamdrok vu depuis le col de Khampa La",5:"Stupa et glacier au col de Karo La",6:"Gyantse et sa forteresse perchée",7:"Le monastère de Tashilhunpo, à Shigatse",8:"Repas sous la tente au camp",9:"Pause pique-nique du groupe sur le plateau tibétain",10:"Repas dans une maison de thé tibétaine",11:"La face nord de l'Everest depuis Rongbuk",12:"Stupas et maisons anciennes de la vallée de Katmandou",13:"Le stupa de Boudhanath, à Katmandou",14:"Temple de Durbar Square, à Katmandou",15:"La grande mosquée de Xining illuminée la nuit",16:"Sommets enneigés du plateau tibétain vus du train",17:"À bord du train Xining–Lhassa, face au plateau",18:"Le palais du Potala, à Lhassa",19:"Un yak sur le plateau tibétain",20:"Les vallées du plateau entre Rongbuk et Tingri",21:"Cyclistes sous les drapeaux de prière d'un col",22:"La route du plateau entre deux collines",23:"Échoppes de tissus colorés à Katmandou",24:"Le lac Yamdrok et ses collines verdoyantes",25:"Sommets enneigés au-dessus du lac Yamdrok",26:"Les rives du lac Yamdrok sous un grand ciel bleu",27:"Les vélos posés au bord du lac Yamdrok",28:"Notre guide, poing levé, au col au-dessus du lac Yamdrok",29:"Repas du groupe sous la tente du camp",30:"La cour et les toits dorés du Jokhang, à Lhassa",31:"Pèlerins en prosternation devant le Jokhang",32:"Moines en assemblée au monastère de Sera",33:"Préparation des vélos dans un magasin de Lhassa",34:"Stupa du monastère de Rongbuk devant la face nord de l'Everest",35:"Déjeuner au wagon-restaurant du train du Tibet",36:"Le groupe à l'entrée du monastère de Sera",37:"Le groupe dans la cour du palais du Potala"},
 'en': {1:"The cycling group in front of the Potala Palace, Lhasa",2:"The group on their bikes in a Lhasa street",3:"The group in front of a monastery in Lhasa",4:"Yamdrok Lake seen from Khampa La pass",5:"Stupa and glacier at Karo La pass",6:"Gyantse and its hilltop fortress",7:"Tashilhunpo Monastery, Shigatse",8:"Dinner in the camp tent",9:"Picnic break on the Tibetan plateau",10:"Lunch in a Tibetan teahouse",11:"Everest's north face from Rongbuk",12:"Stupas and old houses in the Kathmandu valley",13:"Boudhanath stupa, Kathmandu",14:"A temple in Durbar Square, Kathmandu",15:"Xining's great mosque lit up at night",16:"Snow peaks of the Tibetan plateau seen from the train",17:"On board the Xining–Lhasa train",18:"The Potala Palace, Lhasa",19:"A yak on the Tibetan plateau",20:"Plateau valleys between Rongbuk and Tingri",21:"Riders under prayer flags at a pass",22:"The plateau road between two hills",23:"Colourful fabric stalls in Kathmandu",24:"Yamdrok Lake and its green hills",25:"Snow peaks above Yamdrok Lake",26:"The shores of Yamdrok Lake under a big blue sky",27:"Bikes laid down by Yamdrok Lake",28:"Our guide, fist raised, at the pass above Yamdrok Lake",29:"Group meal in the camp tent",30:"The courtyard and golden roofs of the Jokhang, Lhasa",31:"Pilgrims prostrating at the Jokhang",32:"Monks gathered at Sera Monastery",33:"Getting the bikes ready at a Lhasa bike shop",34:"Rongbuk Monastery stupa in front of Everest's north face",35:"Lunch in the dining car of the Tibet train",36:"The group at the entrance of Sera Monastery",37:"The group in the courtyard of the Potala Palace"},
}

T = {
'fr': dict(
  lang='fr', locale='fr_FR', home='/', other='/en/', path='',
  title="Lhassa–Katmandou à vélo — 20 jours / 19 nuits | Lost Horizon",
  desc="Lhassa–Katmandou à vélo, du 18 septembre au 7 octobre 2027 : une dizaine de cols à plus de 4 000 m, le lac Yamdrok, le camp de base de l'Everest et la traversée de l'Himalaya jusqu'à Katmandou. Départ de Xining. 4 590 € par personne.",
  tagline="CHINE · TREKKING &amp; AVENTURE",
  nav=[('#highlights','Points forts'),('#itinerary','Jour par jour'),('#fee','Inclus'),('#contact','Contact')],
  theme="Changer de thème", region="Tibet → Népal",
  h1="Lhassa–Katmandou à vélo",
  sub="Du 18 septembre au 7 octobre 2027 — une douzaine de jours à vélo, une dizaine de cols à plus de 4 000 m et environ 9 000 m de dénivelé, du palais du Potala au camp de base de l'Everest, puis la traversée de l'Himalaya jusqu'à Katmandou.",
  duration="20 jours / 19 nuits",
  summary="Ce n'est pas une simple traversée, c'est un voyage à vélo sur l'un des plateaux les plus hauts et les plus spectaculaires de la planète. Depuis Lhassa et le palais du Potala, une douzaine de jours de vélo sur la route de l'Amitié franchissent une dizaine de cols à plus de 4 000 m — dont plusieurs à plus de 5 000 m, avec le Gyagtso La à 5 220 m — pour environ 9 000 m de dénivelé. Au programme : le lac Yamdrok, les villes de Gyantsé et Shigatsé, le camp de base de l'Everest au pied de sa face nord, puis la traversée de l'Himalaya jusqu'au Népal et aux temples de la vallée de Katmandou. Un itinéraire exigeant, pour des cyclistes entraînés et à l'aise en montagne.",
  price_big="4 590 €", price_unit="par personne", price_line="Édition 2027, du 18 septembre au 7 octobre : <b>4 590 €</b> par personne",
  difficulty="Difficulté", diff_aria="difficulté 5 sur 5",
  meeting="Rendez-vous à Xining — fin à Katmandou", dates_tag="18 sept. → 7 oct. 2027", next="Prochain départ : du 18 septembre au 7 octobre 2027",
  season="Après la mousson et avant l'arrivée des grands froids : la saison idéale pour ce voyage.",
  cta1="Nous contacter", cta2="Voir l'itinéraire jour par jour",
  groups_h="Un groupe de cyclistes venus de plusieurs clubs",
  groups_p="Le groupe réunit des cyclistes de plusieurs clubs francophones (France, Belgique, Suisse, Québec), qui s'inscrivent chacun à titre individuel. En 2026, nous avons emmené un premier groupe de 12 cyclistes de Lhassa à Katmandou. Un itinéraire exigeant, pour des cyclistes entraînés et à l'aise en montagne.",
  hl_cap="Points forts", hl_h="Les temps forts du voyage",
  hls=[(18,"Lhassa et le palais du Potala","Deux jours pour découvrir la ville sainte à vélo, son architecture et son histoire, avant le départ."),
       (32,"Sera, Drepung et le Jokhang","Les trois grands monastères de Lhassa, dont Drepung, le plus grand ensemble monastique du Tibet."),
       (21,"Les cols du toit du monde","Khampa La, Karo La, Gyagtso La, Pang La… une dizaine de cols à plus de 4 000 m, dont plusieurs à plus de 5 000 m, au cœur du plateau tibétain."),
       (11,"Le camp de base de l'Everest","Cinq sommets de plus de 8 000 m visibles depuis le col de Pang La, puis une nuit à Rongbuk, le monastère le plus haut du monde, près du camp de base, face à l'Everest."),
       (8,"La vie de camp en altitude","Un cuisinier et son assistant vous accompagnent tout du long : nuits sous tente et repas chauds, même à 4 800 m."),
       (12,"Katmandou et la vallée népalaise","Deux jours pour découvrir Durbar Square, Patan, Bhaktapur et les stupas de Swayambhunath et Boudhanath.")],
  alt_h="Acclimatation à l'altitude indispensable",
  alt_p="Ce voyage commence haut et monte vite : une douzaine de jours de vélo entre 3 400 et plus de 5 200 m, avec des étapes pouvant dépasser 120 km et 1 300 m de dénivelé positif. Une bonne acclimatation est essentielle : les premiers jours (Xining, puis Lhassa) permettent une montée progressive avant les cols du plateau, et une bouteille d'oxygène de secours fait partie de l'équipement du voyage. Un caisson hyperbare portable (PAC) suit en outre l'équipe tout au long du parcours. Comme pour nos autres itinéraires en très haute altitude, nous pouvons vous aider à préparer votre acclimatation avant le départ.",
  guide_cap="Votre guide", guide_h="Axel, guide et explorateur", guide_role="Guide pendant tout le voyage",
  guide_alt="Axel, notre guide, souriant avec son sac à dos et ses bâtons de marche sur un sentier de montagne",
  guide_ps=["Axel est aventurier professionnel et chef d'expédition en plein air. Il a parcouru des environnements exigeants — les Alpes, l'Amazonie, le Sahara — et mené des expéditions en haute montagne, une traversée en pirogue et des expéditions dans le désert. Cette expérience lui a donné une solide pratique de la vie en pleine nature.",
            "Ancien ingénieur en énergie et environnement, il a travaillé à l'observatoire astronomique de Shanghai. Passionné par l'histoire et la culture chinoises, il a étudié le chinois et l'histoire de la Chine ancienne. Depuis 2024, il emmène des voyageurs sur de longs itinéraires de traversée en Europe, en Chine et dans d'autres pays. Il a déjà guidé au Tibet et a traversé la Chine à vélo.",
            "Il aime l'aventure en montagne et l'observation de la faune, et partage volontiers avec le groupe les anecdotes culturelles du chemin."],
  guide_stats=[("Langues","chinois, anglais, français, espagnol"),("Secourisme","formation de l'Ifremmont (Institut de formation et de recherche en médecine de montagne)")],
  gal_cap="En images", gal_h="Le groupe 2026, de Lhassa au lac Yamdrok", gal_p="Quelques moments du premier voyage, en 2026 : préparation des vélos, visites de Lhassa, pauses au bord du lac Yamdrok et vie de camp.",
  route_cap="Parcours", route_h="Profil d'altitude, de Lhassa à Katmandou",
  profile_aria="Profil d'altitude de Lhassa à Katmandou",
  profile_note="Altitude de chaque étape et de chaque col entre Lhassa (jour 3) et Katmandou (jour 17). Les points dorés marquent les principaux cols.",
  dd_cap="Jour par jour", dd_h="L'itinéraire complet", day="JOUR", dshort="J",
  st=dict(bike="Vélo", elev="Dénivelé", transport="Transport", night="Nuit"),
  fee_cap="Bon à savoir", fee_h="Ce qui est inclus", inc="Inclus", notinc="Non inclus",
  included=[("Hébergement","Hôtels, maisons d'hôtes ou camping en Chine ; hôtel au Népal"),
            ("Transferts","Accueil à votre arrivée à Xining ; transfert à l'aéroport de Katmandou le dernier jour"),
            ("Train","Train de nuit Xining–Lhassa (couchette de 1re classe)"),
            ("Repas","Tous les repas, sauf ceux indiqués comme non inclus"),
            ("Encadrement","Axel, votre guide (chinois, anglais, français, espagnol), pendant tout le voyage"),
            ("Équipe cuisine","Un cuisinier et un assistant, avec tout l'équipement de cuisine de camp"),
            ("Vélo et matériel","Un VTT par personne (Giant ou équivalent) avec pièces de rechange ; tout le matériel de camping sauf votre sac de couchage"),
            ("Permis et droits","Tous les permis d'entrée et de circulation au Tibet, les droits des parcs nationaux (Everest, lac Yamdrok, glacier du Karo La) et toutes les entrées des sites et monastères au programme"),
            ("Véhicules","Un minibus d'assistance et un véhicule logistique"),
            ("Sécurité en altitude","Une bouteille d'oxygène de secours et un caisson hyperbare portable (PAC) qui suit l'équipe")],
  excluded=[("Vols","Vols internationaux jusqu'à Xining et depuis Katmandou"),
            ("Certains repas","Déjeuners et dîners à Xining, Lhassa et Gyantse, et dîners à Katmandou et Shigatse"),
            ("Visa","Frais de visa (pas de visa requis pour la Chine ; environ 30 € pour le Népal)"),
            ("Sac de couchage","À apporter"),
            ("Assurance","Assurance voyage, assistance et annulation"),
            ("Pourboires","Pour votre guide, votre chauffeur, votre cuisinier, etc.")],
  fee_note="Cette page présente le voyage, ce n'est pas un formulaire de réservation en ligne : les dates, la taille du groupe et le programme définitif sont toujours confirmés personnellement avec notre équipe avant le départ.",
  terms_cap="Conditions", terms_h="Conditions de réservation",
  t1h="Si vous devez annuler", t1=["Les conditions d'annulation dépendent de la date à laquelle vous annulez par rapport au départ ; elles vous sont confirmées par écrit à la réservation.","En cas de refus de visa, nous demandons la lettre officielle de refus du consulat et remboursons ce qui peut l'être, déduction faite des frais déjà engagés pour vous.","Une place confirmée peut en général être cédée à un autre voyageur remplissant les conditions."],
  t2h="Si nous devons annuler", t2=["Si des raisons de sécurité ou des restrictions officielles imposent un changement, nous adaptons le voyage ou remboursons la partie non effectuée."],
  c_cap="Contact", c_h="Nous contacter",
  c_p="Nous ne prenons pas de réservation en ligne : ce site est là pour vous présenter le voyage. Appelez-nous ou écrivez-nous pour en parler, que vous soyez cycliste intéressé ou responsable de club.",
  email="E-mail", phone="Téléphone (Mathieu Le Serre)", team="Yannick Benichou et Mathieu Le Serre, Lost Horizon", chat="WeChat et WhatsApp", qr_alt="QR code {} de Yannick",
  legal="Immatriculation et garanties", legal_txt="Atout France IM035240001 · garantie financière APST · vérifier au registre →",
  footer="Lost Horizon — présentation du voyage et demandes d'information ; dates et détails confirmés personnellement avec notre équipe.",
  labels={'Lhasa':'Lhassa','Kathmandu':'Katmandou'},
),
'en': dict(
  lang='en', locale='en_GB', home='/en/', other='/', path='en/',
  title="Lhasa to Kathmandu by Bike — 20 days / 19 nights | Lost Horizon",
  desc="Lhasa to Kathmandu by bike, 18 September to 7 October 2027: around ten passes above 4,000m, Yamdrok Lake, Everest Base Camp and the crossing of the Himalaya to Kathmandu. Starts in Xining. €4,590 per person.",
  tagline="CHINA · TREKKING &amp; ADVENTURE",
  nav=[('#highlights','Highlights'),('#itinerary','Day by Day'),("#fee","What's Included"),('#contact','Contact')],
  theme="Toggle theme", region="Tibet → Nepal",
  h1="Lhasa to Kathmandu by Bike",
  sub="18 September to 7 October 2027 — around twelve days in the saddle, around ten passes above 4,000m and about 9,000m of climbing, from the Potala Palace to Everest Base Camp, then across the Himalaya to Kathmandu.",
  duration="20 days / 19 nights",
  summary="This is not a simple crossing — it's a cycling journey across one of the highest, most spectacular plateaus on Earth. From Lhasa and the Potala Palace, around twelve days of riding along the Friendship Highway cross around ten passes above 4,000m — several of them above 5,000m, including the Gyagtso La at 5,220m — for about 9,000m of climbing. Along the way: Yamdrok Lake, the towns of Gyantse and Shigatse, Everest Base Camp at the foot of the north face, then the crossing of the Himalaya into Nepal and the temples of the Kathmandu valley. A demanding route, for trained cyclists who are at ease in the mountains.",
  price_big="€4,590", price_unit="per person", price_line="2027 departure, 18 September to 7 October: <b>€4,590</b> per person",
  difficulty="Difficulty", diff_aria="difficulty 5 out of 5",
  meeting="Meeting point: Xining — ends in Kathmandu", dates_tag="18 Sep → 7 Oct 2027", next="Next departure: 18 September to 7 October 2027",
  season="After the monsoon and before the cold sets in: the ideal season for this journey.",
  cta1="Enquire About This Trip", cta2="See Day-by-Day Itinerary",
  groups_h="A group of riders from several clubs",
  groups_p="The group brings together cyclists from several French-speaking clubs (France, Belgium, Switzerland, Québec), each signing up individually. In 2026 we took a first group of 12 cyclists from Lhasa to Kathmandu. A demanding route, for trained cyclists who are at ease in the mountains.",
  hl_cap="Highlights", hl_h="Trip Highlights",
  hls=[(18,"Lhasa and the Potala Palace","Two days exploring the holy city by bike, its architecture and history, before setting off."),
       (32,"Sera, Drepung and Jokhang","Lhasa's three great monasteries, including Drepung, the largest monastic complex in Tibet."),
       (21,"The passes of the roof of the world","Khampa La, Karo La, Gyagtso La, Pang La… around ten passes above 4,000m, several of them above 5,000m, across the heart of the Tibetan plateau."),
       (11,"Everest Base Camp","Five 8,000m+ peaks in view from Pang La pass, then a night at Rongbuk, the world's highest monastery, near Base Camp and facing Everest."),
       (8,"High-altitude camp life","A cook and an assistant travel with you the whole way: camp nights and hot meals, even at 4,800m."),
       (12,"Kathmandu and the Nepalese valley","Two days to discover Durbar Square, Patan, Bhaktapur and the stupas of Swayambhunath and Boudhanath.")],
  alt_h="Altitude acclimatisation required beforehand",
  alt_p="This trip starts high and climbs fast: around twelve riding days between 3,400 and over 5,200m, with stages that can exceed 120km and 1,300m of ascent. Good acclimatisation is essential — the first days (Xining, then Lhasa) allow a gentle climb before the passes of the plateau, and a spare oxygen bottle is carried as part of the trip's equipment. A portable hyperbaric chamber (PAC) also travels with the team throughout the trip. As with our other very high-altitude routes, we can help you prepare your acclimatisation before departure.",
  guide_cap="Your Guide", guide_h="Axel, Guide and Explorer", guide_role="Your guide for the whole trip",
  guide_alt="Axel, our guide, smiling with his backpack and trekking poles on a mountain trail",
  guide_ps=["Axel is a professional adventurer and outdoor leader. He has worked in demanding environments — the Alps, the Amazon, the Sahara — and has completed high-mountain expeditions, a dugout canoe crossing and desert expeditions. This experience has given him a deep, practical knowledge of life in the wild.",
            "A former environmental and energy engineer, he worked at the Shanghai Astronomical Observatory. Drawn to Chinese history and culture, he studied Chinese and ancient Chinese history. Since 2024, he has been leading travellers on long-distance crossings in Europe, China and other countries. He has already guided in Tibet and has crossed China by bike.",
            "He loves mountain adventure and wildlife watching, and enjoys sharing the cultural stories of the road with the group."],
  guide_stats=[("Languages","Chinese, English, French, Spanish"),("First aid","Ifremmont training (Institut de formation et de recherche en médecine de montagne)")],
  gal_cap="In Pictures", gal_h="The 2026 group, from Lhasa to Yamdrok Lake", gal_p="A few moments from the first trip, in 2026: getting the bikes ready, visiting Lhasa, breaks by Yamdrok Lake and camp life.",
  route_cap="Route", route_h="Elevation Profile, Lhasa to Kathmandu",
  profile_aria="Elevation profile, Lhasa to Kathmandu",
  profile_note="Altitude of each stage and pass between Lhasa (day 3) and Kathmandu (day 17). Gold points mark the main passes.",
  dd_cap="Day by Day", dd_h="Full Itinerary", day="DAY", dshort="D",
  st=dict(bike="Cycling", elev="Elevation", transport="Transport", night="Overnight"),
  fee_cap="Good to Know", fee_h="What's Included", inc="Included", notinc="Not Included",
  included=[("Accommodation","Hotels, guesthouses or camping in China; hotel in Nepal"),
            ("Transfers","Welcome on arrival in Xining; transfer to Kathmandu airport on the last day"),
            ("Train","Xining–Lhasa overnight train (1st-class sleeper)"),
            ("Meals","All meals except those listed as not included"),
            ("Guiding","Axel, your guide (Chinese, English, French, Spanish), for the whole trip"),
            ("Kitchen crew","A cook and an assistant, with full camp kitchen equipment"),
            ("Bike &amp; gear","One mountain bike per person (Giant or equivalent) with spare parts; all camping equipment except your sleeping bag"),
            ("Permits &amp; fees","All Tibet entry/travel permits, national park fees (Everest, Yamdrok Lake, Karo La glacier) and all site/monastery tickets on the programme"),
            ("Support vehicles","A support minivan and a logistics vehicle"),
            ("Altitude safety","A spare oxygen bottle and a portable hyperbaric chamber (PAC) that travels with the team")],
  excluded=[("Flights","International flights to Xining and from Kathmandu"),
            ("Some meals","Lunches and dinners in Xining, Lhasa and Gyantse, and dinners in Kathmandu and Shigatse"),
            ("Visa","Visa fees (none required for China; about €30 for Nepal)"),
            ("Sleeping bag","Bring your own"),
            ("Insurance","Travel, assistance and cancellation insurance"),
            ("Tips","For your guide, driver, cook, etc.")],
  fee_note="This page is a trip presentation, not an online booking form — dates, group size and final program are always confirmed personally with our team before you travel.",
  terms_cap="Terms", terms_h="Booking Terms",
  t1h="If You Need to Cancel", t1=["Cancellation terms depend on how close to departure you cancel, and are confirmed in writing when your trip is booked.","If a visa application is refused, we ask for the official refusal letter from the consulate and refund what we can once any costs already committed on your behalf are deducted.","A confirmed place can usually be transferred to another eligible traveller."],
  t2h="If We Need to Cancel", t2=["If safety conditions or government restrictions force a change, we'll adapt or refund the unused portion of the trip."],
  c_cap="Contact", c_h="Get in Touch",
  c_p="We don't take bookings online — this site is here to show you the trip. Call or write to us to talk it through, whether you're an interested rider or a club organiser.",
  email="Email", phone="Phone (Mathieu Le Serre)", team="Yannick Benichou and Mathieu Le Serre, Lost Horizon", chat="WeChat &amp; WhatsApp", qr_alt="Yannick's {} QR code",
  legal="Registration &amp; guarantees", legal_txt="Atout France IM035240001 · APST financial guarantee · check the register →",
  footer="Lost Horizon — trip presentation &amp; enquiries, dates and details confirmed personally with our team.",
  labels={},
)}

# Days: (photo, {lang: (title, desc, [(stat_key, value)])})
DAYS = [
 (15, {'fr': ("Arrivée à Xining (2 300 m)", "Arrivée à Xining, la plus grande ville du plateau tibétain. Accueil à votre arrivée et transfert à votre hébergement.", [('night',"Xining, 2 300 m")]),
       'en': ("Arrival in Xining (2300m)", "Arrival in Xining, the largest city on the Tibetan plateau. Welcome on arrival and transfer to your accommodation.", [('night',"Xining, 2300m")])}),
 (35, {'fr': ("Xining → Lhassa", "Journée de visite du monastère de Kumbum, bâti sur le lieu de naissance de Tsongkhapa, où l'exploratrice Alexandra David-Néel a séjourné trois ans. Embarquement le soir à bord du « train du Tibet », le plus haut du monde : environ 22 heures de voyage pour une arrivée en douceur et tout en paysages sur le toit du monde.", [('transport',"Train de nuit"),('night',"À bord du train")]),
       'en': ("Xining → Lhasa", "Full-day visit of Kumbum Monastery, built on the birthplace of Tsongkhapa and where the explorer Alexandra David-Neel once stayed for three years. Boarding in the evening on the “Tibet train”, the highest in the world: around 22 hours on board for a scenic and gentle arrival on the roof of the world.", [('transport',"Overnight train"),('night',"On board the train")])}),
 (16, {'fr': ("Arrivée à Lhassa (3 835 m)", "Arrivée à Lhassa en soirée. Accueil par votre guide et transfert à l'hôtel.", [('night',"Lhassa, 3 835 m")]),
       'en': ("Arrival in Lhasa (3835m)", "Evening arrival in Lhasa. Welcome by your guide and transfer to your hotel.", [('night',"Lhasa, 3835m")])}),
 (33, {'fr': ("Lhassa à vélo", "Tour à vélo de la ville et de ses environs : photo de groupe devant le Potala, le bâtiment le plus imposant de Lhassa et ancien siège du gouvernement tibétain, puis visite des monastères de Sera et de Drepung, à 8 km du centre — le plus grand ensemble monastique du Tibet.", [('night',"Lhassa, 3 835 m")]),
       'en': ("Lhasa by bike", "Cycling tour of the city and its surroundings: group photo in front of the Potala, the most imposing building in Lhasa and former seat of the Tibetan government, followed by a visit to Sera and Drepung monasteries, 8km from the city centre – the largest monastic complex in Tibet.", [('night',"Lhasa, 3835m")])}),
 (31, {'fr': ("Lhassa", "Visite le matin du monastère du Jokhang, construit en 647 lors de l'arrivée du bouddhisme au Tibet — berceau et foyer sacré du bouddhisme tibétain. Temps libre ensuite pour flâner sur le Barkhor, la rue animée qui l'entoure.", [('night',"Lhassa, 3 835 m")]),
       'en': ("Lhasa", "Morning visit of Jokhang Monastery, built in 647 when Buddhism was introduced to Tibet – the cradle and sacred home of Tibetan Buddhism. Free time afterwards to wander the lively Barkhor street surrounding it.", [('night',"Lhasa, 3835m")])}),
 (2, {'fr': ("Lhassa → Quxu (3 600 m)", "Départ vers la région de Chushul en longeant la rivière de Lhassa, principal affluent du Yarlung Tsangpo (Brahmapoutre). Arrêt possible devant une peinture bouddhique rupestre et au temple de Nyethang Drolma Lhakhang, détour par le pont de Chushul. Camp près de Quxu.", [('bike',"85 km"),('elev',"+370 m / −400 m"),('night',"Camp près de Quxu, 3 600 m")]),
       'en': ("Lhasa → Quxu (3600m)", "Departure towards the Chushue area, following the Lhasa river, the main tributary of the Yarlung Tsangpo (Brahmaputra). Possible stop at a Buddhist mural and at Nyethang Drolma Lhakang temple, detour via Chushue bridge. Camp near Quxu.", [('bike',"85km"),('elev',"+370m / −400m"),('night',"Camp near Quxu, 3600m")])}),
 (4, {'fr': ("Quxu → Nagarzê (4 410 m)", "Passage du col de Khampa La (4 795 m), avec une très belle vue sur la vallée du Yarlung, le fleuve Yarlung Tsangpo et le lac Yamdrok. Descente sur plusieurs kilomètres le long du lac. Camp près du lac et de Nagarzê.", [('bike',"59 km"),('elev',"+1 390 m / −560 m"),('night',"Camp près de Nagarzê, 4 410 m")]),
       'en': ("Quxu → Nagarze (4410m)", "Crossing of Khampa La pass (4795m), with a beautiful view over the Yarlung valley, the Yarlung Tsangpo river and Yamdrok Lake. Descent along the lake shore for several kilometres. Camp near the lake and Nagarze.", [('bike',"59km"),('elev',"+1390m / −560m"),('night',"Camp near Nagarze, 4410m")])}),
 (6, {'fr': ("Nagarzê → Gyantsé (4 020 m)", "Passage d'un nouveau col, le Karo La, à 5 045 m. La route monte doucement dans la vallée avant une dernière portion plus raide. L'arrivée au col est spectaculaire, avec un sommet de plus de 7 000 m d'un côté et une montagne de 6 400 m de l'autre. La descente de l'après-midi est longue mais très roulante, avec en vue Gyantsé, ville très typique dominée par sa forteresse perchée sur un promontoire. Nuit à l'hôtel.", [('bike',"122 km"),('elev',"+1 115 m / −1 140 m"),('night',"Gyantsé, 4 020 m")]),
       'en': ("Nagarze → Gyantse (4020m)", "Crossing of a new pass, the Karo La, at 5045m. The road climbs gently up the valley before a steeper final stretch. The arrival at the pass is spectacular, with a 7000m+ peak on one side and a 6400m mountain on the other. The afternoon descent is long but very rideable, with a glimpse of Gyantse – a very typical town with its fortress perched on a promontory overlooking it. Hotel night.", [('bike',"122km"),('elev',"+1115m / −1140m"),('night',"Gyantse, 4020m")])}),
 (7, {'fr': ("Gyantsé → Shigatsé (3 835 m)", "Route ce matin vers Shigatsé, deuxième ville du Tibet. Elle abrite le monastère de Tashilhunpo, ancien siège officiel du panchen-lama, deuxième autorité politique et spirituelle du Tibet, et la plus grande statue de bronze du monde, réalisée en 1904 pour Maitreya, le Bouddha du futur. Nuit à l'hôtel.", [('bike',"94 km"),('elev',"+140 m / −320 m"),('night',"Shigatsé, 3 835 m")]),
       'en': ("Gyantse → Shigatse (3835m)", "Ride this morning towards Shigatse, Tibet's second city. Home to Tashilhunpo Monastery, the former official seat of the Panchen Lama, Tibet's second political and spiritual authority. It houses the world's largest bronze statue, built in 1904 for Maitreya, the Buddha of the future. Hotel night.", [('bike',"94km"),('elev',"+140m / −320m"),('night',"Shigatse, 3835m")])}),
 (29, {'fr': ("Shigatsé → Jingdingzhen (3 905 m)", "Journée de vélo sur la route de l'Amitié, avec deux petits cols assez faciles. Nuit au camp.", [('bike',"98 km"),('elev',"+820 m / −470 m"),('night',"Camp à Jingdingzhen, 3 905 m")]),
       'en': ("Shigatse → Jingdingzhen (3905m)", "Riding day on the Friendship Highway, crossing two fairly easy small passes. Camp night.", [('bike',"98km"),('elev',"+820m / −470m"),('night',"Camp at Jingdingzhen, 3905m")])}),
 (19, {'fr': ("Jingdingzhen → Lhatsé (4 050 m)", "Passage du col de Yulung La (4 450 m), puis descente dans de superbes paysages de haut plateau tibétain jusqu'à Lhatsé. Nuit à l'hôtel.", [('bike',"52 km"),('elev',"+440 m / −610 m"),('night',"Lhatsé, 4 050 m")]),
       'en': ("Jingdingzhen → Lhatse (4050m)", "Crossing of Yulung La pass (4450m), then a descent through superb Tibetan high-plateau scenery down to Lhatse. Hotel night.", [('bike',"52km"),('elev',"+440m / −610m"),('night',"Lhatse, 4050m")])}),
 (22, {'fr': ("Lhatsé → Shegar (4 320 m)", "Le plus haut col du voyage vous attend : le Gyagtso La, à 5 220 m, puis descente dans la vallée. Premières vues sur l'Everest, si le temps le permet. Nuit à l'hôtel.", [('bike',"81 km"),('elev',"+1 300 m / −1 000 m"),('night',"Shegar, 4 320 m")]),
       'en': ("Lhatse → Shegar (4320m)", "The highest pass of the whole trip awaits: Gyagtso La, at 5220m, then a descent into the valley. First views of Everest, weather permitting. Hotel night.", [('bike',"81km"),('elev',"+1300m / −1000m"),('night',"Shegar, 4320m")])}),
 (34, {'fr': ("Shegar → Tashi Dzom → Rongbuk (5 000 m)", "Passage du col de Pang La (5 195 m). Du sommet, la chaîne himalayenne se déploie de façon saisissante, avec pas moins de cinq sommets de plus de 8 000 m face à vous. Descente jusqu'au village de Tashi Dzom, puis transfert en véhicule jusqu'au monastère de Rongbuk, le plus haut du monde, près du camp de base de l'Everest. Nuit en maison d'hôtes.", [('bike',"62 km"),('elev',"+970 m / −1 130 m"),('transport',"Bus, Tashi Dzom → Rongbuk"),('night',"Rongbuk, 5 000 m")]),
       'en': ("Shegar → Tashi Dzom → Rongbuk (5000m)", "Crossing of Pang La pass (5195m). From the top, the Himalayan range unfolds breathtakingly, with no fewer than five 8000m+ peaks in front of you. Descent to Tashi Dzom village, then transfer by vehicle to Rongbuk Monastery, the highest monastery in the world, near Everest Base Camp. Guesthouse night.", [('bike',"62km"),('elev',"+970m / −1130m"),('transport',"Bus, Tashi Dzom → Rongbuk"),('night',"Rongbuk, 5000m")])}),
 (20, {'fr': ("Rongbuk → Tashi Dzom → Tingri (4 350 m)", "Un dernier col à 4 915 m, le Namar La, dans une vallée sauvage et peu fréquentée, suivi d'une descente rapide vers la plaine de Tingri. Nuit à l'hôtel.", [('bike',"59 km"),('elev',"+800 m / −630 m"),('night',"Tingri, 4 350 m")]),
       'en': ("Rongbuk → Tashi Dzom → Tingri (4350m)", "A final pass at 4915m, the Namar La, through a wild and little-used valley, followed by a fast descent to the Tingri plain. Hotel night.", [('bike',"59km"),('elev',"+800m / −630m"),('night',"Tingri, 4350m")])}),
 (9, {'fr': ("Tingri → Nyalam Tongla (4 800 m)", "Retour sur la route de l'Amitié jusqu'au col de Nyalam Tongla. La montée est longue et le dernier replat en usera plus d'un. Descente rapide, puis nuit au camp entre les deux cols, à 4 800 m d'altitude.", [('bike',"88 km"),('elev',"+920 m / −390 m"),('night',"Camp à Nyalam Tongla, 4 800 m")]),
       'en': ("Tingri → Nyalam Tongla (4800m)", "Back on the Friendship Highway, continuing to Nyalam Tongla pass. The climb is long and the final flat stretch will wear more than one rider down. Fast descent, then a camp night between the two passes, at 4800m altitude.", [('bike',"88km"),('elev',"+920m / −390m"),('night',"Camp at Nyalam Tongla, 4800m")])}),
 (10, {'fr': ("Nyalam Tongla → Nyalam (3 400 m)", "Passage du dernier col du voyage, le Yagru Xong La (5 125 m) — aussi le dernier point de vue sur la chaîne himalayenne, avec le Shishapangma, sommet de plus de 8 000 m, sur votre droite. Descente facile et spectaculaire, puis route plus plate dans la vallée. Nuit à l'hôtel.", [('bike',"64 km"),('elev',"+460 m / −1 560 m"),('night',"Nyalam, 3 400 m")]),
       'en': ("Nyalam Tongla → Nyalam (3400m)", "Crossing of the last pass of the trip, Yagru Xong La (5125m) – also the last viewpoint over the Himalayan range, with Xishapangma, an 8000m+ peak, visible on your right. Easy and spectacular descent, then flatter riding down the valley. Hotel night.", [('bike',"64km"),('elev',"+460m / −1560m"),('night',"Nyalam, 3400m")])}),
 (23, {'fr': ("Nyalam → Katmandou (1 350 m)", "Descente en véhicule vers le poste-frontière, dans des paysages magnifiques. Passage de la frontière et formalités de visa népalais, rencontre avec l'équipe népalaise, puis route vers Katmandou. Nuit à l'hôtel.", [('transport',"Bus, 30 km"),('night',"Katmandou, 1 350 m")]),
       'en': ("Nyalam → Kathmandu (1350m)", "Descent by vehicle towards the border post, through magnificent scenery. Border crossing and Nepalese visa formalities, meeting with the Nepalese team, then drive to Kathmandu. Hotel night.", [('transport',"Bus, 30km"),('night',"Kathmandu, 1350m")])}),
 (14, {'fr': ("Katmandou (1 350 m)", "Après le petit-déjeuner, visite de Durbar Square puis de Patan, l'une des trois anciennes cités royales de la vallée, majoritairement bouddhiste et réputée pour ses artisans bronziers. Continuation vers Swayambhunath, temple perché sur une colline, peuplé de singes et coiffé d'un immense stupa dominant la vallée de Katmandou. Nuit à l'hôtel.", [('night',"Katmandou, 1 350 m")]),
       'en': ("Kathmandu (1350m)", "After breakfast, visit Durbar Square then Patan, one of the valley's three ancient royal cities, mainly Buddhist and renowned for its bronze-casting artisans. Continue to Swayambhunath, a hilltop temple home to monkeys and a huge Buddhist stupa overlooking the Kathmandu valley. Hotel night.", [('night',"Kathmandu, 1350m")])}),
 (13, {'fr': ("Katmandou (1 350 m)", "Visite le matin de Bhaktapur, somptueuse cité piétonne à 15 km de Katmandou, la plus belle des trois cités royales de la vallée. Continuation vers le temple de Pashupatinath et le stupa de Boudhanath. Nuit à l'hôtel.", [('night',"Katmandou, 1 350 m")]),
       'en': ("Kathmandu (1350m)", "Morning visit of Bhaktapur, a sumptuous pedestrian city 15km from Kathmandu, the most beautiful of the valley's three royal cities. Continue to Pashupatinath temple and Boudhanath stupa. Hotel night.", [('night',"Kathmandu, 1350m")])}),
 (None, {'fr': ("Katmandou, fin du voyage", "Petit-déjeuner, puis transfert à l'aéroport international de Tribhuvan. Fin de nos services.", [('transport',"Transfert à l'aéroport")]),
         'en': ("Kathmandu, end of the trip", "Breakfast, then transfer to Tribhuvan International Airport. End of our services.", [('transport',"Airport transfer")])}),
]
CAROUSEL = [25, 27, 5, 30, 24, 26]
HLPOS = {18: ' style="object-position:center top"', 21: ' style="object-position:center top"', 11: ' style="object-position:center top"'}
GALLERY = [28, 1, 37, 3, 36, 17]

def short(desc):  # first sentence for the summary strip
    i = desc.find('. ')
    return desc if i == -1 else desc[:i+1]

ICON_MAIL = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8"><rect x="3" y="5" width="18" height="14" rx="2"></rect><path d="m4 7 8 6 8-6"></path></svg>'
ICON_CHAT = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8"><path d="M8.5 13.5c-3.6 0-6.5-2.3-6.5-5.2C2 5.4 4.9 3 8.5 3S15 5.4 15 8.3c0 .9-.3 1.7-.7 2.5"></path><circle cx="6" cy="7.5" r=".6" fill="currentColor" stroke="none"></circle><circle cx="11" cy="7.5" r=".6" fill="currentColor" stroke="none"></circle><path d="M13.2 12c3 0 5.4 1.9 5.4 4.3s-2.4 4.3-5.4 4.3c-.6 0-1.1-.1-1.7-.2L9 21.5l.6-2.2c-1.2-.8-2-2-2-3.4 0-2.4 2.4-4.3 5.4-4.3Z"></path><circle cx="11.3" cy="16" r=".55" fill="currentColor" stroke="none"></circle><circle cx="15" cy="16" r=".55" fill="currentColor" stroke="none"></circle></svg>'
ICON_PHONE = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8"><path d="M5 4h4l2 5-2.5 1.5a11 11 0 0 0 5 5L15 13l5 2v4a2 2 0 0 1-2 2A16 16 0 0 1 3 6a2 2 0 0 1 2-2"></path></svg>'
ICON_SHIELD = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8"><path d="M12 3 4.5 6v6c0 5 3.2 8.7 7.5 9.9 4.3-1.2 7.5-4.9 7.5-9.9V6L12 3Z"></path><path d="m8.5 12 2.4 2.4L16 9.5"></path></svg>'

def page(L):
    t = T[L]; alt = ALT[L]
    url = B + t['home']
    prof = PROFILE.replace('aria-label="Elevation profile, Lhasa to Kathmandu"', f'aria-label="{t["profile_aria"]}"')
    for a, b in t['labels'].items():
        prof = prof.replace(f'>{a}</text>', f'>{b}</text>')
    carousel = '\n'.join(f'      <img{" fetchpriority=\"high\"" if i == 0 else ""} src="/images/photo-{n:02d}.jpg?v=2" alt="{esc(alt[n])}">' for i, n in enumerate(CAROUSEL))
    hls = '\n'.join(f'''      <div class="hl-item">
        <div class="hl-photo"><img loading="lazy" decoding="async" src="/images/photo-{p:02d}.jpg?v=2" alt="{esc(alt[p])}"{HLPOS.get(p, "")}></div>
        <div class="hl-body">
          <div class="hl-num">{k+1:02d}</div>
          <h3>{esc(h)}</h3>
          <p>{esc(d)}</p>
        </div>
      </div>''' for k, (p, h, d) in enumerate(t['hls']))
    guide_ps = '\n'.join(f'          <p class="desc">{esc(p)}</p>' for p in t['guide_ps'])
    guide_stats = '\n'.join(f'            <div class="day-stat">{esc(k)}{" :" if L == "fr" else ":"} <b>{esc(v)}</b></div>' for k, v in t['guide_stats'])
    strip, cards = [], []
    MONTHS = {'fr': ['janvier','février','mars','avril','mai','juin','juillet','août','septembre','octobre','novembre','décembre'],
              'en': ['January','February','March','April','May','June','July','August','September','October','November','December']}
    def day_date(n):
        d = datetime.date(2027, 9, 18) + datetime.timedelta(days=n - 1)
        return f'{d.day} {MONTHS[L][d.month - 1]}' if L == 'fr' else f'{d.day} {MONTHS[L][d.month - 1]}'
    for k, (photo, dd) in enumerate(DAYS):
        n = k + 1; title, desc, stats = dd[L]
        strip.append(f'<div class="itin-row"><div class="itin-day">{t["dshort"]}{n}<small>{day_date(n)}</small></div><div><h4>{esc(title)}</h4><span>{esc(short(desc))}</span></div></div>')
        st = '\n'.join(f'            <div class="day-stat">{t["st"][key]} : <b>{esc(v)}</b></div>' if L == 'fr' else f'            <div class="day-stat">{t["st"][key]}: <b>{esc(v)}</b></div>' for key, v in stats)
        ph = f'\n        <div class="day-photo"><img loading="lazy" decoding="async" src="/images/photo-{photo:02d}.jpg?v=2" alt="{esc(alt[photo])}"></div>' if photo else ''
        style = '' if photo else ' style="grid-template-columns:1fr;"'
        cards.append(f'''      <div class="day-card"{style}>{ph}
        <div>
          <div class="day-num">{t["day"]} {n} · {day_date(n)}</div>
          <h3>{esc(title)}</h3>
          <p class="desc">{esc(desc)}</p>
          <div class="day-stats">
{st}
          </div>
        </div>
      </div>''')
    gallery = '\n'.join(f'        <figure><img loading="lazy" decoding="async" src="/images/photo-{n:02d}.jpg?v=2" alt="{esc(alt[n])}"><figcaption>{esc(alt[n])}</figcaption></figure>' for n in GALLERY)
    rows = lambda items: '\n'.join(f'            <div class="fee-row"><div class="fee-label">{a}</div><div class="fee-detail"><span>{b}</span></div></div>' for a, b in items)
    lis = lambda items: '\n'.join(f'            <li>{esc(x)}</li>' for x in items)
    switch = ('<span class="current">FR</span><a href="/en/" hreflang="en" lang="en">EN</a>' if L == 'fr'
              else '<a href="/" hreflang="fr" lang="fr">FR</a><span class="current">EN</span>')
    nav = '\n      '.join(f'<a href="{h}">{x}</a>' for h, x in t['nav'])
    ld = json.dumps({"@context": "https://schema.org", "@type": "TouristTrip", "name": t['h1'], "description": t['desc'],
                     "url": url, "image": B + "/images/photo-11.jpg?v=2", "inLanguage": L,
                     "touristType": ["Cycling groups", "Adventure travellers"],
                     "provider": {"@type": "TravelAgency", "name": "Lost Horizon", "email": "contact@lhassa-katmandou.com"},
                     "duration": "P20D",
                     "offers": {"@type": "Offer", "price": "4590", "priceCurrency": "EUR", "url": url + "#fee"}}, ensure_ascii=False, indent=2)
    return f'''<!DOCTYPE html>
<html lang="{L}" data-theme="dark">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{esc(t["title"])}</title>
<meta name="description" content="{esc(t["desc"])}">
<link rel="canonical" href="{url}">
<link rel="alternate" hreflang="fr" href="{B}/">
<link rel="alternate" hreflang="en" href="{B}/en/">
<link rel="alternate" hreflang="x-default" href="{B}/">
<link rel="icon" href="/favicon.svg?v=2" type="image/svg+xml">
<link rel="icon" href="/favicon.ico?v=2" sizes="any">
<link rel="icon" type="image/png" sizes="32x32" href="/favicon-32.png?v=2">
<link rel="apple-touch-icon" href="/apple-touch-icon.png?v=2">
<meta property="og:type" content="website">
<meta property="og:site_name" content="Lost Horizon">
<meta property="og:title" content="{esc(t["title"])}">
<meta property="og:description" content="{esc(t["desc"])}">
<meta property="og:url" content="{url}">
<meta property="og:image" content="{B}/images/photo-11.jpg?v=2">
<meta property="og:locale" content="{t["locale"]}">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="{esc(t["title"])}">
<meta name="twitter:description" content="{esc(t["desc"])}">
<meta name="twitter:image" content="{B}/images/photo-11.jpg?v=2">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Noto+Serif+SC:wght@500;700;900&amp;family=Noto+Sans+SC:wght@300;400;500;600;700&amp;family=Inter:wght@500;600&amp;display=swap">
<link rel="stylesheet" href="/styles.css?v=5">
<script type="application/ld+json">
{ld}
</script>
</head>
<body>

<header>
  <div class="nav">
    <a class="brandmark" href="{t["home"]}">
      <img src="/images/logo.png?v=2" alt="Lost Horizon">
      <span><b>Lost Horizon</b><span>{t["tagline"]}</span></span>
    </a>
    <nav class="nav-links">
      {nav}
    </nav>
    <div style="display:flex;align-items:center;gap:8px;">
      <div class="lang-switch">{switch}</div>
      <button class="theme-toggle" id="themeToggle" aria-label="{t["theme"]}">
        <svg id="themeIcon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8"><path d="M21 12.8A9 9 0 1 1 11.2 3a7 7 0 0 0 9.8 9.8Z"></path></svg>
      </button>
    </div>
  </div>
</header>

<main id="top">
  <div class="gallery" id="gallery">
    <div class="gallery-track" id="galleryTrack">
{carousel}
    </div>
    <div class="gallery-overlay">
      <span class="cap">{t["region"]}</span>
      <h1>{esc(t["h1"])}</h1>
      <p class="sub">{esc(t["sub"])}</p>
    </div>
    <div class="gallery-dots" id="galleryDots"></div>
  </div>
  <div class="trip-card-summary">
    <div class="summary-tag-row">
      <span class="tag">{t["region"]}</span>
      <span class="tag tag-navy">{t["dates_tag"]}</span>
    </div>
    <p class="summary-title">{esc(t["summary"])}</p>
    <div class="spec-box">
      <div class="trip-price">{t["price_big"]} <span>{t["price_unit"]}</span></div>
      <div class="meta-row">
        <span class="meta-item">{t["difficulty"]} <span class="star-rating" aria-label="{t["diff_aria"]}"><span class="star-bg">★★★★★</span><span class="star-fg" style="width:100%">★★★★★</span></span></span>
        <span class="meta-item">{esc(t["meeting"])}</span>
      </div>
      <div class="meta-item"><b style="color:var(--ink);font-weight:500;">{esc(t["next"])}</b></div>
      <div class="meta-item">{esc(t["season"])}</div>
    </div>
    <div class="cta-row">
      <a href="#contact" class="btn btn-dark">{esc(t["cta1"])}</a>
      <a href="#itinerary" class="btn btn-line">{esc(t["cta2"])}</a>
    </div>
  </div>

  <section id="highlights" style="padding-top:56px;">
    <div class="wrap-narrow">
      <div class="pillar-card" style="border-left:3px solid var(--gold);">
        <h3>{esc(t["groups_h"])}</h3>
        <p>{esc(t["groups_p"])}</p>
      </div>
      <div class="cap section-eyebrow" style="margin-top:32px;">{t["hl_cap"]}</div>
      <h2 class="section-title">{esc(t["hl_h"])}</h2>
{hls}
      <div class="pillar-card" style="margin-top:24px;border-left:3px solid var(--red);">
        <h3>{esc(t["alt_h"])}</h3>
        <p>{esc(t["alt_p"])}</p>
      </div>
    </div>
  </section>

  <section id="guide" style="padding-top:0;">
    <div class="wrap-narrow">
      <div class="cap section-eyebrow">{t["guide_cap"]}</div>
      <h2 class="section-title">{esc(t["guide_h"])}</h2>
      <div class="day-card" style="border-bottom:1px solid var(--border);">
        <div class="day-photo" style="aspect-ratio:233/329;"><img loading="lazy" decoding="async" src="/images/guide-axel.jpg?v=2" alt="{esc(t["guide_alt"])}" style="object-position:center top;"></div>
        <div>
          <div class="day-num">{esc(t["guide_role"])}</div>
          <h3>Axel</h3>
{guide_ps}
          <div class="day-stats">
{guide_stats}
          </div>
        </div>
      </div>
    </div>
  </section>

  <section id="photos">
    <div class="wrap-narrow">
      <div class="cap section-eyebrow">{t["gal_cap"]}</div>
      <h2 class="section-title">{esc(t["gal_h"])}</h2>
      <p style="color:var(--muted);font-size:16px;max-width:60ch;margin-bottom:22px;">{esc(t["gal_p"])}</p>
      <div class="photo-grid">
{gallery}
      </div>
    </div>
  </section>

  <section id="map">
    <div class="wrap-narrow">
      <div class="cap section-eyebrow">{t["route_cap"]}</div>
      <h2 class="section-title">{esc(t["route_h"])}</h2>
      <div class="map-photo map-photo-lg" style="background:#0D1420;padding:18px 14px 8px;">
{prof}
      </div>
      <p style="color:#9FADC2;font-size:13.5px;margin-top:10px;">{esc(t["profile_note"])}</p>
      <div class="itin-strip">
{chr(10).join(strip)}
      </div>
    </div>
  </section>

  <section id="itinerary">
    <div class="wrap-narrow">
      <div class="cap section-eyebrow">{t["dd_cap"]}</div>
      <h2 class="section-title">{esc(t["dd_h"])}</h2>
{chr(10).join(cards)}
    </div>
  </section>

  <section id="fee">
    <div class="wrap-narrow">
      <div class="cap section-eyebrow">{t["fee_cap"]}</div>
      <h2 class="section-title">{esc(t["fee_h"])}</h2>
      <div class="fee-box">
        <div class="fee-price">{t["price_line"]}</div>
        <div class="fee-table-wrap">
          <div class="fee-table-head">{t["inc"]}</div>
          <div class="fee-table">
{rows(t["included"])}
          </div>
        </div>
        <div class="fee-table-wrap">
          <div class="fee-table-head">{t["notinc"]}</div>
          <div class="fee-table">
{rows(t["excluded"])}
          </div>
        </div>
        <div class="fee-note">{esc(t["fee_note"])}</div>
      </div>
    </div>
  </section>

  <section id="terms" style="padding-top:0;">
    <div class="wrap-narrow">
      <div class="cap section-eyebrow">{t["terms_cap"]}</div>
      <h2 class="section-title">{esc(t["terms_h"])}</h2>
      <div class="fee-box">
        <div class="fee-table-wrap">
          <div class="fee-table-head">{esc(t["t1h"])}</div>
          <ul class="terms-list">
{lis(t["t1"])}
          </ul>
        </div>
        <div class="fee-table-wrap">
          <div class="fee-table-head">{esc(t["t2h"])}</div>
          <ul class="terms-list">
{lis(t["t2"])}
          </ul>
        </div>
      </div>
    </div>
  </section>

  <section id="contact">
    <div class="wrap-narrow">
      <div class="cap section-eyebrow">{t["c_cap"]}</div>
      <h2 class="section-title">{esc(t["c_h"])}</h2>
      <p style="color:var(--muted);font-size:16px;max-width:56ch;">{esc(t["c_p"])}</p>
      <p style="font-size:16px;margin:10px 0 18px;">{esc(t["team"])}</p>
      <div class="contact-list">
        <a class="c-row" href="tel:+33627297977">
          <span class="c-icon">{ICON_PHONE}</span>
          <span class="c-text"><b>{t["phone"]}{" :" if L == "fr" else ":"}</b> <span style="white-space:nowrap">+33 6 27 29 79 77</span></span>
        </a>
        <a class="c-row" href="mailto:contact@lhassa-katmandou.com">
          <span class="c-icon">{ICON_MAIL}</span>
          <span class="c-text"><b>{t["email"]}{" :" if L == "fr" else ":"}</b> contact@lhassa-katmandou.com</span>
        </a>
        <a class="c-row" href="https://registre-operateurs-de-voyages.atout-france.fr" target="_blank" rel="noopener" style="margin-top:2px;">
          <span class="c-icon">{ICON_SHIELD}</span>
          <span class="c-text"><b>{t["legal"]}{" :" if L == "fr" else ":"}</b> {t["legal_txt"]}</span>
        </a>
      </div>
    </div>
  </section>

</main>
<footer>{t["footer"]}</footer>

<script>
(function(){{
  var root = document.documentElement;
  var btn = document.getElementById('themeToggle');
  function applyIcon(){{
    var mode = root.getAttribute('data-theme');
    var isDark = mode === 'dark' || (!mode && window.matchMedia('(prefers-color-scheme: dark)').matches);
    var icon = document.getElementById('themeIcon');
    if(icon) icon.innerHTML = isDark
      ? '<path d="M21 12.8A9 9 0 1 1 11.2 3a7 7 0 0 0 9.8 9.8Z"/>'
      : '<circle cx="12" cy="12" r="4"/><path d="M12 2v2M12 20v2M4.9 4.9l1.4 1.4M17.7 17.7l1.4 1.4M2 12h2M20 12h2M4.9 19.1l1.4-1.4M17.7 6.3l1.4-1.4"/>';
  }}
  if(btn){{
    btn.addEventListener('click', function(){{
      var current = root.getAttribute('data-theme');
      var sysDark = window.matchMedia('(prefers-color-scheme: dark)').matches;
      var currentlyDark = current === 'dark' || (!current && sysDark);
      root.setAttribute('data-theme', currentlyDark ? 'light' : 'dark');
      applyIcon();
    }});
  }}
  applyIcon();

  var track = document.getElementById('galleryTrack');
  var dotsWrap = document.getElementById('galleryDots');
  if(track && dotsWrap){{
    var n = track.children.length;
    for(var i=0;i<n;i++){{
      var d = document.createElement('i');
      if(i===0) d.className='on';
      dotsWrap.appendChild(d);
    }}
    track.addEventListener('scroll', function(){{
      var idx = Math.round(track.scrollLeft / track.clientWidth);
      Array.prototype.forEach.call(dotsWrap.children, function(dot,i){{
        dot.className = i===idx ? 'on' : '';
      }});
    }});
  }}
}})();
</script>
</body>
</html>
'''

for L in ('fr', 'en'):
    open(os.path.join(R, T[L]['path'], 'index.html'), 'w', encoding='utf-8').write(page(L))
print("ok")
