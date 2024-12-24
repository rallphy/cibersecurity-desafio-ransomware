import os
import pyaes
import glob

## encontrar o arquivo com a extensão .ransom
files = glob.glob("*.ransom")
if not files:
    print("Nenhum arquivo .ransom encontrado.")
    exit()

file_name = files[0]

## abrir o arquivo criptografado
file = open(file_name, "rb")
file_data = file.read()
file.close()

## chave para descriptografia
key = b"testeransomwares"
aes = pyaes.AESModeOfOperationCTR(key)
decrypt_data = aes.decrypt(file_data)

## remover o arquivo criptografado
os.remove(file_name)

## criar o arquivo descriptografado
new_file = file_name.replace(".ransom", "")
new_file = open(f'{new_file}', "wb")
new_file.write(decrypt_data)
new_file.close()
