#Strings são arrays:
a = "Hello, World!"
print(a[1])

#String em loop (em forma de círcuito):
for x in "banana":
    print(x)

#Comrpimento de uma string:
a = "Seja bem vindo!"
print(len(a))

#String de verificação:
txt = "The best thing in life are free!"
if "free" in txt:
    print("Yes, 'free' is present.")

txt = "As melhores coisas da vida são baratas."
if "caras" not in txt:
    print("'Caras' não está presente.")