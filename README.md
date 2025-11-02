# Browser GPT Automation 🤖

[![Python](https://img.shields.io/badge/Python-3.7+-blue.svg)](https://www.python.org/)
[![Selenium](https://img.shields.io/badge/Selenium-4.38+-green.svg)](https://www.selenium.dev/)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

Automação inteligente do ChatGPT usando Selenium e undetected-chromedriver, permitindo interações automatizadas mantendo suas sessões e preferências do navegador.

## 📋 Características

- ✅ **Automação Seamless**: Usa `undetected-chromedriver` para evitar detecção de automação
- ✅ **Perfil de Automação**: Cria um perfil separado (`~/.config/chrome-automation`) para não interferir com seu Chrome principal
- ✅ **Context Manager**: Suporte para uso com `with` statement para gerenciamento automático de recursos
- ✅ **Login Automatizado**: Detecta automaticamente se está logado e facilita o processo de login
- ✅ **Envio e Recebimento de Mensagens**: Interface simples para enviar mensagens e obter respostas do ChatGPT
- ✅ **Logging Completo**: Sistema de logs detalhado para debug e monitoramento

## 🚀 Instalação

### Pré-requisitos

- Python 3.7 ou superior
- Google Chrome instalado no sistema

### Instalar dependências

```bash
pip install -r requirements.txt
```

## 📖 Uso

### Script Principal

Execute o script principal para usar a automação:

```bash
cd src
python main.py
```

O script `main.py` realiza as seguintes ações:
1. Inicia o Chrome com o perfil de automação
2. Abre o ChatGPT
3. Verifica se está logado (faz login se necessário)
4. Envia uma mensagem de exemplo e exibe a resposta

### Uso Básico

```python
from src.driver_manager import DriverManager
from src.chatgpt_automation import ChatGPTAutomation

# Criar o driver
driver_manager = DriverManager(use_user_profile=True)
driver = driver_manager.create_driver()

# Instanciar automação
chatgpt = ChatGPTAutomation(driver)

# Abrir ChatGPT
chatgpt.open_chatgpt()

# Verificar login
if not chatgpt.is_logged_in():
    chatgpt.click_login()
    print("Complete o login manualmente se necessário...")

# Fechar o driver
driver_manager.quit()
```

### Usando Context Manager (Recomendado)

```python
from src.driver_manager import DriverManager
from src.chatgpt_automation import ChatGPTAutomation

# Uso seguro com gerenciamento automático de recursos
with DriverManager(use_user_profile=True) as driver:
    chatgpt = ChatGPTAutomation(driver)
    chatgpt.open_chatgpt()
    
    if chatgpt.is_logged_in():
        resposta = chatgpt.send_message("Olá ChatGPT!")
        print(f"Resposta: {resposta}")
    
    # Driver fecha automaticamente ao sair do bloco
```

### Enviando Mensagens e Obtendo Respostas

O método `send_message()` envia uma mensagem e retorna a resposta do ChatGPT:

```python
from src.driver_manager import DriverManager
from src.chatgpt_automation import ChatGPTAutomation
import time

with DriverManager(use_user_profile=True) as driver:
    chatgpt = ChatGPTAutomation(driver)
    chatgpt.open_chatgpt()
    
    if chatgpt.is_logged_in():
        # Envia mensagem e recebe a resposta automaticamente
        resposta = chatgpt.send_message("Explique o que é Python")
        print(f"ChatGPT respondeu:\n{resposta}")
    else:
        print("Por favor, faça login primeiro")
```

## 🎯 Exemplos

### Script de Exemplos

Execute o arquivo de exemplos para ver diferentes formas de uso:

```bash
python example_usage.py
```

O script apresenta 4 exemplos diferentes:
1. **Uso Básico**: Abre o ChatGPT e verifica login
2. **Context Manager**: Uso com gerenciamento automático
3. **Sem Perfil**: Execução com perfil limpo
4. **Ações Customizadas**: Exemplos de extensão

### Modificando o Script Principal

Você pode editar o arquivo `src/main.py` para personalizar o comportamento:

```python
# Linha 55: Altere a mensagem enviada
messageNew = chatgpt.send_message("Sua mensagem personalizada aqui")
logger.info(f"Resposta do ChatGPT:\n\n{messageNew}\n\n")
```

Você também pode adicionar múltiplas mensagens ou implementar lógica condicional baseada nas respostas.

## 📁 Estrutura do Projeto

```
Browser-GPT-Automation/
├── src/
│   ├── __init__.py              # Inicialização do pacote
│   ├── config.py                # Configurações centralizadas
│   ├── driver_manager.py        # Gerenciamento do Chrome driver
│   ├── chatgpt_automation.py    # Classe principal de automação
│   └── main.py                  # Script principal
├── example_usage.py             # Exemplos de uso
├── requirements.txt             # Dependências do projeto
└── README.md                    # Este arquivo
```

## 🔧 Componentes Principais

### DriverManager

Gerencia a criação e configuração do driver do Chrome usando `undetected-chromedriver`.

- **use_user_profile**: Se `True`, usa perfil de automação separado
- **Context Manager**: Suporte para `with` statement
- **Auto-cleanup**: Fecha driver automaticamente

### ChatGPTAutomation

Classe principal para interações com o ChatGPT.

**Métodos principais:**
- `open_chatgpt()`: Abre o site do ChatGPT
- `is_logged_in()`: Verifica se está logado retornando `True` ou `False`
- `click_login()`: Clica no botão de login quando não está logado
- `send_message(message: str) -> str`: Envia uma mensagem e retorna a resposta do ChatGPT
- `wait_for_page_load(timeout: int)`: Aguarda carregamento completo da página

### Config

Configurações centralizadas do projeto.

- **CHATGPT_URL**: URL do ChatGPT
- **DEFAULT_TIMEOUT**: Timeout padrão (10 segundos)
- **AUTOMATION_PROFILE_DIR**: Diretório do perfil de automação

## ⚙️ Configuração

As configurações podem ser ajustadas no arquivo `src/config.py`:

```python
class Config:
    # Tempo de espera padrão
    DEFAULT_TIMEOUT = 10
    
    # URL do ChatGPT
    CHATGPT_URL = "https://chatgpt.com"
    
    # Diretório do perfil de automação
    AUTOMATION_PROFILE_DIR = "~/.config/chrome-automation"
```

## 🔐 Perfil de Automação

O projeto cria um perfil separado em `~/.config/chrome-automation` para não interferir com seu Chrome principal. Isso permite:

- ✅ Executar o script enquanto o Chrome está aberto
- ✅ Manter suas sessões e cookies separadas
- ✅ Evitar conflitos com extensões instaladas
- ✅ Preservar o histórico e configurações do Chrome normal

**Nota**: Quando `use_user_profile=True`, o projeto usa o perfil de automação separado, não o perfil padrão do Chrome. Isso é intencional para evitar conflitos.

## 📝 Logging

O projeto usa o módulo `logging` do Python para registrar todas as operações. O formato padrão inclui timestamp, nome do módulo, nível e mensagem:

```python
import logging

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
```

Os logs são exibidos automaticamente no console durante a execução, facilitando o debug e monitoramento das operações.

## 🐛 Troubleshooting

### ChromeDriver não encontrado
O `undetected-chromedriver` baixa automaticamente a versão correta do ChromeDriver. Se houver problemas, verifique sua conexão com a internet e as permissões do diretório.

### Elementos não encontrados
Se os seletores XPath mudarem (ChatGPT atualizou sua interface), atualize os seletores em `src/chatgpt_automation.py`. Os principais seletores usados são:
- Botão de login: `//button[@data-testid='login-button']`
- Campo de texto: `//div[@id='prompt-textarea']/p`
- Botão de enviar: `//button[@id='composer-submit-button']`
- Mensagens do assistente: `//div[@data-message-author-role='assistant'][last()]`

### Timeout errors
Aumente `DEFAULT_TIMEOUT` em `src/config.py` se estiver enfrentando timeouts frequentes. O valor padrão é 10 segundos.

### Mensagem enviada mas resposta não obtida
O método `send_message()` aguarda 10 segundos após enviar a mensagem antes de tentar ler a resposta. Se as respostas forem muito longas, você pode precisar ajustar o tempo de espera no código.

### Erro de permissões no perfil
Se encontrar erros relacionados ao perfil de automação, verifique as permissões do diretório `~/.config/chrome-automation` ou exclua-o para criar um novo perfil limpo.

## 📄 Licença

Este projeto é licenciado sob a licença MIT.

## 👤 Autor

**Thallyson Luiz**

## 🙏 Contribuições

Contribuições são bem-vindas! Sinta-se à vontade para abrir issues ou pull requests.

## ⚠️ Avisos

- Este projeto é apenas para fins educacionais
- Use com responsabilidade e respeite os termos de serviço do ChatGPT
- Não abuse da automação para criar spam ou violar políticas

## 📚 Dependências

As dependências principais são:

- `selenium==4.38.0`: Framework de automação web
- `undetected-chromedriver==3.5.5`: ChromeDriver que evita detecção de automação

Para instalar todas as dependências:

```bash
pip install -r requirements.txt
```

Veja o arquivo `requirements.txt` para a lista completa de dependências e versões.

## 🔄 Roadmap

- [ ] Suporte para múltiplas conversas simultâneas
- [ ] Salvamento de histórico de conversas
- [ ] Interface gráfica (GUI)
- [ ] Suporte para envio de imagens
- [ ] API REST para integração com outros sistemas
- [ ] Suporte para múltiplos modelos (GPT-4, etc.)
- [ ] Modo headless configurável

## 📞 Suporte

Para problemas, questões ou sugestões, abra uma issue no repositório.
