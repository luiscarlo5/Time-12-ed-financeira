import math
import cv2
import time
import numpy as np

from skimage import restoration
##  Underwater Images Enhancement ##
from skimage.color import rgb2lab, lab2rgb
from skimage.color import rgb2hsv, hsv2rgb

def global_stretching(img_L, height, width):
    length = height * width
    R_rray = (np.copy(img_L)).flatten()
    R_rray.sort()
    # print('R_rray',R_rray)
    I_min = int(R_rray[int(length / 100)])
    I_max = int(R_rray[-int(length / 100)])
    # print('I_min',I_min)
    # print('I_max',I_max)
    array_Global_histogram_stretching_L = np.zeros((height, width))
    for i in range(0, height):
        for j in range(0, width):
            if img_L[i][j] < I_min:
                p_out = img_L[i][j]
                array_Global_histogram_stretching_L[i][j] = 0
            elif (img_L[i][j] > I_max):
                p_out = img_L[i][j]
                array_Global_histogram_stretching_L[i][j] = 100
            else:
                p_out = int((img_L[i][j] - I_min) * ((100) / (I_max - I_min)))
                array_Global_histogram_stretching_L[i][j] = p_out
    return (array_Global_histogram_stretching_L)

def global_Stretching_ab(a, height, width):
    array_Global_histogram_stretching_L = np.zeros((height, width), 'float64')
    for i in range(0, height):
        for j in range(0, width):
            p_out = a[i][j] * (1.3 ** (1 - math.fabs(a[i][j] / 128)))
            array_Global_histogram_stretching_L[i][j] = p_out
    return (array_Global_histogram_stretching_L)

def stretching(img):
    height = len(img)
    width = len(img[0])
    for k in range(0, 3):
        Max_channel = np.max(img[:, :, k])
        Min_channel = np.min(img[:, :, k])
        for i in range(height):
            for j in range(width):
                img[i, j, k] = (img[i, j, k] - Min_channel) * (255 - 0) / (Max_channel - Min_channel) + 0
    return img

def LABStretching(sceneRadiance):
    sceneRadiance = np.clip(sceneRadiance, 0, 255)
    sceneRadiance = np.uint8(sceneRadiance)
    height = len(sceneRadiance)
    width = len(sceneRadiance[0])
    img_lab = rgb2lab(sceneRadiance)
    L, a, b = cv2.split(img_lab)

    img_L_stretching = global_stretching(L, height, width)
    img_a_stretching = global_Stretching_ab(a, height, width)
    img_b_stretching = global_Stretching_ab(b, height, width)

    labArray = np.zeros((height, width, 3), 'float64')
    labArray[:, :, 0] = img_L_stretching
    labArray[:, :, 1] = img_a_stretching
    labArray[:, :, 2] = img_b_stretching
    img_rgb = lab2rgb(labArray) * 255

    return img_rgb


# RGHS
def rghs(img):
    height = len(img)
    width = len(img[0])
    # sceneRadiance = RGB_equalisation(img)

    sceneRadiance = img
    # sceneRadiance = RelativeGHstretching(sceneRadiance, height, width)
    sceneStretched = stretching(sceneRadiance)
    imgRadiance = LABStretching(sceneStretched).astype(np.uint8)

    return imgRadiance

#Equalização do histograma:
def equalizacao_do_histograma(img):

    # Convertendo a imagem para YUV
    img_to_yuv = cv2.cvtColor(img, cv2.COLOR_BGR2YUV)
    # Aplicando equalização do histograma
    img_to_yuv[:, :, 0] = cv2.equalizeHist(img_to_yuv[:, :, 0])
    # Convertendo para escala BGR
    equalizado = cv2.cvtColor(img_to_yuv, cv2.COLOR_YUV2BGR)
    return equalizado

#Correção de gama
def correcao_de_gama15(img):
    img = img/255.0
    img = cv2.pow(img,1.5)
    return img

def correcao_de_gama05(img):
    img = img/255.0
    img = cv2.pow(img,0.5)
    return img

def correcao_de_gama_especial(img):
    img = equalizacao_do_histograma(img)
    img = img/255.0
    img = cv2.pow(img,3.8)
    img = cv2.normalize(img, None, 0, 255, cv2.NORM_MINMAX)
    return img

# Wavelet
def wavelet(img1):
    return restoration.denoise_wavelet(img1, mode="soft", rescale_sigma=True, channel_axis=-1)

# Muitas imagens
def imgs_eh(imgs):
  imgs_eh = []
  tempo_eh = []

  for img in imgs:
    inicio = time.time()
    img_apri = equalizacao_do_histograma(img)
    fim = time.time()
    tempo = fim-inicio
    tempo = round(tempo,2)
    tempo_eh.append(tempo)
    imgs_eh.append(img_apri)
  
  return imgs_eh, tempo_eh

def imgs_eh_cg(imgs):
  imgs_eh_cg38 = []
  tempo_eh_cg38 = []


  for img in imgs:
    inicio = time.time()
    img_apri = correcao_de_gama_especial(img)
    img_apri =  cv2.normalize(img_apri, None, 0, 255, cv2.NORM_MINMAX)
    fim = time.time()
    tempo = fim-inicio
    tempo = round(tempo,2)
    tempo_eh_cg38.append(tempo)
    imgs_eh_cg38.append(img_apri)

  return imgs_eh_cg38, tempo_eh_cg38

def imgs_cg15(imgs):
  imgs_cg15 = []
  tempo_cg15 = []

  for img in imgs:
    inicio = time.time()
    img_apri = correcao_de_gama15(img)
    img_apri =  cv2.normalize(img_apri, None, 0, 255, cv2.NORM_MINMAX)
    fim = time.time()
    tempo = fim-inicio
    tempo = round(tempo,2)
    tempo_cg15.append(tempo)
    imgs_cg15.append(img_apri)

  return imgs_cg15, tempo_cg15

def imgs_cg05(imgs):
  imgs_cg05 = []
  tempo_cg05 = []

  for img in imgs:
    #img = np.array(img1)
    inicio = time.time()
    img_apri = correcao_de_gama05(img)
    img_apri =  cv2.normalize(img_apri, None, 0, 255, cv2.NORM_MINMAX)
    fim = time.time()
    tempo = fim-inicio
    tempo = round(tempo,2)
    tempo_cg05.append(tempo)
    imgs_cg05.append(img_apri)
  return imgs_cg05, tempo_cg05

def imgs_wavelet(imgs):
  imgs_wavelet = []
  tempo_wavelet = []

  for img in imgs:
    inicio = time.time()
    img_apri = wavelet(img)
    img_apri =  cv2.normalize(img_apri, None, 0, 255, cv2.NORM_MINMAX)
    fim = time.time()
    tempo = fim-inicio
    tempo = round(tempo,2)
    tempo_wavelet.append(tempo)
    imgs_wavelet.append(img_apri)
  
  return imgs_wavelet, tempo_wavelet

def imgs_rghs(imgs):
  imgs_rghs = []
  tempo_rghs = []

  for img in imgs:
    inicio = time.time()
    img_apri = rghs(img)
    fim = time.time()
    tempo = fim-inicio
    tempo = round(tempo,2)
    tempo_rghs.append(tempo)
    imgs_rghs.append(img_apri)
  return imgs_rghs, tempo_rghs 




