#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <time.h>

#define HORA 3600
#define DIA (24 * HORA)
#define MES (30 * DIA)
#define QUINZE_MIN 900

typedef enum { PEQUENO, MEDIO, GRANDE, CAMINHONETE, PASSEIO, CARGA } TipoVeiculo;

typedef struct {
    TipoVeiculo tipo;
    long inicio;
    long fim;
} Veiculo;

double calcularValor(Veiculo v, int juiz_de_fora) {
    long atual = (v.fim == 0) ? time(NULL) : v.fim;
    long periodo = atual - v.inicio;
    
    if (juiz_de_fora) {
        if (periodo <= HORA) {
            return 5.0 * ceil((double)periodo / QUINZE_MIN);
        }
    }
    
    switch (v.tipo) {
        case PASSEIO:
            if (periodo < 12 * HORA) {
                return 2.0 * ceil((double)periodo / HORA);
            } else if (periodo >= 12 * HORA && periodo < 15 * DIA) {
                return 26.0 * ceil((double)periodo / DIA);
            } else {
                return 300.0 * ceil((double)periodo / MES);
            }
        case CARGA:
            return 50.0 * ceil((double)periodo / DIA);
        case PEQUENO:
            return 1.5 * ceil((double)periodo / HORA);
        case MEDIO:
            return 2.5 * ceil((double)periodo / HORA);
        case GRANDE:
            return 3.5 * ceil((double)periodo / HORA);
        case CAMINHONETE:
            return 4.5 * ceil((double)periodo / HORA);
        default:
            return 0;
    }
}

int main() {
    Veiculo v;
    int tipo, juiz_de_fora;
    printf("Digite o tipo de veículo (0 = Pequeno, 1 = Médio, 2 = Grande, 3 = Caminhonete, 4 = Passeio, 5 = Carga): ");
    scanf("%d", &tipo);
    v.tipo = (TipoVeiculo)tipo;
    
    printf("Digite o horário de entrada (timestamp em segundos): ");
    scanf("%ld", &v.inicio);
    
    printf("Digite o horário de saída (timestamp em segundos, 0 para agora): ");
    scanf("%ld", &v.fim);
    
    printf("Aplicar regra de Juiz de Fora? (1 = Sim, 0 = Não): ");
    scanf("%d", &juiz_de_fora);
    
    double valor = calcularValor(v, juiz_de_fora);
    printf("Valor a pagar: R$ %.2f\n", valor);
    
    return 0;
}
