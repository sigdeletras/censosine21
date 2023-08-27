## Una vez instalada la libría, lo primero que debemos realizar es su importación

from censosine21 import CensosINE21


# La clase cuenta con métodos estáticos, es decir que pueden ser usados sin necesidad de instanciar un objeto
# que ofree obtener información sobre los parámetros de la API, en concreto el listado de tablas disponibles,
# las métricas o unidades de medida y las variables para cada tabla.

# Muestra las entidades del tipo tablas disponibles de la API
print(20 * '-' + 'Tablas' + 20 * '-')
CensosINE21.show_tables()

# Muestras en pantalla un diccionario con las entidades de tipo métricas de la API
print(20 * '-' + 'Métricas' + 20 * '-')
CensosINE21.show_metrics()

# Muestras en pantalla un diccionarios con las entidades de tipo métricas de la API filtrado por tabla
print(20 * '-' + 'Métricas filtradas por tabla hog' + 20 * '-')
CensosINE21.show_metrics('hog')


## Muestra en pantalla un diccionario con las entidades de tipo variables de la API
print(20 * '-' + 'Variables' + 20 * '-')
CensosINE21.show_variables()

## Muestras las entidades de tipo variable  de la API filtradas por un tipo de tabla
print(20 * '-' + 'Variables filtradas por tabla nuc' + 20 * '-')
CensosINE21.show_variables('nuc')

# Contamos también con la presentanciación de mensajes de errores si el nombre de la tabla es incorrecto.
CensosINE21.show_metrics('hog2')
CensosINE21.show_variables('nuc2')
