import hashlib
import logging
import os

def calcular_hash(arquivo):
    if not os.path.exists(arquivo):
        print(f"Erro: O arquivo '{arquivo}' não existe.")
        return None

    logging.basicConfig(filename='calculo_hash.log', level=logging.INFO, format='%(asctime)s - %(message)s')

    try:
        hash_md5 = hashlib.md5()
        with open(arquivo, "rb") as f:
            for parte in iter(lambda: f.read(4096), b""):
                hash_md5.update(parte)
        hash_hex = hash_md5.hexdigest()
        logging.info(f"Hash MD5 do arquivo '{arquivo}': {hash_hex}")
        return hash_hex
    except Exception as e:
        print(f"Erro ao calcular hash do arquivo: {e}")
        logging.error(f"Erro ao calcular hash do arquivo: {e}")
        return None

arquivo = "/caminho/do/arquivo"
def imprime_resultado():
    hash_resultado = calcular_hash(arquivo)
    if hash_resultado:
        print(f"Hash MD5 do arquivo '{arquivo}': {hash_resultado}")

if __name__ == "__main__":
    imprime_resultado()
