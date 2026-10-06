/*
* Disciplina    : 2026-PCAP
* Problema      : beecrowd 1172 - Array Replacement 1
* Autor         : Luana Eliza dos Santos
* LIAC          : Le 10 inteiros num vetor X. Troca os valores menores ou iguais a zero por 1. Imprime cada posicao no formato "X[i] = valor".
* Data          : 2026.10.06
*/
#include <stdio.h>

int main() {
    int x[10], i;

    for (i = 0; i < 10; i++) {
        scanf("%d", &x[i]);
        if (x[i] <= 0) {
            x[i] = 1;
        }
    }
    for (i = 0; i < 10; i++) {
        printf("X[%d] = %d\n", i, x[i]);
    }

    return 0;
}