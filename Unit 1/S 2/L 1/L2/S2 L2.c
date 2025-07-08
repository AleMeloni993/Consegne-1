// Scrivo un programma che esegue l'operazione di moltiplicazione tra due numeri inseriti dall'utente
#include <stdio.h>

int main () {  
int numero1, numero2;              // Dichiaro le variabili di questo scenario, moltiplicheremo numero1 e numero2
int risultato;                     // Dichiaro la variabile risultato, cioè il risultato della nostra moltiplicazione

printf("Calcolo di una moltipliccazione tra due numeri\n");

printf("Inserire il primo numero:");    // Chiedo all'utente di inserire il primo numero per la moltiplicazione
scanf("%d",&numero1);

printf("Inserire il secondo numero:");   // Chiedo all'utente di inserire il secondo numero per la moltiplicazione
scanf("%d",&numero2);

risultato = numero1 * numero2 ;            // In questa parte si calcola il risultato della nostra moltiplicazione

printf("Il risultato della moltiplicazione è: %d\n", risultato);        // Tramite il printf viene mostrato il risultato della moltiplicazione

printf("Bravo sai contare! ");

return 0;

}







