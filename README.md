# Backup Dash Grafana

Script python3 que gera backup de todas suas Dash através da API do grafana. (Abraço para meu amigo <a href="https://t.me/saulotarsobc">Saulo Costa</a>!)

Para criar uma API entre em seu grafana e no menu <b>Configurações</b> (Engrenagem) selecione <b>API Keys</b> clique em <b>Add API Keys</b>, em <b>Keys name</b> digite Backup em <b>Role</b> selecione Admin, e em <b>Time ti live</b> deixe vazio.

Ira aparece uma janela com sua API (80 caracteres aleatórios) anote e no arquivo <b>backup-grafana-dash.py</b> altere as variáveis <b>server</b> para o endereço do seu servidor grafana e <b>api_token</b> informe sua API. Exemplo:
```
server = 'https://grafana.remontti.com.br'
api_token = '6n1teKM4QklfADUHSRgtdE63pMwpFgciuAgqdlejHK1dodEGYEsKsdLkuL1vR4Skw6na3envxmUsjojq'
```

### Arquivo gerabackup.sh
Este arquivo é o que adiciono ao cron para executar as rotinas de backup, bem como mover posterior todos os backups para um diretório.
