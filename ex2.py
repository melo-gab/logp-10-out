def quantidade(string):
    dicionario={}
    valor=len(string.replace(' ', ''))
    dicionario["string"]=valor
    return dicionario
string=str(input("escreva qualquer coisa: "))
print(quantidade(string))
