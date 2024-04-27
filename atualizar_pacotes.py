import os
import subprocess
import logging
import socket

def verificar_permissao_superusuario():
    if os.geteuid() != 0:
        print("Erro: Esse script precisa ser executado com permissões de superusuário (root).")
        exit(1)

def verificar_conexao_internet():
    try:
        host = "www.google.com"
        socket.create_connection((host, 80), 2)
        print("Conexão com a internet estabelecida.")
    except OSError:
        print("Erro: Não foi possível estabelecer conexão com a internet.")
        exit(1)

def atualizar_pacotes():
    logging.basicConfig(filename='atualizacao_pacotes.log', level=logging.INFO, format='%(asctime)s - %(message)s')

    try:
        subprocess.run(["sudo", "apt", "update"], check=True)
        resultado_upgrade = subprocess.run(["sudo", "apt", "upgrade", "-y"], capture_output=True, text=True)
        logging.info(resultado_upgrade.stdout)
        if resultado_upgrade.returncode == 0:
            print("Atualização de pacotes concluída com sucesso.")
        else:
            print("Erro ao atualizar pacotes. Verifique o arquivo de log para mais detalhes")
            logging.error(resultado_upgrade.stderr)
    except subprocess.CalledProcessError as e:
        print(f"Erro ao executar comando: {e}")
        logging.error(f"Erro ao executar comando: {e}")


