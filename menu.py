import os
from time import sleep
from source import userr 
from source import logo 
from source import git_dump  
from source import user_check 
from source import ip 
from source import cep 
from source import binchecker 
from source import  dd 
from source import extrator 
import subdomian
from source import bank
from rich.console import Console
from source import morse
console = Console()
 


def menu():

    logo.logo()

  
    console.print('[[red]1[/]] [white]Osint Username[/] [[green]ON[/green]]   [[red]7[/]] [white]Consulta DD[/]                          [[green]ON[/green]]                ')
    console.print('[[red]2[/]] [white]Username Check[/] [[red]OFF[/red]]  [[red]8[/]] [white]Link Extractor[/]                       [[green]ON[/green]]           ')
    console.print('[[red]3[/]] [white]Consulta Bank[/]  [[green]ON[/green]]   [[red]9[/]] [white]Gerar Dados Fake [/]                    [[red]OFF[/red]]               ') 
    console.print('[[red]4[/]] [white]Bin Checker[/]    [[green]ON[/green]]   [[red]10[/]] [white]Github Osint[/]                        [[green]ON[/green]]         ')  
    console.print('[[red]5[/]] [white]Consulta CEP[/]   [[green]ON[/green]]   [[red]11[/]] [white]Localizar IP[/]                        [[green]ON[/green]]         ')  
    console.print('[[red]6[/]] [white]Consulta CNPJ[/]  [[red]OFF[/red]]  [[red]12[/]] [white]Discovery Subdomian[/]                 [[green]ON[/green]]             ')  
    console.print('[[red]0[/]] [white]Sair do Programa[/]      [[red]13[/]] [white]Encrypt text in code morse[/]          [[green]ON[/green]]        ')


    try:
        opcao = int(input("==> "))

    except ValueError as err: 

        console.print("[red][ERROR] Digite um número!, Não Letra.")
        console.print("Deseja retornar ao menu? [[green]Y[/green]/[red]N[/red]]")
        opcao = str(input("==> ")).upper().strip()

        if opcao == "":
            console.print("[red][ERROR] Você não digitou a opção!![/red]")
            sleep(1.0)
            os.system("cls || clear")
            sleep(1.0)
            os.system("cls || clear")
            sleep(1.0)
            os.system("cls || clear")
            return menu()
        elif opcao == "Y":
            os.system("cls || clear")
            sleep(1.0)
            os.system("cls || clear")
            sleep(1.0)
            os.system("cls || clear")
            return menu()
        elif opcao == "N":

            console.print("[green]Saindo do Programa...[/green]") 
            sleep(0.15)
            exit(0)
        else:

            console.print("[red][ERROR] Opção inválida!![/red]") 
            sleep(0.15)
            return menu()
    
    if opcao == 1:

        user = console.input("[green][+] Informe o Username/Nickname:[/green] ").strip()

        if user == "":
            console.print("[red][ERROR] Você não digitou o Username!![/red]")
            sleep(1.0)
            os.system("cls || clear")
            sleep(1.0)
            os.system("cls || clear")
            sleep(1.0)
            os.system("cls || clear")
            return menu() 
        
        else:

            userr.userrecon(user)
            console.print("Deseja retornar ao menu? [[green]Y[/green]/[red]N[/red]]")
            opcao = str(input("==> ")).upper().strip()
            if opcao == "":
                console.print("[red][ERROR] Você não digitou a opção!![/red]")
                sleep(1.0)
                os.system("cls || clear")
                sleep(1.0)
                os.system("cls || clear")
                sleep(1.0)
                os.system("cls || clear")
                return menu()
            elif opcao == "Y":
                os.system("cls || clear")
                sleep(1.0)
                os.system("cls || clear")
                sleep(1.0)
                os.system("cls || clear")
                return menu()

            elif opcao == "N":
 
                console.print("[green]Saindo do Programa...[/green]") 
                sleep(0.15)
                exit(0)
            else:

                console.print("[red][ERROR] Opção inválida!![/red]") 
                os.system("cls || clear")
                sleep(1.0)
                os.system("cls || clear")
                sleep(1.0)
                os.system("cls || clear")
                return menu()

    elif opcao == 2: 
        
        console.input("[red][*] Está opção está OFF!![/red]")
        sleep(2.0)
        os.system("cls || clear")
        sleep(1.0)
        os.system("cls || clear")
        sleep(1.0)
        os.system("cls || clear")
        return menu()

    elif opcao == 3:
        try:
           cod = int(console.input("[green][+] Informe o código do banco:[/green] "))
        except:
            console.print("[red][*] Digite número!, Não Letra.[/red]")
            sleep(2.0)
            os.system("cls || clear")
            sleep(1.0)
            os.system("cls || clear")
            sleep(1.0)
            os.system("cls || clear")
            return menu()

        if cod == "":
            console.print("[red][ERROR] Você não digitou o COD do Bank!![/red]")
            sleep(1.0)
            os.system("cls || clear")
            sleep(1.0)
            os.system("cls || clear")
            sleep(1.0)
            os.system("cls || clear")
            return menu() 
        
        else:

            bank.get_bank(cod)
            console.print("Deseja retornar ao menu? [[green]Y[/green]/[red]N[/red]]")
            opcao = str(input("==> ")).upper().strip()
            if opcao == "":
                console.print("[red][ERROR] Você não digitou a opção!![/red]")
                sleep(1.0)
                os.system("cls || clear")
                sleep(1.0)
                os.system("cls || clear")
                sleep(1.0)
                os.system("cls || clear")
                return menu()
            elif opcao == "Y":
                os.system("cls || clear")
                sleep(1.0)
                os.system("cls || clear")
                sleep(1.0)
                os.system("cls || clear")
                return menu()

            elif opcao == "N":
 
                console.print("[green]Saindo do Programa...[/green]") 
                sleep(0.15)
                exit(0)
            else:

                console.print("[red][ERROR] Opção inválida!![/red]") 
                os.system("cls || clear")
                sleep(1.0)
                os.system("cls || clear")
                sleep(1.0)
                os.system("cls || clear")
                return menu()

    elif opcao == 4:
        try:
            binn = int(input("[green][+] Informe o Bin do Cartão:[/green] "))
        except:
            console.print("[red][*] Digite número!, Não Letra.[/red]")
            sleep(2.0)
            os.system("cls || clear")
            sleep(1.0)
            os.system("cls || clear")
            sleep(1.0)
            os.system("cls || clear")
            return menu()
        if binn == "":
            console.print("[red][ERROR] Você não digitou a opção!![/red]")
            sleep(1.0)
            os.system("cls || clear")
            sleep(1.0)
            os.system("cls || clear")
            sleep(1.0)
            os.system("cls || clear")
            return menu() 
        
        if binn <= 8:
            
            console.print("[red][*] ERROR Você não digitou os 8 números do Cartão[/red]")
            sleep(0.15)
            os.system("cls || clear")
            
            sleep(0.15)
            os.system("cls || clear")

            return menu()

        else:

            binchecker.get_bin(binn)
            console.print("Deseja retornar ao menu? [[green]Y[/green]/[red]N[/red]]")
            opcao = str(input("==> ")).upper().strip()
            if opcao == "":
                console.print("[red][ERROR] Você não digitou a opção!![/red]")
                sleep(1.0)
                os.system("cls || clear")
                sleep(1.0)
                os.system("cls || clear")
                sleep(1.0)
                os.system("cls || clear")
                return menu()
            elif opcao == "Y":
                os.system("cls || clear")
                sleep(1.0)
                os.system("cls || clear")
                sleep(1.0)
                os.system("cls || clear")
                return menu()

            elif opcao == "N":
 
                console.print("[green]Saindo do Programa...[/green]") 
                os.system("cls || clear")
                sleep(1.0)
                os.system("cls || clear")
                sleep(1.0)
                os.system("cls || clear")
                exit(0)
            else:

                console.print("[red][ERROR] Opção inválida!![/red]") 
                os.system("cls || clear")
                sleep(1.0)
                os.system("cls || clear")
                sleep(1.0)
                os.system("cls || clear")
                return menu()
    elif opcao == 5:
        
        cepp = str(console.input("[green][+] Informe o CEP:[/green] "))
        if cepp == "":
            console.print("[red][ERROR] Você não digitou o CEP!![/red]")
            sleep(1.0)
            os.system("cls || clear")
            sleep(1.0)
            os.system("cls || clear")
            sleep(1.0)
            os.system("cls || clear")
            return menu() 
        
        else:

            cep.get_cep(cepp)
            console.print("Deseja retornar ao menu? [[green]Y[/green]/[red]N[/red]]")
            opcao = str(input("==> ")).upper().strip()
            if opcao == "":
                console.print("[red][ERROR] Você não digitou a opção!![/red]")
                sleep(1.0)
                os.system("cls || clear")
                sleep(1.0)
                os.system("cls || clear")
                sleep(1.0)
                os.system("cls || clear")
                return menu()
            elif opcao == "Y":
                os.system("cls || clear")
                sleep(1.0)
                os.system("cls || clear")
                sleep(1.0)
                os.system("cls || clear")
                return menu()

            elif opcao == "N":
 
                console.print("[green]Saindo do Programa...[/green]") 
                os.system("cls || clear")
                sleep(1.0)
                os.system("cls || clear")
                sleep(1.0)
                os.system("cls || clear")
                exit(0)
            else:

                console.print("[red][ERROR] Opção inválida!![/red]") 
                sleep(0.15)
                return menu()
    
    elif opcao == 6:

        console.input("[red][*] Está opção está OFF!![/red]")
        sleep(2.0)
        os.system("cls || clear")
        sleep(1.0)
        os.system("cls || clear")
        sleep(1.0)
        os.system("cls || clear")
        return menu()

    elif opcao == 7:
        try:
           ddd = int(console.input("[green][+] Informe o DD:[/green] (EX: 11)"))
        except: 
            console.print("[red][*] Digite número!, Não Letra.[/red]")
            sleep(2.0)
            os.system("cls || clear")
            sleep(1.0)
            os.system("cls || clear")
            sleep(1.0)
            os.system("cls || clear")
            return menu() 
        if ddd == "":
            console.print("[red][ERROR] Você não digitou o DD!![/red]")
            sleep(1.0)
            os.system("cls || clear")
            sleep(1.0)
            os.system("cls || clear")
            sleep(1.0)
            os.system("cls || clear")
            return menu() 
        
        else:

            dd.get_dd(ddd)
            console.print("Deseja retornar ao menu? [[green]Y[/green]/[red]N[/red]]")
            opcao = str(input("==> ")).upper().strip()
            if opcao == "":
                console.print("[red][ERROR] Você não digitou o DD!![/red]")
                sleep(1.0)
                os.system("cls || clear")
                sleep(1.0)
                os.system("cls || clear")
                sleep(1.0)
                os.system("cls || clear")
                return menu()
            elif opcao == "Y":
                os.system("cls || clear")
                sleep(1.0)
                os.system("cls || clear")
                sleep(1.0)
                os.system("cls || clear")
                return menu()

            elif opcao == "N":
 
                console.print("[green]Saindo do Programa...[/green]") 
                sleep(0.15)
                exit(0)
            else:

                console.print("[red][ERROR] Opção inválida!![/red]") 
                os.system("cls || clear")
                sleep(1.0)
                os.system("cls || clear")
                sleep(1.0)
                os.system("cls || clear")
                return menu()
    
    elif opcao == 8:
        
        site = console.input("[green][+] Informe o Site:[/green] ")
        if site == "":
            console.print("[red][ERROR] Você não Informou o Site!![/red]")
            sleep(1.0)
            os.system("cls || clear")
            sleep(1.0)
            os.system("cls || clear")
            sleep(1.0)
            os.system("cls || clear")
            return menu() 
        
        else:

            extrator.crawl(site)
            console.print("Deseja retornar ao menu? [[green]Y[/green]/[red]N[/red]]")
            opcao = str(input("==> ")).upper().strip()
            if opcao == "":
                console.print("[red][ERROR] Você não digitou o Site!![/red]")
                sleep(1.0)
                os.system("cls || clear")
                sleep(1.0)
                os.system("cls || clear")
                sleep(1.0)
                os.system("cls || clear")
                return menu()
            elif opcao == "Y":
                os.system("cls || clear")
                sleep(1.0)
                os.system("cls || clear")
                sleep(1.0)
                os.system("cls || clear")
                return menu()

            elif opcao == "N":
 
                console.print("[green]Saindo do Programa...[/green]") 
                sleep(0.15)
                exit(0)
            else:

                console.print("[red][ERROR] Opção inválida!![/red]") 
                os.system("cls || clear")
                sleep(1.0)
                os.system("cls || clear")
                sleep(1.0)
                os.system("cls || clear")
                return menu()

    elif opcao == 9:
        console.input("[red][*] Está opção está OFF!![/red]")
        sleep(2.0)
        os.system("cls || clear")
        sleep(1.0)
        os.system("cls || clear")
        sleep(1.0)
        os.system("cls || clear")
        return menu()

    elif opcao == 10: 

        user = console.input("[green][+] Informe o Username/Nickname:[/green] ").strip()
        

        if user == "":
            console.print("[red][ERROR] Você não digitou o Username!![/red]")
            sleep(1.0)
            os.system("cls || clear")
            sleep(1.0)
            os.system("cls || clear")
            sleep(1.0)
            os.system("cls || clear")
            return menu() 
        
        else:

            git_dump.git_dumpp(user)
            console.print("Deseja retornar ao menu? [[green]Y[/green]/[red]N[/red]]")
            opcao = str(input("==> ")).upper().strip()
            if opcao == "":
                console.print("[red][ERROR] Você não digitou a opção!![/red]")
                sleep(1.0)
                os.system("cls || clear")
                sleep(1.0)
                os.system("cls || clear")
                sleep(1.0)
                os.system("cls || clear")
                return menu()
            elif opcao == "Y":
                os.system("cls || clear")
                sleep(1.0)
                os.system("cls || clear")
                sleep(1.0)
                os.system("cls || clear")
                return menu()

            elif opcao == "N":
 
                console.print("[green]Saindo do Programa...[/green]") 
                sleep(0.15)
                exit(0)
            else:

                console.print("[red][ERROR] Opção inválida!![/red]") 
                os.system("cls || clear")
                sleep(1.0)
                os.system("cls || clear")
                sleep(1.0)
                os.system("cls || clear")
                return menu()
    elif opcao == 11:
        
        ipp = console.input("[green][+] Informe o IP:[/green]  ")
        if ipp == "" and ipp is None:
            console.print("[red][ERROR] Você não digitou o IP!![/red]")
            sleep(1.0)
            os.system("cls || clear")
            sleep(1.0)
            os.system("cls || clear")
            sleep(1.0)
            os.system("cls || clear")
            
            return menu() 
        
        else:

            ip.get_ip(ipp)
            console.print("Deseja retornar ao menu? [[green]Y[/green]/[red]N[/red]]")
            opcao = str(input("==> ")).upper().strip()
            if opcao == "":
                console.print("[red][ERROR] Você não digitou a opção!![/red]")
                sleep(1.0)
                os.system("cls || clear")
                sleep(1.0)
                os.system("cls || clear")
                sleep(1.0)
                os.system("cls || clear")
                return menu()
            elif opcao == "Y":
                os.system("cls || clear")
                sleep(1.0)
                os.system("cls || clear")
                sleep(1.0)
                os.system("cls || clear")
                return menu()

            elif opcao == "N":
 
                console.print("[green]Saindo do Programa...[/green]") 
                sleep(0.15)
                exit(0)
            else:

                console.print("[red][ERROR] Opção inválida!![/red]") 
                os.system("cls || clear")
                sleep(1.0)
                os.system("cls || clear")
                sleep(1.0)
                os.system("cls || clear")
                return menu()

    elif opcao == 12:
        domi = console.input("[green][+] Informe o Nome do Domínio:[/green] (EX: discord.com)")
        if domi == "":
            console.print("[red][ERROR] Você não digitou o Nome do Domínio!![/red]")
            sleep(1.0)
            os.system("cls || clear")
            sleep(1.0)
            os.system("cls || clear")
            sleep(1.0)
            os.system("cls || clear")
            return menu() 
        
        else:

            subdomian.scanner(domi)
            console.print("Deseja retornar ao menu? [[green]Y[/green]/[red]N[/red]]")
            opcao = str(input("==> ")).upper().strip()
            if opcao == "":
                console.print("[red][ERROR] Você não digitou a opção!![/red]")
                sleep(1.0)
                os.system("cls || clear")
                sleep(1.0)
                os.system("cls || clear")
                sleep(1.0)
                os.system("cls || clear")
                return menu()
            elif opcao == "Y":
                os.system("cls || clear")
                sleep(1.0)
                os.system("cls || clear")
                sleep(1.0)
                os.system("cls || clear")
                return menu()

            elif opcao == "N":
 
                console.print("[green]Saindo do Programa...[/green]") 
                sleep(0.15)
                exit(0)
            else:

                console.print("[red][ERROR] Opção inválida!![/red]") 
                os.system("cls || clear")
                sleep(1.0)
                os.system("cls || clear")
                sleep(1.0)
                os.system("cls || clear")
                return menu()


    elif opcao == 13:
        
        cod = console.input("[green][+] Informe a Palavra para ser Encryptada:[/green] ")
           
        

        if cod == "":
            
            console.print("[red][ERROR] Você não digitou a Palavra!![/red]")
            sleep(1.0)
            os.system("cls || clear")
            sleep(1.0)
            os.system("cls || clear")
            sleep(1.0)
            os.system("cls || clear")
            return menu() 
        
        else:
            morse.main(cod)
            console.print("Deseja retornar ao menu? [[green]Y[/green]/[red]N[/red]]")
            opcao = str(input("==> ")).upper().strip()

            if opcao == "":
                console.print("[red][ERROR] Você não digitou a opção!![/red]")
                sleep(1.0)
                os.system("cls || clear")
                sleep(1.0)
                os.system("cls || clear")
                sleep(1.0)
                os.system("cls || clear")
                return menu()
            elif opcao == "Y":
                os.system("cls || clear")
                sleep(1.0)
                os.system("cls || clear")
                sleep(1.0)
                os.system("cls || clear")
                return menu()

            elif opcao == "N":
 
                console.print("[green]Saindo do Programa...[/green]") 
                sleep(0.15)
                exit(0)
            else:

                console.print("[red][ERROR] Opção inválida!![/red]") 
                os.system("cls || clear")
                sleep(1.0)
                os.system("cls || clear")
                sleep(1.0)
                os.system("cls || clear")
                return menu()

    elif opcao == 0: 

        console.print("[green]Saindo do Programa...[/green]") 
    
        exit(0)
    
    else:
        console.print("[red][ERROR] Opção inválida!![/red]") 
        os.system("cls || clear")
        sleep(1.0)
        os.system("cls || clear")
        sleep(1.0)
        os.system("cls || clear")
        return menu()

menu()