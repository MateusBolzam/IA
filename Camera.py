import glob
import cv2
import os
import shutil
from Vgg1619 import indentificar


def webcam():
    # Verifica se a pasta "imagem" existe, e se não existir, a cria
    pasta_ia = "IA"
    if not os.path.exists(pasta_ia):
        os.makedirs(pasta_ia)

    # Cria uma subpasta dentro da pasta "IA" para as imagens, se não existir
    pasta_imagem = os.path.join(pasta_ia, "imagem")
    if not os.path.exists(pasta_imagem):
        os.makedirs(pasta_imagem)

    captura = cv2.VideoCapture(0)


    # Defina um contador para nomear os arquivos de imagem
    contador = 0                                                                                  

    while True:
        ret, frame = captura.read()
        cv2.imshow("Video", frame)
    
        k = cv2.waitKey(30) & 0xff
        # ESC para fechar o programa
        if k == 27:
            break
        elif k == ord('s'):  # Usar o S para salvar a imagem
            nome_arquivo = os.path.join(pasta_imagem, f"imagem_{contador}.jpg")
            cv2.imwrite(nome_arquivo, frame)
            print(f"Imagem salva como {nome_arquivo}")
            contador += 1

            # Move a imagem para a pasta "IA" após salvá-la
            novo_caminho = os.path.join(pasta_imagem, os.path.basename(nome_arquivo))
            shutil.move(nome_arquivo, novo_caminho)
            print(f"Imagem movida para {novo_caminho}")

            image_paths = sorted(glob.glob(f"{pasta_imagem}/*.jpg"))
            print(image_paths)
            
            indentificar(image_paths)

        elif k == ord('d'):  # Apaga as fotos na pasta
            for arquivo in os.scandir(pasta_imagem):
                if arquivo.is_file():
                    os.remove(arquivo.path)
            contador = 0        
        



    captura.release()
    cv2.destroyAllWindows()




    shutil.rmtree(pasta_imagem)