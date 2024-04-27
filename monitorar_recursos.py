import psutil
import logging

def monitorar_recursos():
    try:
        uso_cpu = psutil.cpu_percent()
        uso_memoria = psutil.virtual_memory().percent
        uso_disco = psutil.disk_usage('/').percent

        print(f"Uso da CPU: {uso_cpu}%")
        print(f"Uso de Memória: {uso_memoria}%")
        print(f"Uso de Disco: {uso_disco}%")

        logging.basicConfig(filename='monitoramento_recursos.log', level=logging.INFO, format='%(asctime)s - %(message)s')
        logging.info(f"Uso da CPU: {uso_cpu}%")
        logging.info(f"Uso de Memória: {uso_memoria}%")
        logging.info(f"Uso de Disco: {uso_disco}%")
    except Exception as e:
        print(f"Erro ao monitorar recursos do sistema: {e}")
        logging.error(f"Erro ao monitorar recursos do sistema: {e}")


if __name__ == "__main__":
    monitorar_recursos()