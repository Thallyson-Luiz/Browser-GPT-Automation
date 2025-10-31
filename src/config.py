"""
Configurações do projeto Browser GPT Automation.
"""
import os
from pathlib import Path


class Config:
    """Classe de configuração centralizada."""
    
    # Diretório do perfil do Chrome do usuário
    # No Linux, o perfil padrão fica em ~/.config/google-chrome
    CHROME_USER_DATA_DIR = os.path.expanduser("~/.config/google-chrome")
    
    # Nome do perfil a ser usado (Default é o perfil padrão)
    CHROME_PROFILE = "Default"
    
    # Diretório para perfil de automação (separado do perfil principal)
    AUTOMATION_PROFILE_DIR = os.path.expanduser("~/.config/chrome-automation")
    
    # Timeout padrão para operações
    DEFAULT_TIMEOUT = 10
    
    # URLs
    CHATGPT_URL = "https://chatgpt.com"
    
    @classmethod
    def get_chrome_profile_path(cls) -> str:
        """
        Retorna o caminho completo do perfil do Chrome.
        
        Returns:
            str: Caminho do perfil do Chrome
        """
        return cls.CHROME_USER_DATA_DIR
    
    @classmethod
    def validate_chrome_profile(cls) -> bool:
        """
        Valida se o perfil do Chrome existe.
        
        Returns:
            bool: True se o perfil existe, False caso contrário
        """
        profile_path = Path(cls.CHROME_USER_DATA_DIR) / cls.CHROME_PROFILE
        return profile_path.exists()
