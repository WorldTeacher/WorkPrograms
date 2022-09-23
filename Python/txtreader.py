import time

with open('AK.P015906_D20220726_T134325.CSV', 'r',encoding='ISO 8859-4') as file:
    for line in file:
        print(line)
        time.sleep(1)
