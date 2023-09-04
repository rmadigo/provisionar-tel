"""Funcao main"""
import json
import os
from time import sleep
from tqdm import tqdm
from device import scan

"""Barra de prograsso TIME"""
def delay():
    for i in tqdm(range(10)):
        pass

CAMINHO_ARQUIVO_SAIDA = "aparelhos_localizados.json"

if __name__ == "__main__":
    while True:
        print("Provisionamento")

        with open(CAMINHO_ARQUIVO_SAIDA, "a+", encoding="utf-8") as arquivo:
            arquivo.seek(0, os.SEEK_END)
            if not arquivo.tell() == 0:
                arquivo.seek(0)
                aparelhos_localizados = json.load(arquivo)
                arquivo.truncate(0)
                print("Arquivo carregado")
                lista_device = scan(aparelhos_localizados)
                json.dump(lista_device, arquivo, ensure_ascii=False, indent=2)

            else:
                aparelhos_localizados = []
                lista_device = scan(aparelhos_localizados)
                arquivo.truncate()
                json.dump(lista_device, arquivo, ensure_ascii=False, indent=2)
        break
        # sleep(10)

