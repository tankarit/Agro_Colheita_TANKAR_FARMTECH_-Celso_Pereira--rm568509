CorteCerto – Controle de Perdas na Colheita de Cana-de-Açúcar
1. Introdução

O agronegócio é um dos pilares da economia brasileira, sendo responsável pela geração de empregos, exportações e abastecimento alimentar. Dentro desse contexto, a colheita da cana-de-açúcar é uma das atividades mais relevantes, mas também uma das que mais sofrem com perdas de produtividade, especialmente devido à mecanização.

De acordo com estudos da SOCICANA, as perdas mecânicas podem chegar a 15% da produção, representando prejuízos significativos ao setor. O projeto CorteCerto foi desenvolvido com o objetivo de oferecer uma solução simples e acessível para monitorar, registrar e analisar as perdas de colheita, apoiando o produtor rural na tomada de decisões.

2. Objetivo do Projeto

O sistema CorteCerto tem como propósito permitir o registro, acompanhamento e análise de perdas na colheita de cana-de-açúcar, utilizando Python como ferramenta principal.
Ele foi desenvolvido com foco em atender os conteúdos abordados nos capítulos 3, 4, 5 e 6 da disciplina, contemplando:

Funções e procedimentos com passagem de parâmetros (subalgoritmos);

Estruturas de dados (listas, tuplas, dicionários e tabela em memória);

Manipulação de arquivos (formato texto e JSON);

Conexão com banco de dados Oracle (opcional).

3. Descrição Geral do Sistema

O CorteCerto é uma aplicação de linha de comando (CLI) que permite:

Cadastrar operações de colheita com data, talhão, equipe, colhedora e perda estimada (%);

Armazenar as informações localmente em um arquivo JSON;

Calcular indicadores (KPIs) médios de perda por talhão, equipe e colhedora;

Gerar relatórios em formato TXT, contendo ranking e recomendações de boas práticas;

(Opcional) Enviar os registros para uma tabela em banco de dados Oracle, utilizando a biblioteca cx_Oracle.
