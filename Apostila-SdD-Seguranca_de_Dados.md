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

> **Última sincronização:** 21/03/2026 18:40:05

## Sumário de Aulas

- Aula 01 - [Apresentação da Disciplina](#apresentação-da-disciplina)
- Aula 02 - [Contextualização a Segurança da Informação](#contextualização-a-segurança-da-informação)

---

## Apresentação da Disciplina

- Arquivo da [aula 01](https://drive.google.com/file/d/18R47Vy-GQOJOcG-okRzwtu3C6v52VZQm/view?usp=sharing).
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

## Critérios de Avaliação

&emsp; Quatro avaliações:

- 2 provas subjetivas(s)/objetiva(s)
- 1 prática
- 1 seminário com apresentação de artigos científicos


---

## Contextualização a Segurança da Informação

- Arquivo da [aula 02](https://drive.google.com/file/d/1u6l8_qFh2uO7lvJyLswK4qXnUlaxKX_q/view?usp=sharing).
- Data de Postagem: 12/03/2026

### Sumário

- [Contextualização a Segurança da Informação](#contextualização-a-segurança-da-informação)
  - [Sumário](#sumário)
  - [Problematização](#problematização)
  - [Evolução da Segurança da Informação](#evolução-da-segurança-da-informação)
  - [Pilares da Segurança](#pilares-da-segurança)

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

### Pilares da Segurança

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


---

