# python-spike-test
 Exemplo simples de modelo proposto em spike python

Exemplo de Spike:
- Leitura de arquivo JSON contendo linhas de itens de pedidos e retornar total

# README.md

Spike demonstrando a leitura de arquivos JSON contendo linhas de itens de pedidos e retornar total
## **Requisitos**

- `python` - [Link](https://www.python.org/downloads/release/python-3104/)
```bash
python3 --version
```

- `pip` - [Link](https://github.com/pypa/get-pip#usage)
```bash
pip3 --version
```

## 1.Ambiente virtual e instalação de dependências Python

```bash
python3 -m venv .venv;source .venv/bin/activate;
pip install -r requirements.txt
cp example.env .env
```

## 2.Execução
- Ao executar será lido o arquivo `test.json` e impresso na tela
```bash
python read_json_file_calc_total.py
```
- Retorno esperado:
```bash
600
```

## 3.Execução de teste
- Para rodar o teste unitário
```bash
pytest
```

## Extra
Caso queira verificar a leitura de um outro arquivo, pode fazer a alteração do caminho do arquivo via variavel `FILEPATH` no arquivo `.env`
Obs.: caso mude o arquivo o teste automatizado somente retornará positivo caso o conteúdo seja:
```json
[{
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
}]
```