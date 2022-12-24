import math
tamanho_bloco = 3*1024 #t    em kilobyte

tamanho_registro = int(input("tamanho do registro em bytes = ")) # r
n_registros = int(input("numero de registros = ")) # n

fator_de_bloco = math.floor(tamanho_bloco / tamanho_registro) # f
espaco_inutilizado = tamanho_bloco - (fator_de_bloco * tamanho_registro)
n_blocos = math.ceil(n_registros / fator_de_bloco) # b
consumo_de_espaco = n_blocos * tamanho_bloco
consumo_em_megabytes = (consumo_de_espaco/1024)/1024

print()
print(f'F/blocagem     = {fator_de_bloco}')
print(f'U/inutilizado  = {espaco_inutilizado} Bytes')
print(f'B/blocos       = {n_blocos}')
print(f'Consumo espaco = {consumo_de_espaco} Bytes / {consumo_em_megabytes} MegaBytes')

