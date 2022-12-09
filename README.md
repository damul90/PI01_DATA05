<p align=center><img src=https://res.cloudinary.com/practicaldev/image/fetch/s--iOsUGN0b--/c_limit%2Cf_auto%2Cfl_progressive%2Cq_auto%2Cw_880/https://dev-to-uploads.s3.amazonaws.com/uploads/articles/l4jt274288k241g94r66.png><p>

# <h1 align=center>**`Primer Proyecto Individual`<br>`Data Engineering`**</h1>

<p align="center">Daniel Muñoz Lopez</p>
<p align="center">Ingeniero físico</p>
<p align="center">Estudiante en Henry de Data Science DATAFT05</p>

<hr>  

## **Introducción**
<p>Este proyecto tiene como objetivo la creación de una API con FastAPI en docker, realizando algunas consultas programdas sobre la misma.

Debido a la versatilidad de la librería FastAPI, realizar la creación de una API se vuelve una tarea un poco más sencilla de implementar. La app tomará datos, que en un principio recibieron un tratamiento de **ETL**, para su posterior uso en la API.

El argumento de este proyecto se precisa en la aplicación de los conocimientos obtenidos durante los módulos de estudio hechos a lo largo de los últimos 3 meses del bootcamp, retándonos a ser **data engineers**, donde no solo hubo que obtener datos, procesarlos y exportarlos, sino también mostrarlos en una aplicación que tuviera la capacidad de adaptarse a diferentes entornos gracias a docker.</p>

## **Pasos del proyecto**

+ Consulta y limpieza de los datasets con python y la librería de pandas.

+ Creación de una API con la librería FastAPI.

+ Instalación de docker desktop para windows.

+ Creación de una imagen para docker de python.

+ Creación del container de docker donde correrá la API.
<hr>

### **Consulta y limpieza**

Hacemos uso de python y la librería pandas para cargar y procesar los datos obtenidos de los datasets

<pre><code>import pandas as pd
</code></pre>

### **Instalación de docker desktop**
[Descargar docker](https://www.docker.com/products/docker-desktop/) y luego abrir el docker.

### **Creación de la imagen de docker**
Se usa un dockerfile:

<pre><code>FROM python:3.9
COPY . usr/src/app
WORKDIR /usr/src/app
RUN pip install -r requirements.txt
ENTRYPOINT uvicorn --host 0.0.0.0 main:app --reload
</code></pre>

Luego correr en la terminal:
<pre><code>docker build -t &lt;nombre de tu app&gt;  .
</code></pre>

### **Creación del container de docker**

Seguidamente colocar en la terminal:
<pre><code>docker run  -p 8000:8000 -v cd://usr/src/app &lt;nombre de tu app&gt;
</code></pre>
<hr>

Daniel Muñoz Lopez

Ingeniero Físico

[GitHub damul90](https://github.com/damul90)

[LinkedIn: Daniel Muñoz López](https://www.linkedin.com/in/daniel-munoz-lopez/)