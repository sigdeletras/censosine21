# censosine21

Python library to interact with the API of the National Institute of Statistics ([INE](https://www.ine.es/en/index.htm) ) of Spain that offers the data [Dissemination System of the Population and Housing Censuses 2021 (SDC21)](https://www.ine.es/dyngs/INEbase/es/operacion.htm?c=Estadistica_C&cid=1254736176992&menu=ultiDatos&idp=1254735572981#:~:text=%C3%9Altima%20Nota%20de%20prensa&text=En%20Espa%C3%B1a%20hab%C3%ADa%2018.539.223,2.514.511%20de%20uso%20espor%C3%A1dico.)

Read this in [Spanish](https://github.com/sigdeletras/censosine21/blob/master/README.es-ES.md)

## Installation

The *censosine21* package is available as an open source library published at [PyPI](https://pypi.org/project/censosine21/).
You can install censosine2021 by simply executing this command:

```bash
pip install censosine21
```

If you already have installed *censosine21*, you can upgrade it using:
```bash
pip install censosine21 --upgrade
```

## Kick off

The first step to use *censosine21* is creating the *CensosINE21* object. 
```python
from censosine21 import CensosINE21

hogares = CensosINE21()
hogares.post("hog", 'SHOGARES', ['ID_RESIDENCIA_N2', 'ID_TENEN_VIV' ], "ES")
```
At this first moment, the object's attributes have no data. Using the *post()* method, the library will make the request to the API according to the indicated parameters (table, metrics, variables and language) and will download the query data (metadata and data).

```python
hogares.post("hog", 'SHOGARES', ['ID_RESIDENCIA_N2', 'ID_TENEN_VIV' ], "ES")
```

## Objet attributes

- table: Data set available from SDC21
- metrics: Unit of measure
- variables: Variables
- language: Language used for the results
- params: JSON of parameters to make the POST request to the API
- api_url: official URL of the INE API
- metadata: Metadata of the response JSON
- data: Response JSON data
### Conversion to CSV format and filters

Once the query is made, the class has the *to_csv()* method to save the data from the data attribute in CSV format.

```python
hogares.to_csv('csv/nhorares_regimen_provincias.csv')

```

It is also possible to filter the dataset by indicating the key-value pair from the variable and the filter text using the *filter()* method.

```python
hogares_filter_asturias = hogares.filter('ID_RESIDENCIA_N2', 'asturias')
```

This same filtering option is also available in the *to_csv()* method.

```python
hogares.to_csv('csv/nhorares_regimen_asturias.csv','ID_RESIDENCIA_N2', '33 Asturias')
```

### Show API entities info

The library has a set of static methods to access the information from the tables, units of measurement and API variables and their description in Spanish and English.

Being static methods, it is not necessary to instantiate an object to use it. We just use the class and the query method

```python
from censosine21 import CensosINE21

CensosINE21.show_tables()
CensosINE21.show_metrics()
CensosINE21.show_variables()
CensosINE21.show_languajes()
```


Information about metrics and variables can be filtered by table.

```python
CensosINE21.show_metrics('hog')
CensosINE21.show_variables('nuc')
```
### Looking for more examples?

Get the source code from the [github repository](https://github.com/sigdeletras/censosine21).

There are more examples in the [/examples](https://github.com/sigdeletras/censosine21/tree/master/examples) directory.
## Links


You can obtain more information about how the INE API works on the [INE official documentation page](https://www.ine.es/dyngs/DataLab/es/manual.html?cid=1259945952385)

## License


The *censosine21* library is developed by [Patricio Soriano](https://www.linkedin.com/in/patriciosorianocastro/) [@sigdeletras](https://twitter.com/sigdeletras) under license
[MIT License](LICENSE.md).


