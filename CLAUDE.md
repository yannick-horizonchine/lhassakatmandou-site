# Lhassa–Katmandou à vélo — site web

Ce dépôt contient le site lhassa-katmandou.com (marque **Lost Horizon** — l'agence s'appelle « Lost Horizon », sans « China »), déployé sur **Cloudflare Pages**.

## Règles de travail

- Ce site relève de Lost Horizon (offre B2B en Chine). Il est distinct de Yunnan Belenos (activités personnelles du propriétaire) et de Horizon Trekking (séjours Europe et Afrique du Nord pour clients sinophones) : ne jamais mélanger leurs contenus, marques ou dépôts.
- Modifier les fichiers **directement dans ce dépôt** (pas de fichiers à copier-coller à la main).
- Chaque changement est commité puis poussé ; Cloudflare Pages redéploie à partir de la branche `main`.
- Garder le site compatible avec Cloudflare Pages (fichiers statiques, ou build dont le dossier de sortie est configuré dans Pages).

## Structure

Site statique, sans étape de build — dans Cloudflare Pages : *Build command* vide, *Build output directory* `/`.

- 📌 **À RAPPELER AU PROPRIÉTAIRE** : une fois les dates définitives appliquées et le site finalisé, lui proposer d'**abandonner le script** `tools/build_site.py` (il l'a demandé). Concrètement : vérifier que la régénération ne change rien, supprimer `tools/build_site.py` (et `tools/profile.svg` si inutile), retirer cette consigne et celles sur le script de ce fichier, et éditer ensuite `index.html` et `en/index.html` directement, dans les 2 langues. Dès que le propriétaire annonce les dates définitives, le rappeler après les avoir mises à jour.
- ⚠️ `index.html` et `en/index.html` sont **générés** par `python3 tools/build_site.py` : modifier les textes, prix, photos et jours **dans `tools/build_site.py`**, puis régénérer (une édition directe des HTML serait écrasée). Voir `tools/README.md`.
- `index.html` — page **française** (langue par défaut, `x-default`)
- `en/index.html` — version anglaise
- `styles.css` — feuille de style commune (reprise de la page d'origine sur horizonchine.com/chinalosthorizon)
- `images/` — `photo-01.jpg` à `photo-37.jpg` (chacune utilisée **une seule fois** sur la page), `logo.png` (logo « LOST HORIZON » : montagne + texte, dérivé du logo Horizon Trekking sans le chinois ; liens en `?v=2`) ; `favicon*`, `apple-touch-icon.png`, `icon-192.png` — icônes (identiques à celles de horizontrekking.com ; liens en `?v=2`)
- `404.html`, `en/404.html` — pages « introuvable » (chemins absolus obligatoires)
- `sitemap.xml`, `robots.txt` — SEO
- `_redirects` — redirige `/CLAUDE.md`, `/README.md` et `/tools/*` vers l'accueil pour ne pas les exposer

## Contenu

- Tarif : **4 590 € par personne** (résumé, section « Inclus » et `offers` du JSON-LD, dans les 2 langues).
- Édition 2027 : **du 18 septembre au 7 octobre 2027** (résumé, sous-titre, section « Inclus », meta description). ⚠️ Dates **provisoires** : le propriétaire confirmera les dates définitives ; les mettre alors à jour partout (FR + EN, y compris la meta description), et vérifier la cohérence avec la durée de 20 jours. L'e-mail aux clubs partira après. Contrainte de dates : avoir passé le camp de base de l'Everest (Rongbuk, jour 13) avant les vacances nationales chinoises (semaine du 1er au 7 octobre) pour éviter la foule ; avec un départ le 18 septembre, Rongbuk tombe le 30 septembre.
- Groupe : cyclistes de plusieurs clubs francophones (France, Belgique, Suisse, Québec) inscrits **à titre individuel** — ne plus parler de « groupes constitués ». Ne pas mentionner le Club des Cent Cols.
- Chiffres clés : une douzaine de jours de vélo, **une dizaine de cols** à plus de 4 000 m (dont plusieurs à plus de 5 000 m — ne pas donner de nombre exact), **environ 9 000 m** de dénivelé, train du Tibet ~22 h.
- Durée annoncée : **20 jours / 19 nuits** (titre, JSON-LD), choix du propriétaire.
- Contact : téléphone de Mathieu Le Serre +33 6 27 29 79 77, e-mail contact@lhassa-katmandou.com. Pas de WeChat ni WhatsApp sur ce site.
- Itinéraire jour par jour (20 jours) : rendez-vous à **Xining** (J1), fin à **Katmandou** (J20). Les vols internationaux ne sont **pas** inclus.
- Toute modification de contenu doit être reportée dans les 2 langues (FR et EN), y compris le résumé jour par jour du profil d'altitude, les balises `canonical`, `hreflang`, Open Graph/Twitter et le JSON-LD de l'en-tête.
- **Visages floutés : uniquement nos clients** (voyageurs étrangers d'environ 65-80 ans), quand leur visage est reconnaissable. Ne **pas** flouter les pèlerins, moines, habitants, passants, personnel (train, magasins), le guide local ni l'équipe Lost Horizon. Exception : `photo-28.jpg` (notre guide, poing levé) reste net. Les maillots « Club des Cent Cols » ne posent pas de problème.
- Galerie « Le groupe 2026 » (section `#photos`).
- Guide Axel (section `#guide`, photo `images/guide-axel.jpg`) ; le caisson hyperbare PAC suit l'équipe ; Axel a la formation de secourisme de l'Ifremmont.
- Après tout remplacement d'une photo existante, incrémenter le `?v=N` des URL d'images (sinon navigateurs et Cloudflare réaffichent l'ancienne version). `_headers` limite le cache des images à 1 jour.
- Images en `loading="lazy"`, sauf celles du carrousel d'en-tête (la première en `fetchpriority="high"`).
- Pas de formulaire : contact par téléphone et e-mail uniquement.
