import os
from dotenv import load_dotenv
import read_json_file_calc_total
import pytest

load_dotenv()

FILEPATH = os.getenv('FILEPATH')

@pytest.fixture
def example_json():
    ''' Exemplo de dados '''
    return [{
        "id": 1,
        "total": 100
    },
    {
        "id": 2,
        "total": 200
    },
    {
        "id": 2,
        "total": 300
    }
    ]

def test_readJsonFile(example_json):
    ''' Verifica se o arquivo está sendo lido corretamente '''

    assert read_json_file_calc_total.readJsonFile(FILEPATH) == example_json

def test_calcTotal(example_json):
    assert read_json_file_calc_total.calcTotal(example_json) == 600
