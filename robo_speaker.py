# operating system liabrary for speaker 
import os 
# main code of project 
while True:
        x = input("Enter the text to pronaounce:- ").lower()
        if x == "q":
            os.system('powershell -Command "Add-Type -AssemblyName System.Speech; '
                      '(New-Object System.Speech.Synthesis.SpeechSynthesizer).Speak(\'Bye Bye Friend !\')"')
            print("Exiting the program !")
            break
        else:
            cmd = f'powershell -Command "Add-Type -AssemblyName System.Speech; (New-Object System.Speech.Synthesis.SpeechSynthesizer).Speak(\'{x}\')'
            os.system(cmd)
