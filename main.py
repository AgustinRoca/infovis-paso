
import pandas as pd
import plotly.express as px
import geojson

def calcular_tercera_fuerza(provincia_df, nombre):
    juntos_por_el_cambio = ['JUNTOS',
                            'JUNTOS POR EL CAMBIO TIERRA DEL FUEGO',
                            'CAMBIA SANTA CRUZ',
                            'JUNTOS POR EL CAMBIO JXC',
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

    votos_totales = provincia_df.groupby('Agrupacion').sum()['votos'].reset_index(name='votos').sum()['votos']
    
    provincia_df = provincia_df.loc[  (~provincia_df['Agrupacion'].isin(juntos_por_el_cambio)) & 
                                        (~provincia_df['Agrupacion'].isin(frente_de_todos)) & 
                                        (provincia_df['Agrupacion'] != 'NaN')
                                    ].groupby('Agrupacion').sum()['votos'].reset_index(name='votos')

    my_filter = provincia_df['votos'] == provincia_df['votos'].max()
    provincia_df = provincia_df[my_filter]

    provincia_df['Provincia'] = nombre
    provincia_df['votos'] = provincia_df['votos'] / votos_totales
    return provincia_df

def calcular_participacion(provincia_df, nombre, electores):
    votantes = provincia_df.loc[provincia_df['Cargo'] == 'DIPUTADOS NACIONALES'
                                ].groupby('Agrupacion').sum()['votos'].reset_index(name='votos').sum()['votos']

    provincia_df['Provincia'] = nombre
    provincia_df['participacion'] = votantes / electores
    return provincia_df

def parse_csvs():
    provincias = {}
    delimiter = ';'
    dtype = {'votos': int, 'IdCircuito': str}
    d = 'Data'
    e = 'Electores' 

    bsas = pd.read_csv("csv/Buenos Aires_0.csv", delimiter=delimiter, dtype=dtype)
    bsas = bsas.append(pd.read_csv("csv/Buenos Aires_1_1.csv", delimiter=delimiter, dtype=dtype))
    bsas = bsas.append(pd.read_csv("csv/Buenos Aires_1_2.csv", delimiter=delimiter, dtype=dtype))
    bsas = bsas.append(pd.read_csv("csv/Buenos Aires_2.csv", delimiter=delimiter, dtype=dtype))
    bsas = bsas.append(pd.read_csv("csv/Buenos Aires_3_1.csv", delimiter=delimiter, dtype=dtype))
    bsas = bsas.append(pd.read_csv("csv/Buenos Aires_3_2.csv", delimiter=delimiter, dtype=dtype))
    bsas = bsas.append(pd.read_csv("csv/Buenos Aires_4.csv", delimiter=delimiter, dtype=dtype))
    bsas = bsas.append(pd.read_csv("csv/Buenos Aires_5.csv", delimiter=delimiter, dtype=dtype))
    bsas = bsas.append(pd.read_csv("csv/Buenos Aires_6.csv", delimiter=delimiter, dtype=dtype))
    bsas = bsas.append(pd.read_csv("csv/Buenos Aires_7.csv", delimiter=delimiter, dtype=dtype))
    nombre = 'Buenos Aires'
    provincias[nombre] = {}
    provincias[nombre][d] = bsas
    provincias[nombre][e] = 12704518

    caba = pd.read_csv("csv/CABA.csv", delimiter=delimiter, dtype=dtype)
    nombre = 'Capital Federal'
    provincias[nombre] = {}
    provincias[nombre][d] = caba
    provincias[nombre][e] = 2552058

    catamarca = pd.read_csv("csv/Catamarca.csv", delimiter=delimiter, dtype=dtype)
    nombre = 'Catamarca' 
    provincias[nombre] = {}
    provincias[nombre][d] = catamarca
    provincias[nombre][e] = 327478

    chaco = pd.read_csv("csv/Chaco.csv", delimiter=delimiter, dtype=dtype)
    nombre = 'Chaco'
    provincias[nombre] = {}
    provincias[nombre][d] = chaco
    provincias[nombre][e] = 967147

    chubut = pd.read_csv("csv/Chubut.csv", delimiter=delimiter, dtype=dtype)
    nombre = 'Chubut' 
    provincias[nombre] = {}
    provincias[nombre][d] = chubut
    provincias[nombre][e] = 448149

    corrientes = pd.read_csv("csv/Corrientes.csv", delimiter=delimiter, dtype=dtype)
    nombre = 'Corrientes' 
    provincias[nombre] = {}
    provincias[nombre][d] = corrientes
    provincias[nombre][e] = 894376

    cordoba = pd.read_csv("csv/Córdoba.csv", delimiter=delimiter, dtype=dtype)
    nombre = 'Córdoba' 
    provincias[nombre] = {}
    provincias[nombre][d] = cordoba
    provincias[nombre][e] = 2984631
    
    entrerios = pd.read_csv("csv/Entre Ríos.csv", delimiter=delimiter, dtype=dtype)
    nombre = 'Entre Ríos' 
    provincias[nombre] = {}
    provincias[nombre][d] = entrerios
    provincias[nombre][e] = 1112939
    
    formosa = pd.read_csv("csv/Formosa.csv", delimiter=delimiter, dtype=dtype)
    nombre = 'Formosa' 
    provincias[nombre] = {}
    provincias[nombre][d] = formosa
    provincias[nombre][e] = 468299
    
    jujuy = pd.read_csv("csv/Jujuy.csv", delimiter=delimiter, dtype=dtype)
    nombre = 'Jujuy' 
    provincias[nombre] = {}
    provincias[nombre][d] = jujuy
    provincias[nombre][e] = 573326
    
    lapampa = pd.read_csv("csv/La Pampa.csv", delimiter=delimiter, dtype=dtype)
    nombre = 'La Pampa' 
    provincias[nombre] = {}
    provincias[nombre][d] = lapampa
    provincias[nombre][e] = 293790
    
    larioja = pd.read_csv("csv/La Rioja.csv", delimiter=delimiter, dtype=dtype)
    nombre = 'La Rioja' 
    provincias[nombre] = {}
    provincias[nombre][d] = larioja
    provincias[nombre][e] = 294509
    
    mendoza = pd.read_csv("csv/Mendoza.csv", delimiter=delimiter, dtype=dtype)
    nombre = 'Mendoza' 
    provincias[nombre] = {}
    provincias[nombre][d] = mendoza
    provincias[nombre][e] = 1439463
    
    misiones = pd.read_csv("csv/Misiones.csv", delimiter=delimiter, dtype=dtype)
    nombre = 'Misiones' 
    provincias[nombre] = {}
    provincias[nombre][d] = misiones
    provincias[nombre][e] = 948500
    
    neuquen = pd.read_csv("csv/Neuquén.csv", delimiter=delimiter, dtype=dtype)
    nombre = 'Neuquén' 
    provincias[nombre] = {}
    provincias[nombre][d] = neuquen
    provincias[nombre][e] = 526441
    
    rionegro = pd.read_csv("csv/Río Negro.csv", delimiter=delimiter, dtype=dtype)
    nombre = 'Río Negro' 
    provincias[nombre] = {}
    provincias[nombre][d] = rionegro
    provincias[nombre][e] = 560880
    
    salta = pd.read_csv("csv/Salta.csv", delimiter=delimiter, dtype=dtype)
    nombre = 'Salta' 
    provincias[nombre] = {}
    provincias[nombre][d] = salta
    provincias[nombre][e] = 1051142
    
    sanjuan = pd.read_csv("csv/San Juan.csv", delimiter=delimiter, dtype=dtype)
    nombre = 'San Juan' 
    provincias[nombre] = {}
    provincias[nombre][d] = sanjuan
    provincias[nombre][e] = 579913
    
    sanluis = pd.read_csv("csv/San Luis.csv", delimiter=delimiter, dtype=dtype)
    nombre = 'San Luis' 
    provincias[nombre] = {}
    provincias[nombre][d] = sanluis
    provincias[nombre][e] = 393472
    
    santacruz = pd.read_csv("csv/Santa Cruz.csv", delimiter=delimiter, dtype=dtype)
    nombre = 'Santa Cruz'
    provincias[nombre] = {}
    provincias[nombre][d] = santacruz
    provincias[nombre][e] = 256388


    santafe = pd.read_csv("csv/Santa Fe.csv", delimiter=delimiter, dtype=dtype)
    nombre = 'Santa Fe' 
    provincias[nombre] = {}
    provincias[nombre][d] = santafe
    provincias[nombre][e] = 2768525
    
    estero = pd.read_csv("csv/Santiago del Estero.csv", delimiter=delimiter, dtype=dtype)
    nombre = 'Santiago del Estero' 
    provincias[nombre] = {}
    provincias[nombre][d] = estero
    provincias[nombre][e] = 778455
    
    fuego = pd.read_csv("csv/Tierra del Fuego, Antártida e Islas del Atlántico Sur.csv", delimiter=delimiter, dtype=dtype)
    nombre = 'Tierra del Fuego' 
    provincias[nombre] = {}
    provincias[nombre][d] = fuego
    provincias[nombre][e] = 141548
    
    tucuman = pd.read_csv("csv/Tucumán.csv", delimiter=delimiter, dtype=dtype)
    nombre = 'Tucumán' 
    provincias[nombre] = {}
    provincias[nombre][d] = tucuman
    provincias[nombre][e] = 1267045
    
    return provincias

def grafico_terceras_fuerzas(provincias):
    with open("geojson/ProvinciasArgentina.geojson", encoding="utf-8") as f:
        gj = geojson.load(f)

    terceras_fuerzas = None
    for nombre in provincias:
        if terceras_fuerzas is None:
            terceras_fuerzas = calcular_tercera_fuerza(provincias[nombre]['Data'], nombre)
        else:
            terceras_fuerzas = terceras_fuerzas.append(calcular_tercera_fuerza(provincias[nombre]['Data'], nombre))

    fig = px.choropleth_mapbox(terceras_fuerzas,
                            geojson = gj,
                            locations='Provincia',
                            color='votos',
                            color_continuous_scale="Inferno",
                            range_color=(0,0.3),
                            mapbox_style="carto-positron",
                            zoom=3, hover_name = 'Agrupacion',
                            center = {"lat": -38.4, "lon": -63.6},
                            opacity=0.5,
                            labels={'votos':'votos'},
                            featureidkey="properties.nombre")

    fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0})
    fig.show()

def grafico_participacion(provincias):
    with open("geojson/ProvinciasArgentina.geojson", encoding="utf-8") as f:
        gj = geojson.load(f)

    participacion = None
    for nombre in provincias:
        if participacion is None:
            participacion = calcular_participacion(provincias[nombre]['Data'], nombre, provincias[nombre]['Electores'])
        else:
            participacion = participacion.append(calcular_participacion(provincias[nombre]['Data'], nombre, provincias[nombre]['Electores']))

    minima = participacion['participacion'].min()
    maxima = participacion['participacion'].max()
    fig = px.choropleth_mapbox(participacion,
                            geojson = gj,
                            locations='Provincia',
                            color='participacion',
                            color_continuous_scale="Viridis",
                            range_color=(minima , maxima),
                            mapbox_style="carto-positron",
                            zoom=3,
                            center = {"lat": -38.4, "lon": -63.6},
                            opacity=0.5,
                            labels={'participacion':'participacion'},
                            featureidkey="properties.nombre")

    fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0})
    fig.show()

if __name__ == '__main__':
    provincias = parse_csvs()
    grafico_terceras_fuerzas(provincias)
    grafico_participacion(provincias)
