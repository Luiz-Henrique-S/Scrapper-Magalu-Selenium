# Projeto de Scraping de Notebooks da Magazine Luiza

Este projeto consiste em um script Python para realizar scraping do site da Magazine Luiza, extrair informações sobre notebooks disponíveis e enviar um relatório por e-mail.

## Funcionalidades

- **Carregamento do Site**: Uma função para carregar o site da Magazine Luiza com tratamento de tentativas e registro de erros em caso de falha.
- **Extração de Dados**: Uma função para extrair dados de notebooks de várias páginas do site e formatá-los em uma lista de dicionários.
- **Salvamento em Excel**: Uma função para salvar os dados extraídos em um arquivo Excel, separando os produtos com base na quantidade de avaliações.
- **Envio de E-mail**: Uma função para enviar um e-mail com um relatório anexado, contendo os dados extraídos.

## Como Usar

1. Instale as dependências do projeto executando `pip install -r requirements.txt`.
2. Abra o arquivo `main.py` em um editor de texto.
3. Na função `main()`, atualize a variável `email_destinatario` com o seu endereço de e-mail, se desejar receber o relatório por e-mail.
4. Execute o script `main.py` para iniciar o scraping e o envio do relatório por e-mail.
5. Verifique o arquivo `Output/Notebooks.xlsx` para os dados extraídos e o log de erros em `log_erro_site.txt`.
6. Se desejar enviar o relatório para outro endereço de e-mail, substitua o endereço na função `enviar_email()`.

## Demonstração

Assista ao vídeo abaixo para ver o robô em ação:




https://github.com/Luiz-Henrique-S/Scrapper-Magalu-Selenium/assets/166565276/8cbc60a7-658a-4439-a688-589fb5dcbe8e

