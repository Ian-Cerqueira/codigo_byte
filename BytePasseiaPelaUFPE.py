Lugar = input()

distancia_percorrida = 0

if Lugar == "Concha Acústica da UFPE" :
    distancia_percorrida += 2*((abs(500-400)**2 + abs(100-500)**2)**0.5)

elif Lugar == "Laguinho da UFPE" :
    distancia_percorrida += 2*((abs(500-300)**2 + abs(100-1000)**2)**0.5)

elif Lugar == "Hospital das Clínicas" :
    distancia_percorrida += 2*((abs(500-1000)**2 + abs(100-1000)**2)**0.5)

else: # o lugar visitado é o Ginasio
    distancia_percorrida += 2*((abs(500-800)**2 + abs(100-100)**2)**0.5)

tempo_gasto = ((distancia_percorrida / 2) / 60) + 15

print(f"Byte visitou {Lugar}, caminhou {distancia_percorrida:.0f} metros e gastou {tempo_gasto:.0f} minutos passeando!")

if Lugar == "Concha Acústica da UFPE" :
    print("Aqui é muito grande mesmo! Muitos eventos ocorrem por aqui!")

elif Lugar == "Laguinho da UFPE" :
    print("Nossa, mas esse lago é longe hein?!")

elif Lugar == "Hospital das Clínicas" :
    print("Um dos hospitais mais importantes do estado também fica na área do Campus da UFPE!")

else: # o primeiro lugar visitado é o Ginasio
    print("Que legal! O Ginásio é bem perto do CIn!")

