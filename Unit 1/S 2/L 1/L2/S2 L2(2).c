#include <stdio.h>      // Includo la libreria standard input/outpu

int main() {             // Funzione principale da cui parte il programma

    int numero1,numero2;    // Dichiaro le due variabili per i numeri inseriti dall'utente
    float media;            // Variabile float per la media ( può avere decimali)

    printf("Inserisci il primo numero: ");     // Messaggio per l'utente
    scanf("%d", &numero1);                   // Primo numero intero

    printf("Inserisci il secondo numero: ");
    scanf("%d", &numero2);

    media = (numero1 + numero2) / 2.0;        // Calcolo la media: sommo i due numeri e divido per la quantità dei numeri (2.0)

    printf(" La media aritmetica è : %.2f\n", media);   // Verrà mostrato su schermo il risultato della media aritmetica

    return 0;





}