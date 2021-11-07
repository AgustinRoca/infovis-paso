import csv

from main import parse_csvs, calcular_tercera_fuerza

def generate_positions_csv(provincias):
    terceras_fuerzas = None
    for nombre in provincias:
        if terceras_fuerzas is None:
            terceras_fuerzas = calcular_tercera_fuerza(provincias[nombre]['Data'], nombre)
        else:
            terceras_fuerzas = terceras_fuerzas.append(calcular_tercera_fuerza(provincias[nombre]['Data'], nombre))

    with open('positions.csv', 'w', newline='') as csvfile:
        writer = csv.writer(csvfile, delimiter=';')
        writer.writerow(['Provincia', 'Partido', 'Posicion'])
        for nombre in provincias:
            df = provincias[nombre]['Data']
            partido = terceras_fuerzas.loc[terceras_fuerzas['Provincia'] == nombre].iloc[0]['Agrupacion']
            writer.writerow([nombre, partido, df.loc[df['Agrupacion'] == partido].index[0]])

def generate_contested_csv(provincias):
    with open('parejo.csv', 'w', newline='') as csvfile:
        writer = csv.writer(csvfile, delimiter=';')
        writer.writerow(['Provincia', 'Parejo'])

        for nombre in provincias:
            votos_totales = provincias[nombre]['Data'].groupby('Agrupacion').sum()['votos'].reset_index(name='votos').sum()['votos']
            df = provincias[nombre]['Data'].iloc[:3]
            df.loc[:, 'votos'] = df['votos'].apply(lambda x: x/votos_totales)

            mean = df['votos'].mean()
            df.loc[:, 'votos'] = df['votos'].apply(lambda x: abs(x - mean))
            parejo = df['votos'].sum()
            writer.writerow([nombre, parejo])


provincias = parse_csvs()
for nombre in provincias:
    provincias[nombre]['Data'] = provincias[nombre]['Data'].groupby('Agrupacion').sum()['votos'].reset_index(
        name='votos').sort_values('votos', ascending=False).reset_index()
generate_positions_csv(provincias)
generate_contested_csv(provincias)

