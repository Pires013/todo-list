import os
import json

tarefas = []
tarefas_refazer = []

ARQUIVO_JSON = 'tarefas.json'

def ler_dados():
    """Lê o arquivo JSON. Se não existir, retorna listas vazias."""
    if not os.path.exists(ARQUIVO_JSON):
        return [], []
    
    with open(ARQUIVO_JSON, 'r', encoding='utf8') as arquivo:
        dados = json.load(arquivo)
        return dados.get('tarefas', []), dados.get('tarefas_refazer', [])

def salvar_dados(tarefas, tarefas_refazer):
    """Salva o estado atual das duas listas no arquivo JSON."""
    dados = {
        'tarefas': tarefas,
        'tarefas_refazer': tarefas_refazer
    }
    with open(ARQUIVO_JSON, 'w', encoding='utf8') as arquivo:
        json.dump(dados, arquivo, indent=2, ensure_ascii=False)

tarefas, tarefas_refazer = ler_dados()


def listar(tarefas):
    print('\nTAREFAS:')
    if not tarefas:
        print('Nada para mostrar.')
    else:
        for tarefa in tarefas:
            print(f'- {tarefa}')
    print()

def desfazer(tarefas, tarefas_refazer):
    if not tarefas:
        print('Nada para desfazer.')
        return
    
    tarefa = tarefas.pop()
    tarefas_refazer.append(tarefa)
    print(f'Desfeito: "{tarefa}"')

def refazer(tarefas, tarefas_refazer):
    if not tarefas_refazer:
        print('Nada para refazer.')
        return
    
    tarefa = tarefas_refazer.pop()
    tarefas.append(tarefa)
    print(f'Refeito: "{tarefa}"')

def adicionar(tarefa, tarefas, tarefas_refazer):
    tarefa = tarefa.strip()
    if not tarefa:
        print('Você não digitou nada.')
        return
    
    tarefas.append(tarefa)
    tarefas_refazer.clear()

while True:
    print('Comandos: [listar, desfazer, refazer, sair]')
    entrada = input('Digite uma tarefa ou comando: ').strip()

    if entrada.lower() == 'listar':
        listar(tarefas)
    
    elif entrada.lower() == 'desfazer':
        if tarefas:
            item = tarefas.pop()
            tarefas_refazer.append(item)
            salvar_dados(tarefas, tarefas_refazer)
            print(f'<- Desfeito: "{item}"')
        else:
            print('Nada para desfazer.')
        listar(tarefas)

    elif entrada.lower() == 'refazer':
        if tarefas_refazer:
            item = tarefas_refazer.pop()
            tarefas.append(item)
            salvar_dados(tarefas, tarefas_refazer)
            print(f'-> Refeito: "{item}"')
        else:
            print('Nada para refazer.')
        listar(tarefas)

    elif entrada.lower() == 'sair':
        print('Até logo!')
        break

    else:
        if entrada:
            tarefas.append(entrada)
            tarefas_refazer.clear()
            salvar_dados(tarefas, tarefas_refazer)
            listar(tarefas)