velocidade = int(input('Quantos KM/H voce estava? '))
KM = int(input('Qual Kilometro você estava? '))

RADAR_1 = 60 
RADAR_RANGE = 100
if velocidade > RADAR_1 and  KM >=(RADAR_1 - RADAR_RANGE) and KM <= (RADAR_1 + RADAR_RANGE) :
    print ('VOCE FOI MULTADO NO RADAR 1!')
else:
    print ('voce nao foi multado!')