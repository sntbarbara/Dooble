# -*- coding: utf-8 -*-
"""
Created on Sun Oct 08 18:27:52 2017

@author: ruiz-i
"""

import os
from PIL import ImageFont
from PIL import Image
from PIL import ImageDraw
import random

#Se define un diccionario con los indices de las 8 imagenes de las 55 tarjetas
#Los indices de las imagenes empezaban en 1 y no debe ser asi, asi que les resto 1.
informacion_tarjetas={0:[57-1,55-1,16-1,4-1,56-1,29-1,38-1,22-1]
,1:[2-1,5-1,44-1,33-1,56-1,20-1,15-1,52-1]
,2:[29-1,12-1,50-1,10-1,19-1,52-1,43-1,48-1]
,3:[8-1,34-1,18-1,52-1,7-1,46-1,38-1,1-1]
,4:[41-1,49-1,33-1,16-1,46-1,45-1,9-1,19-1]
,5:[1-1,21-1,11-1,41-1,29-1,20-1,13-1,28-1]
,6:[18-1,44-1,47-1,55-1,41-1,51-1,10-1,27-1]
,7:[22-1,6-1,17-1,46-1,27-1,43-1,20-1,53-1]
,8:[6-1,35-1,38-1,44-1,40-1,13-1,54-1,19-1]
,9:[46-1,37-1,42-1,23-1,29-1,26-1,44-1,3-1]
,10:[41-1,17-1,4-1,37-1,52-1,54-1,30-1,24-1]
,11:[38-1,41-1,31-1,26-1,5-1,53-1,50-1,14-1]
,12:[18-1,3-1,12-1,16-1,17-1,14-1,13-1,15-1]
,13:[19-1,2-1,1-1,3-1,53-1,39-1,55-1,30-1]
,14:[38-1,30-1,47-1,15-1,43-1,42-1,9-1,21-1]
,15:[51-1,4-1,43-1,14-1,1-1,33-1,40-1,23-1]
,16:[5-1,54-1,16-1,32-1,1-1,48-1,42-1,27-1]
,17:[7-1,3-1,32-1,35-1,41-1,56-1,36-1,43-1]
,18:[56-1,10-1,14-1,21-1,46-1,39-1,25-1,54-1]
,19:[40-1,10-1,36-1,34-1,16-1,26-1,30-1,20-1]
,20:[4-1,20-1,42-1,35-1,18-1,39-1,50-1,49-1]
,21:[54-1,31-1,23-1,12-1,7-1,9-1,20-1,55-1]
,22:[30-1,11-1,49-1,48-1,14-1,44-1,22-1,7-1]
,23:[35-1,11-1,23-1,25-1,52-1,53-1,16-1,47-1]
,24:[47-1,49-1,56-1,6-1,1-1,26-1,12-1,24-1]
,25:[33-1,3-1,22-1,54-1,34-1,50-1,28-1,47-1]
,26:[39-1,51-1,13-1,52-1,9-1,26-1,22-1,32-1]
,27:[40-1,17-1,39-1,7-1,5-1,47-1,29-1,45-1]
,28:[19-1,18-1,5-1,24-1,22-1,36-1,23-1,21-1]
,29:[7-1,26-1,25-1,19-1,4-1,15-1,27-1,28-1]
,30:[33-1,6-1,32-1,30-1,18-1,25-1,31-1,29-1]
,31:[9-1,35-1,29-1,24-1,2-1,14-1,34-1,27-1]
,32:[33-1,39-1,36-1,27-1,37-1,11-1,12-1,38-1]
,33:[25-1,12-1,40-1,41-1,22-1,2-1,42-1,8-1]
,34:[8-1,39-1,24-1,44-1,43-1,16-1,28-1,31-1]
,35:[22-1,45-1,31-1,10-1,15-1,35-1,1-1,37-1]
,36:[2-1,31-1,47-1,46-1,36-1,13-1,4-1,48-1]
,37:[10-1,2-1,38-1,32-1,28-1,17-1,49-1,23-1]
,38:[4-1,6-1,5-1,3-1,11-1,10-1,8-1,9-1]
,39:[16-1,51-1,6-1,2-1,37-1,50-1,21-1,7-1]
,40:[8-1,48-1,35-1,21-1,55-1,33-1,17-1,26-1]
,41:[8-1,36-1,51-1,15-1,29-1,49-1,54-1,53-1]
,42:[11-1,56-1,51-1,19-1,34-1,17-1,31-1,42-1]
,43:[25-1,49-1,55-1,34-1,43-1,5-1,37-1,13-1]
,44:[15-1,32-1,24-1,11-1,50-1,55-1,46-1,40-1]
,45:[36-1,14-1,42-1,6-1,52-1,55-1,28-1,45-1]
,46:[45-1,27-1,30-1,23-1,50-1,13-1,56-1,8-1]
,47:[40-1,28-1,56-1,48-1,53-1,9-1,37-1,18-1]
,48:[53-1,42-1,7-1,24-1,57-1,33-1,10-1,13-1]
,49:[47-1,8-1,19-1,57-1,32-1,20-1,37-1,14-1]
,50:[54-1,11-1,26-1,57-1,43-1,45-1,2-1,18-1]
,51:[57-1,27-1,52-1,3-1,31-1,49-1,40-1,21-1]
,52:[25-1,17-1,57-1,50-1,36-1,44-1,9-1,1-1]
,53:[35-1,30-1,57-1,28-1,12-1,5-1,51-1,46-1]
,54:[48-1,6-1,41-1,23-1,57-1,39-1,34-1,15-1]}

inputFolder='images'
outputFolder='tarjetas'

#Defino funcion para incializar el array de imagenes a partir de una carpeta y sus subcarpetas
#Es importante que el nombre de ninguna subcarpeta lleve puntos y que todos los archivos lleven 
def crearDiccionarioImagenes(folder):
    print 'crearDiccionarioImagenes'
    dict_images={}
    indice = 0
    for fileName in os.listdir(folder):
        if fileName.find('.') >= 0:
            print fileName
            dict_images[indice]=[fileName]
            indice=indice+1
        else:
            for subFolderFile in os.listdir(folder + '\\' + fileName):
                print fileName
                dict_images[indice]=[fileName + '\\' + subFolderFile]
                indice=indice+1
    return dict_images

def modificaImagen(ruta):
    print 'dameImagenRedimensionada'
    print ruta
    img = Image.open(ruta,'r')
    img=rotarImagen(img)
    img=makeWhiteTransparent(img)
    return img.resize(dameTamanoAleatorio(img.size), Image.ANTIALIAS)

def rotarImagen(img):
    #Creamos capa alpha
    img = img.convert('RGBA')
    rot = img.rotate(random.randint(0, 360), expand = 1)
    #Creamos imagen blanca del mismo tamanio que la rotada
    fff = Image.new('RGBA',rot.size, (255)*4)
    #Componemos ambas usando la alpha layer de rot como mascara
    return Image.composite(rot,fff,rot)
    
def dameTamanoAleatorio(size_original):
    random_num=random.randint(-100,30)
    #Con el if else mantenemos la proporcion
    return modificaTamanoProporcionalmente(size_original,random_num+330);

def modificaTamanoProporcionalmente(size_original, nuevo_mayor):
    if size_original[0] < size_original[1]:
        return (size_original[0]*nuevo_mayor/size_original[1],nuevo_mayor)
    else:
        return (nuevo_mayor,size_original[1]*nuevo_mayor/size_original[0]) 

def crearTarjeta(numeroTarjeta, diccionarioImagenes):
    print 'crearTarjeta'
    card =Image.new('RGBA', (1000,1000))
    #Cada tarjeta genera sus posiciones con cierta aleatoriedad
    posicionesStandard=generaPosicionesImagenesEnTarjeta()
    tamanioImagenes = [(0,0),(0,0),(0,0),(0,0),(0,0),(0,0),(0,0),(0,0)]
    random_num=75
    indice = 0
    for indice in range(0,8,1):
        indiceImagen=dameIndiceImagenDobble(numeroTarjeta,indice)
        imagenModificada = modificaImagen(inputFolder + '\\' + diccionarioImagenes[indiceImagen][0])
        tamanioImagenes[indice] = imagenModificada.size
        card.paste(imagenModificada,posicionesStandard[indice], imagenModificada)
    #card.save(outputFolder + '\\tarjeta%d.png' % (numeroTarjeta))
    return card

def dameIndiceImagenDobble(numeroTarjeta, posicionImagenEnTarjeta):
    print 'dameIndiceImagenDobble'
    return informacion_tarjetas.get(numeroTarjeta)[posicionImagenEnTarjeta]

def decidirPosicionImagen(posicionesStandard, indice, tamanioImagenes):
    #if random.randint(0,1) == 0 or indice == 0:
    if indice == 0:
        return posicionesStandard[indice]
    elif indice == 1:
        return (tamanioImagenes[0][0],0)
    elif indice == 2:
        return (0,mayor(tamanioImagenes[0][1],tamanioImagenes[1][1]))
    elif indice == 3:
        return (mayor(tamanioImagenes[0][0],tamanioImagenes[2][0]),mayor(tamanioImagenes[0][1],tamanioImagenes[1][1]))
    elif indice == 4:
        y = posicionesStandard[2][1]
        if random.randint(0,1) == 0:
            y = mayor(tamanioImagenes[0][1],tamanioImagenes[1][1])
        return (0,mayor(tamanioImagenes[2][1],tamanioImagenes[3][1])+y)
    elif indice == 5:
        y = posicionesStandard[2][1]
        if random.randint(0,1) == 0:
            y = mayor(tamanioImagenes[0][1],tamanioImagenes[1][1])
        return (mayor(tamanioImagenes[2][0],tamanioImagenes[4][0]),mayor(tamanioImagenes[2][1],tamanioImagenes[3][1])+y)
    elif indice == 6:
        y = posicionesStandard[4][1]
        if random.randint(0,1) == 0:
            y = mayor(tamanioImagenes[2][1],tamanioImagenes[3][1])+250
        return (0,mayor(tamanioImagenes[4][1],tamanioImagenes[5][1])+y)
    elif indice == 7:
        y = posicionesStandard[4][1]
        if random.randint(0,1) == 0:
            y = mayor(tamanioImagenes[2][1],tamanioImagenes[3][1])+250
        return (mayor(tamanioImagenes[4][0],tamanioImagenes[6][0]),mayor(tamanioImagenes[4][1],tamanioImagenes[5][1])+y)
    else:
        return posicionesStandard[indice]
    
def mayor(valor1, valor2):
    if valor1 > valor2:
        return valor1
    else:
        return valor2

def makeWhiteTransparent(img):
    pixdata = img.load()
    for y in xrange(img.size[1]):
        for x in xrange(img.size[0]):
            pixColor = pixdata[x, y][0]+pixdata[x, y][1]+pixdata[x, y][2]+pixdata[x, y][3]
            #if pixdata[x, y] == (255, 255, 255, 255):
            if pixColor > 970:
                pixdata[x, y] = (255, 255, 255, 0)
    return img

def makeWhiteTransparent2(img):
    datas = img.getdata()
    newData = []
    for item in datas:
        if item[0] == 255 and item[1] == 255 and item[2] == 255:
            newData.append((255, 255, 255, 0))
        else:
            newData.append(item)
    return img.putdata(newData)
    

#nueva idea: se hacen cartas normales, con posiciones maximas y tam maximo aleatoriamente mas pequeno.
#Se podra usar o su posicion estandar o la que sobre de la imagen anterior
def generaPosicionesImagenesEnTarjeta():
    print 'generaPosicionesImagenesEnTarjeta'
    random_num=30
    lista_posiciones = [(0+random.randint(0, random_num),0+random.randint(0, random_num))
            ,(330+random.randint(-random_num, random_num),0+random.randint(0, random_num))
            ,(660+random.randint(0, random_num),0+random.randint(0, random_num))
            ,(0+random.randint(0, random_num),330+random.randint(-random_num, random_num))
            ,(330+random.randint(0, random_num),330+random.randint(-random_num, random_num))
            ,(660+random.randint(-random_num, random_num),330+random.randint(-random_num, random_num))
            ,(0+random.randint(0, random_num),660+random.randint(-random_num, random_num))
            ,(330+random.randint(-random_num, random_num),660+random.randint(-random_num, random_num))
            ,(660+random.randint(-random_num, random_num),660+random.randint(-random_num, random_num))]
    #Borramos uno al azar ya que solo hay 8 figuras
    del lista_posiciones[random.randint(0,8)]
    return lista_posiciones

def generarLeyenda(diccionarioImagenes):
    print 'GenerarLeyenda'
    a4 =Image.new('RGBA', (2480,3508), (255, 255, 255,255))
    pos=(50,50)
    for imagen in diccionarioImagenes.keys():
        font = ImageFont.truetype("Arial.ttf",50)
        a4.paste(dameThumbNail(inputFolder + '\\' + diccionarioImagenes[imagen][0]),(pos[0],pos[1]+5))
        draw = ImageDraw.Draw(a4)
        text = dameNombreDelFicheroSinCarpetaNiExtension(diccionarioImagenes[imagen][0])
        draw.text((pos[0],pos[1]+210),text,(0,0,0),font=font)
        pos = actualizaPosicionLeyenda(pos)
    a4.save(outputFolder + '\\leyenda.png')

def dameNombreDelFicheroSinCarpetaNiExtension(nombre):
    text = nombre.split('.')
    text2 = text[0].split('\\')
    print text2
    if len(text2) == 2:
        return text2[1]
    else:
        return text2[0]
    
def actualizaPosicionLeyenda(pos):
    if pos[0] == 50:
        return (500,pos[1])
    elif pos[0] == 500:
        return (1000,pos[1])
    elif pos[0] == 1000:
        return (1500,pos[1])
    elif pos[0] == 1500:
        return (2000,pos[1])
    elif pos[0] == 2000:
        return (50,pos[1]+260)
       
def dameThumbNail(ruta):
    print 'dameThumbNail'
    img = Image.open(ruta,'r')
    return img.resize(modificaTamanoProporcionalmente(img.size,200), Image.ANTIALIAS)

def generarElJuegoDobble():
    print 'generarElJuegoDobble'
    dict_images = crearDiccionarioImagenes('images')
    generarLeyenda(dict_images)
    posicionesTarjetas = generaPosicionesTarjetasEnPagina()
    for pagina in range(0,60,6):
        a4 =Image.new('RGBA', (3508,2480), (255, 255, 255,255))
        for indice in range(1,7,1):
            if indice+pagina <= 54:
                card = crearTarjeta(indice+pagina,dict_images)
                a4.paste(card,posicionesTarjetas[indice-1])
        a4.save(outputFolder + '\\pagina%d.png' % (pagina))

def generaPosicionesTarjetasEnPagina():
    print 'generaPosicionesTarjetasEnPagina'
    y1 = 120
    y2 = 1240
    return [(120,y1),(1240,y1),(2360,y1),
            (120,y2),(1240,y2),(2360,y2)]

generarElJuegoDobble()





