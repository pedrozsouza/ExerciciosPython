x = int(input("Informe o valor 1:"))
y = int(input("Informe o valor 2:"))

if (x == 0) or (y == 0):
    print("A operação nao pode ser realizada")
elif x!=0 and x > y:
    print("A divisão de {} por {} e {}".format(x,y,x/y))
elif y!=0 and y > x:
    print("A divisão de {} por {} e {}".format(y,x,y/x))