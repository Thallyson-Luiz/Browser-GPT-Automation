"""
Script principal para automação do ChatGPT usando o perfil do Chrome do usuário.

Este script:
1. Inicia o Chrome com o perfil do usuário (mantendo contas logadas)
2. Abre o ChatGPT
3. Verifica se está logado
4. Realiza login se necessário
"""
import logging
import time

from driver_manager import DriverManager
from chatgpt_automation import ChatGPTAutomation


# Configuração de logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)


def main():
    """Função principal do script."""
    logger.info("=" * 60)
    logger.info("Iniciando Browser GPT Automation")
    logger.info("=" * 60)
    
    # Cria o gerenciador do driver com perfil do usuário
    driver_manager = DriverManager(use_user_profile=True)
    
    try:
        # Inicia o Chrome com o perfil do usuário
        driver = driver_manager.create_driver()
        
        # Cria instância da automação do ChatGPT
        chatgpt = ChatGPTAutomation(driver)
        
        # Abre o ChatGPT
        chatgpt.open_chatgpt()
        
        # Verifica se está logado
        if not chatgpt.is_logged_in():
            logger.info("Usuário não está logado. Clicando no botão de login...")
            chatgpt.click_login()
            logger.info("Aguarde para completar o login manualmente se necessário...")
        else:
            logger.info("Usuário já está logado! Pronto para usar.")
        
        # Mantém o navegador aberto para interação
        logger.info("Navegador aberto. Pressione Ctrl+C para encerrar.")

        messageNew =chatgpt.send_message("Quantos anos você tem?")
        logger.info(f"Resposta do ChatGPT:\n\n{messageNew}\n\n")

        logger.info("\nEncerrando aplicação...")
            
    except Exception as e:
        logger.error(f"Erro durante execução: {e}", exc_info=True)
        
    finally:
        # Fecha o driver
        driver_manager.quit()
        logger.info("Aplicação encerrada")


if __name__ == "__main__":
    main()
