C4_FREQ = 261.63
D4_FREQ = 293.66
E4_FREQ = 329.63
F4_FREQ = 349.23
G4_FREQ = 392.00
A4_FREQ = 440.00
B4_FREQ = 493.88

name = input("Enter the two character note name, such as C4: ")

note = name[0]
octave = int(name[1])

if note == "C":
  freq = C4_FREQ
elif note == "D":
  freq = D4_FREQ
elif note == "E":
  freq = E4_FREQ
elif note == "F":
  freq = F4_FREQ
elif note == "G":
  freq = G4_FREQ
elif note == "A":
  freq = A4_FREQ
elif note == "B":
  freq = B4_FREQ

freq = freq / 2 ** (4 - octave)

print("The frequency of", name, "is", freq)