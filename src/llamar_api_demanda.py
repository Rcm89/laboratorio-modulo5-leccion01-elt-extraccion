import sys
import os

import json
import pandas as pd 

import requests
import os
sys.path.append("../")

from src import soporte_codigos as sop


def obtener_datos_demanda(lista_anios, ruta, headers):

    for anio in lista_anios:
        for nombre, ccaa in sop.codigos_comunidades.items():
            
            url_demanda=f"https://apidatos.ree.es/es/datos/demanda/evolucion?start_date={anio}-01-01T00:00&end_date={anio}-12-31T23:59&time_trunc=month&geo_trunk=electric_system&geo_limit=ccaa&geo_ids={ccaa}"
            response = requests.get(url_demanda, headers=headers)
            if response.status_code != 200:
                continue
            else:
                responsa= response.json()  
                df_demanda= pd.DataFrame(responsa['included'][0]['attributes']['values']) 
                df_demanda["cod_ccaa"]= ccaa
                df_demanda.to_csv(os.path.join(ruta, f'{nombre}_{anio}.csv'))

    return df_demanda

