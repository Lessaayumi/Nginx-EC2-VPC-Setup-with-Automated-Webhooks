# Infrastructure Implementation on AWS with Automated Monitoring via Discord WebhooK
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
   
   3.5. [Teste de funcionamento do Nginx](#Teste-de-funcionamento-do-Nginx)
   
   3.6. [Criação do Webhook utilizando Discord](#Criação-do-Webhook-utilizando-Discord)
   
   3.7. [Criando um servidor no Discord](#Criando-um-servidor-no-Discord)
   
   3.8. [Criando um script de automação de logs utilizando Python](#Criando-um-script-de-automação-de-logs-utilizando-Python)
   
   3.9. [Automatizando Script utilizando o crontab](#Automatizando-Script-utilizando-o-crontab)
   
   3.10. [Teste de funcionalidade do WebHook](#Teste-de-funcionalidade-do-WebHook)
   
   3.11. [Criando uma Página em Html](#Criando-uma-Página-em-Html)

   3.12 [Subindo script Html ](#Subindo-script-Html)
      
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

## 3.3. Conexão via SSH:

- Agora procederemos com a conexão via SSH. Para tanto, devemos selecionar nossa instância e clicar no botão "Conectar".

  ![Image](https://github.com/user-attachments/assets/e423e427-a54c-4de3-8163-a7adf148da9d)

- Na página para a qual seremos direcionados, deveremos selecionar o serviço "Cliente SSH".

  ![Image](https://github.com/user-attachments/assets/c13a28c2-a2f2-467b-8901-439f52870095)

- Em seguida, devemos abrir o prompt de comando (CMD) em nossa máquina local.

 ![Image](https://github.com/user-attachments/assets/d0e32f50-3cb0-4c0b-9202-09297fb1899f)

- No prompt de comando (CMD), devemos navegar até o local onde se encontra a nossa chave de acesso via SSH.

 ![Image](https://github.com/user-attachments/assets/f8b794e9-ad6f-4de9-beb9-2a1e6c031735)

- Após acessar o diretório onde o arquivo de chave está disponível, devemos executar o comando fornecido pela própria AWS para obter o acesso via SSH.

   ![Image](https://github.com/user-attachments/assets/4c9f3ca1-34d1-4f9d-a251-85ec760e57ea)

   ![Image](https://github.com/user-attachments/assets/ba95759d-3b60-4bc1-bac3-91fc2c727cd8)

- Após executar esse comando, nossa máquina estabelecerá uma conexão via SSH com a instância Ubuntu hospedada na AWS.

    ![Image](https://github.com/user-attachments/assets/cad28718-8ee7-488e-acbf-0b3156f4245f)

- 


## 3.4. Instalação do Nginx

- Para facilitar nossas configurações, o primeiro comando que vamos executar para prosseguir será o: `sudo -i `

   ![Image](https://github.com/user-attachments/assets/fdad9658-08d4-44d2-92a6-39ae743a37b6)

- Logo, perceberemos que entramos como usuário root. Sendo usuário root, vamos simplificar alguns processos.

  ![Image](https://github.com/user-attachments/assets/cf3997c5-71b2-4b86-ba4c-fb9a6ee80a41)

- Antes de iniciar a instalação do Nginx, vamos executar o comando `apt install update`. Esse comando é utilizado para atualizar a lista de pacotes disponíveis nos repositórios configurados no sistema. Ele não instala ou atualiza pacotes diretamente, mas garante que as informações sobre as versões mais recentes dos pacotes estejam atualizadas, o que é essencial para garantir que a instalação do Nginx ou de qualquer outro pacote seja feita a partir da versão mais recente disponível.

  ![Image](https://github.com/user-attachments/assets/8a72a036-eef3-490e-a50a-30c2587be9c8)

- Logo após, com o comando apt install nginx, iniciaremos a instalação do Nginx. Esse comando irá baixar e instalar o pacote Nginx em sua versão mais recente, conforme a lista de pacotes atualizada previamente.

  ![Image](https://github.com/user-attachments/assets/1f21f694-4e1a-485a-8b89-e9266f1015dc)

- Com o comando nginx -v, podemos verificar qual versão do Nginx está instalada no sistema. Isso é essencial para futuras configurações, pois, dependendo da versão, alguns recursos ou comandos podem variar.

  ![Image](https://github.com/user-attachments/assets/4d059079-c4cc-41f7-a172-f95548771dcf)
  
  ![Image](https://github.com/user-attachments/assets/d3b14b96-44df-4818-bc53-7714a3bc1df9)

- Agora, na página de detalhes da instância na AWS, você encontrará o IP público da sua instância. Vamos copiar esse IP e rodá-lo no nosso navegador. Se o Nginx estiver corretamente instalado e funcionando, você verá a página padrão do Nginx, indicando que o servidor web está rodando corretamente. Caso contrário, pode ser necessário verificar a configuração ou o status do serviço.

   ![Image](https://github.com/user-attachments/assets/54bed0dc-59a3-4488-8b84-cad40d50bda0)

   ![Image](https://github.com/user-attachments/assets/b8d4b113-7df5-47e7-8a52-dbb1f28b1a17)

  ![Image](https://github.com/user-attachments/assets/1518ba7d-cef9-48f2-982d-52fac7c143c4)

- Percebemos que o nosso Nginx está rodando corretamente, pois ao acessarmos o IP fornecido no navegador, ele corresponde à página padrão do Nginx. Agora, para realizar um teste, vamos executar o comando systemctl stop nginx. Esse comando vai parar o funcionamento do serviço Nginx.

  ![Image](https://github.com/user-attachments/assets/4cc9930d-d941-42a1-aaf6-9d249db8165a)

- Vamos atualizar a página do navegador para verificar se o serviço realmente foi parado. Quando o Nginx estiver parado, o navegador não exibirá mais a página padrão do Nginx e, em vez disso, poderá mostrar um erro, como "Erro 502" ou "Não foi possível conectar ao servidor". Isso confirma que o serviço foi interrompido com sucesso.

  ![Image](https://github.com/user-attachments/assets/34af50c5-230d-49b8-827f-41ebb4722a71)




  

  
  

  

  






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

