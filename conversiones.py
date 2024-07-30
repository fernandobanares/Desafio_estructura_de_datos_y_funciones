import sys

Sol=float(sys.argv[1])
Peso_arg=float(sys.argv[2])
Dolar=float(sys.argv[3])
Peso_cl=float(sys.argv[4])

peso_pe = Peso_cl*0.0046
peso_pesoarg = Peso_cl*0.093
peso_dolar = Peso_cl* 0.0013

while True:
    print(f"Los {Peso_cl} pesos equivalen a:\n {peso_pe} Soles\n {peso_pesoarg} Pesos Argentinos\n {peso_dolar} Dólares ")
    break