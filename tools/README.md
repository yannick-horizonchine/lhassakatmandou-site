# Outils (non servis sur le site : `/tools/*` redirige vers l'accueil)

- `build_site.py` — génère `index.html` (FR) et `en/index.html` (EN). `python3 tools/build_site.py`
  Toute modification de texte, de prix, de photo ou de jour de l'itinéraire se fait **dans ce script**, puis on régénère.
  Modifier directement les HTML serait écrasé à la prochaine régénération.
- `profile.svg` — profil d'altitude inséré dans les pages.

## Flouter les visages des clients (méthode, scripts non conservés)
OpenCV (`opencv-python-headless`) + modèle de détection YuNet
(`face_detection_yunet_2023mar.onnx`, dépôt opencv_zoo, à télécharger via l'URL « media.githubusercontent.com »).
Détection multi-échelles et en miroir (seuil ≈ 0,4–0,6), puis **vérification à l'œil photo par photo** : la détection
rate les profils et se trompe parfois (ciel, assiettes). Ne flouter que les clients (voir CLAUDE.md), jamais les habitants.
Après remplacement d'une photo : incrémenter `?v=N` dans le script.
