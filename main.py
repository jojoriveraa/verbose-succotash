
import numpy as np
import pandas as pd

datos_jubilados = np.loadtxt("jubilados.csv", delimiter=',', dtype='str', unpack=True)

fechas_jubilacion = pd.Series(datos_jubilados[1], index=datos_jubilados[0])
pensiones_en_pesos = pd.Series(datos_jubilados[2], index=datos_jubilados[0], dtype=float)
fechas_a_consultar = pd.Series(datos_jubilados[3], index=datos_jubilados[0])

datos_udis = np.loadtxt("udis.csv", delimiter=',', dtype='str', unpack=True)
valor_udis = pd.Series(datos_udis[1], datos_udis[0], dtype=float)

cantidad_udis_por_persona = pd.Series(pensiones_en_pesos.values / valor_udis[list(fechas_jubilacion.values)].values, index=datos_jubilados[0])

a_recibir = pd.Series(cantidad_udis_por_persona * valor_udis[list(fechas_a_consultar)].values, index=datos_jubilados[0])
