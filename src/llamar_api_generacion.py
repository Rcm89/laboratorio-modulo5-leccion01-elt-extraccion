import sys
import os
import http.client
import json
import pandas as pd
import requests
import os
sys.path.append("../")

from src import soporte_codigos as sop


def obtener_datos_generacion(lista_anios, ruta, headers):

    for anio in lista_anios:
        for nombre, ccaa in sop.codigos_comunidades.items():
            
            url_oferta=f"https://apidatos.ree.es/es/datos/generacion/estructura-renovables?start_date={anio}-01-01T00:00&end_date={anio}-12-31T23:59&time_trunc=month&geo_trunk=electric_system&geo_limit=ccaa&geo_ids={ccaa}"

            response = requests.get(url_oferta, headers=headers)
            if response.status_code != 200:
                continue
            else:
                responsa= response.json()  
                df_completo= pd.DataFrame()
                for i in range(0, len(responsa['included'])):
                    df_tipo=pd.DataFrame(responsa['included'][i]['attributes']['values'])
                    df_tipo["type"]= responsa["included"][i]["type"]
                    df_tipo["cod_ccaa"]= ccaa
                    df_completo= pd.concat([df_completo, df_tipo ])
                df_generacion= df_completo.to_csv(os.path.join(ruta, f'{nombre}_{anio}.csv'))

    return df_generacion


