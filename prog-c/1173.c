/*
* Disciplina    : 2026-PCAP
* Problema      : beecrowd 1175 - Array Fill 1
* Autor         : Luana Eliza dos Santos
* LIAC          : Le um inteiro e guarde um N[0]. Preencha as posições de 1 a 9 com o dobro da posição anterior e mostre o vetor.
* Data          : 2026.10.08
*/
#include <stdio.h>

int main() {
    int n[10], i;

    scanf("%d", &n[0]);

    for (i = 1; i < 10; i++) {
        n[i] = n[i - 1] * 2;
    }

    for (i = 0; i < 10; i++) {
        printf("N[%d] = %d\n", i, n[i]);
    }

    return 0;
}