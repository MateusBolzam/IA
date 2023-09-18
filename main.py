
from Camera import webcam
from foto import fotos


while True:
    numero = 0
    while numero == 0:
        print("Voce quer usar a Webcam ou uma foto Propria")
        numero = int(input("Digite 1 para Webcam ou 2 para Foto Propria: "))
        
        if numero == 1:
            webcam()
        elif numero == 2:
            fotos()
        
        elif numero == 9:
            break
        
        else:
            numero = 0

    break  
        