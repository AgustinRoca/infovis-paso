
import pandas as pd
import plotly.express as px
import geojson

def calcular_tercera_fuerza(my_csv, nombre, electores):
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
    my_csv['votos'] = my_csv['votos'] / electores
    return my_csv

def parse_csvs():
    provincias = {}
    delimiter = ';'
    dtype = {'votos': int, 'IdCircuito': str}

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
    provincias['Buenos Aires'] = bsas

    caba = pd.read_csv("csv/CABA.csv", delimiter=delimiter, dtype=dtype)
    provincias['Capital Federal'] = caba

    catamarca = pd.read_csv("csv/Catamarca.csv", delimiter=delimiter, dtype=dtype)
    provincias['Catamarca'] = catamarca

    chaco = pd.read_csv("csv/Chaco.csv", delimiter=delimiter, dtype=dtype)
    provincias['Chaco'] = chaco

    chubut = pd.read_csv("csv/Chubut.csv", delimiter=delimiter, dtype=dtype)
    provincias['Chubut'] = chubut

    corrientes = pd.read_csv("csv/Corrientes.csv", delimiter=delimiter, dtype=dtype)
    provincias['Corrientes'] = corrientes

    cordoba = pd.read_csv("csv/Córdoba.csv", delimiter=delimiter, dtype=dtype)
    provincias['Córdoba'] = cordoba

    entrerios = pd.read_csv("csv/Entre Ríos.csv", delimiter=delimiter, dtype=dtype)
    provincias['Entre Ríos'] = entrerios

    formosa = pd.read_csv("csv/Formosa.csv", delimiter=delimiter, dtype=dtype)
    provincias['Formosa'] = formosa

    jujuy = pd.read_csv("csv/Jujuy.csv", delimiter=delimiter, dtype=dtype)
    provincias['Jujuy'] = jujuy

    lapampa = pd.read_csv("csv/La Pampa.csv", delimiter=delimiter, dtype=dtype)
    provincias['La Pampa'] = lapampa

    larioja = pd.read_csv("csv/La Rioja.csv", delimiter=delimiter, dtype=dtype)
    provincias['La Rioja'] = larioja

    mendoza = pd.read_csv("csv/Mendoza.csv", delimiter=delimiter, dtype=dtype)
    provincias['Mendoza'] = mendoza

    misiones = pd.read_csv("csv/Misiones.csv", delimiter=delimiter, dtype=dtype)
    provincias['Misiones'] = misiones

    neuquen = pd.read_csv("csv/Neuquén.csv", delimiter=delimiter, dtype=dtype)
    provincias['Neuquén'] = neuquen

    rionegro = pd.read_csv("csv/Río Negro.csv", delimiter=delimiter, dtype=dtype)
    provincias['Río Negro'] = rionegro

    salta = pd.read_csv("csv/Salta.csv", delimiter=delimiter, dtype=dtype)
    provincias['Salta'] = salta

    sanjuan = pd.read_csv("csv/San Juan.csv", delimiter=delimiter, dtype=dtype)
    provincias['San Juan'] = sanjuan

    sanluis = pd.read_csv("csv/San Luis.csv", delimiter=delimiter, dtype=dtype)
    provincias['San Luis'] = sanluis

    santacruz = pd.read_csv("csv/Santa Cruz.csv", delimiter=delimiter, dtype=dtype)
    provincias['Santa Cruz'] = santacruz

    santafe = pd.read_csv("csv/Santa Fe.csv", delimiter=delimiter, dtype=dtype)
    provincias['Santa Fe'] = santafe

    estero = pd.read_csv("csv/Santiago del Estero.csv", delimiter=delimiter, dtype=dtype)
    provincias['Santiago del Estero'] = estero

    fuego = pd.read_csv("csv/Tierra del Fuego, Antártida e Islas del Atlántico Sur.csv", delimiter=delimiter, dtype=dtype)
    provincias['Tierra del Fuego'] = fuego

    tucuman = pd.read_csv("csv/Tucumán.csv", delimiter=delimiter, dtype=dtype)
    provincias['Tucumán'] = tucuman

    return provincias

def grafico_terceras_fuerzas(provincias):
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

    terceras_fuerzas = None
    for nombre in provincias:
        if terceras_fuerzas is None:
            terceras_fuerzas = calcular_tercera_fuerza(provincias[nombre], nombre, electores[nombre])
        else:
            terceras_fuerzas = terceras_fuerzas.append(calcular_tercera_fuerza(provincias[nombre], nombre, electores[nombre]))

    fig = px.choropleth_mapbox(terceras_fuerzas,
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

if __name__ == '__main__':
    provincias = parse_csvs()
    grafico_terceras_fuerzas(provincias)