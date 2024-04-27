import os
import logging

def alterar_permissao_arquivos(diretorio, permissao):
    if not os.path.exists(diretorio):
        print(f"Erro: O diretório '{diretorio}' não existe.")
        return

    logging.basicConfig(filename='alteracao_permissao.log', level=logging.INFO, format='%(asctime)s - %(message)s')

    try:
        for raiz, dirs, arquivos in os.walk(diretorio):
            for arquivo in arquivos:
                caminho_arquivo = os.path.join(raiz, arquivo)
                os.chmod(caminho_arquivo, permissao)
                logging.info(f"Permissões alteradas para {caminho_arquivo} para {permissao:o}")
        print("Permissões alteradas com sucesso.")
    except Exception as e:
        print(f"Erro ao alterar permissões: {e}")
        logging.error(f"Erro ao alterar permissões: {e}")

