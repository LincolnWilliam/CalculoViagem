'''
 Faça um algoritmo que calcule a quantidade de litros de combustível gasta em uma viagem,
 utilizando um automóvel que faz 12Km por litro.
 Para obter o cálculo, o usuário deve fornecer o
 tempo gasto na viagem e a velocidade média durante ela.
 Desta forma, será possível obter a distância percorrida com a fórmula DISTANCIA = TEMPO * VELOCIDADE.
 Tendo o valor da distância,
 basta calcular a quantidade de litros de combustível utilizada na viagem com a fórmula:
 LITROS_USADOS = DISTANCIA / 12.
 O programa deve apresentar os valores davelocidade média, tempo gasto na viagem, a distância percorrida e
 a quantidade de litros utilizada na viagem.
'''

# consumo: 12 km/L

# calcular tempo da viagem e velocidade media - DISTANCIA = TEMPO * VELOCIDADE.
tempo_viagem = float(input("Digite o tempo de viagem em horas: "))
velocidade = int(input("Digite a velocidade media da viagem: "))

# calcular km total da viagem
distancia = tempo_viagem * velocidade

# calcular qtde Litros ultilizada na viagem
litros_usados = distancia /12

# print("Você usou na viagem ",litros_usados, "litros")
print("com o tempo de: ",tempo_viagem, "horas e uma velocidade média de :",velocidade,"Km/h")
print("você percorreu uma distância de: ", distancia, "Km")
print("Você usou na viagem {:.2f}".format(litros_usados), "Litros de combustivel")