"""
Exemplos de uso do Browser GPT Automation.

Este arquivo demonstra diferentes formas de usar a biblioteca.
"""
import sys
import time
from pathlib import Path

# Adiciona o diretório src ao path
sys.path.insert(0, str(Path(__file__).parent / "src"))

from driver_manager import DriverManager
from chatgpt_automation import ChatGPTAutomation
import logging


# Configuração de logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)


def example_basic_usage():
    """Exemplo básico: Abrir ChatGPT e verificar login."""
    logger.info("=== Exemplo 1: Uso Básico ===")
    
    driver_manager = DriverManager(use_user_profile=True)
    
    try:
        driver = driver_manager.create_driver()
        chatgpt = ChatGPTAutomation(driver)
        
        chatgpt.open_chatgpt()
        
        if chatgpt.is_logged_in():
            logger.info("✓ Você está logado!")
        else:
            logger.info("✗ Você não está logado")
            chatgpt.click_login()
        
        time.sleep(5)
        
    finally:
        driver_manager.quit()


def example_context_manager():
    """Exemplo usando context manager (recomendado)."""
    logger.info("=== Exemplo 2: Context Manager ===")
    
    with DriverManager(use_user_profile=True) as driver:
        chatgpt = ChatGPTAutomation(driver)
        chatgpt.open_chatgpt()
        
        logger.info("Navegador aberto com context manager")
        time.sleep(5)
    
    logger.info("Navegador fechado automaticamente")


def example_without_user_profile():
    """Exemplo sem usar o perfil do usuário."""
    logger.info("=== Exemplo 3: Sem Perfil do Usuário ===")
    
    with DriverManager(use_user_profile=False) as driver:
        chatgpt = ChatGPTAutomation(driver)
        chatgpt.open_chatgpt()
        
        logger.info("Chrome aberto sem perfil do usuário (sessão limpa)")
        time.sleep(5)


def example_custom_actions():
    """Exemplo com ações customizadas."""
    logger.info("=== Exemplo 4: Ações Customizadas ===")
    
    with DriverManager(use_user_profile=True) as driver:
        chatgpt = ChatGPTAutomation(driver)
        chatgpt.open_chatgpt()
        
        # Aguarda carregamento completo
        chatgpt.wait_for_page_load()
        
        # Verifica status de login
        is_logged = chatgpt.is_logged_in()
        logger.info(f"Status de login: {'Logado' if is_logged else 'Não logado'}")
        
        # Você pode adicionar suas próprias ações aqui
        # Por exemplo: navegar para outras páginas, interagir com elementos, etc.
        
        time.sleep(5)


def main():
    """Executa todos os exemplos."""
    examples = [
        ("Uso Básico", example_basic_usage),
        ("Context Manager", example_context_manager),
        ("Sem Perfil do Usuário", example_without_user_profile),
        ("Ações Customizadas", example_custom_actions),
    ]
    
    print("\n" + "="*60)
    print("EXEMPLOS DE USO - Browser GPT Automation")
    print("="*60)
    
    for i, (name, func) in enumerate(examples, 1):
        print(f"\n{i}. {name}")
    
    print("\n0. Executar todos")
    print("="*60)
    
    try:
        choice = input("\nEscolha um exemplo (0-4): ").strip()
        
        if choice == "0":
            for name, func in examples:
                print(f"\n{'='*60}")
                func()
                time.sleep(2)
        elif choice.isdigit() and 1 <= int(choice) <= len(examples):
            examples[int(choice)-1][1]()
        else:
            print("Opção inválida!")
            
    except KeyboardInterrupt:
        print("\n\nExecução interrompida pelo usuário")
    except Exception as e:
        logger.error(f"Erro durante execução: {e}", exc_info=True)


if __name__ == "__main__":
    main()
