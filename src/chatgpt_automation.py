"""
Módulo de automação do ChatGPT.
"""
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException
import logging
import time

from config import Config


logger = logging.getLogger(__name__)


class ChatGPTAutomation:
    """Classe para automação de interações com o ChatGPT."""
    
    def __init__(self, driver):
        """
        Inicializa a automação do ChatGPT.
        
        Args:
            driver: Instância do Selenium WebDriver
        """
        self.driver = driver
        self.wait = WebDriverWait(driver, Config.DEFAULT_TIMEOUT)
    
    def open_chatgpt(self):
        """Abre o site do ChatGPT."""
        logger.info(f"Abrindo {Config.CHATGPT_URL}...")
        self.driver.get(Config.CHATGPT_URL)
        time.sleep(2)  # Aguarda carregamento inicial
        logger.info("ChatGPT aberto com sucesso")
    
    def is_logged_in(self) -> bool:
        """
        Verifica se o usuário está logado no ChatGPT.
        
        Returns:
            bool: True se logado, False caso contrário
        """
        try:
            # Tenta encontrar o botão de login
            # Se não encontrar, provavelmente está logado
            self.driver.find_element(By.XPATH, "//button[@data-testid='login-button']")
            logger.info("Usuário não está logado")
            return False
        except NoSuchElementException:
            logger.info("Usuário já está logado")
            return True
    
    def click_login(self):
        """Clica no botão de login."""
        try:
            logger.info("Procurando botão de login...")
            login_button = self.wait.until(
                EC.element_to_be_clickable((By.XPATH, "//button[@data-testid='login-button']"))
            )
            login_button.click()
            logger.info("Botão de login clicado")
            time.sleep(2)
        except TimeoutException:
            logger.warning("Botão de login não encontrado - usuário pode já estar logado")
        except Exception as e:
            logger.error(f"Erro ao clicar no botão de login: {e}")
            raise
    
    def wait_for_page_load(self, timeout: int = None): # type: ignore
        """
        Aguarda o carregamento completo da página.
        
        Args:
            timeout: Tempo máximo de espera em segundos
        """
        if timeout is None:
            timeout = Config.DEFAULT_TIMEOUT
            
        try:
            self.wait.until(
                lambda driver: driver.execute_script("return document.readyState") == "complete"
            )
            logger.info("Página carregada completamente")
        except TimeoutException:
            logger.warning("Timeout ao aguardar carregamento da página")
    
    def send_message(self, message: str):
        """
        Envia uma mensagem para o ChatGPT.
        
        Args:
            message: Mensagem a ser enviada
        
        return:
            message: str
        """
        try:
            logger.info(f"Enviando mensagem: {message[:50]}...")
            
            # Localiza o campo de texto (pode variar dependendo da versão do ChatGPT)
            input = self.wait.until(
                EC.presence_of_element_located((By.XPATH, "//div[@id='prompt-textarea']/p"))
            )
            
            input.click()
            input.clear()
            input.send_keys(message)
            time.sleep(1)
            
            # Procura e clica no botão de enviar
            try:
                send_button = self.driver.find_element(
                    By.XPATH, 
                    "//button[@id='composer-submit-button']"
                )
                send_button.click()
                
                logger.info("Mensagem enviada com sucesso")
            except NoSuchElementException:
                logger.error("Botão de enviar não encontrado")
                raise

            time.sleep(10)

            # Aguarda a resposta do ChatGPT

            message_ai = self.wait.until(EC.presence_of_element_located((By.XPATH, "//div[@data-message-author-role='assistant'][last()]")))

            return message_ai.text

        except Exception as e:
            logger.error(f"Erro ao enviar mensagem: {e}")
            raise
