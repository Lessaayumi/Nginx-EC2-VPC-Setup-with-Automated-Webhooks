# Infrastructure-Implementation-on-AWS-with-Automated-Monitoring-via-Discord-WebhooK
Este repositório contém a implementação de uma infraestrutura em nuvem baseada na AWS, desenvolvida no âmbito do Programa de Bolsas (PB) da Compass UOL, na trilha de estudos em AWS e DevSecOps.

## Índice

1. [Resumo](#Resumo)  

2. [Objetivos](#objetivos)  
   - [Capacitação em Computação em Nuvem](#Capacitação-em-Computação-em-Nuvem)  
   - [Configuração de Servidor Web](#Confifguração-de-Servidor-Web)  
   - [Automação e Segurança](#Automação-e-Segurança)  
   - [Monitoramento Contínuo](#Monitoramento-Contínuo)  

3. [Passo a Passo](#passo-a-passo)  
   3.1. [Criando uma VPC](#Criando-uma-VPC)
   
   3.2. [Criação de uma instância EC2, utilizando o sistema operacional Ubuntu](#Criação-de-uma-instânia-EC2,-utilizando-o-sistema-operacional-Ubuntu)
   
   3.3. [Conexão via SSH](#Conexão-via-SSH)
   
   3.4. [Instalação do Nginx](#Instalação=do-Nginx)
   
      3.4.1. [Teste de funcionamento do Nginx](#Teste-de-funcionamento-do-Nginx)
   
   3.5. [Criação do Webhook utilizando Discord](#Criação-do-Webhook-utilizando-Discord)
   
      3.5.1 [Criando um servidor no Discord](#Criando-um-servidor-no-Discord)
   
      3.5.2 [Criando um script de automação de logs: Utilizando Python](#Criando-um-script-de-automação-de-logs:-Utilizando-Python)
   
      3.5.3 [Automatizando Script utilizando o crontab](#Automatizando-Script-utilizando-o-crontab)
   
      3.5.4 [Teste de funcionalidade do WebHook](#Teste-de-funcionalidade-do-WebHook)
   
   3.6. [Criando uma Página em Html](#Criando-uma-Página-em-Html)    
      
5. [Testes finais](#Testes-finais)  
   4.1. [Logs quando o sistema está online](#logs-quando-o-sistema-está-online)  
   4.2. [Logs quando o sistema está offline](#logs-quando-o-sistema-está-offline)

7. [Considerações](#Considerações)

8.  [Referências](#Referências)

## 1. Resumo:
A atividade foi desenvolvida com base no Programa de Bolsas (PB) da Compass UOL, dentro da trilha de estudos em AWS e DevSecOps. O objetivo principal é capacitar os participantes na criação e configuração de uma infraestrutura na nuvem, seguindo boas práticas de segurança e automação.  

No escopo da atividade, o participante deve provisionar uma Virtual Private Cloud (VPC) e uma instância EC2 utilizando o sistema operacional Ubuntu. Em seguida, deve estabelecer conexão remota via SSH, instalar e configurar o servidor web Nginx e desenvolver uma página web em HTML.  

Além disso, foi implementado um mecanismo de monitoramento automatizado utilizando a funcionalidade de Webhook do Discord. Para isso, foi desenvolvido um script em Python que verifica a disponibilidade do site a cada minuto e envia um alerta para um canal no Discord caso o serviço apresente indisponibilidade.

## 2. Objetivos:
- _Capacitação em Computação em Nuvem_: Proporcionar experiência prática na criação e configuração de uma infraestrutura na AWS, utilizando serviços essenciais como VPC e EC2.

- _Configuração de Servidor Web_: Instalar e configurar o servidor Nginx, permitindo a hospedagem de uma página web simples em HTML.

- _Automação e Segurança_: Implementar boas práticas de acesso remoto via SSH, garantindo a correta configuração e segurança da instância.
    
- _Monitoramento Contínuo_: Desenvolver um script em Python para verificar a disponibilidade do site e integrar com o Discord Webhook para alertas automáticos em caso de falhas

## 3. Passo a Passo

## 3.1. Criando uma VPC:
- Para criar uma VPC na AWS, é necessário acessar a página inicial do console da AWS e localizar a opção **VPC** no menu de navegação.
  
  ![Image](https://github.com/user-attachments/assets/dd4300a1-c127-434c-bc75-e110914a3e64)
  
- Para criar uma VPC na AWS, é necessário acessar a página inicial do console da AWS e localizar a opção **VPC** no menu de navegação.
  
  ![Image](https://github.com/user-attachments/assets/3158d1a8-46c0-4cf6-84ce-3af678ae4b12)
  
- Após essa etapa, o sistema redirecionará para a página de criação da VPC. Como nosso objetivo é configurar uma VPC com duas sub-redes públicas e duas privadas, selecionaremos a opção **Criar VPC e mais** para prosseguir com a configuração.
  
  ![Image](https://github.com/user-attachments/assets/7d91290a-501f-4987-b5b1-2f2b95f3f47b)

- O próximo passo consiste na definição de um nome para a sua VPC.
  
  ![Image](https://github.com/user-attachments/assets/e8ae51a7-bd25-4c15-b9ef-d8ac28dbdb56)

- Agora, é necessário definir o endereço IP e o tipo de bloco a ser utilizado. Neste caso, adotaremos a configuração padrão, considerando a finalidade do projeto.

  ![Image](https://github.com/user-attachments/assets/84f9fbb1-155c-415a-8661-57c5c952d75b)

- O próximo passo consiste na criação das sub-redes. Como o projeto exige duas sub-redes públicas e duas privadas, seguiremos as configurações detalhadas a seguir.

   ![Image](https://github.com/user-attachments/assets/3d55fd64-d430-4098-9879-cb5193d5e712)
  
   ![Image](https://github.com/user-attachments/assets/21631163-6b92-47c8-946f-96654d7057ed)

- Após a realização das configurações, a arquitetura da VPC será estruturada da seguinte forma.

   ![Image](https://github.com/user-attachments/assets/642fa485-d415-47cd-a1bd-3a16bdcd32f6)

- Após a verificação, para concluir a criação da VPC, basta selecionar o botão **"Criar VPC"**.

  ![Image](https://github.com/user-attachments/assets/69acf7eb-d002-4b0c-9f76-6da722ca0348)

- Após essa etapa, nossa VPC estará criada, concluindo assim o processo de sua configuração.

   ![Image](https://github.com/user-attachments/assets/e40aec9a-bb55-40c3-8514-dba876888563)

## 3.2. Criação de uma instância EC2, utilizando o sistema operacional Ubuntu:

-  Na página inicial da AWS, é necessário localizar a opção **EC2**. Caso não esteja visível no menu principal, podemos utilizar a barra de pesquisa **"Search"** para digitar **EC2**, facilitando sua localização.

  ![Image](https://github.com/user-attachments/assets/78973ca7-a8c2-460a-a23d-2045640a8ae3)

- Ao selecionar a opção **EC2**, seremos direcionados ao painel correspondente. Nesse painel, deve-se localizar a opção **Executar instância**, para iniciar o processo de criação da instância.

   ![Image](https://github.com/user-attachments/assets/c250ecfc-2255-403e-aab5-13d98a5e93a4)

- Agora, estamos no painel de criação da instância EC2. Nesse momento, será necessário adicionar um nome e as tags fornecidas pela sua empresa para a criação da instância.

  ![Image](https://github.com/user-attachments/assets/92203e9b-5af5-4155-a10a-98b3a7354b13)

- Em seguida, selecionaremos o servidor **Ubuntu**, que foi o escolhido para a criação da instância.

  ![Image](https://github.com/user-attachments/assets/cae85007-8e06-46b1-aad8-8a24c0bbe6bc)

- Confira nas imagens as configurações necessárias para o correto funcionamento do sistema, a fim de evitar problemas futuros com os serviços.

 ![Image](https://github.com/user-attachments/assets/cae85007-8e06-46b1-aad8-8a24c0bbe6bc)
  
 ![Image](https://github.com/user-attachments/assets/e1917323-2991-4146-a771-ae4efabed38a)

- Agora, será necessário selecionar o par de chaves para realizar a conexão via SSH.

![Image](https://github.com/user-attachments/assets/a098884b-ee8c-4b94-87c2-e19548064900)
 
- O próximo passo é selecionar e criar um grupo de segurança, conforme proposto no projeto. Esse grupo de segurança tem a função de controlar o tráfego de rede permitido para a instância, definindo quais portas podem ser acessadas e por quais fontes, garantindo assim a segurança da comunicação.

 ![Image](https://github.com/user-attachments/assets/c7ccbffc-6319-4710-8dee-bda6b437f329)  

- Como proposto, manteremos os serviços **SSH** e **HTTP** ativos. Para isso, selecionaremos as opções que permitem o tráfego **SSH** e **HTTP**. O tráfego **SSH** é necessário para realizar a conexão segura e remota com a instância, enquanto o tráfego **HTTP** é essencial para permitir o acesso à aplicação ou site hospedado no servidor. Essas permissões garantem a funcionalidade dos serviços de administração e comunicação da instância.

  ![Image](https://github.com/user-attachments/assets/04ebb4ca-4dff-4862-b463-3540c733210e)

  ![Image](https://github.com/user-attachments/assets/2b79e9c9-ce43-4cd0-98df-e1972079147e)

- Após essa etapa, será necessário definir o armazenamento a ser alocado para a instância.

   ![Image](https://github.com/user-attachments/assets/4c4bc17b-c494-4097-a1b1-b306b2f84c39)

- Após essa etapa, basta selecionar o botão **Executar instância** para que ela seja criada.

   ![Image](https://github.com/user-attachments/assets/3d14955f-1437-44c4-830b-dc39efbcc92e)

- A imagem abaixo demonstra que a instância foi criada com sucesso. Ao selecionar o botão **Selecionar instância**, seremos redirecionados para a página de visualização da instância.

   ![Image](https://github.com/user-attachments/assets/59ab61c4-a230-4fef-811b-d98d2cfb95c9)
   ![Image](https://github.com/user-attachments/assets/709af886-7c5a-42a7-9797-0e85e8ab5698)

- Neste processo da 3.1. e 3.2., criamos uma VPC na AWS, configurando sub-redes públicas e privadas conforme as necessidades do projeto. Em seguida, acessamos o painel EC2, onde configuramos e lançamos uma instância, definindo seu nome, sistema operacional (Ubuntu), grupo de segurança e armazenamento. Também habilitamos os serviços SSH e HTTP para garantir a conectividade e o acesso adequado. Por fim, executamos a instância e verificamos sua criação com sucesso. Esse procedimento garante uma infraestrutura básica e segura para hospedar aplicações e serviços na AWS.
 
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


![Captura de tela 2024-12-18 160007](![Image](https://github.com/user-attachments/assets/dd4300a1-c127-434c-bc75-e110914a3e64))

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
