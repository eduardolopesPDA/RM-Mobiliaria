import csv 

#classe base 
class imovel:
    def calcular_aluguel(self):
        pass

#classes filhas
class Apartamento(imovel):
    def __init__(self, quartos, tem_crianca, garagem):
        self.aluguel = 700
        self.quartos = quartos
        self.tem_crianca = tem_crianca
        self.garagem = garagem

    def calcular_aluguel(self):
        if self.quartos == 2:
            self.aluguel += 200

        if not self.tem_crianca:
            self.aluguel *= 0.95  # desconto 5%

        if self.garagem:
            self.aluguel += 300

        return self.aluguel

class casa(imovel):
     def __init__(self, quartos, garagem):
        self.aluguel = 900
        self.quartos = quartos
        self.garagem = garagem

     def calcular_aluguel(self):
        if self.quartos == 2:
            self.aluguel += 250

        if self.garagem:
            self.aluguel += 300

        return self.aluguel

class estudio(imovel):
    def __init__(self, vagas):
        self.aluguel = 1200
        self.vagas = vagas

    def calcular_aluguel(self):
        if self.vagas >= 2:
            self.aluguel += 250
            if self.vagas > 2:
                self.aluguel += (self.vagas - 2) * 60
        return self.aluguel
    
#classe da regra de negocios
class orçamento:
    def __init__(self, imovel):
        self.imovel = imovel
        self.contrato = 2000

    def parcelar_contrato(self, parcelas):
        if parcelas < 1 or parcelas > 5:
            parcelas = 1
        return self.contrato / parcelas
       
       #função que vai gera o arquivo do contrato 
    def gerar_csv(self, valor_aluguel):
        with open("orcamento_rm.csv", "w", newline="", encoding="utf-8") as f:
            writer = csv.writer(f)
            writer.writerow(["Mês", "Valor do Aluguel (R$)"])
            for mes in range(1, 13):
                writer.writerow([mes, f"{valor_aluguel:.2f}"])
    

print("Olá somos a RM Mobiliaria! estamos aqui para auxiliar na escolha do seu novo lar!")
print("1 - Apartamento")
print("2 - Casa")
print("3 - Estúdio")
tipo = input("Escolha o tipo de imóvel: ")

if tipo == "1":
    quartos = int(input("Quartos (1 ou 2): "))
    tem_crianca = input("Possui crianças? (s/n): ").lower() == "s"
    garagem = input("Deseja garagem? (s/n): ").lower() == "s"
    imovel = Apartamento(quartos, tem_crianca, garagem)

elif tipo == "2":
    quartos = int(input("Quartos (1 ou 2): "))
    garagem = input("Deseja garagem? (s/n): ").lower() == "s"
    imovel = casa(quartos, garagem)

elif tipo == "3":
    vagas = int(input("Quantidade de vagas: "))
    imovel = estudio(vagas)

else:
    print("Opção inválida.")
    exit()

orcamento = orçamento(imovel)
valor_final = imovel.calcular_aluguel()

parcelas = int(input("Contrato em quantas vezes? (1 a 5): "))
valor_parcela = orcamento.parcelar_contrato(parcelas)

print("Aqui está seu orçamento final: ")
print(f"Aluguel mensal: R$ {valor_final:.2f}")
print(f"Contrato: R$ 2000.00")
print(f"Contrato parcelado em {parcelas}x de R$ {valor_parcela:.2f}")

gerar = input("Deseja gerar CSV com 12 meses? (s/n): ")
if gerar == "s":
    orcamento.gerar_csv(valor_final)
    print("Arquivo 'orcamento_rm.csv' gerado com sucesso!")
else: 
    print("Sem problemas! Obrigado por confiar nos nossos sewrviços!")