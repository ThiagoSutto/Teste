def verificar_velocidade(velo):
    if velo>80:
        return "multado"
    else:
        return "seguro"

velo = int(input("digite a velocidade: "))
print(verificar_velocidade(velo))        





