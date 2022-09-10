import cv2
import pickle
# o pacote pickle vai ser usado para salvar as posições das vagas.


img = cv2.imread('carParkImg.png')

width, height = 107,48

#verifica se já existe vagas cadastradas.
try:
    with open('CarParkPos','rb') as f:
        posList = pickle.load(f)
except:
    posList = []


#Ao clicar o mouse esquerdo será salvo as posições na lista posList[] e no mouse direito será escluido
def mouseClick(events, x,y,flags,params):
    if events == cv2.EVENT_LBUTTONDOWN:
        posList.append((x,y))
    if events == cv2.EVENT_RBUTTONDOWN:
        for i,pos, in enumerate(posList):
            x1,y1 = pos
            if x1<x<x1+width and y1<y<y1+height:
                posList.pop(i)
    with open('CarParkPos','wb') as f:
        pickle.dump(posList,f)


while True :
    # Decobrindo o tamanho da vaga.
    #cv2.rectangle(img,(50,192),(158,240),(255,0,255),2)
    img = cv2.imread('carParkImg.png')

    #show position in image
    for pos in posList:
        cv2.rectangle(img,pos, (pos[0]+width,pos[1]+height), (255, 0, 255), 2)
    #show image
    cv2.imshow("Image",img)
    cv2.setMouseCallback("Image",mouseClick)
    cv2.waitKey(1)


