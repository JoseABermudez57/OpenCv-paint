import cv2
import numpy as np

ventana = 'Paint UP'
img = 255*np.ones((600, 800, 3), dtype = np.uint8)
temporal = img.copy()
color = (0, 0, 0)
figura = 'circulo'
bandera = True
activar = False

cv2.namedWindow(ventana)


def get_radious(x1, y1, x2, y2):
    return np.sqrt((x2-x1)**2 + (y2-y1)**2)

def dibujar_interfaz():
    cv2.rectangle(img, (20, 20), (90, 70), (0, 0, 0), 3) # Borde del color rojo
    cv2.rectangle(img, (20, 20), (90, 70), (0, 0, 255), -1)

    cv2.rectangle(img, (20, 80), (90, 130), (0, 0, 0), 3) # Borde del color azul
    cv2.rectangle(img, (20, 80), (90, 130), (255, 0, 0), -1)

    cv2.rectangle(img, (20, 140), (90, 190), (0, 0, 0), 3)  # Borde del color verde
    cv2.rectangle(img, (20, 140), (90, 190), (0, 255, 0), -1)

    cv2.rectangle(img, (20, 200), (90, 250), (0, 0, 0), 3) # Borde del color negro
    cv2.rectangle(img, (20, 200), (90, 250), (0, 0, 0), -1)

    cv2.rectangle(img, (20, 260), (90, 310), (0, 0, 0), 3) # Boton de circulo
    cv2.rectangle(img, (20, 260), (90, 310), (255, 255, 255), -1)
    cv2.circle(img, (55, 285), 20, (0, 0, 0), 2)

    cv2.rectangle(img, (20, 320), (90, 370), (0, 0, 0), 3) # Boton de rectangulo
    cv2.rectangle(img, (20, 320), (90, 370), (255, 255, 255), -1)
    cv2.rectangle(img, (35, 330), (75, 360), (0, 0, 0), 2)

    cv2.rectangle(img, (20, 380), (90, 430), (0, 0, 0), 3) # Boton de linea
    cv2.rectangle(img, (20, 380), (90, 430), (255, 255, 255), -1)
    cv2.line(img, (35, 390), (75, 420), (0, 0, 0), 2)

    cv2.rectangle(img, (20, 440), (90, 490), (0, 0, 0), 3) # Boton de limpiar dibujos
    cv2.rectangle(img, (20, 440), (90, 490), (255, 255, 255), -1)
    cv2.rectangle(img, (35, 450), (75, 480), (0, 0, 0), 3) # Boton de rectangulo
    cv2.rectangle(img, (35, 450), (75, 480), (193, 193, 255), -1)
    cv2.rectangle(img, (60, 450), (75, 480), (255, 255, 255), -1)


def dibujar(evento, x, y, banderas, params):
    global x1, x2, y1, y2, ix, iy, img, activar, radious, color, figura

    if evento == cv2.EVENT_LBUTTONDOWN:
        activar = True
        x1, y1 = x, y
        ix, iy = x, y
        
        temporal = img.copy()
        if x > 20 and x < 90 and y > 20 and y < 70:
            activar = False
            color = (0, 0, 255)
        if x > 20 and x < 90 and y > 80 and y < 130:
            activar = False
            color = (255, 0, 0)
        if x > 20 and x < 90 and y > 140 and y < 190:
            activar = False
            color = (0, 255, 0)
        if x > 20 and x < 90 and y > 200 and y < 250:
            activar = False
            color = (0, 0, 0)
        if x > 20 and x < 90 and y > 260 and y < 310:
            activar = False
            figura = 'circulo'
        if x > 20 and x < 90 and y > 320 and y < 370:
            activar = False
            figura = 'rectangulo'
        if x > 20 and x < 90 and y > 380 and y < 430:
            activar = False
            figura = 'linea'
        if x > 20 and x < 90 and y > 440 and y < 490:
            activar = False
            img = 255*np.ones((600, 800, 3), dtype = np.uint8)
    if evento == cv2.EVENT_MOUSEMOVE:
        x2, y2, = x, y
        if activar:
            radious = get_radious(x1, y1, x2, y2)
            temporal = img.copy()
            if figura == 'circulo':
                cv2.circle(temporal, (x1, y1), int(radious), color, 2)
            if figura == 'rectangulo':
                cv2.rectangle(temporal, (x1, y1), (x, y), color, 2)
            if figura == 'linea':
                cv2.line(img, (ix, iy), (x, y), color, thickness=2, lineType=cv2.LINE_AA)
                ix, iy = x, y
            cv2.imshow(ventana, temporal)
    if evento == cv2.EVENT_LBUTTONUP:
        x2, y2, = x, y
        if activar:
            if figura == 'circulo':
                img = cv2.circle(img, (x1, y1), int(radious), color, 2)
            if figura == 'rectangulo':
                img = cv2.rectangle(img, (x1, y1), (x, y), color, 2)
            if figura == 'linea':
                cv2.line(img, (ix, iy), (x, y), color, thickness=2, lineType=cv2.LINE_AA)
        cv2.imshow(ventana, img)
        activar = False

cv2.setMouseCallback(ventana, dibujar)

while bandera:
    dibujar_interfaz()
    key = cv2.waitKey(10) & 0xFF
    if key == 27:
        break
cv2.destroyAllWindows()