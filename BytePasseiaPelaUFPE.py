Lugar_1 = input()
Lugar_2 = input()

distancia_percorrida = 0 # o valor da distancia a ser percorrida por Byte é inicializado em 0 para que possa ser interado posteriormente. Uma outra alternativa seria inicializar o valor da variavel na primeira linha com calculo, como na linha 7

if Lugar_1 == "Concha Acústica da UFPE" :
    # o uso da função abs() é recomendado pois muitas vezes durante o algoritmo a formula para descobrir a distância pode resultar em valores negativos, o que quebrará todo o resto do algoritmo, já que estamos trabalhando com distâncias, que deveriam ser sempre positivas
    distancia_percorrida += (abs(500-400)**2 + abs(100-500)**2)**0.5 # calcula a distancia cin -> ponto1
    # existem outros caminhos para evitar o problema de "distancia negativa", como criar uma serie de condicionais para evitar que isso ocorra ou simplesmente escrever o codigo nunca deixando um valor menor ser subtraído por um maior, o que nao afeta o resultado final. Entretanto, o uso de abs() deixa o algoritmo mais conciso, além de apresentar ao aluno uma função útil para outras atividades

    # falando sobre a estruturação do algoritmo em si, o aluno pode fazer de várias formas, como definir variaveis x_lugar_1, y_lugar_1, x_lugar_2, y_lugar_2 baseadas nas entradas e só após isso calcular as distâncias. Fiz dessa forma pois julgo ser mais natural e de fácil visualização
    # independente da forma que o aluno faça o código, é esperado que haja encadeamento de comandos condicionais

    if Lugar_2 == "Laguinho da UFPE" :
        distancia_percorrida += (abs(400-100)**2 + abs(500-1000)**2)**0.5 # calcula distancia ponto1 -> ponto2
        distancia_percorrida += (abs(500-100)**2 + abs(100-1000)**2)**0.5 # calcula distancia ponto2 -> cin

    elif Lugar_2 == "Hospital das Clínicas" :
        distancia_percorrida += (abs(400-1000)**2 + abs(500-1000)**2)**0.5 # calcula distancia ponto1 -> ponto2
        distancia_percorrida += (abs(500-1000)**2 + abs(100-1000)**2)**0.5 # calcula distancia ponto2 -> cin

    else: # Ginasio
        distancia_percorrida += (abs(400-900)**2 + abs(500-100)**2)**0.5 # calcula distancia ponto1 -> ponto2
        distancia_percorrida += (abs(500-900)**2 + abs(100-100)**2)**0.5 # calcula distancia ponto2 -> cin

elif Lugar_1 == "Laguinho da UFPE" :
    distancia_percorrida += (abs(500-100)**2 + abs(100-1000)**2)**0.5 # calcula a distancia cin -> ponto1

    if Lugar_2 == "Concha Acústica da UFPE" :
        distancia_percorrida += (abs(100-400)**2 + abs(1000-500)**2)**0.5  # calcula distancia ponto1 -> ponto2
        distancia_percorrida += (abs(500-400)**2 + abs(100-500)**2)**0.5  # calcula distancia ponto2 -> cin

    elif Lugar_2 == "Hospital das Clínicas" :
        distancia_percorrida += (abs(100-1000)**2 + abs(1000-1000)**2)**0.5 # calcula distancia ponto1 -> ponto2
        distancia_percorrida += (abs(500-1000)**2 + abs(100-1000)**2)**0.5 # calcula distancia ponto2 -> cin

    else: # Ginasio
        distancia_percorrida += (abs(100-90)**2 + abs(1000-100)**2)**0.5 # calcula distancia ponto1 -> ponto2
        distancia_percorrida += (abs(500-90)**2 + abs(100-100)**2)**0.5  # calcula distancia ponto2 -> cin

elif Lugar_1 == "Hospital das Clínicas" :
    distancia_percorrida += (abs(500-1000)**2 + abs(100-1000)**2)**0.5 # calcula a distancia cin -> ponto1

    if Lugar_2 == "Concha Acústica da UFPE" :
        distancia_percorrida += (abs(1000-400)**2 + abs(1000-500)**2)**0.5 # calcula distancia ponto1 -> ponto2
        distancia_percorrida += (abs(500-400)**2 + abs(100-500)**2)**0.5 # calcula distancia ponto2 -> cin

    elif Lugar_2 == "Laguinho da UFPE" :
        distancia_percorrida += (abs(1000-100)**2 + abs(1000-1000)**2)**0.5 # calcula distancia ponto1 -> ponto2
        distancia_percorrida += (abs(500-100)**2 + abs(100-1000)**2)**0.5 # calcula distancia ponto2 -> cin

    else: # Ginasio
        distancia_percorrida += (abs(1000-900)**2 + abs(1000-100)**2)**0.5 # calcula distancia ponto1 -> ponto2
        distancia_percorrida += (abs(500-900)**2 + abs(100-100)**2)**0.5 # calcula distancia ponto2 -> cin

else: # o primeiro lugar visitado é o Ginasio
    distancia_percorrida += (abs(500-900)**2 + abs(100-100)**2)**0.5 # calcula a distancia cin -> ponto1

    if Lugar_2 == "Concha Acústica da UFPE" :
        distancia_percorrida += (abs(900-400)**2 + abs(100-500)**2)**0.5 # calcula distancia ponto1 -> ponto2
        distancia_percorrida += (abs(500-400)**2 + abs(100-500)**2)**0.5 # calcula distancia ponto2 -> cin

    elif Lugar_2 == "Laguinho da UFPE" :
        distancia_percorrida += (abs(900-100)**2 + abs(100-1000)**2)**0.5 # calcula distancia ponto1 -> ponto2
        distancia_percorrida += (abs(500-100)**2 + abs(100-1000)**2)**0.5 # calcula distancia ponto2 -> cin

    else: # Hospital
        distancia_percorrida += (abs(900-1000)**2 + abs(100-1000)**2)**0.5 # calcula distancia ponto1 -> ponto2
        distancia_percorrida += (abs(500-1000)**2 + abs(100-1000)**2)**0.5 # calcula distancia ponto2 -> cin

tempo_gasto = ((distancia_percorrida / 2) / 60) + 30 # para obter o tempo em MINUTOS, é necessário fazer uma série simples de operações, nao necessariamente, mas é recomendado que seja nessa ordem: 1. divide a distancia pela velocidade de Byte, resultando no tempo em segundos. 2. apos ter o tempo em segundos, divide por 60, obtendo o tempo em minutos. 3. apos obter o tempo em minutos, soma os 30 (15 + 15) minutos que Byte ficará parado, em qualquer que seja a condição
# o tempo parado pode ser somado separadamente dentro das condicionais, mas isso pode levar ao erro. além disso, o aluno pode criar uma outra variavel tipo tempo_parado e interar seu valor 2x em 15 e ao fim, após obter o tempo em minutos, somar os valores

print(f"Byte visitou {Lugar_1} e {Lugar_2}, caminhou {distancia_percorrida:.2f} metros e gastou {tempo_gasto:.2f} minutos!")

# é esperado que o aluno saiba formatar um valor float para que ele seja printado com apenas 2 casas decimais. 
