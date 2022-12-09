from fastapi import FastAPI
import pandas as pd
import numpy
import uvicorn


df_actors = pd.read_csv("actors.csv")
df = pd.read_csv("dataframe.csv")
df_generos = pd.read_csv("generos.csv")

app = FastAPI(title='Consultas con FastAPI', description='Esta API permite realizar consultas a los dataset de peliculas provistos')

@app.get("/")
def index():
    return{'Proyecto individual 1 hecho por Daniel Muñoz López'}

@app.get("/about")
def about():
    return{'API creada para proyecto individual de Henry hecha con FASTAPI y UVICORN'}


@app.get("/get_max_duration")
async def get_max_duration(año:float, plataforma:str, tipo_film:str):
    message = f"Máximo de {plataforma} en {año} es"
    return {message:df[(df['release_year']==año)&(df['plataform']==plataforma)&(df['type (min-seasons)']== tipo_film)]['duration'].max()}

@app.get("/get_count_plataform")
async def get_count_plataform(plataforma:str):  
    return{f"Cantidad de películas en {plataforma} es":df[(df['plataform']==plataforma)&(df['type']=='movie')]['type'].count().tolist(),
            f"Cantidad de series en {plataforma} es":df[(df['plataform']==plataforma)&(df['type']=='tv show')]['type'].count().tolist()}

@app.get("/get_listedin")
async def get_listedin(genero:str):
    return {df_generos[(df_generos["genero"]==genero)]["plataforma"].value_counts().idxmax():
    df_generos[(df_generos["genero"]==genero)]["plataforma"].value_counts().max().tolist()}

@app.get("/get_actor")
async def get_actor(plataforma:str, año:int):
    data = df_actors[(df_actors['year']==año)&(df_actors['plataform']==plataforma)]['actor']
    if data.value_counts().index[0] == 'sin dato':
        return {data.value_counts().index[1]:data.value_counts()[1].tolist()}
    elif data.value_counts().index[0] != 'sin dato':
        return {data.value_counts().index[0]:data.value_counts()[0].tolist()}