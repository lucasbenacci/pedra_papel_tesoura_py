import random

cpu = 0
cont = 1
camp = 0
camppc = 0

def resultppt():
    pc = ['pedra', 'papel', 'tesoura']

    print(f"O Cpu jogou: {pc[cpu]}")

while cont < 4:

    ppt = int(input("Escolha pedra(1), papel(2) ou tesoura(3): "))

    print('=' * 50)

    cpu = random.randrange(0, 2) 

    resultppt()

    if ppt == 1 and cpu == 3:
        print("Você venceu!")
        camp += 1

    elif ppt == 3 and cpu == 2:
        print("Você venceu!")
        camp += 1

    elif ppt == 2 and cpu == 1:
        print("Você venceu!")
        camp += 1

    elif ppt == cpu:
        print("Empatou!")  

    else:
        print("Você perdeu!")
        camppc += 1
    
    cont +=1 

print(f"Você: {camp}")
print(f"Computador: {camppc}")

if camp > camppc:
    print("Você foi campeão")

elif camp == camppc:
    print("Foi um empate!")

else:
    print("infelizmente você não foi campeão!")

print("Muito obrigado por jogar!")


