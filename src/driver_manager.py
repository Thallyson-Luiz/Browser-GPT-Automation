"""
Gerenciador do driver do Chrome com perfil do usuário.
"""
import undetected_chromedriver as uc
from selenium.webdriver.chrome.options import Options
from typing import Optional
import logging

from config import Config


# Configuração de logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)


class DriverManager:
    """Gerencia a criação e configuração do driver do Chrome."""
    
    def __init__(self, use_user_profile: bool = True):
        """
        Inicializa o gerenciador do driver.
        
        Args:
            use_user_profile: Se True, usa o perfil do Chrome do usuário
        """
        self.use_user_profile = use_user_profile
        self.driver: Optional[uc.Chrome] = None
        
    def create_driver(self) -> uc.Chrome:
        """
        Cria e configura o driver do Chrome.
        
        Returns:
            uc.Chrome: Instância do driver configurado
        """
        options = self._configure_options()
        
        try:
            logger.info("Iniciando Chrome com undetected_chromedriver...")
            
            # Remove use_subprocess quando usa perfil do usuário
            # para evitar problemas de comunicação
            self.driver = uc.Chrome(options=options)
            
            if self.use_user_profile:
                logger.info(f"Chrome iniciado com perfil: {Config.CHROME_PROFILE}")
            else:
                logger.info("Chrome iniciado sem perfil do usuário")
                
            return self.driver
            
        except Exception as e:
            logger.error(f"Erro ao criar driver: {e}")
            raise
    
    def _configure_options(self) -> Options:
        """
        Configura as opções do Chrome.
        
        Returns:
            Options: Opções configuradas
        """
        options = uc.ChromeOptions()
        
        if self.use_user_profile:
            # Usa perfil de automação separado para evitar conflitos
            # Isso permite que o Chrome normal continue aberto
            options.add_argument(f"--user-data-dir={Config.AUTOMATION_PROFILE_DIR}")
            logger.info(f"Configurado para usar perfil de automação: {Config.AUTOMATION_PROFILE_DIR}")
        
        # Opções adicionais para melhor funcionamento
        options.add_argument("--no-first-run")
        options.add_argument("--no-default-browser-check")
        options.add_argument("--disable-blink-features=AutomationControlled")
        
        # Opções para evitar problemas de inicialização
        options.add_argument("--disable-dev-shm-usage")
        options.add_argument("--disable-gpu")
        options.add_argument("--no-sandbox")
        
        # Desabilita notificações e popups
        options.add_argument("--disable-notifications")
        options.add_argument("--disable-popup-blocking")
        
        return options # type: ignore
    
    def quit(self):
        """Fecha o driver se estiver aberto."""
        if self.driver:
            try:
                self.driver.quit()
                logger.info("Driver fechado com sucesso")
            except Exception as e:
                logger.error(f"Erro ao fechar driver: {e}")
            finally:
                self.driver = None
    
    def __enter__(self):
        """Context manager entry."""
        return self.create_driver()
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        """Context manager exit."""
        self.quit()
