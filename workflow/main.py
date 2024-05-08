from envio_email import enviar_email
from scraping import carregar_site, extrair_dados, salvar_excel
import requests
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from time import sleep
import pandas as pd
import os


def main():
    url = "https://www.magazineluiza.com.br/"
    num_paginas = 17
    max_tentativas = 3

    if not carregar_site(url, max_tentativas):
        return

    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.get(url)
    driver.maximize_window()

    campo_pesquisa = driver.find_element_by_id("input-search")
    campo_pesquisa.send_keys("notebooks")
    campo_pesquisa.send_keys(Keys.ENTER)
    sleep(3)
    
    #chamando a função extrair_dados e criando um data frame a partir da lista de dados_produtos
    dados_produtos = extrair_dados(driver, url, num_paginas)
    df = pd.DataFrame(dados_produtos)

    # convertendo a coluna para numerica e tratando erros
    df["QTD_AVAL"] = pd.to_numeric(df["QTD_AVAL"], errors="coerce")
    df_piores = df[df["QTD_AVAL"] < 100]
    df_melhores = df[df["QTD_AVAL"] >= 100]

    output_file_path = os.path.join("Output", "Notebooks.xlsx")
    salvar_excel(df_melhores, df_piores, output_file_path)

    driver.quit()

    email_destinatario = "luiz2562@gmail.com"
    assunto = "Relatório Notebooks"
    corpo = """Olá, aqui está o seu relatório dos notebooks extraídos da Magazine Luiza.

    Atenciosamente,
    Robô"""

    enviar_email(email_destinatario, assunto, corpo, output_file_path)

    print("E-mail enviado com sucesso!")

if __name__ == "__main__":
    main()
