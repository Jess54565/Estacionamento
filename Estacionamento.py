from datetime import datetime, timedelta
import math

HORA = 3600
DIA = HORA * 24
MES = DIA * 30
QUINZE_MIN = 900

class TipoVeiculo:
    PEQ = 1
    MED = 2
    GRA = 3
    CAM = 4

class ContaEstacionamento:
    def __init__(self, tipo, hora_entrada, hora_saida):
        self.tipo = tipo
        self.hora_entrada = hora_entrada
        self.hora_saida = hora_saida

def regra_juiz_de_fora(veiculo):
    permanencia = veiculo.hora_saida - veiculo.hora_entrada
    permanencia_seg = permanencia.total_seconds()

    if permanencia_seg < HORA:
        return 0.5 * math.ceil(permanencia_seg / QUINZE_MIN)
    else:
        return calcDiaria(veiculo)

def calcDiaria(veiculo):
    permanencia = veiculo.hora_saida - veiculo.hora_entrada
    perm = permanencia.total_seconds()

    if veiculo.tipo == TipoVeiculo.PEQ:
        if perm <= 12 * HORA:
            return 2.0 * math.ceil(perm / HORA)
        elif perm <= 15 * DIA:
            return 26.0 * math.ceil(perm / DIA)
        else:
            return 300.0 * math.ceil(perm / MES)
            
    elif veiculo.tipo == TipoVeiculo.MED:
        return 2.5 * math.ceil(perm / HORA)
    elif veiculo.tipo == TipoVeiculo.GRA:
        return 3.5 * math.ceil(perm / HORA)
    elif veiculo.tipo == TipoVeiculo.CAM:
        return 4.5 * math.ceil(perm / HORA)
    
    return 0.0  # Caso o tipo seja inválido

def main():
    tipo = int(input("Digite o tipo de veículo (1 = Pequeno, 2 = Médio, 3 = Grande, 4 = Caminhonete): "))
    
    hora_entrada = input("Insira a hora de entrada (HH:MM): ").strip()
    hora_saida = input("Insira a hora de saída (HH:MM): ").strip()

    formato = "%H:%M"
    entrada = datetime.strptime(hora_entrada, formato)
    saida = datetime.strptime(hora_saida, formato)

    if saida <= entrada:
        print("Erro: A hora de saída deve ser posterior à hora de entrada.")
        return

    aplicar_regra_jf = int(input("Aplicar regra de Juiz de Fora? (1 = Sim, 0 = Não): "))

    veiculo = ContaEstacionamento(tipo, entrada, saida)

    if aplicar_regra_jf == 1:
        valor = regra_juiz_de_fora(veiculo)
    else:
        valor = calcDiaria(veiculo)

    print(f"Valor a pagar: R$ {valor:.2f}")

if __name__ == "__main__":
    main()