import os

cars = [
    ("Fiat Mille", 320, 0.75, 5),
    ("Volkswagen Gol", 550, 0.85, 7),
    ("Hyundai HB20", 900, 0.95, 10),
    ("Toyota Corolla", 1400, 1.10, 12),      
    ("Honda Civic", 1920, 1.30, 15),         
    ("Jeep Compass", 3840, 1.55, 20),        
    ("BMW X6", 7680, 1.85, 30),              
]

day = 1
money = 0
salary = 120
public_transport = (20, 0.65)

purchased = []


def header(text):
    print("============")
    print(text)
    print("============\n")

def show_car_list(list_cars):
    for i, car in enumerate(list_cars): 
        print("[{}] {}\n    R$ {}\n    Ganho de tempo: {}%\n    Manutenção R$ {}/dia.".format(i, car[0], car[1], int(car[2]*100), int(car[3])))
    print("\n")

def show_one_car(car):
    print("{} - R$ {}.".format(car[0], car[1]))
    print("\n")

def del_and_append_cars(list, newList,index, devalue):
    show_one_car(list[index])

    if devalue:
        list[index] = (list[index][0], list[index][1] * 0.6, list[index][2], list[index][3])
    else:
        list[index] = (list[index][0], list[index][1] / 0.6, list[index][2], list[index][3])

    newList.append(list[index])
    list.remove(list[index])
    

while True:
    os.system("cls")

    header("Bom dia! O que deseja fazer")

    print(f"Seu dinheiro: R${money}")
    print(f"Seu salário atual: R${salary}")
    
    if len(purchased) == 0:
        print(f"Valor da condução: {public_transport[0]}")
    else:
        print(f"Seu carro comprado: {purchased[0][0]} R$ {purchased[0][1]}")

    print()
    print(f"Dia atual {day}")
    print()
    
    print("0 - Comprar um carro | 1 - Vender o carro | 2 - Trabalhar")
    
    op = int(input(">> "))

    os.system("cls")


    if op == 0:
        if len(purchased) == 1:
            header("Você pode ter apenas 1 carro.")
        else:
            header("Nosso carros disponíveis.")

        show_car_list(cars)


        if len(purchased) == 1:
            pass
        else:
            header("Digite o número do carro que você deseja comprar ou aperte S para SAIR.")
            cod = input(">> ")

            if cod == "s" or cod == "S":
                continue
            else:
                cod_car = int(cod)

                if money < cars[cod_car][1]:
                    print("Você não possui dinheiro suficiente para comprar esse carro.")
                else:
                    if cod_car >= 0 and cod_car < len(cars):
                        os.system("cls")
                        cost = int(cars[cod_car][1])

                        del_and_append_cars(cars, purchased, cod_car, True)

                        money = money - cost
                        day = day + 1

                        print("Você perdeu 1 dia comprando o carro")


                    else: 
                        print("Esse carro não existe, digite novamente.")



    if op == 1: 
        if len(purchased) == 0:
            header("Nenhum carro comprado.")
        else:
            header("Seu carro.")
            show_car_list(purchased)

            header("Deseja vender seu carro? Digite S ou N")
            c = input(">> ")

            if c == "s" or c == "S":
                os.system("cls")
                cost = int(purchased[0][1])

                del_and_append_cars(purchased, cars, 0, False)
                money = money + cost
                day = day + 1
                
                print("Carro vendido com sucesso.")

    if op == 2:
        header("Seu dia finalizou\nResumo do dia")

        if len(purchased) == 0:
            print(f"Transporte publico")
            print(f"Gasto do dia R${public_transport[0]}")
            print(f"Tempo trabalhado {public_transport[1]*100}%")

            s = int(salary * public_transport[1])
            balance = s - public_transport[0]
            money = money + balance
            day = day + 1

            print(f"Saldo liquido: R$ {balance}")
        else:
            print(purchased[0][0])
            newPurchased = purchased[0]
            print(f"Custo de manutenção do carro R${newPurchased[3]}")
            print(f"Tempo trabalhado {newPurchased[2]*100}%")

            s = int(salary * newPurchased[2])
            balance = s - newPurchased[3]
            money = money + balance
            day = day + 1

            print(f"Saldo liquido: R$ {balance}")
            

    print("\n============")
    print("0 para VOLTAR | Digite 1 para SAIR")
    if float(input(">> ")) == 1:
        break