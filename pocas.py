"""
***************************************************************************
MIT License

Copyright (c) 2025 Gonçalo J. B. Pereira

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
***************************************************************************
"""
import time
import datetime
import csv
import unicodedata
#determinar os dias
dias_da_semana = ["Domingo", "Segunda", "Terça", "Quarta", "Quinta", "Sexta", "Sábado"]

def primeiro_domingo_julho():
    ano = datetime.date.today().year
    # Começa no dia 1 de julho
    for dia in range(1, 8):
        data = datetime.date(ano, 7, dia)
        if data.weekday() == 6:  # 6 = domingo
            return data

def primeiro_domingo_junho():
    ano = datetime.date.today().year
    # Começa no dia 1 de junho
    for dia in range(1, 8):
        data = datetime.date(ano, 6, dia)
        if data.weekday() == 6:  # 6 = domingo
            return data

def proxima_terca_mais_proxima():
    hoje = datetime.date.today()
    ano = hoje.year
    data_base = datetime.date(ano, 6, 29)
    # Se já passou 29 de junho este ano, pode querer considerar o próximo ano
    # (remova o comentário da linha abaixo se quiser sempre olhar para o futuro)
    # if hoje > data_base: data_base = datetime.date(ano+1, 6, 29)

    # Encontrar a terça-feira mais próxima (antes ou depois)
    dias_para_terca = (1 - data_base.weekday()) % 7  # 1 = terça-feira
    proxima_terca = data_base + datetime.timedelta(days=dias_para_terca)
    dias_para_terca_antes = (data_base.weekday() - 1) % 7
    terca_antes = data_base - datetime.timedelta(days=dias_para_terca_antes)

    # Decide qual terça-feira está mais próxima
    if abs((proxima_terca - data_base).days) < abs((terca_antes - data_base).days):
        return proxima_terca
    else:
        return terca_antes

def proxima_segunda_mais_proxima():
    hoje = datetime.date.today()
    ano = hoje.year
    data_base = datetime.date(ano, 6, 29)

    dias_para_segunda = (0 - data_base.weekday()) % 7  # 0 = segunda-feira
    proxima_segunda = data_base + datetime.timedelta(days=dias_para_segunda)
    dias_para_segunda_antes = (data_base.weekday() - 0) % 7
    segunda_antes = data_base - datetime.timedelta(days=dias_para_segunda_antes)

    if abs((proxima_segunda - data_base).days) < abs((segunda_antes - data_base).days):
        return proxima_segunda
    else:
        return segunda_antes

def proxima_segunda_mais_proxima_antes():
    hoje = datetime.date.today()
    ano = hoje.year
    data_base = datetime.date(ano, 6, 29)

    # weekday(): Monday=0 ... Sunday=6
    dias_para_segunda_antes = (data_base.weekday() - 0) % 7
    # If the 29th is Monday itself, we want the Monday BEFORE it (7 days earlier)
    if dias_para_segunda_antes == 0:
        dias_para_segunda_antes = 7

    segunda_antes = data_base - datetime.timedelta(days=dias_para_segunda_antes)
    return segunda_antes

#---------------------------selecionar a poça

pocas={"Javid":0, "Insuas":1, "Amaral":2,"Cal":3}

def get_poca():
    #time.sleep(0.5)
    print("Selecione a poça:")
    for name, index in pocas.items():
        #time.sleep(0.5)
        print(f"{index}: {name}")
    
    while True:
        try:
            choice = int(input("Digite o número da poça: "))
            for name, index in pocas.items():
                if choice == index:
                    return name
        except ValueError:
            print("Entrada inválida. Por favor, digite um número.")




def listar_consortes(horas_dict, inicio, unidade="minutos"):
    if isinstance(inicio, datetime.date) and not isinstance(inicio, datetime.datetime):
        inicio = datetime.datetime(inicio.year, inicio.month, inicio.day, 0, 0)
    # Mostra a lista de consortes com índice
    consortes = list(horas_dict.keys())
    print("Consortes:")
    for idx, nome in enumerate(consortes):
        print(f"{idx}: {nome}")
    # Usuário escolhe o consorte
    print("")
    escolha = int(input("Escolha o número do consorte: "))
    if escolha < 0 or escolha >= len(consortes):
        print("Opção inválida.")
        return
    nome_escolhido = consortes[escolha]
    tempo_ciclo = sum(horas_dict.values())
    print(f"\nTurnos de {nome_escolhido}:")
    acumulado = 0
    turno_idx = 1
    turnos_csv = []
    for nome, tempo in horas_dict.items():
        inicio_turno = inicio + (datetime.timedelta(minutes=acumulado) if unidade=="minutos" else datetime.timedelta(hours=acumulado))
        fim_turno = inicio_turno + (datetime.timedelta(minutes=tempo) if unidade=="minutos" else datetime.timedelta(hours=tempo))
        if nome == nome_escolhido:
            print(f"Turno {turno_idx}:")
            print(f"  Início: {inicio_turno.strftime('%d/%m/%Y %H:%M')}")
            print(f"  Fim:    {fim_turno.strftime('%d/%m/%Y %H:%M')}")
            turnos_csv.append([turno_idx, nome_escolhido, inicio_turno.strftime('%d/%m/%Y %H:%M'), fim_turno.strftime('%d/%m/%Y %H:%M')])
            turno_idx += 1
        acumulado += tempo
    exportar = input("\nDeseja exportar estes turnos para CSV? (1=Sim, 0=Não): ").strip()
    if exportar == "1":
        path=input("Digite o caminho da pasta para guardar:")
        nome_arquivo = f"{path}\{nome_escolhido.replace(' ', '_')}.csv"
                # Gera todos os turnos até ao fim do ano
        turnos_csv = []
        turno_idx = 1
        tempo_ciclo = sum(horas_dict.values())
        acumulado_total = 0
        data_fim_ano = datetime.datetime(inicio.year, 12, 31, 23, 59)
        while True:
            for nome, tempo in horas_dict.items():
                inicio_turno = inicio + (datetime.timedelta(minutes=acumulado_total) if unidade=="minutos" else datetime.timedelta(hours=acumulado_total))
                fim_turno = inicio_turno + (datetime.timedelta(minutes=tempo) if unidade=="minutos" else datetime.timedelta(hours=tempo))
                if nome == nome_escolhido:
                    if inicio_turno > data_fim_ano:
                        break
                    turnos_csv.append([turno_idx, nome_escolhido, inicio_turno.strftime('%d/%m/%Y %H:%M'), fim_turno.strftime('%d/%m/%Y %H:%M')])
                    turno_idx += 1
                acumulado_total += tempo
            if inicio_turno > data_fim_ano:
                break
        with open(nome_arquivo, "w", newline='', encoding="utf-8") as f:
            writer = csv.writer(f)
            writer.writerow(["Turno", "Consorte", "Início", "Fim"])
            writer.writerows(turnos_csv)
        print(f"Arquivo '{nome_arquivo}' criado com sucesso!")
  

#---------------------------selecionar a poça Javid
# horas de cada consorte da poça Javid
horas_javid = {
    "1º Maria Amélia Machado Pereira do Vale": 2910,  # 48h30m
    "2º Manuel Viera Cardoso": 530,                   # quinta 21:40 → sexta 06:30 (~8h50m)
    "3º José Viera Rego": 870,                        # sexta 06:30 → sexta 21:00 (~14h30m)
    "4º Carolina Fernandes do Vale": 570,             # sexta 21:00 → sábado 06:30 (~9h30m)
    "5º José Viera Rego": 870,                        # sábado 06:30 → sábado 21:00 (~14h30m)
    "6º Carolina Fernandes do Vale": 2880,            # sábado 21:00 → segunda 21:00 (48h)
    "7º Maria Amélia Machado Pereira do Vale": 3690,  # 61h30m
    "8º Joaquim Martins da Silva": 1800,              # 30h
    "9º António de Sousa Silva (Pita)": 120,          # 2h
    "10º Eugénio de Sousa Magalhães": 2400,           # 40h
    "11º Eduardo Fernades Maciel": 480,               # 8h
    "12º Manuel Viera Cardoso": 3040,                 # domingo 20:00 → terça 21:10 (~49h10m)
}



def get_javid():
    print("Selecione a opção:")
    print("0: Ver consortes e suas respetivas horas")
    print("1: Consultar consorte por dia e hora")
    resposta = int(input("Digite o número da opção: "))
    if resposta==0:
        print("Consultando consortes da poça Javid...")
        ano = datetime.date.today().year
        # Data de início: 1º de julho, 00:00 do ano atual
        inicio_data = proxima_terca_mais_proxima()
        inicio = datetime.datetime(ano, inicio_data.month, inicio_data.day, 21, 10)
        fim = datetime.datetime(ano, 12, 31, 23, 59)
        listar_consortes(horas_javid, inicio, unidade="minutos")
    elif resposta==1: 
        # Usuário escolhe dia e hora (sem ano)
        dia_str = input("Digite o dia (dd): ")
        mes_str = input("Digite o mês (mm): ")
        hora_str = input("Digite a hora (hh:mm): ")
        ano = datetime.date.today().year  # sempre o ano atual
        data_hora = datetime.datetime.strptime(f"{dia_str}/{mes_str}/{ano} {hora_str}", "%d/%m/%Y %H:%M")
        
        # Data de início: 1º de julho, 00:00 do ano atual
        inicio_data = proxima_terca_mais_proxima()
        inicio = datetime.datetime(ano, inicio_data.month, inicio_data.day, 21, 10)
        fim = datetime.datetime(ano, 12, 31, 23, 59)
        if not (inicio <= data_hora <= fim):
            print(f"Data fora do intervalo válido ({inicio_data.day} de {inicio_data.month} a 31 de dezembro).")
            return None

        minutos_decorridos = int((data_hora - inicio).total_seconds() // 60)
        total_ciclo = sum(horas_javid.values())
        minutos_no_ciclo = minutos_decorridos % total_ciclo  # ciclo se repete
        minutos_no_ciclo = minutos_decorridos % total_ciclo
        ciclos_completos = minutos_decorridos // total_ciclo


        # Determina o consorte e o início/fim do turno
        acumulado = 0
        for nome, tempo in horas_javid.items():
            if minutos_no_ciclo < acumulado + tempo:
                print(f"Neste momento ({data_hora}), o consorte é: {nome}")
                inicio_turno = inicio + datetime.timedelta(minutes=ciclos_completos * total_ciclo + acumulado)
                fim_turno = inicio_turno + datetime.timedelta(minutes=tempo)
                print(f"Início do turno: {inicio_turno.strftime('%d/%m/%Y %H:%M')}")
                print(f"Fim do turno:    {fim_turno.strftime('%d/%m/%Y %H:%M')}")
                break
            acumulado += tempo
        else:
            print("Nenhum consorte encontrado para esse momento.")
            return None
    return None

#---------------------------selecionar a poça Ínsuas

horas_insuas = {
    "Terras de Fate - David Fernandes":36,
    "Rigueira - António Pereira": 36,
    "Pomar - Carlos Xavier":12,
    "Rigueira - Rosa":12,
    "Rigueira - Joaquim Vale": 12,
    "nome da terra - Nídia":12,
    "Rigueira - António Maciel":12,
    "Compra - Rosa Machado": 12,
    "Rigueira - Cândido":12,
    "Rigueira - António Maciel":12,
    "Sepeira - Silvério": 24,  
    "Terras da Insua de baixo - Alfredo Pereira": 24,
    "Rigueira - Fondecescas":24,  
}

def get_insua():
    print("Selecione a opção:")
    print("0: Ver consortes e suas respetivas horas")
    print("1: Consultar consorte por dia e hora")
    resposta = int(input("Digite o número da opção: "))
    if resposta==0:
        print("Consultando consortes da poça Ínsuas...")
        ano = datetime.date.today().year
        inicio_data = primeiro_domingo_julho() - datetime.timedelta(days=1)
        inicio = datetime.datetime(ano, inicio_data.month, inicio_data.day, 21, 0)
        fim = datetime.datetime(ano, 12, 31, 23, 59)
        listar_consortes(horas_insuas, inicio, unidade="hours")
    elif resposta==1:
        # Usuário escolhe dia e hora (sem ano)
        dia_str = input("Digite o dia (dd): ")
        mes_str = input("Digite o mês (mm): ")
        hora_str = input("Digite a hora (hh:mm): ")
        ano = datetime.date.today().year  # sempre o ano atual
        data_hora = datetime.datetime.strptime(f"{dia_str}/{mes_str}/{ano} {hora_str}", "%d/%m/%Y %H:%M")
        
        # Data de início: 1º Domingo de julho, 00:00 do ano atual
        inicio_data = primeiro_domingo_julho() - datetime.timedelta(days=1)
        inicio = datetime.datetime(ano, inicio_data.month, inicio_data.day, 21, 0)
        fim = datetime.datetime(ano, 12, 31, 23, 59)
        if not (inicio <= data_hora <= fim):
            print(f"Data fora do intervalo válido ( {inicio_data.day} de {inicio_data.month} a 31 de dezembro).")
            return None

        horas_decorridas = int((data_hora - inicio).total_seconds() // 3600)
        total_ciclo = sum(horas_insuas.values())
        horas_no_ciclo = horas_decorridas % total_ciclo  # ciclo se repete
        ciclos_completos = horas_decorridas // total_ciclo

        # Determina o consorte
        acumulado = 0
        for nome, tempo in horas_insuas.items():
            acumulado += tempo
            if horas_no_ciclo < acumulado:
                print(f"Neste momento ({data_hora}), o consorte é: {nome}")
                # Stats do consorte
                #inicio_turno = inicio + datetime.timedelta(hours=ciclos_completos * total_ciclo + acumulado)
                inicio_turno = inicio + datetime.timedelta(hours=ciclos_completos * total_ciclo + (acumulado - tempo))
                fim_turno = inicio_turno + datetime.timedelta(hours=tempo)
                print(f"Início do turno: {inicio_turno.strftime('%d/%m/%Y %H:%M')}")
                print(f"Fim do turno:    {fim_turno.strftime('%d/%m/%Y %H:%M')}")
                return nome
        print("Nenhum consorte encontrado para esse momento.")
    
    
    return None
#---------------------------selecionar a poça Amaral

horas_amaral = {
    "António Silva":12, # **António Monteiro**
    "Nídia": 0,
    "Zé da Loba": 0,
    "Outra Pessoa":0,
    "Freitas":0,
    "António Monteiro": 24, # **António Monteiro**
    "Silvério Castro":0,
    "Outra Pessoa":0,
    "1º Tia Candinha": 7+2/3, #sábado de manhã (~=6h) até 13h40m **Tia Candinha**
    "Joaquim Rego": 16+1/3, # **Tia Candinha**
    "2º Tia Candinha": 10+2/3, #domingo de manhã (~=6h) até 16h40m **Tia Candinha**
    "Zé da Loba": 0,
    "Madanelo": 0,
    "Joaquim Monteiro":0,
    "Alice Martins":0,  
    "Azevedo": 0,
    "Outra Pessoa":300-1/3,  
}

def get_amaral():
    print("Selecione a opção:")
    print("0: Ver consortes e suas respetivas horas")
    print("1: Consultar consorte por dia e hora")
    resposta = int(input("Digite o número da opção: "))
    if resposta==0:
        print("Consultando consortes da poça de Amaral...")
        ano = datetime.date.today().year
        inicio_data = proxima_segunda_mais_proxima_antes()
        inicio = datetime.datetime(ano, inicio_data.month, inicio_data.day, 9, 0)
        fim = datetime.datetime(ano, 12, 31, 23, 59)
        listar_consortes(horas_amaral, inicio, unidade="hours")
    elif resposta==1:
        # Usuário escolhe dia e hora (sem ano)
        dia_str = input("Digite o dia (dd): ")
        mes_str = input("Digite o mês (mm): ")
        hora_str = input("Digite a hora (hh:mm): ")
        ano = datetime.date.today().year  # sempre o ano atual
        data_hora = datetime.datetime.strptime(f"{dia_str}/{mes_str}/{ano} {hora_str}", "%d/%m/%Y %H:%M")
        
        # Data de início: 1º Domingo de julho, 00:00 do ano atual
        inicio_data = proxima_segunda_mais_proxima_antes()
        inicio = datetime.datetime(ano, inicio_data.month, inicio_data.day, 9, 0)
        fim = datetime.datetime(ano, 12, 31, 23, 59)
        if not (inicio <= data_hora <= fim):
            print(f"Data fora do intervalo válido ( {inicio_data.day} de {inicio_data.month} a 31 de dezembro).")
            return None

        horas_decorridas = int((data_hora - inicio).total_seconds() // 3600)
        total_ciclo = sum(horas_amaral.values())
        horas_no_ciclo = horas_decorridas % total_ciclo  # ciclo se repete
        ciclos_completos = horas_decorridas // total_ciclo

        # Determina o consorte
        acumulado = 0
        for nome, tempo in horas_amaral.items():
            acumulado += tempo
            if horas_no_ciclo < acumulado:
                print(f"Neste momento ({data_hora}), o consorte é: {nome}")
                # Stats do consorte
                #inicio_turno = inicio + datetime.timedelta(hours=ciclos_completos * total_ciclo + acumulado)
                inicio_turno = inicio + datetime.timedelta(hours=ciclos_completos * total_ciclo + (acumulado - tempo))
                fim_turno = inicio_turno + datetime.timedelta(hours=tempo)
                print(f"Início do turno: {inicio_turno.strftime('%d/%m/%Y %H:%M')}")
                print(f"Fim do turno:    {fim_turno.strftime('%d/%m/%Y %H:%M')}")
                return nome
        print("Nenhum consorte encontrado para esse momento.")

#---------------------------selecionar a poça Cal

horas_cal = {
    #1ª semana
    "1ªs Joaquim Aurélio 1º":18, # 21:10->15:10 = 18h domingo->segunda
    "1ªs Emélia Rocha": 6, # 15:10->21:10 = 6h segunda->segunda
    "1ªs Isabel 1º": 4+1/2, #4h:30 ou 21:10->1:40 segunda-terça
    "1ªs Nuno":4+1/2, # 4h:30 0u 1:40->6:10 terça->terça
    "1ªs Mendanha 1º":15, # 6:10->21:10 terça->terça
    "1ªs Monteiro": 24, #terça 21:10->quarta 21:10
    "1ªs Salvador":15, # quarta 21:10-> quinta 12:10
    "1ªs Maria Cancela":9, # quinta 12:10-> quinta 21:10
    "1ªs Joaquim Aurélio 2º": 9, #quinta 21:10-> sexta 6:10
    "1ªs Cândido Fontainha": 15, # sexta 6:10 -> sábado 21:10
    "1ªs Mendanha 2º": 9, # sábado 21:10 -> domingo 6:10
    "1ªs Isabel 2º": 15,  # domingo 6:10 -> domingo 21:10 (:
    #2ª semana
    "2ªs Joaquim Aurélio 1º":18, #domingo 21:10 -> segunda 15:10
    "2ªs Emélia Rocha": 6, # segunda 15:10 -> segunda 21:10
    "2ªs Mendanha 1º":9, # segunda 21:10 -> terça 6:10
    "2ªs Isabel 1º": 7+1/2, # terça 6:10 -> terça 13.40 
    "2ªs Nuno":7+1/2, # terça 13:40 -> terça 21:10
    "2ªs Alfredo Machado":0, #-> falta 9h o que faltava da terça 21:10 -> quarta 6:10
    "2ªs Monteiro": 15, #quarta 6:10 -> quarta 21:10
    "2ªs Salvador":15, # quarta 21:10 -> quinta 12:10
    "2ªs Maria Cancela":9, # quinta 12:10 -> quinta 21:10
    "2ªs Cândido Fontainha": 9, # quinta 21:10 -> sexta 6:10 
    "2ªs ":0, # falta 6h30m sexta 6:10 -> sábado 13:40
    "2ªs Joaquim Aurélio 2º": 9, # sexta 13:40 -> sábado 6:10
    "2ªs Isabel 2º": 24, # sábado 6:10 -> domingo 6:10
    "2ªs Mendanha 2º": 15, # domingo 6:10 -> domingo 21:10
}

def get_cal():
    print("Selecione a opção:")
    print("0: Ver consortes e suas respetivas horas")
    print("1: Consultar consorte por dia e hora")
    resposta = int(input("Digite o número da opção: "))
    if resposta==0:
        print("Consultando consortes da poça de Cal...")
        ano = datetime.date.today().year
        inicio_data = primeiro_domingo_junho()
        inicio = datetime.datetime(ano, inicio_data.month, inicio_data.day, 21, 10)
        fim = datetime.datetime(ano, 12, 31, 23, 59)
        listar_consortes(horas_cal, inicio, unidade="hours")
    elif resposta==1:
        # Usuário escolhe dia e hora (sem ano)
        dia_str = input("Digite o dia (dd): ")
        mes_str = input("Digite o mês (mm): ")
        hora_str = input("Digite a hora (hh:mm): ")
        ano = datetime.date.today().year  # sempre o ano atual
        data_hora = datetime.datetime.strptime(f"{dia_str}/{mes_str}/{ano} {hora_str}", "%d/%m/%Y %H:%M")
        
        # Data de início: 1º Domingo de julho, 00:00 do ano atual
        inicio_data = primeiro_domingo_junho()
        inicio = datetime.datetime(ano, inicio_data.month, inicio_data.day, 21, 10)
        fim = datetime.datetime(ano, 12, 31, 23, 59)
        if not (inicio <= data_hora <= fim):
            print(f"Data fora do intervalo válido ( {inicio_data.day} de {inicio_data.month} a 31 de dezembro).")
            return None

        horas_decorridas = int((data_hora - inicio).total_seconds() // 3600)
        total_ciclo = sum(horas_cal.values())
        horas_no_ciclo = horas_decorridas % total_ciclo  # ciclo se repete
        ciclos_completos = horas_decorridas // total_ciclo

        # Determina o consorte
        acumulado = 0
        for nome, tempo in horas_cal.items():
            acumulado += tempo
            if horas_no_ciclo < acumulado:
                print(f"Neste momento ({data_hora}), o consorte é: {nome}")
                # Stats do consorte
                #inicio_turno = inicio + datetime.timedelta(hours=ciclos_completos * total_ciclo + acumulado)
                inicio_turno = inicio + datetime.timedelta(hours=ciclos_completos * total_ciclo + (acumulado - tempo))
                fim_turno = inicio_turno + datetime.timedelta(hours=tempo)
                print(f"Início do turno: {inicio_turno.strftime('%d/%m/%Y %H:%M')}")
                print(f"Fim do turno:    {fim_turno.strftime('%d/%m/%Y %H:%M')}")
                return nome
        print("Nenhum consorte encontrado para esse momento.")



#---------------------------start do programa
print("Bem-vindo ao sistema de consortes das poças!")
#time.sleep(1)
print("Escolha uma poça para consultar os consortes:")
#time.sleep(1)
# Solicita ao usuário escolher uma poça
escolhida = get_poca()
print(f"Você escolheu: {escolhida}")
if escolhida == "Javid":
    get_javid()
elif escolhida == "Ínsuas":
    get_insua()
elif escolhida == "Amaral":
    get_amaral()
elif escolhida == "Cal":
    get_cal()
else:
    print("Poça inválida selecionada.")


#Made in Quintiães





