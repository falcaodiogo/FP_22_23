from numpy import double


CTP = double(input("Digite o valor do CTP: "))
CP = double(input("Digite o valor do CP: "))

if CTP <= 6 or CP <= 6:
    print("Reprovado por nota mínima")

NotaFinal = CTP * 0.4 + CP * 0.6

if NotaFinal >= 9.5:
    print("Aprovado")
else:
    print("Reprovado, mas com direito a recurso")
    CTPR = double(input("Digite o valor do CTP Recurso: "))
    CPR = double(input("Digite o valor do CP Recurso: "))
    NotaFinalRecurso = CTPR * 0.4 + CPR * 0.6
    if NotaFinalRecurso >= 9.5:
        print("Aprovado")
    else:
        print("Reprovado")