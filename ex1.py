temperaturas=[]
def conversao(temperaturas, origem, destino):
    temperaturas_convertidas=[]
    if origem=="Celsius" and destino=="Fahrenheit":
        for item in temperaturas:
            item=item*9/5+32
            temperaturas_convertidas.append(item)
    if origem=="Fahrenheit" and destino=="Celsius":
        for item in temperaturas:
            item=(item-32)*5/9
            temperaturas_convertidas.append(item)
    return temperaturas_convertidas
origem=str(input("Insira a escala de origem (Celsius ou Fahrenheit): "))
if origem=='c' or origem=='C' or origem=='celsius' or origem=='Celsius':
    origem='Celsius'
elif origem=='f' or origem=='F' or origem=='fahrenheit' or origem=='Fahrenheit':
    origem='Fahrenheit'
if origem=='Celsius':
    destino='Fahrenheit'
elif origem=='Fahrenheit':
    destino='Celsius'
while True:
    item=float(input(f"Insira uma temperatura em graus {origem}: "))
    temperaturas.append(item)
    continuar=str(input("Deseja continuar? (S/N): "))
    if continuar=='s' or continuar=='S':
        continue
    elif continuar=='n' or continuar=='N':
        break
print(f"As temperaturas em graus {destino} são {conversao(temperaturas, origem, destino)}")

