num1 = int(input().strip())
num2 = int(input().strip())

natA = 0.02
natB = 0.03
ano = 0

paisa = num2
paisb = num1

if num1 > num2:
    paisa = num1
    paisb = num2
        
while paisb <= paisa:
    ano+=1
    paisa = paisa + paisa * natA
    paisb = paisb + paisb * natB

print(ano)
