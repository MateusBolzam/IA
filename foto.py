import glob
import cv2
import os
import shutil
from Vgg1619 import indentificar 


def fotos():
    pasta_ia = "IA"
    if not os.path.exists(pasta_ia):
        os.makedirs(pasta_ia)

    # Cria uma subpasta dentro da pasta "IA" para as imagens, se não existir
    pasta_fotos = os.path.join(pasta_ia, "fotos")
    if not os.path.exists(pasta_fotos):
        os.makedirs(pasta_fotos)
    
    image_paths = sorted(glob.glob(f"{pasta_fotos}/*.*"))
    print(image_paths)

    indentificar(image_paths)
    
