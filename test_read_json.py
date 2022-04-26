import os
import json
from dotenv import load_dotenv

load_dotenv()

FILEPATH = os.getenv('FILEPATH')

def readJsonFile(file):
     with open(file) as json_file:
        return json.load(json_file)

def test_readJsonFile():
    expectedJson = {
                    "id": 1,
                    "valor": 100
                }
    assert readJsonFile(FILEPATH) == expectedJson

def main():
    print(readJsonFile(FILEPATH))

if __name__ == '__main__':
    main()