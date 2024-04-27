import shutil
import os
import datetime
import zipfile

def fazer_backup(diretorio_origem, diretorio_destino):
    if not os.path.exists(diretorio_origem):
        print(f"Erro: O diretório de origem '{diretorio_origem}' não existe.")
        return
    
    if not os.path.exists(diretorio_destino):
        try:
            os.makedirs(diretorio_destino)
        except OSError as e:
            print(f"Erro ao criar o diretório de destino: {e}")
            return

    timestamp = datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
    nome_backup = f"backup_{timestamp}"
    destino_backup = os.path.join(diretorio_destino, nome_backup)

    try:
        with zipfile.ZipFile(destino_backup + ".zip", 'w', zipfile.ZIP_DEFLATED) as zipf:
            for root, dirs, files in os.walk(diretorio_origem):
                for file in files:
                    zipf.write(os.path.join(root, file), os.path.relpath(os.path.join(root, file), diretorio_origem))
        print(f"Backup compactado criado com sucesso em: {destino_backup}.zip")
    except Exception as e:
        print(f"Erro ao compactar os arquivos: {e}")
        return

    try:
        print(f"Backup criado com sucesso em: {destino_backup}")
    except Exception as e:
        print(f"Erro ao fazer backup: {e}")

