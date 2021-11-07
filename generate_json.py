import pandas as pd
import os
import json

pathnames=[]
for pathname in os.listdir("csv"):
    name = os.path.splitext(pathname)[0]
    try:
        place_of_underscore = name.index("_")
    except ValueError:
        place_of_underscore = -1
    if place_of_underscore >= 0:
        name = name[0:place_of_underscore]
    pathnames.append({
        "file":"csv/"+pathname,
        "name":name
    })
with open("partidosInCharge.json") as fr:
    partidos_in_charge = json.load(fr)
d = {}
partidos = []
for p in pathnames:
    print(p["name"])
    dataset = pd.read_csv(p["file"],sep=";",dtype={'votos': int, 'IdCircuito': str})
    votos_nulos = dataset[["votos"]][dataset["tipoVoto"].isin(['nulos'])].sum()
    resultados = dataset[["Agrupacion","votos"]].groupby(["Agrupacion"]).sum()
    ganador = resultados.sort_values("votos",ascending=False).iloc[0].name
    votos_totales = dataset[["votos"]].sum()
    if p["name"] in d:
        resultads_dict = resultados.to_dict()["votos"]
        d[p["name"]]["votos_nulos"] += votos_nulos.to_dict()["votos"]
        d[p["name"]]["votos_totales"] += votos_totales.to_dict()["votos"]
        for k in resultads_dict.keys():
            if k in d[p["name"]]["resultados"]:
                d[p["name"]]["resultados"][k] += resultads_dict[k]
            else:
                d[p["name"]]["resultados"][k] = resultads_dict[k]

        name_ganador = ""
        votos_ganador = -1
        for k in d[p["name"]]["resultados"].keys():
            if d[p["name"]]["resultados"][k] > votos_ganador:
                name_ganador = k
                votos_ganador = d[p["name"]]["resultados"][k]

        d[p["name"]]["ganador"] = name_ganador
        d[p["name"]]["cambioDePartido"] = name_ganador == partidos_in_charge[p["name"]]
    else:
        d[p["name"]] = {
            "votos_nulos":votos_nulos.to_dict()["votos"],
            "resultados":resultados.to_dict()["votos"],
            "ganador":ganador,
            "cambioDePartido": ganador == partidos_in_charge[p["name"]],
            "votos_totales": votos_totales.to_dict()["votos"]
        }
    for p in resultados.to_dict()["votos"]:
        if p not in partidos:
            partidos.append(p)
with open("observableData.json","w") as fw:
    json.dump(d,fw,indent=True)