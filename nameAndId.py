name = input("[NAME] : ")
id = int(input("[ID] : "))
m = "Money"
print(f"How much {m} do u want ?")
money = input("-> ")
money = int(money)
money_p = 0
i = 1
while i <= money :
    money_p = money * (money/i)
    print(f"{i}$.{money_p}%")
    i+=1
txm = i * (10/money)
print(f"Here you go {name} -> Money = {money}$ \n percentage = {money_p}")
print(f"Tax cut [10%] {txm}: {i} -> {i-txm}")