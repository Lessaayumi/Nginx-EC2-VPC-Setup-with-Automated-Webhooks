# Automated AWS Infrastructure: EC2, VPC, HTML on NGINX, and Discord Downtime Alerts with Webhooks
Este repositório contém a implementação de uma infraestrutura em nuvem baseada na AWS, desenvolvida no âmbito do Programa de Bolsas (PB) da Compass UOL, na trilha de estudos em AWS e DevSecOps.

## Índice

1. [Resumo e tecnologias](#Resumo)  

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
   
   3.5. [Criação do Webhook utilizando Discord](#Criação-do-Webhook-utilizando-Discord)
   
   3.6. [Criando um script de automação de logs utilizando Python](#Criando-um-script-de-automação-de-logs-utilizando-Python)
   
   3.7. [Automatizando Script utilizando o crontab](#Automatizando-Script-utilizando-o-crontab)
   
   3.8. [Teste de funcionalidade do WebHook](#Teste-de-funcionalidade-do-WebHook)
   
   3.9. [Criando uma Página em Html](#Criando-uma-Página-em-Html)

   3.10. [Subindo script Html ](#Subindo-script-Html)
      
5. [Testes finais](#Testes-finais)  
   4.1. [Logs quando o sistema está online](#logs-quando-o-sistema-está-online)  
   4.2. [Logs quando o sistema está offline](#logs-quando-o-sistema-está-offline)

7. [Considerações](#Considerações)

8.  [Referências](#Referências)

# 1. Resumo e tecnologias:
A atividade foi desenvolvida com base no Programa de Bolsas (PB) da Compass UOL, dentro da trilha de estudos em AWS e DevSecOps. O objetivo principal é capacitar os bolsistas na criação e configuração de uma infraestrutura na nuvem, seguindo boas práticas de segurança e automação.  

No escopo da atividade, o participante deve provisionar uma Virtual Private Cloud (VPC) e uma instância EC2 utilizando o sistema operacional Ubuntu. Em seguida, deve estabelecer conexão remota via SSH, instalar e configurar o servidor web Nginx e desenvolver uma página web em HTML.  

Além disso, foi implementado um mecanismo de monitoramento automatizado utilizando a funcionalidade de Webhook do Discord. Para isso, foi desenvolvido um script em Python que verifica a disponibilidade do site a cada minuto e envia um alerta para um canal no Discord caso o serviço apresente indisponibilidade.

## 2. Objetivos:
- _Capacitação em Computação em Nuvem_: Proporcionar experiência prática na criação e configuração de uma infraestrutura na AWS, utilizando serviços essenciais como VPC e EC2.

- _Configuração de Servidor Web_: Instalar e configurar o servidor Nginx, permitindo a hospedagem de uma página web simples em HTML.

- _Automação e Segurança_: Implementar boas práticas de acesso remoto via SSH, garantindo a correta configuração e segurança da instância.
    
- _Monitoramento Contínuo_: Desenvolver um script em Python ou bash para verificar a disponibilidade do site e integrar com o Discord Webhook para alertas automáticos em caso de falhas

## 3. Passo a Passo

## 3.1. Criando uma VPC:
- Para criar uma VPC na AWS, é necessário acessar a página inicial do console da AWS e localizar a opção **VPC** no menu de navegação.
  
  ![Image](https://github.com/user-attachments/assets/dd4300a1-c127-434c-bc75-e110914a3e64)
  
  
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

- Após a verificação, para concluir a criação da VPC, basta selecionar o botão **"Criar VPC"**. Logo a essa etapa, nossa VPC estará criada, concluindo assim o processo de sua configuração e criação.

   ![Image](https://github.com/user-attachments/assets/e40aec9a-bb55-40c3-8514-dba876888563)

## 3.2. Criação de uma instância EC2, utilizando o sistema operacional Ubuntu:

-  Na página inicial da AWS, é necessário localizar a opção **EC2**. Caso não esteja visível no menu principal, podemos utilizar a barra de pesquisa **"Search"** para digitar **EC2**, facilitando sua localização.

- Ao selecionar a opção **EC2**, seremos direcionados ao painel correspondente. Nesse painel, deve-se localizar a opção **Executar instância**, para iniciar o processo de criação da instância.

   ![Image](https://github.com/user-attachments/assets/c250ecfc-2255-403e-aab5-13d98a5e93a4)

- Agora, estamos no painel de criação da instância EC2. Nesse momento, será necessário adicionar um nome e as tags fornecidas pela sua empresa para a criação da instância.

  ![Image](https://github.com/user-attachments/assets/92203e9b-5af5-4155-a10a-98b3a7354b13)

- Em seguida, selecionaremos o servidor **Ubuntu**, que foi o escolhido e proposto no projeto.

  ![Image](https://github.com/user-attachments/assets/cae85007-8e06-46b1-aad8-8a24c0bbe6bc)

- Nas imagens contém as configurações necessárias para o correto funcionamento do sistema, a fim de evitar problemas futuros com os serviços.

 ![Image](https://github.com/user-attachments/assets/cae85007-8e06-46b1-aad8-8a24c0bbe6bc)
  
 ![Image](https://github.com/user-attachments/assets/e1917323-2991-4146-a771-ae4efabed38a)

- Agora, será necessário selecionar o par de chaves para realizar a conexão via SSH, caso não tenha criado, ao lado encontramos a opção criar novo par de chaves.

![Image](https://github.com/user-attachments/assets/a098884b-ee8c-4b94-87c2-e19548064900)
 
- O próximo passo é selecionar e criar um grupo de segurança, conforme proposto no projeto. Esse grupo de segurança tem a função de controlar o tráfego de rede permitido para a instância, definindo quais portas podem ser acessadas e por quais fontes, garantindo assim a segurança da comunicação.

    ![Image](https://github.com/user-attachments/assets/cadec82d-b8e6-464a-b6c9-0f5f96a010a6)

- Como proposto, manteremos os serviços **SSH** e **HTTP** ativos. Para isso, selecionaremos as opções que permitem o tráfego **SSH** e **HTTP**. O tráfego **SSH** é necessário para realizar a conexão segura e remota com a instância, enquanto o tráfego **HTTP** é essencial para permitir o acesso à aplicação ou site hospedado no servidor. Essas permissões garantem a funcionalidade dos serviços de administração e comunicação da instância.

   ![Image](https://github.com/user-attachments/assets/96001a75-9fc6-451b-bea6-27819a5fb798)

- Após essa etapa, será necessário definir o armazenamento a ser alocado para a instância, no caso deixaremos o padrão da AWS.

- Para finalizar a criação da instância basta selecionar o botão **Executar instância**.

   ![Image](https://github.com/user-attachments/assets/3d14955f-1437-44c4-830b-dc39efbcc92e)

- A imagem abaixo demonstra que a instância foi criada com sucesso. Ao selecionar o botão **Selecionar instância**, seremos redirecionados para a página de visualização da instância.

   ![Image](https://github.com/user-attachments/assets/59ab61c4-a230-4fef-811b-d98d2cfb95c9)

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

- Nessa etapa, realizamos a conexão via SSH completamente.

## 3.4. Instalação do Nginx

- Para facilitar nossas configurações, o primeiro comando que vamos executar para prosseguir será o: `sudo -i `
  
- Logo, perceberemos que entramos como usuário root. Sendo usuário root, vamos simplificar alguns processos.

  ![Image](https://github.com/user-attachments/assets/cf3997c5-71b2-4b86-ba4c-fb9a6ee80a41)

- Antes de iniciar a instalação do Nginx, vamos executar o comando `apt install update`. Esse comando é utilizado para atualizar a lista de pacotes disponíveis nos repositórios configurados no sistema. Ele não instala ou atualiza pacotes diretamente, mas garante que as informações sobre as versões mais recentes dos pacotes estejam atualizadas, o que é essencial para garantir que a instalação do Nginx ou de qualquer outro pacote seja feita a partir da versão mais recente disponível.

- Logo após, com o comando `apt install nginx`, iniciaremos a instalação do Nginx. Esse comando irá baixar e instalar o pacote Nginx em sua versão mais recente, conforme a lista de pacotes atualizada previamente.

  ![Image](https://github.com/user-attachments/assets/1f21f694-4e1a-485a-8b89-e9266f1015dc)

- Com o comando `nginx -v`, podemos verificar qual versão do Nginx está instalada no sistema. Isso é essencial para futuras configurações, pois, dependendo da versão, alguns recursos ou comandos podem variar.
  
  ![Image](https://github.com/user-attachments/assets/d3b14b96-44df-4818-bc53-7714a3bc1df9)

- Agora, na página de detalhes da instância na AWS, você encontrará o IP público da sua instância. Vamos copiar esse IP e rodá-lo no nosso navegador. Se o Nginx estiver corretamente instalado e funcionando, você verá a página padrão do Nginx, indicando que o servidor web está rodando corretamente. Caso contrário, pode ser necessário verificar a configuração ou o status do serviço.

   ![Image](https://github.com/user-attachments/assets/54bed0dc-59a3-4488-8b84-cad40d50bda0)

   ![Image](https://github.com/user-attachments/assets/b8d4b113-7df5-47e7-8a52-dbb1f28b1a17)

  ![Image](https://github.com/user-attachments/assets/1518ba7d-cef9-48f2-982d-52fac7c143c4)

- Percebemos que o nosso Nginx está rodando corretamente, pois ao acessarmos o IP fornecido no navegador, ele corresponde à página padrão do Nginx. Agora, para realizar um teste, vamos executar o comando `systemctl stop nginx`. Esse comando vai parar o funcionamento do serviço Nginx.

  ![Image](https://github.com/user-attachments/assets/4cc9930d-d941-42a1-aaf6-9d249db8165a)

- Vamos atualizar a página do navegador para verificar se o serviço realmente foi parado. Quando o Nginx estiver parado, o navegador não exibirá mais a página padrão do Nginx e, em vez disso, poderá mostrar um erro, como "Erro 502" ou "Não foi possível conectar ao servidor". Isso confirma que o serviço foi interrompido com sucesso.

  ![Image](https://github.com/user-attachments/assets/34af50c5-230d-49b8-827f-41ebb4722a71)

- Com isso, podemos ver que nosso servidor está respondendo ao Nginx e executando corretamente os comandos que enviamos.

  ## 3.5. Criação do Webhook utilizando Discord

  - Neste estágio do projeto, será necessário criar um servidor webhook no Discord. Este servidor deverá ser notificado a cada minuto, caso o site Nginx esteja fora do ar. O primeiro passo para isso é acessar o Discord e, em seguida, deve-se selecionar a opção de criação.

  - Após isso, selecione a opção "Criar o meu", e em seguida a opção "Para meus amigos e eu"
 
     ![Image](https://github.com/user-attachments/assets/c8b8ef55-b29c-43ce-980f-988051ca48fd)

     ![Image](https://github.com/user-attachments/assets/5c146815-b103-4e7d-a187-740e4f0afb1b)

   - Logo em seguida, deve-se escolher o nome do serviço e clicar na opção "Criar".
 
     ![Image](https://github.com/user-attachments/assets/46808eb8-4172-4132-918d-137bd2affb77)

   - Com isso, o servidor que iremos utilizar para monitorar o serviço Nginx foi criado. No entanto, é necessário habilitar nele a opção "Webhook", que nada mais é do que um mecanismo de comunicação entre sistemas, permitindo que o servidor envie automaticamente informações para outro sistema (no caso, o Discord) sempre que determinado evento ocorrer. Para isso, devemos acessar as configurações, conforme mostrado na imagem abaixo.
 
   ![Image](https://github.com/user-attachments/assets/044bff05-8a47-4b31-9a57-7c806f67d437)

- Após isso, devemos selecionar a opção "Interações" e criar um serviço Webhook.

  ![Image](https://github.com/user-attachments/assets/75a6c652-32e2-44b6-8376-1e4b980ea2bc)

  ![Image](https://github.com/user-attachments/assets/75356d6b-503c-4aff-b4de-5358d707bab3)

   ![Image](https://github.com/user-attachments/assets/12d8d7f1-0a6d-44f1-8226-0e8523849697)

- Com isso, o serviço Webhook foi criado. Agora, devemos selecionar o serviço que foi gerado, copiar a URL e armazená-la, para que possamos iniciar a automatização desse serviço.

   ![Image](https://github.com/user-attachments/assets/8feb6400-0224-46ac-b441-d9629f0ca560)

  ![Image](https://github.com/user-attachments/assets/976ff049-2cbc-41cf-b4cd-d7517518a018)

- A URL do servidor Webhook deve ser armazenada, pois, ao criarmos o script para automatizar o processo, precisaremos dela. As informações desse passo a passo foram retiradas do artigo [Usando Webhooks](https://support.discord.com/hc/pt-br/articles/228383668-Usando-Webhooks) do Discord. Consulte-o em caso de dúvidas.

  ## 3.6. Criando um script de automação de logs utilizando Python

  - O objetivo do projeto é criar um serviço de automação que envie uma mensagem de erro no Discord caso o Nginx esteja fora do ar. Para isso, inicialmente, é necessário verificar a versão do software Python instalada.
 
    ![Image](https://github.com/user-attachments/assets/c0ccf0f2-20a8-408e-a78d-2011243046d1)

  - Caso o software não esteja atualizado, é necessário executar o seguinte comando para atualizar o Python:
 
        sudo apt-get install python3

- Será necessário desenvolver um script que receba informações sobre o endereço IP, armazene esses dados e, caso um serviço esteja inativo, tome as ações apropriadas, como enviar uma notificação. Com o comando `vim` ou `nano`criamos nosso arquivo que irá armazenar nosso script.

      vim monitoramento.py

- Foi criado o seguinte Script

      import requests

      #tenho a url do servidor que criei

      WEBHOOK_URL= "https://discordapp.com/api/webhooks/1339647118004191348/cTE7JOOgK1qc51TYIsvohT50arXOhSShIr43x1xlwNrJJiRUjrpXdvh-YGCdEk2Yymzj"

      # Vou ter um alerta caso o nginx não estaja funcionando

      def send_alert(message):
      requests.post(WEBHOOK_URL, json={"content": message})

      def check_site(url):
      try:
        response = requests.get(url, timeout=5)
        if response.status_code == 200:
            print("Site is alive!")
        else:                                                                           send_alert(f"⚠ Site {url} returned status code: {response.status_code}")
      except:
        send_alert(f"❌ Site {url} is down!")

      #ip publico que o nginx está rodando                                                                                                                    check_site('http://3.89.92.220:80')


- Esse script em Python atende bem às necessidades do projeto. Ele faz a verificação do status do serviço Nginx e, caso o serviço esteja fora do ar, envia um alerta para o Discord, conforme o objetivo do projeto.


## 3.7. Automatizando Script utilizando o crontab

- O crontab é uma ferramenta do Ubuntu que permite agendar e automatizar a execução de tarefas em intervalos de tempo específicos. Ela é usada para configurar jobs (tarefas) que podem ser executados de forma recorrente, como diariamente, semanalmente ou em horários pré-determinados. Aqui, utilizaremos o **crontab**, pois o projeto propõe que haja uma verificação no Nginx a cada um minuto, para isso no terminal teremos que digitar o seguinte comando:

        contrab -e
 
 - O serviço nos fornecerá um arquivo para edição, no qual devemos inserir os cinco asteriscos (** * **), uma vez que, no **crontab**, o asterisco representa uma execução em todos os intervalos possíveis (minuto, hora, dia, mês, e dia da semana). Após isso, devemos indicar o comando para executar o Python e, em seguida, especificar o caminho completo onde o nosso script se encontra.

   ![Image](https://github.com/user-attachments/assets/f5aa3c15-1087-456a-aea8-6f7313d6247d)

## 3.8. Teste de funcionalidade do WebHook

- Agora, realizaremos os primeiros testes para verificar o funcionamento do serviço. O primeiro passo é verificar se o serviço Nginx está ativo, utilizando o seguinte comando:

      sudo systemctl status nginx

![Image](https://github.com/user-attachments/assets/69cc1019-ead6-4f80-8447-e32aec9cd5ca)

- O comando indicou que o Nginx estava ativo. Para pausá-lo, devemos utilizar o seguinte comando:

      sudo systemctl stop nginx

- Logo após um minuto que desativamos o serviço Nginx começamos a receber as mensagens de alerta no Discord.

![Image](https://github.com/user-attachments/assets/1de34b38-f369-4683-b8d5-1822a4c75390)

- Este teste demonstrou que o serviço Nginx está em funcionamento e que o webhook está operando corretamente, enviando notificações conforme esperado.

## 3.9. Criando uma Página em Html

- O projeto propõe a hospedagem de uma página web desenvolvida em HTML no serviço Nginx. Para isso, uma página foi criada e hospedada com sucesso no servidor Nginx.

![Image](https://github.com/user-attachments/assets/ac791717-9aff-42f5-800c-77752c4c5886)

- Para a criação dessa página, além de HTML, foram utilizados CSS e um pouco de JavaScript. Abaixo, deixo o código para consulta.

      <!DOCTYPE html>
      <html lang="en">
      <head>
      <meta charset="UTF-8">
      <meta name="viewport" content="width=device-width, initial-scale=1.0">
      <title>Atividades PB</title>
      </head>
      <body style="font-family: 'Arial', sans-serif; margin: 0; padding: 0; background: url('background.jpg') no-repeat center center fixed; background-size: cover; color: #f4f4f4;">
      <div style="max-width: 900px; margin: 40px auto; padding: 20px; background: rgba(0, 0, 0, 0.8); border-radius: 10px; box-shadow: 0 4px 8px rgba(0, 0, 0, 0.3);">
      <h1 style="text-align: center; color: #cda76e;">Atividades PB</h1>
      <p style="font-size: 16px; line-height: 1.6;">
      Bem vindo, nessa pagina trago um resumo sobre meu ultimo projeto.
      </p>
    
      <button onclick="toggleDropdownProject1()" style="display: block; width: 100%; background: #7693b0; color: #fff; padding: 15px; font-size: 18px; border: none; border-radius: 5px; text-align: left; cursor: pointer; margin-top: 20px; transition: background 0.3s ease;">
      Projeto 1 - Configuração de Servidor Web com Monitoramento
      </button>
      <ul id="projectDropdown" style="display: none; list-style: none; margin: 10px 0 0; padding: 10px; background: rgba(255, 255, 255, 0.1); border-radius: 5px; opacity: 0; transform: translateY(-10px); transition: all 0.3s ease;">
        <h3 style="color: #cda76e;">Etapa 1: Configuração do Ambiente Tarefas</h3>
        <ol style="margin-left: 20px;">
          <li>Criar uma VPC na AWS com:</li>
          <ul style="margin-left: 20px; list-style-type: circle;">
            <li>2 sub-redes públicas (para acesso externo)</li>
            <li>2 sub-redes privadas (para futuras expansões)</li>
            <li>Uma Internet Gateway conectada às sub-redes públicas</li>
          </ul>
          <li>Criar uma instância EC2 na AWS</li>
          <ul style="margin-left: 20px; list-style-type: circle;">
            <li>Escolher uma AMI baseada em Linux (Ubuntu/Debian/Amazon Linux)</li>
            <li>Instalar na sub-rede pública criada anteriormente</li>
            <li>Associar um Security Group que permita tráfego HTTP (porta 80) e SSH (porta 22, opcional)</li>
          </ul>
          <li>Acessar a instância via SSH para realizar configurações futuras</li>
        </ol>
        
        <h3 style="color: #cda76e; margin-top: 20px;">Etapa 2: Configuração do Servidor Web</h3>
        <ol style="margin-left: 20px;">
          <li>Instalar o servidor Nginx na EC2</li>
          <li>Criar uma página HTML simples para ser exibida pelo servidor.</li>
          <li>Configurar o Nginx para servir a página corretamente</li>
        </ol>
      
        <h3 style="color: #cda76e; margin-top: 20px;">Etapa 3: Monitoramento e notificações</h3>
        <ol style="margin-left: 20px;">
          <li>Criar um script em Bash ou Python para monitorar a disponibilidade do site</li>
          <li>O script deve:</li>
          <ol style="margin-left: 20px; list-style-type: circle;">
            <li>Verificar se o site responde corretamente a uma requisição HTTP</li>
            <li>Criar logs das verificações em /var/log/monitoramento.log</li>
            <li>Enviar uma notificação via Discord, Telegram ou Slack se detectar indisponibilidade</li>
          </ol>
          <li>Configurar o script para rodar automaticamente a cada 1 minuto usando cron ou systemd timers</li>
        </ol>

        <h3 style="color: #cda76e; margin-top: 20px;">Etapa 4: Automação e Testes</h3>
        <ol style="margin-left: 20px;">
          <li>Testar a implementação:</li>
          <ol style="margin-left: 20px; list-style-type: circle;">
            <li>Verificar se o site está acessível via navegador</li>
            <li>Parar o Nginx e verificar se o script detecta e envia alertas corretamente</li>
          </ol>
          <li>Criar uma documentação no GitHub explicando (este projeto se encontra em <a href="https://github.com/Lessaayumi" style="color: #cda76e;">https://github.com/Lessaayumi</a>):</li>
          <ol style="margin-left: 20px; list-style-type: circle;">
            <li>Como configurar o ambiente</li>
            <li>Como instalar e configurar o servidor web</li>
            <li>Como funciona o script de monitoramento</li>
            <li>Como testar e validar a solução</li>
        </ol>
      </ul>

      <button onclick="toggleDropdownPb()" style="display: block; width: 100%; background: #7693b0; color: #fff; padding: 15px; font-size: 18px; border: none; border-radius: 5px; text-align: left; cursor: pointer; margin-top: 20px; transition: background 0.3s ease;">
        Programa de Bolsas
      </button>
      <ul id="pbDropdown" style="display: none; list-style: none; margin: 10px 0 0; padding: 10px; background: rgba(255, 255, 255, 0.1); border-radius: 5px; opacity: 0; transform: translateY(-10px); transition: all 0.3s ease;">
        <li>Aqui vamos falar um pouco sobre PB!</li>
      </ul>

      <h2 style="color: #7693b0; margin-top: 30px;">Contato</h2>
      <p>Caso queira entrar em contato, sinta-se a vontade em enviar um e-mail para <a href="mailto:alessandra.lopes.pb@compasso.com.br" style="color: #cda76e;">alessandra.lopes.pb@compasso.com.br</a>.</p>
      </div>

      <script>
       let dropdownVisible = false;
    
       function toggleDropdownProject1() {
      const dropdown = document.getElementById('projectDropdown');
      if (!dropdownVisible) {
        dropdown.style.display = 'block';
        setTimeout(() => {
          dropdown.style.opacity = '1';
          dropdown.style.transform = 'translateY(0)';
        }, 10);
      } else {
        dropdown.style.opacity = '0';
        dropdown.style.transform = 'translateY(-10px)';
        setTimeout(() => {
          dropdown.style.display = 'none';
        }, 300);
      }
      dropdownVisible = !dropdownVisible;
       }

      function toggleDropdownPb() {
      const dropdown = document.getElementById('pbDropdown');
      if (!dropdownVisible) {
        dropdown.style.display = 'block';
        setTimeout(() => {
          dropdown.style.opacity = '1';
          dropdown.style.transform = 'translateY(0)';
        }, 10);
      } else {
        dropdown.style.opacity = '0';
        dropdown.style.transform = 'translateY(-10px)';
        setTimeout(() => {
          dropdown.style.display = 'none';
        }, 300);
      }
      dropdownVisible = !dropdownVisible;
      }
       </script>
      </body>
       </html>


## 3.10. Subindo script Html

- Agora, vamos subir o programa em HTML que foi desenvolvido e configurar o Nginx para executá-lo. Primeiro vamos criar o conteúdo em HTML utilizando o comando nano

      nano /etc/nginx/sites-available/meusite

  - Nesse arquivo vamos por as infromações contidas na imagem abaixo, elas são importantes pois é primordial para a hospedagem da página.
 
  ![Image](https://github.com/user-attachments/assets/8c9c858b-dfe9-4aef-8cd5-679fdb9d8fe8)

  - Logo, iremos criar uma pasta para armazenar o conteúdo a ser transmitido.
 
    ![Image](https://github.com/user-attachments/assets/dcafaed3-ac09-496c-827d-c659c79fe5aa)

  - Em seguida iremos criar um arquivo dentro dessa pasta para armazenar o script do site.
 
        nano /var/www/meusite/index.html

  - Nessa arquivo foi armazenado o conteudo que será transmitido
 
    ![Image](https://github.com/user-attachments/assets/49910362-de40-4ef6-9921-45cc6de1c6fe)

- Após fazer o script, os seguintes comandos devem ser realizados para configurar o nginx e subir/hospedar a página no IP.

  ![Image](https://github.com/user-attachments/assets/08e5df6d-21f2-45fb-a501-8f2c6aba216e)

  ![Image](https://github.com/user-attachments/assets/a8373112-c8e7-45ec-b2c1-cd75a3c481dd)

   ![Image](https://github.com/user-attachments/assets/26c182e6-79d0-4059-a951-e98df6cbd08d)

  ![Image](https://github.com/user-attachments/assets/e37b44b3-7940-497b-b0e2-15509157add4)

- Esses comandos são as configurações necessárias para que o script seja executado dentro do Nginx e seja transmitido online via HTTP para outros computadores. E após isso temos um site, em html rodando dentro do serviço Nginx

  ![Image](https://github.com/user-attachments/assets/ac791717-9aff-42f5-800c-77752c4c5886)

## 4. Testes finais:

- Agora, nesta seção, realizaremos dois testes: o primeiro para verificar o funcionamento do site e o segundo para testar o recebimento de mensagens no Discord quando o serviço do Nginx não estiver respondendo.

  ## 4.1.  Alertas quando o sistema está online

  - Reiniciamos o sistema e o Nginx começa a funcionar automaticamente assim que a instância é iniciada.

-Inicia o Nginx:
      
        systemctl start nginx

 - Verifica o estado do Nginx:

       systemctl status nginx

- A imagem abaixo ilustra o serviço Nginx em funcionamento, com o site sendo executado juntamente com o script.

  ![Image](https://github.com/user-attachments/assets/7ca1b4c5-31af-451e-b4c5-1d67ebfee51f)

   ## 4.2. Alertas quando o sistema está offline

  - Agora, vamos pausar o serviço e verificar o recebimento das mensagens no Discord.
 
  - Para o Nginx:
 
        systemctl stop nginx

   - A imagem abaixo comprova que o site não está no ar, o Nginx está parado e o Discord está recebendo os alertas de que o sistema não está funcionando.
 
  ![Image](https://github.com/user-attachments/assets/ae2675be-aa3e-4726-b06b-9b95d69c1f7b)

- Concluímos que o projeto desenvolvido atende a todos os requisitos propostos, incluindo a criação da VPC, a configuração da instância EC2, a hospedagem do site Nginx e a implementação da verificação via Discord em caso de indisponibilidade do serviço, garantindo a automação do monitoramento e a notificação em tempo real.

## 5. Considerações

- Este projeto é de grande importância, pois oferece uma solução completa para monitoramento e automação de serviços críticos, como o Nginx, em ambientes de produção. A criação da infraestrutura necessária na AWS, incluindo a VPC e a instância EC2, além da configuração do servidor Nginx, permite a hospedagem de aplicações de forma escalável e segura. A implementação de alertas via Discord em caso de falha do serviço garante uma resposta rápida e eficaz a problemas, minimizando o tempo de inatividade e contribuindo para a continuidade dos serviços. Esse tipo de automação é essencial em ambientes de produção, onde a disponibilidade e o monitoramento constante são cruciais para a operação estável e segura das aplicações.

## 6. Referências

- support.discord.com/hc/pt-br/articles/228383668-Usando-Webhooks - Acesso: 17 de fevereiro de 2025, ás 14h26.
- docs.aws.amazon.com/pt_br/vpc/latest/userguide/create-vpc.html#:~:text=Para%20criar%20uma%20VPC%2C%20sub,more%20(VPC%20e%20mais) Acesso: 15 de fevereiro de 2025, ás 19h51.
- docs.aws.amazon.com/pt_br/AWSEC2/latest/UserGuide/EC2_GetStarted.html - Acesso: 17 de Fevereiro de 2025, ás 20h22.
- digitalocean.com/community/tutorials/how-to-install-nginx-on-ubuntu-20-04-pt - Acesso: 17 de Fevereiro de 2025, ás 20h43.
  






  
  




   





  
    

  
  


  

  
  

  

  







