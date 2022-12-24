import math

# Parse para o print
def Replace(str1):
    if ((str1 - math.floor(str1)) > 0):
        str1 = f'{str1:,.2f}'
    else:
        str1 = f'{str1:,}'
    maketrans = str1.maketrans
    return str1.translate(maketrans(',.', '.,', ''))

def toInt(str1):
    return int(str1.translate({ord(i): None for i in '.KB '}))

# Dados base
print('--------- Dados do Arquivo ---------')
foo                         = input("Nome do arquivo               = ")
tamanho_bloco               = toInt(input("Tamanho do bloco              = ")) * 1024
tamanho_registro            = toInt(input("Tamanho do registro           = "))
n_registros                 = toInt(input("Numero de registros           = "))
tam_chave_primaria          = toInt(input("Tamanho da chave primaria     = "))
tam_ponteiro                = toInt(input("Tamanho do ponteiro           = "))
num_chaves_estrangeiras     = toInt(input("Numero de chaves estrangeiras = "))

# Arquivo Indexado
fator_de_bloco              = math.floor(tamanho_bloco / tamanho_registro)
num_blocos                  = math.ceil(n_registros/fator_de_bloco)
espaco                      = num_blocos * tamanho_bloco
espaco_megabytes            = (espaco/1024)/1024
pesquisa_por_chave_primaria = math.ceil(math.log2(num_blocos))
pesquisa_por_outro_campo    = num_blocos

# Indice Multinivel Estatico
fator_de_bloco_ISAM = math.floor(tamanho_bloco / (tam_chave_primaria + tam_ponteiro))
num_blocos_ISAM_n1 = math.ceil(num_blocos / fator_de_bloco_ISAM)
num_blocos_ISAM_n2 = math.ceil(num_blocos_ISAM_n1 / fator_de_bloco_ISAM)
espaco_ISAM = (num_blocos_ISAM_n1 + 1) * tamanho_bloco
espaco_megabytes_ISAM = (espaco_ISAM/1024)/1024
pesquisa_por_chave_primaria_ISAM = math.ceil(math.log(num_blocos, fator_de_bloco_ISAM) + 1)

print()
print('--------- Arquivo Indexado ---------')
print(f'F/blocagem                    = {Replace(fator_de_bloco)}')
print(f'B/blocos                      = {Replace(num_blocos)}')
print(f'Consumo espaco                = {Replace(espaco)} Bytes / {Replace(espaco_megabytes)} MegaBytes')
print(f'Acesso Chave Primaria         = {Replace(pesquisa_por_chave_primaria)}')
print(f'Acesso por outro campo        = {Replace(pesquisa_por_outro_campo)}')
print()
print('---- Indice Multinivel Estatico ----')
print(f'F/blocagem                    = {Replace(fator_de_bloco_ISAM)}')
print(f'B/blocos nivel 1              = {Replace(num_blocos_ISAM_n1)}')
print(f'B/blocos nivel 2              = {Replace(num_blocos_ISAM_n2)}')
print(f'Consumo espaco                = {Replace(espaco_ISAM)} Bytes / {Replace(espaco_megabytes_ISAM)} MegaBytes')
print(f'Acesso ISAM                   = {Replace(pesquisa_por_chave_primaria_ISAM)}')



# Arvore B+
if (num_chaves_estrangeiras > 0):
    print()
    print('---- Indice Multinivel Dinamico ----')
    while(num_chaves_estrangeiras > 0):
        nome_da_chave = input("Nome da chave estrangeira     = ")
        tamanho_chave = toInt(input("Tamanho do elemento           = "))
        ponteiro_de_no = toInt(input("Tamanho do ponteiro de no     = "))
        
        # No Indice
        tamanho_do_elemento_no_indice = tamanho_chave
        elementos_por_no_indice = math.floor((tamanho_bloco - ponteiro_de_no) / (tamanho_do_elemento_no_indice + ponteiro_de_no))
        ordem_da_arvore = elementos_por_no_indice + 1
        altura_da_arvore = math.ceil(math.log(n_registros, ordem_da_arvore))
        altura_de_nos_indice = altura_da_arvore - 1

        # No Registro
        tamanho_do_elemento_no_registro = tamanho_do_elemento_no_indice + tam_ponteiro
        elementos_por_no_registro = math.floor((tamanho_bloco - ponteiro_de_no) / (tamanho_do_elemento_no_registro))

        # Dados propriamente ditos
        fator_de_bloco_arvore = math.ceil(elementos_por_no_registro * 0.69)
        num_blocos_arvore = math.ceil(n_registros / fator_de_bloco_arvore)
        num_blocos_nos_de_indice = math.ceil(num_blocos_arvore / ((math.ceil(elementos_por_no_indice * 0.69)) + altura_de_nos_indice))
        espaco_arvore = (num_blocos_arvore + num_blocos_nos_de_indice) * tamanho_bloco
        espaco_megabytes_arvore = (espaco_arvore/1024)/1024
        pesquisa_por_chave_primaria_arvore = altura_da_arvore + 1

        print(f'F/blocagem                    = {Replace(fator_de_bloco_arvore)}')
        print(f'Numero de blocos de indice    = {Replace(num_blocos_nos_de_indice)}')
        print(f'Consumo espaco                = {Replace(espaco_arvore)} Bytes / {Replace(espaco_megabytes_arvore)} MegaBytes')
        print(f'Acesso arvore                 = {Replace(pesquisa_por_chave_primaria_arvore)}')
        print()

        num_chaves_estrangeiras = num_chaves_estrangeiras - 1
