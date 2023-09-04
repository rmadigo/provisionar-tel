import logging
import sys

# Configurações de formatação
formatter = logging.Formatter('%(asctime)s | %(levelname)s | %(message)s')

# Configuração do logger
logger = logging.getLogger()
logger.setLevel(logging.INFO)

# Manipulador de saída para console
stdout_handler = logging.StreamHandler(sys.stdout)
stdout_handler.setLevel(logging.DEBUG)
stdout_handler.setFormatter(formatter)
logger.addHandler(stdout_handler)

# Manipulador de saída para arquivo de log
file_handler = logging.FileHandler('logs.log')
file_handler.setLevel(logging.DEBUG)
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)
