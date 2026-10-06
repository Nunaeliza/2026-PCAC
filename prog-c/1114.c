/*
Problema 1073 beecrowd
Data: 2026.10.06
Autor: Luana Eliza dos Santos
*/
#include <stdio.h>

int main() {
    int senha;

    scanf("%d", &senha);

    while (senha != 2002) {
        printf("Senha Invalida\n");
        scanf("%d", &senha);
    }

    printf("Acesso Permitido\n");

    return 0;
}