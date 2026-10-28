# Outils (non servis sur le site : `/tools/*` redirige vers l'accueil)

Le script de génération des pages a été abandonné : `index.html` et `en/index.html` s'éditent directement.

## Flouter les visages des clients (méthode, scripts non conservés)
OpenCV (`opencv-python-headless`) + modèle de détection YuNet
(`face_detection_yunet_2023mar.onnx`, dépôt opencv_zoo, à télécharger via l'URL « media.githubusercontent.com »).
Détection multi-échelles et en miroir (seuil ≈ 0,4–0,6), puis **vérification à l'œil photo par photo** : la détection
rate les profils et se trompe parfois (ciel, assiettes). Ne flouter que les clients (voir CLAUDE.md), jamais les habitants.
Après remplacement d'une photo : incrémenter `?v=N` dans le script.
