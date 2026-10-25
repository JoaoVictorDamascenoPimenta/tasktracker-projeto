def exibir_menu():
    print("\n===== TASKTRACKER =====")
    print("1 - Cadastrar nova tarefa")
    print("2 - Visualizar tarefas cadastradas")
    print("3 - Sair")


def cadastrar_tarefa(tarefas):
    titulo = input("Digite o título da tarefa: ").strip()

    while not titulo:
        print("Erro: o título não pode ficar vazio.")
        titulo = input("Digite o título da tarefa: ").strip()

    descricao = input("Digite a descrição da tarefa: ").strip()

    prioridade = input("Digite a prioridade (Alta, Média ou Baixa): ").strip().capitalize()

    while prioridade not in ["Alta", "Média", "Baixa"]:
        print("Erro: prioridade inválida. Digite Alta, Média ou Baixa.")
        prioridade = input("Digite a prioridade (Alta, Média ou Baixa): ").strip().capitalize()

    data_limite = input("Digite a data limite (DD/MM/AAAA): ").strip()

    tarefa = {
        "titulo": titulo,
        "descricao": descricao,
        "prioridade": prioridade,
        "data_limite": data_limite,
        "status": "Pendente"
    }

    tarefas.append(tarefa)
    print("Tarefa cadastrada com sucesso!")


def visualizar_tarefas(tarefas):
    if not tarefas:
        print("Não há tarefas cadastradas.")
        return

    print("\n===== TAREFAS CADASTRADAS =====")

    for numero, tarefa in enumerate(tarefas, start=1):
        print(f"\nTarefa {numero}")
        print(f"Título: {tarefa['titulo']}")
        print(f"Descrição: {tarefa['descricao']}")
        print(f"Prioridade: {tarefa['prioridade']}")
        print(f"Data limite: {tarefa['data_limite']}")
        print(f"Status: {tarefa['status']}")


def main():
    tarefas = []

    while True:
        exibir_menu()
        opcao = input("Escolha uma opção: ").strip()

        if opcao == "1":
            cadastrar_tarefa(tarefas)
        elif opcao == "2":
            visualizar_tarefas(tarefas)
        elif opcao == "3":
            print("Encerrando o TaskTracker. Até mais!")
            break
        else:
            print("Opção inválida. Escolha 1, 2 ou 3.")


if __name__ == "__main__":
    main()
