import pytest
from censosine21 import CensosINE21

@pytest.fixture
def censos_instance():
    return CensosINE21()

def test_show_tables( censos_instance):
    censos_instance.show_tables()
    assert True

def test_show_languages( censos_instance):
    censos_instance.show_languages()
    assert True

def test_show_metrics_all(censos_instance):
    all_metrics = censos_instance.show_metrics()
    assert all_metrics is True

def test_show_metrics_filtered(censos_instance):
    table_metrics = censos_instance.show_metrics('hog')
    assert table_metrics is True

def test_show_metrics_filtered_error(censos_instance):
    error_table_metrics = censos_instance.show_metrics('hog2')
    assert error_table_metrics is False

def test_show_variables_all(censos_instance):
    all_variables = censos_instance.show_variables()
    assert all_variables is True

def test_show_variables_filtered(censos_instance):
    table_variables = censos_instance.show_variables('nuc')
    assert table_variables is True

def test_show_variables_filtered_error(censos_instance):
    error_table_variables = censos_instance.show_variables('nuc2')
    assert error_table_variables is False


