def calcularTempoEspera(n, processos, quantum, pConcluidos):
    if processos[0]['tProcesso'] <= quantum:
        processos[0]['tProcessado'] = processos[0]['tProcesso']
        pConcluidos.append(processos[0].copy())
    else:
        processos[0]['tProcessado'] += quantum
        processos.append(processos[0].copy())

    i=1
    while len(pConcluidos) < n:
        processos[i]['tEspera'] = processos[i-1]['tProcessado'] + processos[i-1]['tEspera'] - processos[i]['tProcessado']
        pRestante = processos[i]['tProcesso'] - processos[i]['tProcessado']
        if pRestante <= quantum:
            processos[i]['tProcessado'] = processos[i]['tProcesso']
            pConcluidos.append(processos[i].copy())
        else:
            processos[i]['tProcessado'] += quantum
            processos.append(processos[i].copy())
        i += 1

def calcularTempoRetorno(processos):
    for pr in processos:
        pr['tRetorno'] = pr['tEspera'] + pr['tProcesso']

def calcularMedia(n, processos, quantum, pConcluidos):
    from random import shuffle
    
    totEspera, totRetorno = 0, 0
    shuffle(processos) # Função responsável pelo "sorteio"

    calcularTempoEspera(n, processos, quantum, pConcluidos)
    calcularTempoRetorno(pConcluidos)

    print('-=' * 30)
    print(f'{"PID":>3} {"Processamento":>15} {"Espera":>8} {"Retorno":>8}')
    for pr in pConcluidos:
        totEspera += pr['tEspera']
        totRetorno += pr['tRetorno']
        print(f'{pr["PID"]:>3} {pr["tProcesso"]:>15} {pr["tEspera"]:>8} {pr["tRetorno"]:>8}')
    s = totEspera/n
    t = totRetorno/n
    print(f'Tempo total de Espera: {totEspera}\nTempo total de Retorno: {totRetorno}')
    print(f'Tempo médio de Espera: {s:.2f}\nTempo médio de Retorno: {t:.2f}')

    print('-=' * 30)
    print('Processamentos:')
    for i in processos: print(i)
    print('-=' * 30)
    print('Concluidos:')
    for i in pConcluidos: print(i)
    print('-=' * 30)

def main():
    p1 = {
        'PID': 1,
        'tProcesso': 5,
        'tProcessado': 0,
        'tEspera': 0,
        'tRetorno': 0
    }
    p2 = {
        'PID': 2,
        'tProcesso': 6,
        'tProcessado': 0,
        'tEspera': 0,
        'tRetorno': 0
    }
    p3 = {
        'PID': 3,
        'tProcesso': 4,
        'tProcessado': 0,
        'tEspera': 0,
        'tRetorno': 0
    }
    p4 = {
        'PID': 4,
        'tProcesso': 2,
        'tProcessado': 0,
        'tEspera': 0,
        'tRetorno': 0
    }
    processos = [p1, p2, p3, p4]
    n = len(processos)
    quantum = 2
    pConcluidos = []
    calcularMedia(n, processos, quantum, pConcluidos)

if __name__ == '__main__':
    main()
