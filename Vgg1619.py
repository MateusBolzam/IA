

from skimage import io
import matplotlib.pyplot as plt
import tensorflow as tf
from PIL import Image
import glob as glob



def indentificar(imagem):
    #aqui estou inicializando o modelo pre treinado vgg16
    model_vgg16 = tf.keras.applications.vgg16.VGG16()
    model_vgg19 = tf.keras.applications.vgg19.VGG19()

    print(model_vgg19.input_shape)

    print(model_vgg16.input_shape)

    #aqui estou usando a função glob para encontrar todos os aquivos com .png dentro
    # do arquivos do colab, alem que o sorted serve apenas para organizalos em ordem alfaberica.

    #aqui estou apenas mostrando as imagens, esta num for pq iniciamente era 4 imagens que eu estava passando
   
    for image_path in imagem:
        img = Image.open(image_path)
        plt.imshow(img)
        plt.axis('off')  # Opcional: para remover as coordenadas do eixo
        plt.show()
    


    def process_single_image(model, imagem, size, preprocess_input,nome = "modelo"):

        # Lendo as Imagens Usando o TensorFlow, transformando em uma sequência de bytes
        tf_image = tf.io.read_file(imagem)

        # Aqui pegamos essa sequência e a transformamos em um número que representa a imagem
        decoded_image = tf.image.decode_image(tf_image)

        # Aqui pegamos e redimensionamos a imagem para o tamanho desejado
        image_resized = tf.image.resize(decoded_image, size)

        # Pelo que entendi aqui colocamos nossa imagem em um lote, que é comum mesmo quando é uma única imagem
        # mas mesmo sendo apenas 1 imagem, a colocamos em um lote de tamanho 1.
        image_batch = tf.expand_dims(image_resized, axis=0)

        # Aqui estamos preparando a imagem para o modelo, aplicando o pré-processamento adequado.
        image_batch = preprocess_input(image_batch)

        # Aqui passamos finalmente nossa imagem para o modelo.
        preds = model.predict(image_batch)

        # Aqui decodificamos as previsões em uma lista de tuplas contendo as 5 melhores previsões.
        decoded_preds = tf.keras.applications.imagenet_utils.decode_predictions(
            preds=preds,
            top=5
        )

        # Aqui é apenas para imprimir os resultados
        plt.imshow(decoded_image)
        plt.axis('off')
        label = decoded_preds[0][0][1]
        score = decoded_preds[0][0][2] * 100
        
        
        if score < 40:
            print("Infelizmente nao tenho uma raça certa para esse animal...")
        else:
            title = label + ' ' + str('{:.2f}%'.format(score))
            plt.title(title, fontsize=16)
            plt.show()
            
            print(nome)
            #print(f"{label}: {round(score, 2)}%")
        

    # Aqui você declara qual é o seu modelo, no caso o VGG19, e que quer os tamanhos 224x224.
    model = model_vgg19  # Alterado para usar o VGG19
    size = (224, 224)
    modelName = "modelo vgg19"

    # Esta função é do VGG19 e especifica as normalizações que o modelo requer.
    preprocess_input = tf.keras.applications.vgg19.preprocess_input

    # Aqui você executa a função para processar cada imagem.
    for image_path in imagem:
        process_single_image(model, image_path, size, preprocess_input,modelName)

    #aqui declaro qual e meu modelo no caso o VGG16 e que quero os tamnhos 224,224.
    model = model_vgg16
    size = (224, 224)
    modelName = "modelo vgg16"

    #essa aqui e uma função do vgg16 que espesifica as normalizações que o modelo pede.
    preprocess_input = tf.keras.applications.vgg16.preprocess_input

    #aqui so executo a função.
    for image_path in imagem:
        process_single_image(model, image_path, size, preprocess_input,modelName)