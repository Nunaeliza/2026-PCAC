/*
* Disciplina    : 2026-PCAP
* Problema      : beecrowd 1175 - Array Change 1
* Autor         : Luana Eliza dos Santos
* LIAC          : Le 20 inteiros num vetor N. Mostrar o vetor com a ordem invertida: o último lido aparece na posição 0 e o primeiro lido na posição 19.
* Data          : 2026.10.08
*/
#include <stdio.h>

int main() {
    int n[20], i;

    for (i = 0; i < 20; i++) {
        scanf("%d", &n[i]);
    }

    for (i = 0; i < 20; i++) {
        printf("N[%d] = %d\n", i, n[19 - i]);
    }

    return 0;
}