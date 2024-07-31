recordatorios = [['2021-01-01', "11:00", "Levantarse y ejercitar"],
 ['2021-05-01', "15:00", "No trabajar"],
 ['2021-07-15', "13:00", "No hacer nada es feriado"],
 ['2021-09-18', "16:00", "Ramadas"],
 ['2021-12-25', "00:00", "Navidad"]]


nuevo_evento = ['2021-02-02', "06:00", "Empezar el Año"]
recordatorios.append(nuevo_evento)

recordatorios.sort()

for i in range(len(recordatorios)):
    if recordatorios[i][0] == '2021-07-15':
        recordatorios[i][0] = '2021-07-16'
        break

for i in range(len(recordatorios)):
    if recordatorios[i][0] == '2021-05-01':
        del recordatorios[i]
        break

cena_navidad = ['2021-12-25', "22:00", "Cena de Navidad"]
cena_ano_nuevo = ['2021-12-31', "22:00", "Cena de Año Nuevo"]
recordatorios.append(cena_navidad)
recordatorios.append(cena_ano_nuevo)

recordatorios.sort()

for evento in recordatorios:
    print(evento)