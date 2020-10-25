"""18. Faça um programa que peça o tamanho de um arquivo para download (em MB) e a velocidade de um link de
Internet (em Mbps), calcule e informe o tempo aproximado de download do arquivo usando este link (em minutos)."""

tamanho_arquivo = float(input('Tamanho do arquivo a ser baixado em MB/s: '))
velocidade_internet = float(input('Qual a velocidade da sua internet? '))
tempo_de_download = tamanho_arquivo / velocidade_internet / 60

print(f'Seu arquivo demorará {tempo_de_download:.2f} minutos para ser baixado!')