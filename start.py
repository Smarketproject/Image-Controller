import requests
import sys
sys.path.append('/usr/local/lib/python2.7/site-packages')
import cv2
import numpy as np
from os import listdir
from os.path import isfile, join

def analyze():

    img_rgb = cv2.imread('/home/alpha_lion/Programas/PY/teste.jpg')
    img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)
    threshold = 0.67

    product_list = ['diamante_negro', 'lolo', 'soda', 'suco'] #vem por GET
    for product in product_list:
        directory_path = "/home/alpha_lion/Programas/PY/{}_templates/".format(product)
        is_recognized = False
        list_templates = [f for f in listdir(directory_path) if isfile(join(directory_path, f))]
        
        for templates in list_templates:
            print("{}{}".format(directory_path, templates)) 
            template = cv2.imread("{}{}".format(directory_path, templates),0)
            w, h = template.shape[::-1]
            res = cv2.matchTemplate(img_gray,template,cv2.TM_CCOEFF_NORMED)
            loc = np.where( res >= threshold)
            list_matches = zip(*loc[::-1])
            if len(list_matches) > 0:
                is_recognized = True
                break
       
        if is_recognized == False:
        #Some product has problem
            break

   # print (is_recognized) #retornar o booleano POST
    return is_recognized


def make_list(content):
    l = []
    for item in content:
        l.append(item.name)
    return l

while True:
    result = requests.get('https://homol.redes.unb.br/ptr022017B/carrinho/produto').json()
    result = list(result)
    if len(result) > 0:
        r = requests.post('https://homol.redes.unb.br/ptr022017B/validacao', data = {'validator': analyze()})
    time.sleep(2)


    


