
dias = int(input("Días: "))
horas = int(input("Horas: "))
minutos = int(input("Minutos: "))
segundos = int(input("Segundos: "))

seg_dia = int(dias * 86400)
seg_hora = int(horas * 3600)
seg_min = int(minutos * 60)

total_seg = seg_dia + seg_hora + seg_min + segundos

print ("Suman un total de ", total_seg, "segundos")


