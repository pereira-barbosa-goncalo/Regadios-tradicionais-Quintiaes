import datetime
import csv
import os

# Determinar os dias
dias_da_semana = ["Domingo", "Segunda", "Terça", "Quarta", "Quinta", "Sexta", "Sábado"]

def primeiro_domingo_julho():
    ano = datetime.date.today().year
    for dia in range(1, 8):
        data = datetime.date(ano, 7, dia)
        if data.weekday() == 6:  # 6 = domingo
            return data

def proxima_terca_mais_proxima():
    hoje = datetime.date.today()
    ano = hoje.year
    data_base = datetime.date(ano, 6, 29)

    dias_para_terca = (1 - data_base.weekday()) % 7
    proxima_terca = data_base + datetime.timedelta(days=dias_para_terca)
    dias_para_terca_antes = (data_base.weekday() - 1) % 7
    terca_antes = data_base - datetime.timedelta(days=dias_para_terca_antes)

    return proxima_terca if abs((proxima_terca - data_base).days) < abs((terca_antes - data_base).days) else terca_antes

def proxima_segunda_mais_proxima():
    hoje = datetime.date.today()
    ano = hoje.year
    data_base = datetime.date(ano, 6, 29)

    dias_para_segunda = (0 - data_base.weekday()) % 7
    proxima_segunda = data_base + datetime.timedelta(days=dias_para_segunda)
    dias_para_segunda_antes = (data_base.weekday() - 0) % 7
    segunda_antes = data_base - datetime.timedelta(days=dias_para_segunda_antes)

    return proxima_segunda if abs((proxima_segunda - data_base).days) < abs((segunda_antes - data_base).days) else segunda_antes

#--------------------------- Selecionar a poça
pocas = {"Javid": 0, "Ínsuas": 1}

def get_poca():
    print("Selecione a poça:")
    for name, index in pocas.items():
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

    consortes = list(horas_dict.keys())
    print("Consortes:")
    for idx, nome in enumerate(consortes):
        print(f"{idx}: {nome}")

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
        path = input("Digite o caminho da pasta para guardar: ").strip()
        nome_arquivo = os.path.join(path, f"{nome_escolhido.replace(' ', '_')}.csv")

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

# --------------------------- Horas Javid
horas_javid = {
    "1º Maria Amélia Machado Pereira do Vale": 2910,
    "2º Manuel Viera Cardoso": 530,
    "3º José Viera Rego": 870,
    "4º Carolina Fernandes do Vale": 570,
    "5º José Viera Rego": 870,
    "6º Carolina Fernandes do Vale": 2880,
    "7º Maria Amélia Machado Pereira do Vale": 3690,
    "8º Joaquim Martins da Silva": 1800,
    "9º António de Sousa Silva (Pita)": 120,
    "10º Eugénio de Sousa Magalhães": 2400,
    "11º Eduardo Fernades Maciel": 480,
    "12º Manuel Viera Cardoso": 3040,
}

# --------------------------- Horas Ínsuas
horas_insuas = {
    "Terras de Fate - David": 36,
    "Rigueira - Madanelo": 36,
    "Pomar - Carlos Xavier": 12,
    "Rigueira - Rosa": 12,
    "Rigueira - Joaquim Lumbrem": 12,
    "nome da terra - Nídia": 12,
    "Rigueira - Domingos Aurélio": 12,
    "Compra - Rosa": 12,
    "nome da terra - Cândido": 12,
    "nome da terra - Domingos Aurélio": 12,
    "Sepeira - Silvério": 24,
    "Terras da ínssua de baixo - Madanelo": 24,
    "Rigueira - Fondecescas": 24,
}

# --------------------------- Start
print("Bem-vindo ao sistema de consortes das poças!")
escolhida = get_poca()
print(f"Você escolheu: {escolhida}")

if escolhida == "Javid":
    # Chamar função específica de Javid
    listar_consortes(horas_javid, datetime.datetime(datetime.date.today().year, *proxima_terca_mais_proxima().timetuple()[1:3], 21, 10))
elif escolhida == "Ínsuas":
    listar_consortes(horas_insuas, datetime.datetime(datetime.date.today().year, *primeiro_domingo_julho().timetuple()[1:3], 21, 0), unidade="hours")
else:
    print("Poça inválida selecionada.")
