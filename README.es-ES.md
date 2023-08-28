# censosine21

Librería Python para interactuar con la API del Instituto Nacional de Estadística ([INE](https://www.ine.es/)) que ofrece datos del [Sistema de Difusión de los Censos de Población y Viviendas 2021 (SDC21)](https://www.ine.es/dyngs/INEbase/es/operacion.htm?c=Estadistica_C&cid=1254736176992&menu=ultiDatos&idp=1254735572981#:~:text=%C3%9Altima%20Nota%20de%20prensa&text=En%20Espa%C3%B1a%20hab%C3%ADa%2018.539.223,2.514.511%20de%20uso%20espor%C3%A1dico.).

Read this in [English](https://github.com/sigdeletras/censosine21/blob/master/README.md).

## Instalación

El paquete **censosine21** está disponible como una librería de código abierto en [PyPI](https://pypi.org/project/censosine21/).

Puedes instalar **censosine21** ejecutando el siguiente comando:
```bash
pip install censosine21
```

Si ya tienes instaladao **censosine21**, puedes actualizarlo usando:
```bash
pip install censosine21 --upgrade
```

## Primer paso

El primer paso para utilizar *censosine21* es crear un objeto *CensosINE21*.
```python
from censosine21 import CensosINE21

hogares = CensosINE21()
```
En este primer momento, los atributos del objeto no cuentan con datos. Usando el método *post()* la librería realizará la petición a la API según los parámetros indicados (tabla, unidad de medida, variables e idioma) y descargará los datos de la consulta (metadata y data).

```python
hogares.post("hog", 'SHOGARES', ['ID_RESIDENCIA_N2', 'ID_TENEN_VIV' ], "ES")
```

## Atributos del objeto

- table: Conjunto de datos disponibles del SDC21
- metrics: Unidad de médida
- variables: Variables 
- language: Lenguaje usado para los resultados
- params: json de parámetros para hacer la petición POST a la API
- api_url: ULR oficial de la API del INE
- metadata: Metadatos del JSON de respuesta
- data: Datos del JSON de respuesta
 
## Conversión a formato CSV y filtros

Una vez realizada la consulta, la clase cuenta con el método *to_csv()* para guardar los datos del atributo data a formato CSV

```python
hogares.to_csv('csv/nhorares_regimen_provincias.csv')
```

Es también posible filtrar el conjunto de datos indicando el par clave-valor a partir de la variable y el texto de filtro usando el método *filter()*.

```python
hogares_filter_asturias = hogares.filter('ID_RESIDENCIA_N2', 'asturias')
```

Esta misma opción de filtrado también está disponible en el método **to_csv()**

```python
hogares.to_csv('csv/nhorares_regimen_asturias.csv','ID_RESIDENCIA_N2', '33 Asturias')
```

## Mostrar información de las entidades de la API

La librería posee un cojunto de métodos estáticos para acceder a la información de las tablas, unidades de médida y variables de la API y su descripción en español e inglés.

Al ser métodos estáticos no es necesario instanciar un objeto para usarlo. Simplemente usamos la clase y el método de consulta

```python
from censosine21 import CensosINE21

CensosINE21.show_tables()
CensosINE21.show_metrics()
CensosINE21.show_variables()
CensosINE21.show_languages()
```

La información sobre métricas y variables puede ser filtrada por tabla.

```python
CensosINE21.show_metrics('hog')
CensosINE21.show_variables('nuc')
```
## ¿Más ejemplos?

Obtenga el código fuente en el [repositorio de github](https://github.com/sigdeletras/censosine21).

Hay más ejemplos en el directorio [/examples](https://github.com/sigdeletras/censosine21/tree/master/examples).

## Enlace oficial

Puedes obtener más información sobre cómo funciona la API del INE en la [página oficial de documentación del INE](https://www.ine.es/dyngs/DataLab/es/manual.html?cid=1259945952385)

## Licencia

La librería *censosine21* está desarrollada por [Patricio Soriano](https://www.linkedin.com/in/patriciosorianocastro/) [@sigdeletras](https://twitter.com/sigdeletras) bajo licencia
[MIT License.](LICENSE.md)


