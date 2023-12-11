import pandas as pd
from twilio.rest import Client
from datetime import datetime
import time
import schedule

# Configuração do Twilio
account_sid = 'AC7ee2d07c488d1f4eff8df9f89102c614'
auth_token = '60e1cc878c1e808322da4c6b33e6d752'
client = Client(account_sid, auth_token)
twilio_number = ['+15598380127', '+122939825421']

# Carregar a tabela de Excel com os aniversários
df = pd.read_excel('aniv.xlsx')  # Substitua 'tabela_aniversarios.xlsx' pelo nome do seu arquivo Excel

# Obter a data de hoje
hoje = datetime.today()

# Iterar pelas linhas da tabela
for index, row in df.iterrows():
    nome = row['Nome']
    celular = row['Celular']
    data_aniversario = row['Aniversario'].date()

    # Verificar se hoje é o aniversário
    if hoje.day == data_aniversario.day and hoje.month == data_aniversario.month:
        mensagem = f"Olá, hoje é aniversário de @{celular}, {nome}. Deseje felicitações!!!"
        destinatario = ['5511968395044', '+5511941794097']

        # Enviar a mensagem usando o Twilio
        client.messages.create(
            body= f"Olá, hoje é aniversário de @{celular}, {nome}. Deseje felicitações!!!",
            from_= '+15598380127',
            to= '+5511968395044'
        )

        print("Mensagem de aniversário enviadas.")




while True:
    schedule.run_pending()
    time.sleep(1)
