from django.http import StreamingHttpResponse
from django.views.decorators import gzip
from django.http import HttpResponseServerError
from django.views.decorators.csrf import csrf_exempt
from django.views import View

import cv2
import threading
import time

# Parámetros de la cámara frontal
cam_id = 0
cam_width = 640
cam_height = 480

# Variable para almacenar el último fotograma
current_frame = None

# Función para obtener el último fotograma
def get_frame():
    global current_frame
    capture = cv2.VideoCapture(cam_id)
    capture.set(cv2.CAP_PROP_FRAME_WIDTH, cam_width)
    capture.set(cv2.CAP_PROP_FRAME_HEIGHT, cam_height)

    while True:
        ret, frame = capture.read()
        if not ret:
            # Manejar el caso de fallo en la captura
            print("Error al capturar el fotograma.")
            current_frame = None
            continue

        _, img_encoded = cv2.imencode('.jpg', frame)
        current_frame = img_encoded.tobytes()
        time.sleep(0.1)  # Ajusta la velocidad de c
# Inicia el hilo para la captura de video
video_thread = threading.Thread(target=get_frame)
video_thread.daemon = True

@csrf_exempt
@gzip.gzip_page
def Enlive(request):
    global video_thread

    if not video_thread.is_alive():
        # Inicia el hilo solo si no está en ejecución
        video_thread.start()

    return StreamingHttpResponse(video_stream(), content_type='multipart/x-mixed-replace; boundary=frame')

# Genera el contenido de video para transmitir
def video_stream():
    global current_frame
    while True:
        if current_frame is not None:
            yield (b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + current_frame + b'\r\n\r\n')
        else:
            # Manejar el caso en el que current_frame es None
            print("No hay fotograma disponible.")
            time.sleep(0.1)