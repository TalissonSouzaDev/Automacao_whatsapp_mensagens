import time
import pandas as pd
import urllib #transforma texto para url
import os
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

navegador = webdriver.Chrome() # poderia ser com qualquer navegador para abrir precisa instalação da extensão do navegador que deseja
navegador.get("https://web.whatsapp.com") #abrindo o whatsapp no navagador

#espera tela carregar

while len(navegador.find_elements(By.XPATH,'//*[@id="app"]/div/div[2]/div[3]/header')) #criar uma lista quando o whatsapp ta aberto caso não esteja vai fazer verificar a cada um minuto.
  time.sleep(1)
time.sleep(2) #certifica se whatsapp esta aberta

#carregar os arquivos no excel com panda
tabela =  pd.read_excel("nome do excel.xlsx")
display(tabela[["nome","mensagem",'telefone']]) # conferindo se ta retornado as informações

for linha in tabela.index:
  nome =  tabela.loc[linha,"nome"]
  mensagem =  tabela.loc[linha,"mensagem"]
  telefone =  tabela.loc[linha,"telefone"]
  arquivo =  tabela.loc[linha,"arquivo"]

  textoformatado = mensagem.replace("fulano",nome) # retira todo nome que tive fulano e atribuir o nome
  texto = urllib.parse.quote(textoformatado) #formata para padrão web

  #enviar as mensagens
  link =  f"https://web.whatsapp.com/send?phone={telefone}&text={texto}"
  navegador.get(link)
  
  while len(navegador.find_elements(By.ID,'side')): #criar uma lista quando o whatsapp ta aberto caso não esteja vai fazer verificar a cada um minuto.
    time.sleep(1)
  time.sleep(2) #certifica se whatsapp esta aberta

  #verificar se o numero é invalido
  if len(navegador.find_elements(By.XPATH,'//*[@id="app"]/div/span[2]/div/span/div/div/div/div/div/div[1]')) < 1:
    #abrindo a janela de manda fotos,videos,documentos no whatsapp
    navegador.find_elements(By.XPATH,'//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[2]/button/span').click()

    if arquivo != "N":
      #carregando o arquivo 
      caminho_arquivo  =  os.apth.abspatch(f"caminho/{arquivo}")
      #abrindo a janela pra manda arquivos no whatsapp
      navegador.find_elements(By.XPATH,'//*[@id="main"]/footer/div[1]/div/span[2]/div/div[1]/div[2]/div/div/div/span').click()
      #colacando arquivo no input file
      navegador.find_elements(By.XPATH,'//*[@id="main"]/footer/div[1]/div/span[2]/div/div[1]/div[2]/div/span/div/ul/div/div[1]/li/div/input').send_keys(caminho_arquivo)
      time.sleep(2)
      #enviando
      navegador.find_elements(By.XPATH,'//*[@id="app"]/div/div[2]/div[2]/div[2]/span/div/span/div/div/div[2]/div/div[2]/div[2]/div/div/span').click()

  time.sleep(5)
