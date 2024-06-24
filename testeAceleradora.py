import datetime


def exibir_menu_principal():
    print("\nMenu Principal")
    print("1- Cadastrar Paciente")
    print("2- Marcar Consulta")
    print("3- Cancelar Consulta")
    print("4- Sair")
    opcao = input("Escolha uma opção: ")
    return opcao


def cadastrar_paciente(pacientes):
    nome = input("Digite o nome do paciente: ")
    telefone = input("Digite o telefone do paciente: ")

    # Verifica se o telefone já está cadastrado
    for paciente in pacientes:
        if paciente['telefone'] == telefone:
            print("Paciente já cadastrado!")
            return

    paciente = {
        "nome": nome,
        "telefone": telefone
    }
    pacientes.append(paciente)
    print("Paciente cadastrado com sucesso!")


def listar_pacientes(pacientes):
    if not pacientes:
        print("Nenhum paciente cadastrado.")
        return False
    print("\nLista de Pacientes:")
    for idx, paciente in enumerate(pacientes):
        print(f"{idx + 1}. {paciente['nome']} - {paciente['telefone']}")
    return True


def validar_data_hora(dia, hora):
    try:
        data_hora = datetime.datetime.strptime(f"{dia} {hora}", "%d/%m/%Y %H:%M")
        if data_hora < datetime.datetime.now():
            print("Não é possível agendar consultas retroativas.")
            return False
        return data_hora
    except ValueError:
        print("Data ou hora inválida.")
        return False


def marcar_consulta(pacientes, consultas):
    if not listar_pacientes(pacientes):
        return
    paciente_num = int(input("Escolha o número do paciente: ")) - 1
    if 0 <= paciente_num < len(pacientes):
        dia = input("Digite o dia da consulta (DD/MM/AAAA): ")
        hora = input("Digite a hora da consulta (HH:MM): ")

        data_hora = validar_data_hora(dia, hora)
        if not data_hora:
            return

        especialidade = input("Digite a especialidade da consulta: ")

        # Verifica se já existe uma consulta no mesmo dia e hora
        for consulta in consultas:
            if consulta['dia'] == dia and consulta['hora'] == hora:
                print("Horário já agendado para outra consulta.")
                return

        consulta = {
            "paciente": pacientes[paciente_num],
            "dia": dia,
            "hora": hora,
            "especialidade": especialidade
        }
        consultas.append(consulta)
        print("Consulta marcada com sucesso!")
    else:
        print("Número de paciente inválido.")


def listar_consultas(consultas):
    if not consultas:
        print("Nenhuma consulta marcada.")
        return False
    print("\nLista de Consultas:")
    for idx, consulta in enumerate(consultas):
        paciente = consulta["paciente"]
        print(f"{idx + 1}. {paciente['nome']} - {consulta['dia']} {consulta['hora']} - {consulta['especialidade']}")
    return True


def cancelar_consulta(consultas):
    if not listar_consultas(consultas):
        return
    consulta_num = int(input("Escolha o número da consulta para cancelar: ")) - 1
    if 0 <= consulta_num < len(consultas):
        consulta = consultas[consulta_num]
        paciente = consulta["paciente"]
        print(f"Consulta de {paciente['nome']} - {consulta['dia']} {consulta['hora']} - {consulta['especialidade']}")
        confirmar = input("Deseja realmente cancelar esta consulta? (s/n): ").lower()
        if confirmar == 's':
            consultas.pop(consulta_num)
            print("Consulta cancelada com sucesso!")
        else:
            print("Cancelamento não confirmado.")
    else:
        print("Número de consulta inválido.")


def main():
    pacientes = []
    consultas = []
    while True:
        opcao = exibir_menu_principal()
        if opcao == '1':
            cadastrar_paciente(pacientes)
        elif opcao == '2':
            marcar_consulta(pacientes, consultas)
        elif opcao == '3':
            cancelar_consulta(consultas)
        elif opcao == '4':
            print("Saindo...")
            break
        else:
            print("Opção inválida. Tente novamente.")


# Executa o programa principal
if __name__ == "__main__":
    main()
