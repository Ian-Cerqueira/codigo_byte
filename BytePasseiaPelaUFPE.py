Lugar = input()

distancia_percorrida = 0

if Lugar == "Concha Acústica da UFPE" :
    # o uso da função abs() é recomendado pois muitas vezes durante o algoritmo a formula para descobrir a distância pode resultar em valores negativos, o que quebrará todo o resto do algoritmo, já que estamos trabalhando com distâncias, que deveriam ser sempre positivas
    distancia_percorrida += 2*((abs(500-400)**2 + abs(100-500)**2)**0.5) # calcula a distancia do cin para o ponto a ser visitado e multiplica por 2 pois Byte irá fazer o caminho duas vezes (ida e volta)
    # existem outros caminhos para evitar o problema de "distancia negativa", como criar uma serie de condicionais para evitar que isso ocorra ou simplesmente escrever o codigo nunca deixando um valor menor ser subtraído por um maior, o que nao afeta o resultado final. Entretanto, o uso de abs() deixa o algoritmo mais conciso, além de apresentar ao aluno uma função útil para outras atividades

elif Lugar == "Laguinho da UFPE" :
    distancia_percorrida += 2*((abs(500-300)**2 + abs(100-1000)**2)**0.5) # calcula a distancia do cin para o ponto a ser visitado e multiplica por 2 pois Byte irá fazer o caminho duas vezes (ida e volta)

elif Lugar == "Hospital das Clínicas" :
    distancia_percorrida += 2*((abs(500-1000)**2 + abs(100-1000)**2)**0.5) # calcula a distancia do cin para o ponto a ser visitado e multiplica por 2 pois Byte irá fazer o caminho duas vezes (ida e volta)

else: # o lugar visitado é o Ginasio
    distancia_percorrida += 2*((abs(500-800)**2 + abs(100-100)**2)**0.5) # calcula a distancia do cin para o ponto a ser visitado e multiplica por 2 pois Byte irá fazer o caminho duas vezes (ida e volta)

tempo_gasto = ((distancia_percorrida / 2) / 60) + 15 # para obter o tempo em MINUTOS, é necessário fazer uma série simples de operações, nao necessariamente, mas é recomendado que seja nessa ordem: 1. divide a distancia pela velocidade de Byte, resultando no tempo em segundos. 2. apos ter o tempo em segundos, divide por 60, obtendo o tempo em minutos. 3. apos obter o tempo em minutos, soma os 15 minutos que Byte ficará parado, em qualquer que seja a condição, o tempo parado pode ser somado separadamente dentro das condicionais, mas isso pode levar ao erro. além disso, o aluno pode criar uma outra variavel tipo tempo_parado e atribuir 15 e ao fim, após obter o tempo em minutos, somar os valores

print(f"Byte visitou {Lugar}, caminhou {distancia_percorrida:.0f} metros e gastou {tempo_gasto:.0f} minutos passeando!") # arredondar para o inteiro mais proximo é só formatar :.0f

if Lugar == "Concha Acústica da UFPE" :
    print("Aqui é muito grande mesmo! Muitos eventos ocorrem por aqui!")

elif Lugar == "Laguinho da UFPE" :
    print("Nossa, mas esse lago é longe hein?!")

elif Lugar == "Hospital das Clínicas" :
    print("Um dos hospitais mais importantes do estado também fica na área do Campus da UFPE!")

else: # o lugar visitado é o Ginasio
    print("Que legal! O Ginásio é bem perto do CIn!")

