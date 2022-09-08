from configparser import ConfigParser
from datetime import *
from dateutil.tz import tzoffset

config = ConfigParser()

# Le o arquivo de configurações
config.read('config.config')

# Transforma em variavel as configurações
pasta_de_entrada_dos_arquivos = config['DEFAULT']['PASTA_DE_ENTRADA_DOS_ARQUIVOS']
pasta_de_saida_dos_arquivos = config['DEFAULT']['PASTA_DE_SAIDA_DOS_ARQUIVOS']
formato_arquivos_lidos = config['DEFAULT']['FORMATO_ARQUIVOS_LIDOS'].replace(' ', '').split(',')
adicionar_data_no_nome_do_arquivo = config['DEFAULT']['ADICIONAR_DATA_NO_NOME_DO_ARQUIVO'].lower() in ['true', 'verdadeiro']
mover_e_criar_copia_em_outra_pasta = config['DEFAULT']['MOVER_E_CRIAR_COPIA_EM_OUTRA_PASTA'].lower() in ['true', 'verdadeiro']
pasta_de_saida_da_copia = config['DEFAULT']['PASTA_DE_SAIDA_DA_COPIA']


# Configuração das Datas
hoje = datetime.now(tzoffset("BRST", -10800))
dia = datetime.strftime(hoje, '%d')
mes = datetime.strftime(hoje, '%m')
ano = datetime.strftime(hoje, '%Y')
hora = datetime.strftime(hoje, '%H')
min = datetime.strftime(hoje, '%M')
seg = datetime.strftime(hoje, '%S')
data = datetime.strftime(hoje, '%d/%m/%Y')
data_no_arquivo = f'_{ano}{mes}_{dia}_{hora}{min}{seg}'
data_pasta = f'{ano}_{mes}'