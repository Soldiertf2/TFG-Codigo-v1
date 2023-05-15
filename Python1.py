# Importamos la libreria Pandas para importar el csv
import pandas
datos = pandas.read_csv('animales.csv')
animal = None

while not animal:
# creamos una variable para que nos muestre solo las preguntas o encabezados
    preguntas = list(datos.columns[1:].values)
    respuesta = []

    for pregunta in preguntas:
        respuesta.append(datos[pregunta].sum())

    siguiente_pregunta = preguntas[respuesta.index(max(respuesta))]
    tipo_respuesta = input(f'{siguiente_pregunta} (S: Si / N: No / NS: NO SE)')

    if tipo_respuesta == 'S':
        datos = datos[datos[siguiente_pregunta] == 1].drop(columns=[siguiente_pregunta])
    elif tipo_respuesta == 'N':
        datos = datos[datos[siguiente_pregunta] == 0].drop(columns=[siguiente_pregunta])

    if len(datos.index) == 1:
        animal = datos['animal'].values[0]
    elif len(datos.index) == 0:
        print('Las respuestas no son conclusivas, ¿quieres empezar de nuevo?')
        datos = pandas.read_csv('animales.csv')

print(f'La respuesta es:{animal}')
