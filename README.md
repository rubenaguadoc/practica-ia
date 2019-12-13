# Práctica de IA de la ETSIINF UPM

## Datos Recogidos

Los datos de las distancias reales entre estaciones han sido recogidos con ayuda de la página web [HyperDia][http://www.hyperdia.com/en/] con las opciones 10:00 am y solo recogiendo los trenes "Local Train" y "Japan Railway(JR)"

## Instalación

Servidor python 3

```bash
cd backend/src
pip install flask sqlite3
```

Servidor web

```bash
cd web
npm i
```

## Uso

Iniciar el servidor python (flask) con un solo endpoint que ejecuta el algoritmo en http://localhos:4567/

```bash
cd backend/src
python main.py
```

Iniciar el servidor web en http://localhos:5000/

```bash
cd web
npm run run
```

## Licencia

Uso restringido a uso académico y formativo, y en tal caso, se agradece la mención, reconocimiento y redirección a este repositorio.
