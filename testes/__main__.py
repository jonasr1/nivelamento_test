from transformacao_dados.main import main as transformacao_main
from web_scraping.main import main as web_scraping_main


def display_menu():
    print('Escolha qual parte do projeto deseja executar:')
    print('1. Web Scraping')
    print('2. Transformação de Dados')
    print('Digite o número da opção:')
    
def get_user_choice():
    while True:
        choice = input()
        if choice in {'1', '2'}:
            return choice
        print('Opção inválida!')

def execute_choice(choice):
    try:
        if choice == '1':
            print('Executando Web Scraping...')
            web_scraping_main()
        elif choice == '2':
            print('Executando Transformação de Dados...')
            transformacao_main()
    except Exception as e:
        print(f'Erro ao executar a opção escolhida: {e}')

def main():
    display_menu()
    choice = get_user_choice()
    execute_choice(choice)

if __name__ == "__main__":
    main()
