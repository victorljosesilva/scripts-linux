import os
import logging

<<<<<<< HEAD
def limpar_temporarios(diretorio):
    if not os.path.exists(diretorio):
        print(f"Erro: O diretório '{diretorio}' não existe.")
        return

    logging.basicConfig(filename='limpeza_temporarios.log', level=logging.INFO, format='%(asctime)s - %(message)s')

    try:
        total_removidos = 0
        for raiz, dirs, arquivos in os.walk(diretorio):
            for arquivo in arquivos:
                if arquivo.endswith(".tmp"):
                    caminho_arquivo = os.path.join(raiz, arquivo)
                    os.remove(caminho_arquivo)
                    logging.info(f"Arquivo temporário removido: {caminho_arquivo}")
                    total_removidos += 1
        print(f"Total de arquivos temporários removidos: {total_removidos}")
    except Exception as e:
        print(f"Erro ao limpar arquivos temporários: {e}")
        logging.error(f"Erro ao limpar arquivos temporários: {e}")

diretorio = # "/caminho/do/diretorio"