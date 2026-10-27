/*
* Disciplina    : 2026-PCAP
* Problema      : beecrowd 1178 - Array Fill 3
* Autor         : Luana Eliza dos Santos
* LIAC          : Le um valor real e guarde em N[0]. Preencha as posições de 1 a 99 com a metade da posição anterior. Mostre as cem posições com quatro casas decimais.
* Data          : 2026.10.08
*/
#include <stdio.h>

int main() {
    int n[100];
    int i;

    scanf("%d", &n[0]);

    for (i = 1; i < 100; i++) {
        n[i] = n[i - 1] / 2;
    }

    for (i = 0; i < 100; i++) {
        printf("N[%d] = %d\n", i, n[i]);
    }

    return 0;
}