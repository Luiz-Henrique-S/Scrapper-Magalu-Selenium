import requests
from datetime import datetime
import os
import pandas as pd

# função de carregamento da pagina recebendo os parametros de url e tentativas maximas
def carregar_site(url: str, max_tentativas=3):
    tentativa = 0
    while tentativa < max_tentativas:
        try:
            resposta = requests.get(url)
            resposta.raise_for_status()
            print("Site carregado com sucesso!")
            return True
        except requests.exceptions.RequestException as erro:
            tentativa += 1
            print(f"Erro ao carregar o site. Tentativa {tentativa}/{max_tentativas}: {erro}")
            if tentativa == max_tentativas:
                registrar_erro(url)
                return False
# função recebendo a url do site para gerar a log de erro 
def registrar_erro(url: str):
    with open("log_erro_site.txt", "a") as arquivo_log:
        agora = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        arquivo_log.write(f"{agora} - Site fora do ar: {url}\n")
    print("Erro ao carregar o site após o número máximo de tentativas. Log de erro gerado.")
# função para extrair dados da pagina recebendo os parametros do driver do selenium, a url base do site e o numero de paginas totais
def extrair_dados(driver, url_base, num_paginas):
    dados_produtos = []
    #loop para iterar sobre o numero de paginas
    for pagina in range(1, num_paginas + 1):
        url_pagina = f"{url_base}/busca/notebooks/?page={pagina}"
        driver.get(url_pagina)
        produtos = driver.find_elements_by_xpath("//*[@data-testid='product-card-container']")
        #loop para iterar sobre cada produto na pagina
        for produto in produtos:
            nome_produto_elemento = produto.find_element_by_xpath(".//*[@data-testid='product-title']")
            nome_produto = nome_produto_elemento.text
            url_produto = produto.get_attribute('href')
            try:
                qtd_aval_elemento = produto.find_element_by_xpath(".//span[@format='score-count']")
                qtd_aval = qtd_aval_elemento.text.split("(")[1].split(")")[0]
            except:
                qtd_aval = "N/A"
            dados_produtos.append({
                "PRODUTO": nome_produto,
                "QTD_AVAL": qtd_aval,
                "URL": url_produto
            })
    return dados_produtos
# função para salvar o excel recebendo os parametros de dt melhores/piores e o caminho do arquivo de saida
def salvar_excel(df_melhores, df_piores, output_file_path):
    output_folder = "Output"
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
    with pd.ExcelWriter(output_file_path, engine="xlsxwriter") as writer:
        df_melhores.to_excel(writer, sheet_name="Melhores", index=False)
        df_piores.to_excel(writer, sheet_name="Piores", index=False)

    print(f"Dados extraídos e salvos em '{output_file_path}'")
    
