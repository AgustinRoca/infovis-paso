
import pandas as pd
import plotly.express as px
import geojson



bsas = pd.read_csv("Buenos Aires_ Capital.csv",delimiter=";")

bsas  =bsas.append(pd.read_csv("Buenos Aires_ Primera.csv",delimiter=";"))
bsas = bsas.append( pd.read_csv("Buenos Aires_Segunda.csv",delimiter=";"))
bsas = bsas.append(pd.read_csv("Buenos Aires_Tercera.csv",delimiter=";"))
bsas = bsas.append(pd.read_csv("Buenos Aires_Cuarta.csv",delimiter=";"))
bsas = bsas.append(pd.read_csv("Buenos Aires_Quinta.csv",delimiter=";"))
bsas = bsas.append(pd.read_csv("Buenos Aires_Sexta.csv",delimiter=";"))
bsas = bsas.append(pd.read_csv("Buenos Aires_Septima.csv",delimiter=";"))


#votos_circuitos = df.loc[(df['Agrupacion'] != 'JUNTOS') & (df['Agrupacion'] != 'FRENTE DE TODOS')].groupby(['IdCircuito','Agrupacion']).sum()['votos']\
#    .reset_index(name ='votos')

#aux = votos_circuitos.groupby(['IdCircuito'])['votos'].transform(max) == votos_circuitos['votos']



#print( votos_circuitos[aux])
#votos_circuitos = votos_circuitos[aux]




with open("ProvinciasArgentina.geojson", encoding="utf-8") as f:
    gj = geojson.load(f)







def calcular_tercera_fuerza(my_csv):
    my_csv=my_csv.loc[(my_csv['Agrupacion'] != 'JUNTOS')& (my_csv['Agrupacion'] != 'JUNTOS POR EL CAMBIO TIERRA DEL FUEGO')
                      & (my_csv['Agrupacion'] != 'CAMBIA SANTA CRUZ') & (my_csv['Agrupacion'] != 'JUNTOS POR EL CAMBIO JXC')& (my_csv['Agrupacion'] != 'JUNTOS SOMOS RIO NEGRO')& (my_csv['Agrupacion'] != 'JUNTOS POR EL CAMBIO +')
                      &  (my_csv['Agrupacion'] != 'FRENTE JUNTOS POR EL CAMBIO')& (my_csv['Agrupacion'] != 'CAMBIA MENDOZA')
                      & (my_csv['Agrupacion'] != 'CAMBIA JUJUY')& (my_csv['Agrupacion'] != 'FRENTE CIVICO POR SANTIAGO')& (my_csv['Agrupacion'] != 'UNIDOS POR SAN LUIS')& (my_csv['Agrupacion'] != 'VAMOS LA RIOJA') & (my_csv['Agrupacion'] != 'JUNTOS POR FORMOSA LIBRE') & (my_csv['Agrupacion'] != 'JUNTOS POR ENTRE RÍOS')
                      & (my_csv['Agrupacion'] != 'CHACO CAMBIA + JUNTOS POR EL CAMBIO') & (my_csv['Agrupacion'] != 'ECO + VAMOS CORRIENTES') & (my_csv['Agrupacion'] != 'JUNTOS POR EL CAMBIO CHUBUT') & (my_csv['Agrupacion'] != 'FRENTE DE TODOS') & (my_csv['Agrupacion'] != 'NaN') & (my_csv['Agrupacion'] != "JUNTOS POR EL CAMBIO")].groupby(
        ['Agrupacion']).sum()['votos'] \
        .reset_index(name='votos')

    my_filter = my_csv['votos'] == my_csv['votos'].max()

    return my_csv[my_filter]

#print(calcular_tercera_fuerza(df))



caba = calcular_tercera_fuerza(pd.read_csv("CABA.csv",delimiter=";"))
caba['votos'] = caba['votos'] / 2552058
caba['Provincia'] = "Capital Federal"
provincias = caba
#print(caba)
catamarca = calcular_tercera_fuerza(pd.read_csv("Catamarca.csv",delimiter=";"))
catamarca['votos'] = catamarca['votos'] / 327478
catamarca['Provincia'] = "Catamarca"
provincias = provincias.append(catamarca)
#print(catamarca)
chaco = calcular_tercera_fuerza(pd.read_csv("Chaco.csv",delimiter=";"))
chaco['votos'] = chaco['votos'] / 967147
chaco['Provincia'] = "Chaco"
provincias =provincias.append(chaco)

#print(chaco)
chubut = calcular_tercera_fuerza(pd.read_csv("Chubut.csv",delimiter=";"))
chubut['votos'] = chubut['votos'] / 448149
chubut['Provincia'] = "Chubut"
provincias =provincias.append(chubut)

#print(chubut)
corrientes = calcular_tercera_fuerza(pd.read_csv("Corrientes.csv",delimiter=";"))
corrientes['votos'] = corrientes['votos'] / 894376
corrientes['Provincia'] = "Corrientes"
provincias =provincias.append(corrientes)

#print(corrientes)
cordoba = calcular_tercera_fuerza(pd.read_csv("Córdoba.csv",delimiter=";"))
cordoba['votos'] = cordoba['votos'] / 2984631
cordoba['Provincia'] = "Córdoba"
provincias =provincias.append(cordoba)

#print(cordoba)
entrerios = calcular_tercera_fuerza(pd.read_csv("Entre Rios.csv",delimiter=";"))
entrerios['votos'] = entrerios['votos'] / 1112939
entrerios['Provincia'] = "Entre Ríos"

provincias =provincias.append(entrerios)

#print(entrerios)
formosa = calcular_tercera_fuerza(pd.read_csv("Formosa.csv",delimiter=";"))
formosa['votos'] = formosa['votos'] / 468299
formosa['Provincia'] = "Formosa"
provincias =provincias.append(formosa)

#print(formosa)
jujuy = calcular_tercera_fuerza(pd.read_csv("Jujuy.csv",delimiter=";"))
jujuy['votos'] = jujuy['votos'] / 573326
jujuy['Provincia'] = 'Jujuy'
provincias =provincias.append(jujuy)

#print(jujuy)
lapampa = calcular_tercera_fuerza(pd.read_csv("La Pampa.csv",delimiter=";"))
lapampa['votos'] = lapampa['votos'] / 293790
lapampa['Provincia'] = "La Pampa"

provincias =provincias.append(lapampa)

#print(lapampa)
larioja = calcular_tercera_fuerza(pd.read_csv("La Rioja.csv",delimiter=";"))
larioja['votos'] = larioja['votos'] / 294509
larioja['Provincia'] = "La Rioja"
provincias =provincias.append(larioja)

#print(larioja)
mendoza = calcular_tercera_fuerza(pd.read_csv("Mendoza.csv",delimiter=";"))
mendoza['votos'] = mendoza['votos'] / 1439463
mendoza['Provincia'] = "Mendoza"
provincias =provincias.append(mendoza)

#print(mendoza)
misiones = calcular_tercera_fuerza(pd.read_csv("Misiones.csv",delimiter=";"))
misiones['votos'] = misiones['votos'] / 948500
misiones['Provincia'] = "Misiones"
provincias =provincias.append(misiones)

#print(misiones)
neuquen = calcular_tercera_fuerza(pd.read_csv("Neuquén.csv",delimiter=";"))
neuquen['votos'] = neuquen['votos'] / 526441
neuquen['Provincia'] = "Neuquén"
provincias =provincias.append(neuquen)

#print(neuquen)
rionegro = calcular_tercera_fuerza(pd.read_csv("Río Negro.csv",delimiter=";"))
rionegro['votos'] = rionegro['votos'] / 560880
rionegro['Provincia'] = "Río Negro"
provincias =provincias.append(rionegro)

#print(rionegro)
salta = calcular_tercera_fuerza(pd.read_csv("Salta.csv",delimiter=";"))
salta['votos'] = salta['votos'] / 1051142
salta['Provincia'] = "Salta"
provincias =provincias.append(salta)

#print(salta)
sanjuan = calcular_tercera_fuerza(pd.read_csv("San Juan.csv",delimiter=";"))
sanjuan['votos'] = sanjuan['votos'] / 579913
sanjuan['Provincia'] = "San Juan"
provincias =provincias.append(sanjuan)

#print(sanjuan)
sanluis = calcular_tercera_fuerza(pd.read_csv("San Luis.csv",delimiter=";"))
sanluis['votos'] = sanluis['votos'] / 393472
sanluis['Provincia'] = "San Luis"
provincias =provincias.append(sanluis)

#print(sanluis)
santacruz = calcular_tercera_fuerza(pd.read_csv("Santa Cruz.csv",delimiter=";"))
santacruz['votos'] = santacruz['votos'] / 256388
santacruz['Provincia'] = "Santa Cruz"
provincias =provincias.append(santacruz)

#print(santacruz)
fuego = calcular_tercera_fuerza(pd.read_csv("Tierra del Fuego, Antártida e Islas del Atlántico Sur.csv",delimiter=";"))
fuego['votos'] = fuego['votos'] / 141548
fuego['Provincia'] = "Tierra del Fuego"
provincias =provincias.append(fuego)

#print(fuego)
estero = calcular_tercera_fuerza(pd.read_csv("Santiago del Estero.csv",delimiter=";"))
estero['votos'] = estero['votos'] / 778455
estero['Provincia'] = "Santiago del Estero"
provincias =provincias.append(estero)

#print(estero)
tucuman = calcular_tercera_fuerza(pd.read_csv("Tucumán.csv",delimiter=";"))
tucuman['votos'] = tucuman['votos'] / 1267045
tucuman['Provincia'] = "Tucumán"
provincias =provincias.append(tucuman)

#print(tucuman)


santafe = calcular_tercera_fuerza(pd.read_csv("Santa Fe.csv",delimiter=";"))
santafe['votos'] = santafe['votos'] / 2768525
santafe['Provincia'] = "Santa Fe"
provincias =provincias.append(santafe)


bsas = calcular_tercera_fuerza(bsas)
bsas['votos'] = bsas['votos'] / 12704518
bsas['Provincia'] = "Buenos Aires"
provincias =provincias.append(bsas)

print(provincias)


fig = px.choropleth_mapbox(provincias
                           ,geojson = gj,
                           locations='Provincia',
                           color='votos',
                           color_continuous_scale="Viridis",
                           range_color=(0,1),
                           mapbox_style="carto-positron",
                           zoom=10,
                           center = {"lat": -34.6, "lon": -58.38},
                           opacity=0.5,
                           labels={'votos':'votos'},featureidkey="properties.nombre")

fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0})
fig.show()

