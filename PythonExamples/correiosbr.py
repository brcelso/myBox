import requests
import xml.etree.ElementTree as ET

# Código de rastreamento da encomenda
codigo_rastreio = 'QP291221565BR'

# Endpoint da API dos Correios
url = f'http://webservice.correios.com.br/service/rest/rastro/rastroMobile?usuario=USUARIO&senha=SENHA&tipo=L&resultado=T&objetos={codigo_rastreio}'

# Fazer solicitação GET para a API dos Correios
response = requests.get(url)

# Verificar se a solicitação foi bem sucedida
if response.status_code == 200:
    # Analisar a resposta XML
    root = ET.fromstring(response.content)
    
    # Obter as informações da encomenda
    evento = root.findall('.//evento')[0]
    data = evento.find('data').text
    hora = evento.find('hora').text
    descricao = evento.find('descricao').text
    
    # Imprimir as informações da encomenda
    print(f'Encomenda {codigo_rastreio}: {descricao} em {data} às {hora}')
else:
    # Se a solicitação falhar, imprimir a mensagem de erro
    print(f'Erro ao rastrear encomenda {codigo_rastreio}: {response.content}')