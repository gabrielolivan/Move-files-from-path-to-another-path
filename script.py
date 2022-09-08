import os
import shutil
import configs

# Verifica se já existe a pasta de saida dos arquivos, caso não, cria ela
if not os.path.isdir(configs.pasta_de_saida_dos_arquivos): os.mkdir(configs.pasta_de_saida_dos_arquivos)
if not os.path.isdir(fr'{configs.pasta_de_saida_dos_arquivos}\{configs.data_pasta}'): os.mkdir(fr'{configs.pasta_de_saida_dos_arquivos}\{configs.data_pasta}')
if (configs.mover_e_criar_copia_em_outra_pasta):
    if not os.path.isdir(configs.pasta_de_saida_da_copia): os.mkdir(configs.pasta_de_saida_da_copia)
    if not os.path.isdir(fr'{configs.pasta_de_saida_da_copia}\{configs.data_pasta}'): os.mkdir(fr'{configs.pasta_de_saida_da_copia}\{configs.data_pasta}')

pasta_saida = fr'{configs.pasta_de_saida_dos_arquivos}\{configs.data_pasta}'
pasta_saida_copia = fr'{configs.pasta_de_saida_da_copia}\{configs.data_pasta}'

# Lista de arquivos na pasta de chegada
files_in = os.listdir(configs.pasta_de_entrada_dos_arquivos)

# Loop para realizar a movimentação dos arquivos dentro da pasta de chegada
for fname in files_in:

    # Verifica se o arquivo termina com o formato desejado nas configurações
    if fname.endswith(tuple(configs.formato_arquivos_lidos)):

        # Renomeia o arquivo para adicionar a data nele caso esteja configurado
        arquivo_out = f'{fname.split(".")[0]}{configs.data_no_arquivo}.{fname.split(".")[1]}' if configs.adicionar_data_no_nome_do_arquivo else fname

        # Verifica se é para criar uma cópia do arquivo, caso sim, ele move o arquivo para a pasta de saida de arquivos
        # e depois cria a cópia na pasta de saida de cópia.
        # caso não, ele apenas moverá o arquivo para a pasta de saida de arquivos.
        if configs.mover_e_criar_copia_em_outra_pasta:
            os.rename(fr'{configs.pasta_de_entrada_dos_arquivos}\{fname}', fr'{pasta_saida}\{arquivo_out}')
            shutil.copyfile(fr'{pasta_saida}\{arquivo_out}', fr'{pasta_saida_copia}\{arquivo_out}')
        else:
            os.rename(fr'{configs.pasta_de_entrada_dos_arquivos}\{fname}', fr'{pasta_saida}\{arquivo_out}')