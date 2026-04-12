<style>
    /* Reiniciando a Contagem Geral */
    body {
        counter-reset: contadorh1 1 contadorLegenda 0;
    }

    /* Aplica o estilo para H1 e informa que a contagem de H2 deve começar do 0 sempre que um H1 aparecer */
    h1 {
        counter-reset: contadorh2;
        text-align: center;
    }

    h1::before {
        counter-increment: contadorh1;
    }

    /* Aplica o estilo para H2 e informa que a contagem de H3 deve começar do 0 sempre que um H2 aparecer */
    h2 {
        counter-reset: contadorh3;
    }

    h2::before {
        counter-increment: contadorh2;
        content: counter(contadorh2) ". ";
    }

    /* Aplica estilo para H3 */
    h3::before {
        counter-increment: contadorh3;
        content: counter(contadorh2) "." counter(contadorh3) ". ";
    }

    /* Legendas */
    .legenda::before {
    /* Incrementa o contador toda vez que a classe aparece */
    counter-increment: contadorLegenda;
    /* Define o texto automático */
    content: "Figura " counter(contadorLegenda) ": ";
    font-weight: bold;
}
</style>

# Segurança de Dados

> **Última sincronização:** 12/04/2026 17:41:42

## Sumário de Aulas

- Aula 01 - [Apresentação da Disciplina](#apresentação-da-disciplina)
- Aula 02 - [Contextualização a Segurança da Informação](#contextualização-a-segurança-da-informação)
- Aula 04 - [Criptografia de Chave Simétrica](#criptografia-de-chave-simétrica)
- Aula 07 - [Título não encontrado](#título-não-encontrado)

---

## Apresentação da Disciplina

- Arquivo da [aula 01]().
- Data da Postagem: 11/03/2026

### Tópicos

- Apresentação do Professor
- Experiência Profissional
- [Dados Gerais](#dados-gerais)
- As redes de Computadores
  - Breve Histórico
- Motivação da Disciplina
- Objetivo Geral
- Objetivos Específicos
- Ementa
- [Conteúdo Programático](#conteúdo-programático)
- [Avaliações](#critérios-de-avaliação)
- Bibliografia

### Dados Gerais

- Carga Horária (CH): 120h
- Aulas
  - Quintas: 09:45 - 11:25 (últimas duas aulas)
  - Sexta: 07:00 - 08:40 (primeiras duas aulas)
  - Local: Laboratório de Informática 06
- Número de Avaliações: 4

### Conteúdo Programático

1. Histórico e Motivação para uso das redes de computadores
2. Topologias físicas e lógicas de redes de computadores
3. Transmissão da Informação
   1. Sinais: analógico e digital
   2. Fontes de Distorção nos Enlaces
   3. Teoremas de Nyquist e Shannon
   4. Multiplexação e seus tipos
4. Comunicação e seus tipos
5. Meios de transmissão: com e sem fio
6. Introdução à Arquitetura de Redes
7. O Modelo RM-OSI
   1. Motivação
   2. Camadas e suas funções
8. Confeccionando cabos de rede (par traçado UTP 5e) - Prática
9. O Padrão IEEE 802
   1.  Motivação
   2.  Camadas e suas funções
   3.  Comparação com o RM-OSI
   4.  Padrões
10. Arquitetura TCP/IP
    1.  Camadas e suas funções
    2.  Comparação com o RM-OSI e IEEE 802
    3.  Camadas: Protocolos e suas funções
11. Internet ou Inter-Rede
    1.  Endereçamento IP
    2.  Datagrama IP
    3.  ARP e RARP
    4.  NAT
12. Redes Virtuais e Software-Defined Networks (SDN)
    1.  Montagem e Avaliação
    2.  Controladores e Simulador SDN (Mininet)
    3.  Protocolos de Tunelamento em SDN com Prática
13. Transporte
    1.  TCP
    2.  Cabeçalho
    3.  Algoritmos de Controle de Congestionamento
    4.  UDP
    5.  SCTP
14. Aplicação
    1.  HTTPS
    2.  DNS
    3.  SSH

### Critérios de Avaliação

&emsp; Quatro avaliações:

- 2 provas subjetivas(s)/objetiva(s)
- 1 prática
- 1 seminário com apresentação de artigos científicos

---

## Contextualização a Segurança da Informação

- Arquivo da [aula 02]().
- Data de Postagem: 12/03/2026

### Sumário

- [Contextualização a Segurança da Informação](#contextualização-a-segurança-da-informação)
  - [Sumário](#sumário)
  - [Problematização](#problematização)
  - [Evolução da Segurança da Informação](#evolução-da-segurança-da-informação)
  - [Pilares da Segurança da Informação](#pilares-da-segurança-da-informação)
  - [Criptografia](#criptografia)
  - [Tipos de Criptografia](#tipos-de-criptografia)
  - [Controle de Acesso](#controle-de-acesso)
  - [CERT.BR](#certbr)
  - [Incidentes de Segurança](#incidentes-de-segurança)
  - [Estatísticas de Ataques de Amplificação](#estatísticas-de-ataques-de-amplificação)
  - [Estatísticas de DNS maliciosos](#estatísticas-de-dns-maliciosos)
  - [Estatísticas de SPAM](#estatísticas-de-spam)
  - [As 20 Portas TCP que mais sofreram varreduras em 2020](#as-20-portas-tcp-que-mais-sofreram-varreduras-em-2020)
  - [Ataques por Número de Sistema Autônomo (ASN)](#ataques-por-número-de-sistema-autônomo-asn)
  - [Ataques a Servidores Web](#ataques-a-servidores-web)
  - [Nomas ISO](#nomas-iso)
  - [Recomendações Mercadológicas](#recomendações-mercadológicas)
    - [COBIT: Control Objectives for Information and related Technology](#cobit-control-objectives-for-information-and-related-technology)
    - [Information Technology Infrastructure Library (ITIL)](#information-technology-infrastructure-library-itil)
  - [Reflexão](#reflexão)
  - [Referências](#referências)

### Problematização

&emsp; As informações são os bens mais preciosos que possuímos hoje em dia, por isso veremos um dos principais focos das empresas que é a **Segurança de Dados** e como ela pode proteger esse bem tão precioso que temos.

### Evolução da Segurança da Informação

- 1940 - Mark I
  - Aplicação: Otimizar a trajetória dos mísseis
- 1957 - Satélite Sputnik
- 1962 - Arpanet ou Darpanet (Defense Advanced Research Projects Agency)
  - Aplicação: Trocar dados sigilosos entre bases militares, mesmo quando uma ou várias destas ficarem sem conexão, funcionando em forma de grafo

- 1970 - Início da Arquitetura TCP/IP
  - E-mail (1969) e Primeira aplicação: 1972
  - DNS
  - TCP evolução do NCP
  - [x] Store and Forward (único mecanismo de segurança) [1]
  - [x] Fim da década de 70: separação do TCP em 'TCP' e 'IP'

- 1980
  - Popularização dos Computadores
  - Padronização TCP/IP (1983) [2]
  - NFSNET
  - Surgimento da Cultura Hacker [3]
  - WWW (1989)

- 1990
  - Internet
  - Vândalos da Internet
  - Wireless Fidelity (Wi-Fi)

- 2000/2010/2020
  - Crimes profissionais na internet
  - Popularização da Computação Móvel
  - Computação em Nuvem
  - IoT (MANET, VANET, etc)
  - SDN, 5G
  - Smart Cities

### Pilares da Segurança da Informação

- Estados da Informação
  - Transmissão
  - Armazenamento
  - Processamento
- Propriedades da Segurança da Informação
  - Confidencialidade
  - Integridade
  - Disponibilidade
- Medidas de Segurança
  - Tecnologias
  - Políticas e Procedimentos
  - Conscientização

&emsp; As informações estão em diversos locais e a segurança depende de múltiplos fatores. Imagine cada **Pilar de Segurança** sendo uma face de um cubo.

- CID [5]
  - **Confidencialidade**: visa impedir a leitura não autorizada de informações.
  - **Integridade**: se dá, caso uma escrita não autorizada for proibida.
  - **Disponibilidade**: fazer com que os sistemas estejam sempre disponíveis ao usuário.
- Segundo [5]
  - **Criptologia**: é a arte e a ciência de fazer e quebrar "códigos secretos".
  - A **Criptografia** é a criação de "códigos secretos".
  - **Criptoanálise** é a ruptura de "códigos secretos".

### Criptografia

&emsp; De acordo com [6]:

- Teve origem no Egito, em meados de 1900 A.C.
- Usado no Império Romano com a Cifra de César (substituição por _n_)
- Disco de Cifra - Início da Mecanização de Cifragem
  - Século XV: italiano Leon Battista Alberti (1404-1472) com dois cilindros para implementar a Cifra de César
  - Século XVIII: cilindro de Jefferson (Thomas Jefferson) com 36 discos implementando uma cifra de substituição polialfabética.
  - Cifra polialfabética consiste em usar uma tabela 26x26 que cria 26 alfabetos.
- Em 1918, Arthur Scherbius patenteou a máquina de criptografia denominada Enigma. [Vídeo de explicação](https://www.youtube.com/watch?v=mdSvGUd0_c).
  - Baseada no Princípio de Kerchhoff
- Em 1949, Claude Shannon criou a Teoria Matemática da Comunicação ([link de vídeo](https://www.youtube.com/watch?v=yIEnE-jfI54)).
- Em 1972: DES (Data Encryption Standard)
- Década de 90: AES (Advanced Encryption Standard).

```js
plain_text = [a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, u, v, w, x, y, z]

cipher_text = [D, E, F, G, H, I, J, K, L, M, N, O, P, Q, R, S, T, U, V, W, X, Y, Z, A, B, C]
```

<p align="right" class="legenda">
  <ins><i>Cifra de César com n = 3</i></ins>
</p>

### Tipos de Criptografia

- **Simétrica**: só uma chave é compartilhada entre origem e destino. Exemplos:
  - RC4
  - A5/1
  - DES (3DES)
  - AES
- **Assimétrica** ou **Criptografia de Chaves**: um par de chaves é trocado, uma para cifrar (pública) e outra diferente para decifrar (privada). Exemplos:
  - RSA
  - Curvas Elípticas

&emsp; Exemplos de Tipos de Criptografia:

```txt
1. Mensagem original enviada
2. Algoritmo de criptografar (Chave Secreta Compartilhada)
3. Texto Cifrado (Meio Seguro)
4. Algoritmo de descriptografar (Chave Secreta Compartilhada)
5. Mensagem original recebida
```

<p align="right" class="legenda">
  <ins><i>Criptografia Simétrica</i></ins>
</p>

```txt
1. Mensagem original enviada
2. Algoritmo para criptografar (Chave Pública)
3. Texto cifrado
4. Algoritmo para descriptografar (Chave Privada)
5. Mensagem original recebida
```

<p align="right" class="legenda">
  <ins><i>Criptografia Assimétrica</i></ins>
</p>

### Controle de Acesso

- **Autenticação**: forma de um usuário provar que ele é ele mesmo, através de provar:
  - Algo que você sabe (senha)
  - Algo que você tem (smartcard, cartão de banco, assinatura digital)
  - Algo que você é (biometria: leitor digital, leitor da íris e análise da palma da mão)
- **Autorização**: após a autenticação, o usuário estará apto ao sistema, seguindo restrições impostas pelo mesmo

### CERT.BR

> &emsp; Grupo de Resposta a Incidentes de Segurança para a Internet no Brasil. mantido pelo NIC.br, do Comitê Gestor da Internet no Brasil. É responsável por tratar incidentes de segurança em computadores que envolvam redes conectadas à Internet no Brasil.
>
> &emsp; Atua como um ponto central para notificações de incidentes de segurança no Brasil, provendo a coordenação e o apoio no processo de resposta a incidentes e, quando necessário, colocando as partes envolvidas em contato.
>
> &emsp; Além do processo de tratamento a incidentes em si, o CERT.br também atua através do trabalho de conscientização sobre os problemas de segurança, da análise de tendências e correlação entre eventos na Internet brasileira e do auxílio ao estabelecimento de novos CSIRTs no Brasil.
>
> &emsp; Estas atividades têm como objetivo estratégico aumentar os níveis de segurança e de capacidade de tratamento de incidentes das redes conectadas à Internet no Brasil.
>
> &emsp; As atividades conduzidas pelo CERT.br fazem parte das atribuições do CGI.br de:
> 
> - I - estabelecer diretrizes estratégicas relacionadas ao uso e desenvolvimento da Internet no Brasil;
> - IV - promover estudos e recomendar procedimentos, normas e padrões técnicos e operacionais, para a
segurança das redes e serviços de Internet, bem assim para a sua crescente e adequada utilização pela sociedade
> - VI - ser representado nos fóruns técnicos nacionais e internacionais relativos à Internet; Bem como dos objetivos do NIC.br, conforme seu Estatuto:
> - IV - atender aos requisitos de segurança e emergências na Internet Brasileira em articulação e cooperação com as entidades e os órgãos responsáveis;
> - VII - promover ou colaborar na realização de cursos, simpósios, seminários, conferências, feiras e congressos, visando contribuir para o desenvolvimento e aperfeiçoamento do ensino e dos conhecimentos nas áreas de suas especialidades.

### Incidentes de Segurança

&emsp; Como afirma o CERT (Centro de Estudos, Resposta e Tratamento de Incidentes de Segurança no Brasil), em [5]:

> "Qualquer evento adverso, confirmado ou sob suspeita, relacionado à segurança dos sistemas de computação ou das redes de computadores".
>
> "O ato de violar uma política de segurança, explícita e implícita".

&emsp; Ainda segundo o CERT:

- **Worm**: notificações de atividades maliciosas relacionadas com o processo automatizado de propagação de códigos maliciosos na rede.
- **(DoS -- Denial of Service)**: notificações de ataques de negação de serviço, onde atacante utiliza um computador ou um conjunto de computadores para tirar de operação um serviço, computador ou rede.
- **Invasão**: um ataque bem sucedido que resulte no acesso não autorizado a um computador ou rede.
- **Web**: um caso particular de ataque visando especificamente o comprometimento de servidores Web ou desfigurações de páginas na Internet.
- **Scan**: notificações de varreduras em redes de computadores, com o intuito de identificar quais computadores estão ativos e quais serviços estão sendo disponibilizados por eles. É amplamente utilizado por atacantes para identificar potenciais alvos, pois permite associar possíveis vulnerabilidades aos serviços habilitados em um computador.
- **Fraude**: segundo Houaiss, é "qualquer ato ardiloso, enganoso, de má-fé, com intuito de lesar ou ludibriar outrem, ou de não cumprir determinado dever; logro". Esta categoria engloba as notificações de tentativas de fraudes, ou seja, de incidentes em que ocorre uma tentativa de obter vantagem.
- **Outros**: notificações de incidentes que não se enquadram nas categorias anteriores.

![Gráfico de Notificações de Incidentes recebidas por Ano pelo CERT.br](../output/aula02-g1-slide20.png)

<p align="right" class="legenda">
  <ins><i>Incidentes de Segurança reportados entre 2012 e 2023.</i></ins>
</p>

![Gráfico de Notificações sobre Equipamentos participando de ataques DoS](../output/aula02-g2-slide21.png)

<p align="right" class="legenda">
  <ins><i>Equipamentos participando de Ataques DoS.</i></ins>
</p>

![Gráfico sobre "Incidentes Notificados ao CERT.br -- Janeiro/2023 a Junho/2023"](../output/aula02-g3-slide22.png)

<p align="right" class="legenda">
  <ins><i>Categorias de Incidentes Notificados (CERT.br) - Janeiro/2023 até Junho/2023.</i></ins>
</p>

![Gráfico sobre "Portas que mais sofreram varreduras (scan) ou ataques sem sucesso -- Janeiro/2023 a Junho/2023"](../output/aula02-g4-slide23.png)

<p align="right" class="legenda">
  <ins><i>Portas mais Atacadas - Janeiro/2023 até Junho/2023.</i></ins>
</p>

![Gráfico sobre "Incidentes de MALWARE Notificados ao CERT.br -- Janeiro até Junho de 2023"](../output/aula02-g5-slide24.png)

<p align="right" class="legenda">
  <ins><i>Malwares reportados ao CERT.br - Janeiro/2023 até Junho/2023.</i></ins>
</p>

![Gráfico sobre "Incidentes de PHISHING Notificados ao CERT.br -- Janeiro até Junho de 2023"](../output/aula02-g6-slide24.png)

<p align="right" class="legenda">
  <ins><i>Phishings reportados ao CERT.br - Janeiro/2023 até Junho/2023.</i></ins>
</p>

![Gráfico sobre "Top10 Países dos endereços IP de origem de varredura de ataque"](../output/aula02-g7-slide25.png)

<p align="right" class="legenda">
  <ins><i>Top10 países que possuem mais origem de endereços de IP de varredura - Janeiro/2023 até Junho/2023.</i></ins>
</p>

![Gráfico sobre "Páginas Falsas -- Janeiro até Junho de 2023"](../output/aula02-g8-slide26.png)

<p align="right" class="legenda">
  <ins><i>Quantidade de Páginas Falsas - Janeiro/2023 até Junho/2023.</i></ins>
</p>

![Categorias de Páginas Falsas que afetam Organizações no Exterior -- Janeiro a Junho de 2023.](../output/aula02-g09-slide27.png)

<p align="right" class="legenda">
  <ins><i>Categorias de Páginas Falsas que afetam Organizações no Exterior -- Janeiro a Junho de 2023.</i></ins>
</p>

![Países de Alocação de Endereços IP onde as Páginas Falsas estão Hospedados -- Janeiro a Junho de 2023](../output/aula02-g10-slide28.png)

<p align="right" class="legenda">
  <ins><i>Países de Alocação de Endereços IP onde as Páginas Falsas estão Hospedados -- Janeiro a Junho de 2023</i></ins>
</p>

![Sistemas Autônomos (AS) dos Endereços IP onde as Páginas estão Hospedadas -- Janeiro a Junho de 2023](../output/aula02-g11-slide29.png)

<p align="right" class="legenda">
  <ins><i>Sistemas Autônomos (AS) dos Endereços IP onde as Páginas estão Hospedadas -- Janeiro a Junho de 2023</i></ins>
</p>

![Páginas Falsas - Uptime: AS13335 - CloudFlareNet, Estados Unidos (US) - TOTAL -- Janeiro a Junho de 2023](../output/aula02-g12-slide30.png)

<p align="right" class="legenda">
  <ins><i>Páginas Falsas - Uptime: AS13335 - CloudFlareNet, Estados Unidos (US) - TOTAL -- Janeiro a Junho de 2023</i></ins>
</p>

![Páginas Falsas - Uptime: AS13335 - CloudFlareNet, Estados Unidos (US) - BRASIL -- Janeiro a Junho de 2023](../output/aula02-g13-slide30.png)

<p align="right" class="legenda">
  <ins><i>Páginas Falsas - Uptime: AS13335 - CloudFlareNet, Estados Unidos (US) - BRASIL -- Janeiro a Junho de 2023</i></ins>
</p>

![Páginas Falsas - Uptime: AS13335 - CloudFlareNet, Estados Unidos (US) - EXTERIOR -- Janeiro a Junho de 2023](../output/aula02-g14-slide30.png)

<p align="right" class="legenda">
  <ins><i>Páginas Falsas - Uptime: AS13335 - CloudFlareNet, Estados Unidos (US) - EXTERIOR -- Janeiro a Junho de 2023</i></ins>
</p>

![Páginas Falsas - Uptimes: AS15169 - Google, Estados Unidos (US) - TOTAL -- Janeiro a Junho de 2023](../output/aula02-g15-slide30.png)

<p align="right" class="legenda">
  <ins><i>Páginas Falsas - Uptimes: AS15169 - Google, Estados Unidos (US) - TOTAL -- Janeiro a Junho de 2023</i></ins>
</p>

![Páginas Falsas - Uptimes: AS15169 - Google, Estados Unidos (US) - BRASIL -- Janeiro a Junho de 2023](../output/aula02-g16-slide30.png)

<p align="right" class="legenda">
  <ins><i>Páginas Falsas - Uptimes: AS15169 - Google, Estados Unidos (US) - BRASIL -- Janeiro a Junho de 2023</i></ins>
</p>

![Páginas Falsas - Uptimes: AS15169 - Google, Estados Unidos (US) - EXTERIOR -- Janeiro a Junho de 2023](../output/aula02-g17-slide30.png)

<p align="right" class="legenda">
  <ins><i>Páginas Falsas - Uptimes: AS15169 - Google, Estados Unidos (US) - EXTERIOR -- Janeiro a Junho de 2023</i></ins>
</p>

![Incidentes Reportados por Tipo -- Janeiro a Dezembro de 2020](../output/aula02-g21-slide35.png)

<p align="right" class="legenda">
  <ins><i>Incidentes Reportados por Tipo -- Janeiro a Dezembro de 2020</i></ins>
</p>

### Estatísticas de Ataques de Amplificação

&emsp; Os administradores de sistemas autônomos brasileiros (ASN) são notificados regularmente pelo CERT.br, cujas redes possuam sistema mal configurados que possam ser abusados para a realização de ataques de negação de serviço, com o objetivo de reduzir o número de redes brasileiras passíveis de serem abusadas para a realização de ataques DDoS.

&emsp; INSERIR **``Gráfico de Notificações de endereços de IP com serviços permitindo amplificação - (agosto/2022 até julho/2023)``**

### Estatísticas de DNS maliciosos

&emsp; É **definido** como `servidor DNS malicioso` aquele que está fornecendo respostas incorretas para nome(s) de domínio(s) de instituições vítima. Em geral, instituições financeiras, de comércio eletrônico, redes sociais e/ou domínios bastantes conhecidos.

&emsp; Seu **propósito** é direcionar os usuários para sites falsos, como parte de ataques de pharming.

&emsp; São **instalados**, em sua maioria, pelo próprio atacante contratando serviços de hospedagem ou de nuvem.

&emsp; O CERT.br notifica regularmente os ASNs que hospedam esses servidores, solicitando que sejam aplicadas as políticas adequadas para que o serviço seja retirando do ar.

&emsp; INSERIR **``Gráfico de Servidores DNS maliciosos no Brasil e fora do Brasil (ativos por dia) - (agosto/2021 até agosto/2023)``**

> ### ATENÇÃO
>
> &emsp; Estas estatísticas são **relativas** a servidores DNS maliciosos (rogue) sendo usados para **sequestro de DNS (DNS Hijacking)**. Ou seja, um servidor:
>
> * autoritativa para os domínios das vítimas
> * recursivo aberto, para resposta às demais consultas
>
> &emsp; Estas estatísticas:
>
> * <spam style="color: red">não são</spam> de DNS invadidos;
> * <spam style="color: red">não são</spam> de envenenamento (cache poisoning);
> * <spam style="color: red">não são</spam> de sequestro de domínio (domain hijacking).

### Estatísticas de SPAM

![Gráfico de Spams Reportador ao CERT.br por Ano -- 2012 até 2023](../output/aula02-g20-slide34.png)

<p align="right" class="legenda">
  <ins><i>Gráfico de Spams Reportador ao CERT.br por Ano -- 2012 até 2023</i></ins>
</p>

### As 20 Portas TCP que mais sofreram varreduras em 2020

&emsp; As varreduras pelas portas TCP 23, 22, 81, 5555, 8000 e 8080 estão todas relacionadas com atividades de propagação de botnets de IoT, como a Mirai e suas variantes e a Bashlite e suas variantes. Os ataques nessas portas são tentativas de força bruta de credenciais ou tentativas de explorar vulnerabilidades nas interfaces de gerência de roteadores de banda larga ou de Wi-Fi.

&emsp; As portas que mais tiveram aumento de varreduras de 2019 para 2020 foram, na ordem de variação: 3389/TCP - 118%, 21/TCP - 101%, 1433/TCP - 85% e 23/TCP - 65%.

&emsp; Outro fato interessante é a continuidade da procura por serviços relacionados com e-mail, mais notadamente as portas POP3 (110/TCP), SMTPS (465/TCP). Este comportamento pode ser relacionado com o aumento de força bruta em serviços de e-mail que temos visto nas notificações de incidentes de segurança recebidas pelo CERT.br.

### Ataques por Número de Sistema Autônomo (ASN)

![Top10 de ASNs Origem de Ataques -- 2020](../output/aula02-g22-slide38.png)

<p align="right" class="legenda">
  <ins><i>Top10 de ASNs Origem de Ataques -- 2020</i></ins>
</p>

### Ataques a Servidores Web

&emsp; A maioria absoluta das falhas de segurança nos sistemas desktop e web são por falha de programação:

- Falta de validação de entrada
- Falta de checagem de erros

&emsp; Como a segurança está sempre em último plano os testes de segurança são realizados depois dos lançamentos dos produtos, gerando uma série de atualizações

### Nomas ISO

- **ISO 27001** - Técnicas de segurança — Sistemas de gestão de segurança da informação — Requisitos
- **ISO 27002** – Técnicas de Segurança: Código de práticas para a gestão de segurança da informação

### Recomendações Mercadológicas

#### COBIT: Control Objectives for Information and related Technology

&emsp; É um guia de boas práticas apresentado como framework, dirigido para a gestão de tecnologia de informação (TI). 

&emsp; Mantido pelo ISACA (Information Systems Audit and Control Association), possui uma série de recursos que podem servir como um modelo de referência para gestão da TI, incluindo um sumário executivo, **um framework, objetivos de controle, mapas de auditoria, ferramentas para a sua implementação e principalmente, um guia com técnicas de gerenciamento [6]**.

#### Information Technology Infrastructure Library (ITIL)

&emsp; É um conjunto de boas práticas a serem aplicadas na infraestrutura, operação e manutenção de serviços de tecnologia da informação (TI). Foi desenvolvido no final dos anos 1980 pela CCTA (Central Computer and Telecommunications Agency) e atualmente está sob custódia da OGC (Office for Government Commerce) da Inglaterra.

&emsp; A ITIL busca promover a gestão com foco no cliente e na qualidade dos serviços de tecnologia da informação (TI). A ITIL lida com estruturas de processos para a gestão de uma organização de TI apresentando um conjunto abrangente de processos e procedimentos gerenciais, organizados em disciplinas, com os quais uma organização pode fazer sua gestão tática e operacional em vista de alcançar o alinhamento estratégico com os negócios.

&emsp; ITIL dá uma descrição detalhada sobre importantes práticas de IT com checklists, tarefas e procedimentos que uma organização de IT pode customizar para suas necessidades [7]

### Reflexão

> “É um fato bem conhecido que nenhuma outra parte da população recorre mais facilmente e rapidamente, aos mais recentes triunfos da ciência, do que a classe criminosa”.
> Inspetor John Bofield – Chicago Herald, 1888 [8].

### Referências

- [1] LEINER, Barry M.; KAHN, Robert E.; POSTEL, John; CERF, Vinton G.; KLEINROCK, Leonard; ROBERTS, Larry G.; Clark, David. D.; LYNCH, Daniel C.; WOLFF, Stephen. A Brief History of the Internet, Volume 39, Number 5, ACM SIGCOMM Computer Communication Review, October 2009.
- [2] Wikipedia: História da Internet. Documentação online. Disponível na URL: http://pt.wikipedia.org/wiki/Hist%C3%B3ria_da_Internet e acessado em 24 de Abril de 2012.
- [3] SHAHRYAR, Suheil. Web Security 2005. Documentação online. Disponível na URL: http://complianceandprivacy.com/WhitePapers/VeriSign-Web-Security-2005.pdf e acessado em 24 de Abril de 2012. 
- [4] HOEPERS, Cristine. Tratamento de Incidentes de Segurança e Tendências no Brasil. Documentação online. Disponível na URL: http://www.cert.br/docs/palestras/certbr-jornada-sisp2012.pdf e acessado em 24 de Abril de 2012.
- [5] STAMP, Mark. Information security: principles and practice, 1st Edition, John Wiley, 2005, ISBN: 20050471738484
- [6] Wikipedia: COBIT. Documentação online. Disponível na URL: http://pt.wikipedia.org/wiki/CobiT, acessado em 24 de Abril de 2012. 
- [7] Wikipedia: ITIL. Documentação online. Disponível na URL: http://pt.wikipedia.org/wiki/ITIL, acessado em 24 de Abril de 2012.
- [8] STAMDAGE, TOM. The Victorian Internet: The Remarkable Story of the Telegraph and the Nineteenth Century's On-Line Pioneers, Walker & Company; 1st edition (September 18, 2007), ISBN-13: 978-0802716040.
- [9] Estaơsticas do CERT.br – Disponível na URL: https://stats.cert.br/ e acessado em 15/08/2023
- Prof. Francisco DALADIER Marques JÚNIOR, PhD Instituto Federal de Educação, Ciência e Tecnologia da Paraíba (IFPB) - daladierjr@ifpb.edu.br


---

## Criptografia de Chave Simétrica

- Aula: 26/03/2026

### Tópicos

- [Criptografia de Chave Simétrica](#criptografia-de-chave-simétrica)
  - [Tópicos](#tópicos)



---



---

