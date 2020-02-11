import os
import glob
file = open(
    "D:/Dev/stf - log agente/log/scriptResumido/scriptResumido.txt", "w")
os.chdir("D:/Dev/stf - log agente/log")
for fileName in glob.glob("*.txt"):
    logFile = open(fileName, 'r')
    whenConcat = False
    whatIllWrite = ""
    while True:
        fileLine = logFile.readline()
        if fileLine.find('Error') >= 0 or fileLine.find('ERRO') >= 0 or whenConcat:
            whatIllWrite += fileLine
            whenConcat = True
            if fileLine.find('Dispositivos conectados:') >= 0:
                whenConcat = False
        if not fileLine:
            break
    file.write('\n' + whatIllWrite + '\n' + '---------------------------------------------------------------------------------------------------------------------------------------------------------------------------' + '\n')
    logFile.close()
file.close()
