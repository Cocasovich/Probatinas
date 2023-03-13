segs = int(input("Segundos: "))

dias = segs / 86400
segs = segs % 86400

horas = segs / 3600
segs = segs % 3600

minutos = segs / 60
segs = segs % 60

print( "El equivalente de duración es de:", "%d:%02d:%02d:%02d." % (dias, horas, minutos, segs))