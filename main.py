
import pandas as pd
import plotly.express as px
import geojson

def calcular_tercera_fuerza(my_csv, nombre):
    juntos_por_el_cambio = ['JUNTOS',
                            'JUNTOS POR EL CAMBIO TIERRA DEL FUEGO',
                            'CAMBIA SANTA CRUZ',
                            'JUNTOS POR EL CAMBIO JXC',
                            'JUNTOS SOMOS RIO NEGRO',
                            'JUNTOS POR EL CAMBIO +',
                            'FRENTE JUNTOS POR EL CAMBIO',
                            'CAMBIA MENDOZA',
                            'CAMBIA JUJUY',
                            'UNIDOS POR SAN LUIS',
                            'JUNTOS POR FORMOSA LIBRE',
                            'VAMOS LA RIOJA',
                            'JUNTOS POR ENTRE RÍOS',
                            'CHACO CAMBIA + JUNTOS POR EL CAMBIO',
                            'ECO + VAMOS CORRIENTES',
                            'JUNTOS POR EL CAMBIO CHUBUT',
                            'JUNTOS POR EL CAMBIO'
                           ]

    frente_de_todos = [ 'FRENTE DE TODOS',
                        'FRENTE CIVICO POR SANTIAGO']

    my_csv = my_csv.loc[(~my_csv['Agrupacion'].isin(juntos_por_el_cambio)) & 
                        (~my_csv['Agrupacion'].isin(frente_de_todos)) & 
                        (my_csv['Agrupacion'] != 'NaN')
                       ].groupby('Agrupacion').sum()['votos'].reset_index(name='votos')

    my_filter = my_csv['votos'] == my_csv['votos'].max()
    my_csv = my_csv[my_filter]

    my_csv['Provincia'] = nombre
    my_csv['votos'] = my_csv['votos'] / electores[nombre]
    return my_csv

with open("geojson/ProvinciasArgentina.geojson", encoding="utf-8") as f:
    gj = geojson.load(f)

electores = {   'Buenos Aires': 12704518,
                'Capital Federal': 2552058,
                'Catamarca': 327478,
                'Chaco': 967147,
                'Chubut': 448149,
                'Corrientes': 894376,
                'Córdoba': 2984631,
                'Entre Ríos': 1112939,
                'Formosa': 468299,
                'Jujuy': 573326,
                'La Pampa': 293790,
                'La Rioja': 294509,
                'Mendoza': 1439463,
                'Misiones': 948500,
                'Neuquén': 526441,
                'Río Negro': 560880,
                'Salta': 1051142,
                'San Juan': 579913,
                'San Luis': 393472,
                'Santa Cruz': 256388,
                'Santa Fe': 2768525,
                'Santiago del Estero': 778455,
                'Tierra del Fuego': 141548,
                'Tucumán': 1267045,
            }

bsas = pd.read_csv("csv/Buenos Aires_0.csv", delimiter=";", dtype={'votos': int})
bsas = bsas.append(pd.read_csv("csv/Buenos Aires_1_1.csv", delimiter=";", dtype={'votos': int}))
bsas = bsas.append(pd.read_csv("csv/Buenos Aires_1_2.csv", delimiter=";", dtype={'votos': int}))
bsas = bsas.append(pd.read_csv("csv/Buenos Aires_2.csv", delimiter=";", dtype={'votos': int, 'IdCircuito': str}))
bsas = bsas.append(pd.read_csv("csv/Buenos Aires_3_1.csv", delimiter=";", dtype={'votos': int}))
bsas = bsas.append(pd.read_csv("csv/Buenos Aires_3_2.csv", delimiter=";", dtype={'votos': int}))
bsas = bsas.append(pd.read_csv("csv/Buenos Aires_4.csv", delimiter=";", dtype={'votos': int}))
bsas = bsas.append(pd.read_csv("csv/Buenos Aires_5.csv", delimiter=";", dtype={'votos': int}))
bsas = bsas.append(pd.read_csv("csv/Buenos Aires_6.csv", delimiter=";", dtype={'votos': int}))
bsas = bsas.append(pd.read_csv("csv/Buenos Aires_7.csv", delimiter=";", dtype={'votos': int}))
bsas3 = calcular_tercera_fuerza(bsas, 'Buenos Aires')
provincias = bsas3
print(bsas)

caba = calcular_tercera_fuerza(pd.read_csv("csv/CABA.csv", delimiter=";", dtype={'votos': int}), 'Capital Federal')
provincias = provincias.append(caba)
#print(caba)

catamarca = calcular_tercera_fuerza(pd.read_csv("csv/Catamarca.csv", delimiter=";", dtype={'votos': int}), 'Catamarca')
provincias = provincias.append(catamarca)
#print(catamarca)

chaco = calcular_tercera_fuerza(pd.read_csv("csv/Chaco.csv", delimiter=";", dtype={'votos': int}), 'Chaco')
provincias = provincias.append(chaco)
#print(chaco)

chubut = calcular_tercera_fuerza(pd.read_csv("csv/Chubut.csv", delimiter=";", dtype={'votos': int}), 'Chubut')
provincias = provincias.append(chubut)
#print(chubut)

corrientes = calcular_tercera_fuerza(pd.read_csv("csv/Corrientes.csv", delimiter=";", dtype={'votos': int}), 'Corrientes')
provincias = provincias.append(corrientes)
#print(corrientes)

cordoba = calcular_tercera_fuerza(pd.read_csv("csv/Córdoba.csv", delimiter=";", dtype={'votos': int}), 'Córdoba')
provincias = provincias.append(cordoba)
#print(cordoba)

entrerios = calcular_tercera_fuerza(pd.read_csv("csv/Entre Ríos.csv", delimiter=";", dtype={'votos': int}), 'Entre Ríos')
provincias = provincias.append(entrerios)
#print(entrerios)

formosa = calcular_tercera_fuerza(pd.read_csv("csv/Formosa.csv", delimiter=";", dtype={'votos': int}), 'Formosa')
provincias = provincias.append(formosa)
#print(formosa)

jujuy = calcular_tercera_fuerza(pd.read_csv("csv/Jujuy.csv",delimiter=";", dtype={'votos': int}), 'Jujuy')
provincias = provincias.append(jujuy)
#print(jujuy)

lapampa = calcular_tercera_fuerza(pd.read_csv("csv/La Pampa.csv",delimiter=";", dtype={'votos': int}), 'La Pampa')
provincias = provincias.append(lapampa)
#print(lapampa)

larioja = calcular_tercera_fuerza(pd.read_csv("csv/La Rioja.csv",delimiter=";", dtype={'votos': int}), 'La Rioja')
provincias = provincias.append(larioja)
#print(larioja)

mendoza = calcular_tercera_fuerza(pd.read_csv("csv/Mendoza.csv",delimiter=";", dtype={'votos': int}), 'Mendoza')
provincias = provincias.append(mendoza)
#print(mendoza)

misiones = calcular_tercera_fuerza(pd.read_csv("csv/Misiones.csv",delimiter=";", dtype={'votos': int}), 'Misiones')
provincias = provincias.append(misiones)
#print(misiones)

neuquen = calcular_tercera_fuerza(pd.read_csv("csv/Neuquén.csv",delimiter=";", dtype={'votos': int}), 'Neuquén')
provincias = provincias.append(neuquen)
#print(neuquen)

rionegro = calcular_tercera_fuerza(pd.read_csv("csv/Río Negro.csv",delimiter=";", dtype={'votos': int}), 'Río Negro')
provincias = provincias.append(rionegro)
#print(rionegro)

salta = calcular_tercera_fuerza(pd.read_csv("csv/Salta.csv",delimiter=";", dtype={'votos': int}), 'Salta')
provincias = provincias.append(salta)
#print(salta)

sanjuan = calcular_tercera_fuerza(pd.read_csv("csv/San Juan.csv",delimiter=";", dtype={'votos': int}), 'San Juan')
provincias = provincias.append(sanjuan)
#print(sanjuan)

sanluis = calcular_tercera_fuerza(pd.read_csv("csv/San Luis.csv",delimiter=";", dtype={'votos': int}), 'San Luis')
provincias = provincias.append(sanluis)
#print(sanluis)

santacruz = calcular_tercera_fuerza(pd.read_csv("csv/Santa Cruz.csv",delimiter=";", dtype={'votos': int}), 'Santa Cruz')
provincias = provincias.append(santacruz)
#print(santacruz)

santafe = calcular_tercera_fuerza(pd.read_csv("csv/Santa Fe.csv",delimiter=";", dtype={'votos': int}), 'Santa Fe')
provincias = provincias.append(santafe)
#print(santafe)

estero = calcular_tercera_fuerza(pd.read_csv("csv/Santiago del Estero.csv",delimiter=";", dtype={'votos': int}), 'Santiago del Estero')
provincias = provincias.append(estero)
#print(estero)

fuego = calcular_tercera_fuerza(pd.read_csv("csv/Tierra del Fuego, Antártida e Islas del Atlántico Sur.csv",delimiter=";", dtype={'votos': int}), 'Tierra del Fuego')
provincias =provincias.append(fuego)
#print(fuego)

tucuman = calcular_tercera_fuerza(pd.read_csv("csv/Tucumán.csv",delimiter=";", dtype={'votos': int}), 'Tucumán')
provincias = provincias.append(tucuman)
#print(tucuman)

print(provincias)


fig = px.choropleth_mapbox(provincias,
                           geojson = gj,
                           locations='Provincia',
                           color='votos',
                           color_continuous_scale="Viridis",
                           range_color=(0,1),
                           mapbox_style="carto-positron",
                           zoom=3,
                           center = {"lat": -38.4, "lon": -63.6},
                           opacity=0.5,
                           labels={'votos':'votos'},
                           featureidkey="properties.nombre")

fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0})
fig.show()

