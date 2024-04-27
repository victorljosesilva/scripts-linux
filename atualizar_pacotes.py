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

