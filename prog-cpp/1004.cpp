/*
* Disciplina: 2026-PCAP
* Problema  : beecrowd 1004 - Produto simples
* Autor     : Luana Eliza dos Santos
* LIAC      : Le dois inteiros A e B, um por linha. Imprime a mensagem no formato "PROD = a * b", com espacos em volta do sinal de igual.
*/
#include <iostream>
using namespace std;

int main() {
    int a, b;

    std::cin >> a >> b;
    std::cout << "PROD = " << a * b << std::endl;

    return 0;
}