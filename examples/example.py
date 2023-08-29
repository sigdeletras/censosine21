# Ejemplo: Obtener el total de hogares por régimen de tenencia de la vivienda y provincias

# Los parámetros necesarios son:
# - Tabla hogares (hog) o grupos de personas residentes en la misma vivienda familiar
# - Unidad de medida o métrica : Número de Hogares (SHOGARES)
# - Variable 1: 'ID_RESIDENCIA_N2' 'Provincia de residencia'
# - Variable 2: 'ID_TENEN_VIV' 'Régimen de tenencia de la vivienda'

## Una vez instalada la libría, lo primero que debemos realizar es su importación

from censosine21 import CensosINE21
# Creamos un instancia un objeto de la clase CensosINE21
hogares = CensosINE21()

# Podemos comprobar que los atributos están vacíos
print(hogares)

# Los primeros cuatros atributos son los necesarios para realizar la petición de datos.
# - table
# - metrics
# - variables
# - language

# Los dos atributos siguientes son los parámeteros necesarios para hacer la petición.
# - params: json de parámetros para hacer el POST
# - api_url: ULR oficial de la API del INE

# Para terminar, contamos con los dos atributos que almacenan los datos obtenidos en la petición POST a la API
# - metata
# - data

## Podemos previamento usar los métodos estáticos para obtener información sobre la propia API
hogares.show_tables()
hogares.show_metrics('hog')
hogares.show_variables('hog')

# Ya que conocemos los parámetros a pasar realizamos la Petición de datos con el método de clase post()
hogares.post("hog", 'SHOGARES', ['ID_RESIDENCIA_N2', 'ID_TENEN_VIV' ], "ES")

# La librería también está preparada para informarnos de errores
## Ej 1. Error en el nombre de la tabla. La tabla hog2 no existe
## hogares.post("hog2", "SHOGARES", ["ID_TAM_HOG_6"], "ES")

## Ej 2. Error en el nombre de la unidad de métidoa. "SHOGARES2" no es una métrica de la tabla  "hog"
## hogares.post("hog", "SHOGARES2", ["ID_TAM_HOG_6"], "ES")

#  Tras realizar la consulta a la API el objeto ya cuenta con información en sus atributos
print(hogares)

# Y podemos ver sus atributos

print(hogares.metrics)
print(hogares.variables)
print(hogares.language)
print(hogares.api_url)
print(hogares.params)
print(hogares.metadata)
print(hogares.data)


# Si lo deseamos podemos convertir los resultados del atributo data a un archivo CSV.
# Esto se realiza con el método to_csv() indicando la ruta y nombre del csv añadiendo la extensión.

hogares.to_csv('nhorares_regimen_provincias.csv')

# Para terminar, con el método filter() podemos ver los datos del atributo data filtrando por una de las variables
# En el ejemplo, limitamos los datos a la provicia de Asturias
hogares_filter_asturias = hogares.filter('ID_RESIDENCIA_N2', 'asturias')
print(hogares_filter_asturias)

## y crear igualmente un csv con los datos filtrados.
hogares.to_csv('nhorares_regimen_asturias.csv','ID_RESIDENCIA_N2', '33 Asturias')

