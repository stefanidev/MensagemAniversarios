import pandas as pd
import schedule
import time
from datetime import datetime
from twilio.rest import Client

# stefani
account_sid = 'AC7ee2d07c488d1f4eff8df9f89102c614'
auth_token = '60e1cc878c1e808322da4c6b33e6d752'
client = Client(account_sid, auth_token)

# raiza
account_sid = 'ACfa861da3c6c76a25310092468abbfa09'
auth_token = 'ac6e7761ae7d374747ad9b0d93f81934'
client = Client(account_sid, auth_token)

# Números de destino
recipient_numbers = ['+15598380127', '+122939825421']

# Carregue a tabela do Excel com as datas de aniversário
file_path = 'aniv.xlsx'
df = pd.read_excel(file_path)

# Função para enviar mensagens de aniversário
def enviar_mensagens_aniversario():
    today = datetime.today()
    for index, row in df.iterrows():
        nomes = row['Nome']
        data_aniversario = row['Aniversario'].date()
        cel = row['Celular']
        cel = str(df['Celular'][index]).strip()
        numero = cel.replace('.0', '')

        # Verifique se o aniversário é hoje
        if today.month == data_aniversario.month and today.day == data_aniversario.day:
    
            # Inicialize o cliente Twilio
            client = Client(account_sid, auth_token)

            # Envie a mensagem SMS para os números de destino
            for recipient_number in recipient_numbers:
                message = client.messages.create(
                    to= ['+5511941794097'], 
                    from_= ['+12293982542'],
                    body=f"Olá, hoje é aniversário de {numero}, {nomes}! Deseje felicitações!"
            
                )



            print(f"SMS enviado para {recipient_numbers}: {message.sid}")

# Agende o envio de mensagens
schedule.every().day.at("7:00:00").do(enviar_mensagens_aniversario)

# Mantenha o programa em execução para agendar o envio de mensagens
while True:
    schedule.run_pending()
    time.sleep(1)
