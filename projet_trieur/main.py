"""
Trier les fichiers contenus dans le dossier data selon les associations suivantes :
mp3, wav, flac : Musique
avi, mp4, gif : Videos
bmp, png, jpg : Images
txt, pptx, csv, xls, odp, pages : Documents
autres : Divers
"""
from pathlib import Path

dirs = {".png": "Images",
        ".bmp": "Images",
        ".jpg": "Images",
        ".gif": "Images",
        ".mp4": "Videos",
        ".mov": "Videos",
        ".avi": "Videos",
        ".zip": "Archives",
        ".pptx": "Documents",
        ".csv": "Documents",
        ".xls": "Documents",
        ".odp": "Documents",
        ".pages": "Documents",
        ".txt": "Documents",
        ".mp3": "Musiques",
        ".wav": "Musique",
        ".flac": "Musique"}

tri_dir = Path.home() / "C:/Users/Pavel/Desktop/formation_python/projet_trieur/data"
files = [f for f in tri_dir.iterdir() if f.is_file()]
for f in files:
    output_dir = tri_dir / dirs.get(f.suffix, "Autres")
    output_dir.mkdir(exist_ok=True)
    f.rename(output_dir / f.name)