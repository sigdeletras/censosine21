# API para la consulta de los Censos de Población y Viviendas 2021

[https://www.ine.es/dyngs/DataLab/es/manual.html?cid=1259945952385](https://www.ine.es/dyngs/DataLab/es/manual.html?cid=1259945952385)

El servicio permite la consulta de datos del Sistema de Difusión de los Censos de Población y Viviendas 2021 (SDC21).

Únicamente se considera el método POST para recuperar la información.

Este servicio se invoca con la estructura de parámetros documentada a continuación.


Clase para interactur con la API del Instituto Nacional de Estadística (INE) de España  que ofrece los datos Sistema de Difusión de los Censos de Población y Viviendas 2021 (SDC21)

## Parámetros

- "idioma": "EN". Idiomas en los que se puede mostrar los resultados
- "metrica":["SPERSONAS"].  Unidades de medida (métricas) disponibles para cada tabla
- "tabla":"per.ppal" Tablas disponibles
- "variables": ["ID_RESIDENCIA_N1","ID_SEXO"]. unidades de medida (métricas) disponibles para cada tabla. Máximo 4

La petición devuelve los datos que corresponden a una selección de un mínimo de 1 variable y hasta un máximo de 4 variables por tabla.

Descripción de parámetros

- lista de tablas disponibles.
- lista de las variables disponibles para cada tabla.
- lista de las unidades de medida (métricas) disponibles para cada tabla.
- lista de idiomas en los que se puede mostrar el resultado de la consulta.

## Respuesta Json
```json
{
"Metadata": [
      {
            "Column": "ID_RESIDENCIA_N1"
      },
      {
            "Column": "ID_SEXO"
      },
      {
            "Column": "SPERSONAS"
      }
],
"Data": [
      {
            "ID_RESIDENCIA_N1": "Andalucia",
            "ID_SEXO ": "Hombre",
            "SPERSONAS": 4182618
      },
      ...
      ]
}

```

## Limitaciones de servicio

El uso de la API se rige por las mismas condiciones que el SDC21. Además, se limita inicialmente a 2 el número de peticiones concurrentes que pueden estar activas a través de la API.

Aquellas consultas que se consideren significativamente grandes para la ejecución y respuesta en vivo no serán procesadas, en este caso el objeto de respuesta será:

````json
{
      "Debido al tamaño de la consulta ésta no puede ser procesada por el sistema"
}
````

## Errores en las respuestas

Para los errores controlados de la aplicación, el objeto de respuesta será:

````json
{
      "error":"texto descriptivo del problema"
}
````
