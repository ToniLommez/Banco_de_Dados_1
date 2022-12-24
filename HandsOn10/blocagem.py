import math
# tamanho_bloco = int(input("tamanho do bloco em disco = "))*1024 #t    em kilobyte
tamanho_bloco = 2*1024 #t    em kilobyte

tamanho_registro = int(input("tamanho do registro = ")) # r
n_registros = int(input("numero de registros = ")) # n

fator_de_bloco = math.floor(tamanho_bloco / tamanho_registro) # f
espaco_inutilizado = tamanho_bloco - (fator_de_bloco * tamanho_registro)
n_blocos = math.ceil(n_registros / fator_de_bloco) # b
consumo_de_espaco = n_blocos * tamanho_bloco
consumo_em_megabytes = (consumo_de_espaco/1024)/1024
indice_primario = math.ceil(math.log2(n_blocos)) + 1
indice_secundario = n_blocos

print(f'F/blocagem          = {fator_de_bloco}')
print(f'U/inutilizado       = {espaco_inutilizado} Bytes')
print(f'B/blocos            = {n_blocos}')
print(f'Consumo espaco      = {consumo_de_espaco} Bytes / {consumo_em_megabytes} MegaBytes')
print(f'Acesso Ordenado     = {indice_primario}')
print(f'Acesso Desordenado  = {indice_secundario}')

