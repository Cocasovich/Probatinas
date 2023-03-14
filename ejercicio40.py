
sound_level = float(input("Enter the sound level in decibels: "))

if sound_level < 40:
    print("The sound level is lower than the quietest noise in the table.")

elif sound_level >= 40 and sound_level < 70:
    print("The sound level is between Quiet Room and Alarm Clock.")

elif sound_level >= 70 and sound_level < 106:
    print("The sound level is between Alarm Clock and Gas Lawnmower.")

elif sound_level >= 106 and sound_level < 130:
    print("The sound level is between Gas Lawnmower and Jackhammer.")

elif sound_level >= 130:
    print("The sound level is higher than the loudest noise in the table.")
    
else:
    print("Invalid input.")