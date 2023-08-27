import csv

t1 = 'SDC21_tablas_disponibles.csv'
t2 = 'SDC21_idiomas.csv'
t3 = 'SDC21_unidades_medida_disponibles.csv'
t4 = 'SDC21_variables_disponibles.csv'

def csv_to_dict(csv_filename):
    result = []
    with open(csv_filename, encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            result.append(row)
    return result


TABLES = csv_to_dict(t1)
LANGUAGES = csv_to_dict(t2)
METRICTS = csv_to_dict(t3)
VARIABLES = csv_to_dict(t4)


