import os
import subprocess
import logging
import socket

def verificar_permissao_superusuario():
    if os.geteuid() != 0:
        print("Erro: Esse script precisa ser executado com permissões de superusuário (root).")
        exit(1)

