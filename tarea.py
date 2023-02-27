# import module
import platform
import os

# displaying platform processor
print('Arquitectura:', platform.architecture())
print('Maquina:', platform.machine())
print('Plataforma:', platform.platform())
print('Procesador:', platform.processor())
print('Sistema:', platform.system())
 
# Running the aforementioned command and saving its output
output = os.popen('wmic process get description, processid').read()
 
# Displaying the output
print(output)