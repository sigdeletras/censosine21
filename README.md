# censosine21

Python library to interact with the API of the National Institute of Statistics ([INE](https://www.ine.es/) ) of Spain that offers the data Dissemination System of the Population and Housing Censuses 2021 (SDC21)

## Installation

censosine21 package is available as an open source library published at [PyPI](https://pypi.org/project/censosine21/).
You can install censosine2021 by simply executing this command:

```bash
pip install censosine21
```

If you already have installed censosine21, you can upgrade it using:
```bash
pip install censosine21 --upgrade
```

## Kick off

The first step to use censosine21 is creating our DatasetINE object. 
```python
from censosine21 import CensosINE21

hogares = CensosINE21()
hogares.post("hog", 'SHOGARES', ['ID_RESIDENCIA_N2', 'ID_TENEN_VIV' ], "ES")
```
En este primer momento, los atributos del objeto no cuentan con datos. Usando el método post() la librería realizará la petición a la API según los parámetros indicados (table, métrica, variables e idioma) y descargará los datos de la consulta.

```python
hogares.post("hog", 'SHOGARES', ['ID_RESIDENCIA_N2', 'ID_TENEN_VIV' ], "ES")
```

## Objet attributes

- table
- metrics
- variables
- language
- params: json de parámetros para hacer el POST
- api_url: ULR oficial de la API del INE
- metata: almacenan los datos obtenidos en la petición POST a la API
- data
### Conversión a formato CSV y filtros

Una vez realizada la consulta la clase cuenta con el método to_csv() para guardar los datos del atributo data a formato CSV

```python
hogares.to_csv('csv/nhorares_regimen_provincias.csv')

```

Es también posible filtrar el dataset indicando el par clave valor a partir de la variable y el texto de filtro usando el método filter().

```python
hogares_filter_asturias = hogares.filter('ID_RESIDENCIA_N2', 'asturias')
```

Esta misma opción de filtrado también está disponible en el método to_csv()

```python
hogares.to_csv('csv/nhorares_regimen_asturias.csv','ID_RESIDENCIA_N2', '33 Asturias')
```

### Show API entities info

La librería posee un cojunto de métodos estáticos para acceder a la información de las tablas, unidades de médida y variables de la API.
Las ser métodos estáticos no es necesario instanciar un objeto para usarlo. Simplemente usamos la clase y el método de consulta

```python
from censosine21 import CensosINE21

CensosINE21.show_tables()
CensosINE21.show_metrics()
CensosINE21.show_variables()
CensosINE21.show_languajes()
```

La información sobre métricas y variables puede ser filtrada por tabla.

```python
CensosINE21.show_metrics('hog')
CensosINE21.show_variables('nuc')
```
### Looking for more examples?

Get the source code in my [github repo](https://github.com/sigdeletras/censosine21).
There are more examples at /examples directory
## Links

You can get more info about how INE API works, URLs Definitions or how to get table identifiers,
in the [INE official page](https://www.ine.es/dyngs/DataLab/es/manual.html?cid=1259945952385)

## License

Shield: [![CC BY-SA 4.0][cc-by-sa-shield]][cc-by-sa]

*censosine2021* by [Patricio Soriano](https://github.com/sigdeletras) is licensed under a
[Creative Commons Attribution-ShareAlike 4.0 International License][cc-by-sa].

[![CC BY-SA 4.0][cc-by-sa-image]][cc-by-sa]

[cc-by-sa]: http://creativecommons.org/licenses/by-sa/4.0/
[cc-by-sa-image]: https://licensebuttons.net/l/by-sa/4.0/88x31.png
[cc-by-sa-shield]: https://img.shields.io/badge/License-CC%20BY--SA%204.0-lightgrey.svg
