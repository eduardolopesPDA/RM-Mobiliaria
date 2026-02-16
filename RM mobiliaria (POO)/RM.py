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
    