# Lhassa–Katmandou à vélo — site web

Ce dépôt contient le site lhassa-katmandou.com (marque Lost Horizon / China Lost Horizon), déployé sur **Cloudflare Pages**.

## Règles de travail

- Modifier les fichiers **directement dans ce dépôt** (pas de fichiers à copier-coller à la main).
- Chaque changement est commité puis poussé ; Cloudflare Pages redéploie à partir de la branche `main`.
- Garder le site compatible avec Cloudflare Pages (fichiers statiques, ou build dont le dossier de sortie est configuré dans Pages).

## Structure

Site statique, sans étape de build — dans Cloudflare Pages : *Build command* vide, *Build output directory* `/`.

- `index.html` — page **française** (langue par défaut, `x-default`)
- `en/index.html` — version anglaise
- `styles.css` — feuille de style commune (reprise de la page d'origine sur horizonchine.com/chinalosthorizon)
- `images/` — `photo-01.jpg` à `photo-37.jpg` (chacune utilisée **une seule fois** sur la page), `logo.png` (Lost Horizon), QR codes WeChat et WhatsApp ; `favicon*`, `apple-touch-icon.png`, `icon-192.png` — icônes (Everest et drapeaux de prière)
- `404.html`, `en/404.html` — pages « introuvable » (chemins absolus obligatoires)
- `sitemap.xml`, `robots.txt` — SEO
- `_redirects` — redirige `/CLAUDE.md` et `/README.md` vers l'accueil pour ne pas les exposer

## Contenu

- Tarif : **4 500 € par personne** (résumé, section « Inclus » et `offers` du JSON-LD, dans les 2 langues).
- Édition 2027 : **du 19 septembre au 10 octobre 2027** (résumé, sous-titre, section « Inclus », meta description).
- Groupe : cyclistes de plusieurs clubs francophones (France, Belgique, Suisse, Québec) inscrits **à titre individuel** — ne plus parler de « groupes constitués ». Ne pas mentionner le Club des Cent Cols.
- Chiffres clés : une douzaine de jours de vélo, **une dizaine de cols** à plus de 4 000 m (dont plusieurs à plus de 5 000 m — ne pas donner de nombre exact), **environ 9 000 m** de dénivelé, train du Tibet ~22 h.
- Durée annoncée : **20 jours / 19 nuits** (titre, JSON-LD), choix du propriétaire.
- Contact : téléphone de Mathieu Le Serre +33 6 27 29 79 77, e-mail info@chinalosthorizon.com, QR codes WeChat et WhatsApp.
- Itinéraire jour par jour (20 jours) : rendez-vous à **Xining** (J1), fin à **Katmandou** (J20). Les vols internationaux ne sont **pas** inclus.
- Toute modification de contenu doit être reportée dans les 2 langues (FR et EN), y compris le résumé jour par jour du profil d'altitude, les balises `canonical`, `hreflang`, Open Graph/Twitter et le JSON-LD de l'en-tête.
- **Visages floutés** sur toutes les photos où ils sont reconnaissables (voyageurs, moines, passants), sauf `photo-28.jpg` (cycliste poing levé, accord du propriétaire). Toute nouvelle photo avec des visages nets doit être floutée avant d'être ajoutée. Les maillots « Club des Cent Cols » visibles sur les photos ne posent pas de problème.
- Galerie « Le groupe 2026 » (section `#photos`).
- Images en `loading="lazy"`, sauf celles du carrousel d'en-tête (la première en `fetchpriority="high"`).
- Pas de formulaire : contact par e-mail (info@chinalosthorizon.com), WeChat et WhatsApp (QR codes).
