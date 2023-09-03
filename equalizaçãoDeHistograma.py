# Importa as bibliotecas necessárias
import cv2  # OpenCV para manipulação de imagem
import matplotlib.pyplot as plt  # Matplotlib para exibição de gráficos
import math  # Biblioteca Math para operações matemáticas

# Carrega a imagem de entrada
input_image = cv2.imread('/content/photo2.jpg')

# Inicializa três listas para processamento do histograma
cores = [0] * 256  # Lista para contar a ocorrência de cada intensidade de cinza
coresNovas = [0] * 256  # Lista para armazenar as novas intensidades após a equalização
aux = [0] * 256  # Lista auxiliar para mapear as intensidades de cinza

# Inicializa a lista auxiliar para mapear intensidades de cinza de 0 a 255
for i in range(0, 256):
    aux[i] = i

# Loop aninhado para calcular o histograma da imagem original
for i in range(0, 492):
    for j in range(0, 492):
        (b, g, r) = imput_image[j, i]
        cores[b] = cores[b] + 1

# Calcula o número de tons de cinza diferentes na imagem
gDeCinza = 0
for i in range(0, 256):
    if cores[i] > 0:
        gDeCinza += 1

print(gDeCinza)

# Calcula a intensidade média de cinza e ajusta as novas intensidades de cinza
iDeCinza = (492 * 492) / gDeCinza
auxCor = 0
for i in range(0, 256):
    if cores[i] > 0:
        auxCor += cores[i]
        if (auxCor // iDeCinza) - 1 > 0:
            coresNovas[i] = (auxCor // iDeCinza) - 1

# Atualiza a imagem original com as novas intensidades de cinza
for i in range(0, 492):
    for j in range(0, 492):
        (b, g, r) = imput_image[j, i]
        if b > 0:
            imput_image[j, i] = (coresNovas[b], coresNovas[b], coresNovas[b])

# Exibe o histograma da imagem original
plt.bar(aux, cores)
plt.suptitle("Antiga")
plt.show()

# Calcula o histograma da imagem após a equalização e o exibe
instoNovo = [0] * 256
for i in range(0, 492):
    for j in range(0, 492):
        (b, g, r) = imput_image[j, i]
        instoNovo[b] = instoNovo[b] + 1

plt.bar(aux, instoNovo)
plt.suptitle("Nova")
plt.show()

# Exibe a imagem após a equalização
plt.imshow(imput_image)
