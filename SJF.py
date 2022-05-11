# Encontra tempo de espera de cada processo
def encontrarTempoEspera(n, tProcessamento, tEspera):
    tEspera.append(0) # Tempo de espera do primeiro proceeso é 0
    for i in range(1, n, 1):
        # Tempo de espera de cada processo: Tempo de espera do Processo anterior + seu tempo de processamento
        tEspera.append(tProcessamento[i-1] + tEspera[i-1])

# Encontra o tempo de saída do escalonador de cada processo
def encontrarTempoRetorno(n, tProcessamento, tEspera, tRetorno):
    for i in range(n):
        # Tempo de retorno == Tempo de Saída do Escalonador: Tempo de espera + Tempo de Processamento
        tRetorno.append(tProcessamento[i] + tEspera[i])

# Encontra informações totais de tempo de processamento e tempo médio
def encontrarTempoMedio(n, tempoProcess):
    tEspera, tRetorno, totEspera, totRetorno = [], [], 0, 0 # tot --> Total

    # Ordena os processos por Tempo de Processamento
    tempoProcess = sorted(tempoProcess)

    encontrarTempoEspera(n, tempoProcess, tEspera)
    encontrarTempoRetorno(n, tempoProcess, tEspera, tRetorno)

    print(f'{"ID":>3} {"Processamento":>15} {"Espera":>8} {"Retorno":>8}')
    for i in range(n):
        totEspera += tEspera[i]
        totRetorno += tRetorno[i]
        print(f'{(i+1):>3} {tempoProcess[i]:>15} {tEspera[i]:>8} {tRetorno[i]:>8}')
    s = totEspera / n
    t = totRetorno / n
    print(f'Tempo total de Espera: {totEspera}\nTempo total de Retorno: {totRetorno}')
    print(f'Tempo médio de Espera: {s:.2f}\nTempo médio de Retorno: {t:.2f}')

def main():
    processos = (1, 2, 3) # Processos
    n = len(processos) # Tamanho dos processos
    tempoProcessamento = (10, 5, 8) # Tempo de processamento dos processos
    encontrarTempoMedio(n, tempoProcessamento)


if __name__ == '__main__':
    main()
