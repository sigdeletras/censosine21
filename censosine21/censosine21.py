import requests
import csv
from .entities import TABLES, LANGUAGES, METRICS, VARIABLES

from dataclasses import dataclass


def _is_valid_table(table: str) -> bool:
    """
    Check if the provided table name is valid.

    Args:
        table (str): The name of the table to be checked.

    Returns:
        bool: True if the table is valid, False otherwise.
    """
    if any(table in entry.values() for entry in TABLES):
        return True
    print(f"Error. There is not any table with name '{table}' in the API")
    return False


def _filter_metrics_by_table(table: str):
    """
    Filter available metrics based on the provided table name.

    Args:
        table (str): The name of the table to filter metrics for.

    Returns:
        list: A list of filtered metrics.
    """
    return [item for item in METRICS if item.get('table') == table]


def _is_valid_metrics(table: str, metrics: str, metrics_filtered: list) -> bool:
    """
    Check if the provided metric name is valid for the given table.

    Args:
        table (str): The name of the table.
        metrics (str): The name of the metric to be checked.
        metrics_filtered (list): List of filtered metrics for the given table.

    Returns:
        bool: True if the metric is valid for the table, False otherwise.
    """
    if any(metrics in entry.values() for entry in metrics_filtered):
        return True
    print(f"Error. There is no metric with name '{metrics}' in the table '{table}'")
    return False


def _filter_variables_by_table(table: str):
    """
    Filter available variables based on the provided table name.

    Args:
        table (str): The name of the table to filter variables for.

    Returns:
        list: A list of filtered variables.
    """
    return [item for item in VARIABLES if item.get('table') == table]


def _is_valid_variables(table: str, variable: str, variables_filtered: list) -> bool:
    """
    Check if the provided variable name is valid for the given table.

    Args:
        table (str): The name of the table.
        variable (str): The name of the variable to be checked.
        variables_filtered (list): List of filtered variables for the given table.

    Returns:
        bool: True if the variable is valid for the table, False otherwise.
    """
    if any(variable in entry.values() for entry in variables_filtered):
        return True
    print(f"Error. There is no metric with name '{variable}' in the table '{table}'")
    return False


@dataclass
class CensosINE21:
    """
    Class to interact with the API of the National Institute of Statistics (INE) of Spain
    that offers the data Dissemination System of the Population and Housing Censuses 2021 (SDC21)

    More information at https://www.ine.es/dyngs/DataLab/es/manual.html?cid=1259945952385

    Attributes:
        table (str): The name of the table.
        metrics (str): The name of the metric.
        variables (list): A list of variables.
        language (str): The language for API responses.
        params (list): Additional parameters for API requests.
        api_url (str): The URL of the INE API.
        metadata (list): Metadata information from API responses.
        data (list): Data retrieved from API responses.
    """
    table: str = None
    metrics: str = None
    variables: list = None
    language: str = 'ES'
    params: list = None
    api_url: str = 'https://www.ine.es/Censo2021/api'
    metadata: list = None
    data: list = None

    @staticmethod
    def show_tables() -> None:
        """
        Display the list of available APIS tables.
        """
        for item in TABLES:
            print(item)
        return True

    @staticmethod
    def show_languages() -> None:
        """
        Display the list of available API languages.
        """
        for item in LANGUAGES:
            print(item)
        return True

    @staticmethod
    def show_metrics(table: str = '') -> None:
        """
        Display available API metrics, optionally filtered by a specific table.

        Args:
            table (str, optional): The name of the table to filter metrics.
            If not provided, all available metrics will be displayed.
        """
        check = False
        if table == '':
            for item in METRICS:
                print(item)
                check = True
        else:
            if any(table in entry.values() for entry in TABLES):
                metrics_filtered = [item for item in METRICS if item.get('table') == table]
                for item in metrics_filtered:
                    print(item)
                check = True
            else:
                print(f"Error. There is not a table with name '{table}' in the API")
                check = False

        return check

    @staticmethod
    def show_variables(table: str = '') -> None:
        """
        Display available API variables, optionally filtered by a specific table.

        Args:
            table (str, optional): The name of the table to filter variables.
            If not provided, all available variables will be displayed.
        """
        if table == '':
            for item in VARIABLES:
                print(item)
                return True
        else:
            if any(table in entry.values() for entry in TABLES):
                variables_filtered = [item for item in VARIABLES if item.get('table') == table]
                for item in variables_filtered:
                    print(item)
                return True
            else:
                print(f"Error. There is not a table with name '{table}' in the API")
                return False

    def post(self, table: str, metrics: str, variables: list, language='ES') -> dict:
        """
        Make a POST request to the INE API.

        Args:
            table (str): The name of the table to retrieve data from.
            metrics (str): The name of the metric.
            variables (list): A list of variables.
            language (str, optional): The language for API responses. Default is 'ES'.

        Returns:
            dict: The API response as a dictionary.
        """
        if not _is_valid_table(table):
            return

        metrics_filtered = _filter_metrics_by_table(table)

        if not _is_valid_metrics(table, metrics, metrics_filtered):
            return

        variables_filtered = _filter_variables_by_table(table)
        for variable in variables:
            if not _is_valid_variables(table, variable, variables_filtered):
                return


        self.params = {
            "tabla": table,
            "idioma": language,
            "metrica": [metrics],
            "variables": variables
        }

        try:
            headers = {'Content-type': 'application/json'}
            response = requests.post(self.api_url, json=self.params, headers=headers)
            #response.raise_for_status()
            response_json = response.json()

            self.table = table
            self.language = language
            self.metrics = metrics
            self.variables = variables
            self.metadata = response_json['metadata']
            self.data = response_json['data']

            return response_json
        except requests.exceptions.RequestException as e:
            raise Exception(f"Error making POST request: {e}")

    def to_csv(self, filename: str, key: str = None, value: str = None) -> None:
        """
        Write retrieved data to a CSV file.

        Args:
            filename (str): The name of the CSV file to write to.
            key (str, optional): Filter data based on this key. Default is None.
            value (str, optional): Value to match when filtering data. Default is None.
        """
        if not self.data or not isinstance(self.data, list) or not isinstance(self.data[0], dict):
            raise ValueError("Invalid data format. Expecting a list of dictionaries.")

        columns_name = list(self.data[0].keys())

        with open(filename, mode='w', newline='', encoding='utf-8') as file_csv:
            writer = csv.DictWriter(file_csv, fieldnames=columns_name)

            writer.writeheader()

            if key:
                data_filtered = [item for item in self.data if item.get(key) == value]
                for row in data_filtered:
                    writer.writerow(row)
            else:
                for row in self.data:
                    writer.writerow(row)

    def filter(self, key: str, value: str) -> list:
        """
        Filter data based on a specific key-value pair.

        Args:
            key (str): The key to filter by.
            value (str): The value to match.

        Returns:
            list: List of filtered data.
        """
        data_filter = [item for item in self.data if item.get(key) == value]
        return data_filter
