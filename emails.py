import time
import os
import random
import string
import names

try:
    import colorama
    from colorama import Fore, Style
    colorama.init(autoreset=True)
except ImportError:
    print("Colorama não está instalado. Instalando...")
    os.system('pip install colorama')
    from colorama import Fore, Style

os.system('cls' if os.name == 'nt' else 'clear')

print(f"{Fore.RED}{Style.BRIGHT}{'█▄░▄█ ▄▀▄ ▀ █░░ █▄░▄█ ▄▀▄ ▄▀▀ ▀█▀ █▀▀ █▀▀▄'}")
print(f"{Fore.RED}{Style.BRIGHT}{'█░█░█ █▀█ █ █░▄ █░█░█ █▀█ ░▀▄ ░█░ █▀▀ █▐█▀'}")
print(f"{Fore.RED}{Style.BRIGHT}{'▀░░░▀ ▀░▀ ▀ ▀▀▀ ▀░░░▀ ▀░▀ ▀▀░ ░▀░ ▀▀▀ ▀░▀▀'}{Style.RESET_ALL}\n")

__author__ = "WhiteKnight"

def generate_email():
    letters = string.ascii_lowercase
    numbers = string.digits
    domains = ["hotmail.com", "gmail.com", "yahoo.com", "outlook.com"]
    email = ''.join(random.choice(letters + numbers) for _ in range(random.randint(5, 10)))
    domain = random.choice(domains)
    return email + "@" + domain

def generate_name():
    return names.get_full_name()

try:
    num_emails = int(input("Quantos e-mails você deseja gerar? "))
    if num_emails <= 25:
        
        print(f"\nGerando {num_emails} e-mails...\n")
        for i in range(num_emails):
            name = generate_name()
            email = generate_email()
            print(f"{name} - {email}")
            time.sleep(1)
            
    else:
        print(f"Você digitou {num_emails} e-mails. Eu vou agilizar esse trabalho para você. Deseja continuar?")
        answer = input("Digite 'S' para sim e 'N' para não: ")
        if answer.lower() == 's':
            print(f"\nGerando {num_emails} e-mails...\n")
            for i in range(num_emails):
                name = generate_name()
                email = generate_email()
                print(f"{name} - {email}")
        else:
            print("Programa encerrado pelo usuário.")
except ValueError:
    print(f"{Fore.RED}Erro: insira um valor numérico válido.{Style.RESET_ALL}")

print(f"\n{Fore.YELLOW}By: {__author__}{Style.RESET_ALL}")
