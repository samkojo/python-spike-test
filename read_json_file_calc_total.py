import os
import json
from dotenv import load_dotenv

load_dotenv()

FILEPATH = os.getenv('FILEPATH')

def readJsonFile(file):
     with open(file) as json_file:
        return json.load(json_file)

def calcTotal(itens):
    sum = 0
    for item in itens:
        sum += item['total']
    return sum

def main():
    print(calcTotal(readJsonFile(FILEPATH)))

if __name__ == '__main__':
    main()