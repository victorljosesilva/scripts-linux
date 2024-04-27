def monitorar_logs(arquivo_log, num_linhas=None):
    if not os.path.exists(arquivo_log):
        print(f"Erro: O arquivo de log '{arquivo_log}' não existe.")
        return

    try:
        with open(arquivo_log, "r") as f:
            if num_linhas is not None:
                linhas = f.readlines()[-num_linhas:]
            else:
                linhas = f.readlines()
            for linha in linhas:
                print(linha, end='')
        print("Monitoramento de logs concluído.")
    except Exception as e:
        print(f"Erro ao monitorar logs do arquivo: {e}")

arquivo_log = "/caminho/do/arquivo.log"

num_linhas = 10

if __name__ == "__main__":
    monitorar_logs(arquivo_log, num_linhas)
