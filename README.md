# Infrastructure-Implementation-on-AWS-with-Automated-Monitoring-via-Discord-WebhooK
Este repositório contém a implementação de uma infraestrutura em nuvem baseada na AWS, desenvolvida no âmbito do Programa de Bolsas (PB) da Compass UOL, na trilha de estudos em AWS e DevSecOps.

## Índice

1. [Resumo](#Resumo)  

2. [Objetivos](#objetivos)  
   - [Capacitação em Computação em Nuvem](#Capacitação-em-Computação-em-Nuvem)  
   - [Configuração de Servidor Web](#Confifguração-de-Servidor-Web)  
   - [Automação e Segurança](#Automação-e-Segurança)  
   - [Monitoramento Contínuo](#Monitoramento-Contínuo)  
   - [Integração com DevSecOps](#Integração-com-DevSecOps)  

3. [Passo a Passo](#passo-a-passo)  
   3.1. [Criando uma VPC](#Criando-uma-VPC)  

   3.2. [Instalar o Ubuntu](#instalar-o-ubuntu)  
   3.3. [Instalar o servidor NGINX no Ubuntu](#instalar-o-servidor-nginx-no-ubuntu)  
   3.4. [Criar script para verificação de status do NGINX](#criar-script-para-verificação-de-status-do-nginx)  
   3.5. [Executar o script](#executar-o-script)  
   3.6. [Automatizar a execução do script](#automatizar-a-execução-do-script)    
      3.6.1. [Adicionar linha ao crontab](#adicionar-linha-ao-crontab)  
      3.6.2. [Explicação da sintaxe](#explicação-da-sintaxe)  

4. [Resultado](#resultado)  
   4.1. [Logs quando o sistema está online](#logs-quando-o-sistema-está-online)  
   4.2. [Logs quando o sistema está offline](#logs-quando-o-sistema-está-offline)  


## 1. Resumo:
A atividade foi desenvolvida com base no Programa de Bolsas (PB) da Compass UOL, dentro da trilha de estudos em AWS e DevSecOps. O objetivo principal é capacitar os participantes na criação e configuração de uma infraestrutura na nuvem, seguindo boas práticas de segurança e automação.  

No escopo da atividade, o participante deve provisionar uma Virtual Private Cloud (VPC) e uma instância EC2 utilizando o sistema operacional Ubuntu. Em seguida, deve estabelecer conexão remota via SSH, instalar e configurar o servidor web Nginx e desenvolver uma página web em HTML.  

Além disso, foi implementado um mecanismo de monitoramento automatizado utilizando a funcionalidade de Webhook do Discord. Para isso, foi desenvolvido um script em Python que verifica a disponibilidade do site a cada minuto e envia um alerta para um canal no Discord caso o serviço apresente indisponibilidade.

## 2. Objetivos:
- _Capacitação em Computação em Nuvem_: Proporcionar experiência prática na criação e configuração de uma infraestrutura na AWS, utilizando serviços essenciais como VPC e EC2.

- _Configuração de Servidor Web_: Instalar e configurar o servidor Nginx em uma instância Ubuntu, permitindo a hospedagem de uma página web simples em HTML.

- _Automação e Segurança_: Implementar boas práticas de acesso remoto via SSH, garantindo a correta configuração e segurança da instância.
    
- _Monitoramento Contínuo_: Desenvolver um script em Python para verificar a disponibilidade do site e integrar com o Discord Webhook para alertas automáticos em caso de falhas

- _Integração com DevSecOps_: Aplicar conceitos de automação e monitoramento para assegurar a disponibilidade e confiabilidade da aplicação, alinhando-se a práticas de DevSecOps.

## 3. Passo a Passo

## 3.1. Criando uma VPC:
- Abra o power shell como administrador e execute o seguinte comando:
powershell
wsl --install

- Reinicie o sistema após a instalação, se solicitado.

## 3.2. Instalar o Ubuntu:
- Após a instalação do WSL, abra o Microsoft Store e instale o Unbutu 20.04 ou superior.

## 3.3. Instalar o servidor Nginx no Ubuntu:
- No terminal Ubuntu, digite:
powershell
sudo apt install nginx

- Após a instalação, para verificar se o Nginx está funcionando, digite:
powershell
sudo systemctl status nginx


![Captura de tela 2024-12-18 143816](https://github.com/user-attachments/assets/1de157ca-347f-482b-8f30-2da8349a845d)


- Abra seu navegador e digite http://localhost. Se o Nginx estiver funcionando, você verá a seguinte página:
  
  
![Captura de tela 2024-12-18 144651](https://github.com/user-attachments/assets/ac160411-fce7-4d5c-acde-a6e84f760cb4)


- Configurar as permissões de escrita na pasta /var/log/nginx para criar logs personalizados:

bash
sudo chmod 722 /var/log/nginx


![Captura de tela 2024-12-18 160007](https://github.com/user-attachments/assets/a7554b2c-2684-4606-ab9e-048e7e5e3d6c)

- Criar os arquivos de log com os seguintes comandos:
  
bash
sudo touch /var/log/nginx/servico_online.log
sudo touch /var/log/nginx/servico_offline.log
`

![Captura de tela 2024-12-1…
[15:14, 11/02/2025] Alessandra Lopes: #!/bin/bash

#Var em que guarda o caminho para o diretorioem que o log sera salvo
LOG_DIR="/var/log/nginx"

#Var para os arquivos de log online e offline
LOG_ONLINE="$LOG_DIR/servico_online.log"
LOG_OFFLINE="$LOG_DIR/servico_offline.log"

#Para data e hora local
DATA_HORA=$(date '+%Y-%m-%d %H:%M:%S')

#Nome do servico
SERVICO="nginx"

#Var em que o status do atual do nginx é armazenado
STATUS=$(systemctl is-active $SERVICO)

#Condcional para verificar o status do serviço
if [ "$STATUS" == "active" ]; then
        ESTADO="ONLINE"
        MENSAGEM="O servico $SERVICO está ONLINE."
        LOG="$DATA_HORA | Serviço: $SERVICO | STATUS: $ESTADO | Mensagem: $MENSAGEM"
        #Escreve log no arquivo servico_online.log
        echo "$LOG" >> "$LOG_ONLINE"
        echo -e "\033[0;32m Online \033[0m"
else
        ESTADO="OFLLINE"
        MENSAGEM="O serviço $SERVICO está OFFLINE"
        LOG="$DATA_HORA | Serviço: $SERVICO | STATUS: $ESTADO | Mensagem: $MENSAGEM"
        #Escreve log no arquivo servico_offline.log
        echo "$LOG" >> "$LOG_OFFLINE"
        echo -e "\033[0;31m Offline \033[0m"
fi
