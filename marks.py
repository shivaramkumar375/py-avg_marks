eng = int(input("Marks in English : "))
mat = int(input("Marks in Maths : "))
soc = int(input("Marks in Social : "))
sci = int(input("Marks in Science : "))
tam = int(input("Marks in Tamil : "))
avg = (eng+mat+soc+sci+tam)/5
if avg<35:
    print("Your Average is : ",avg," .Additional CLasses required")
else:
    print("Your Average is : ",avg,".Good to go")
