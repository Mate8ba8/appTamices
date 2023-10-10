import base64


imagen_path = 'C:\\Users\\Mateo Bohorquez Angu\\Desktop\\Sin título.png'
with open(imagen_path, 'rb') as imagen_file:
    imagen_base64 = base64.b64encode(imagen_file.read()).decode('ascii')