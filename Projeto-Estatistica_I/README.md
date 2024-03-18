# Módulo: Estatística I #

Oferecido por: 
 <i class="fas fa-laptop"></i> 📔 AdaTech e Ifood <i class="fas fa-laptop"></i> 📔


**Professores:**
<i class="fas fa-laptop"></i> 📔 Alex Lima <i class="fas fa-laptop"></i> 📔


**Participação**

⭐ O grupo é composto por 6 integrantes, trabalhamos via Git/GitHub e podemos ver a participação conforme a quantidade de commits realizadas no Projeto.


**Grupo 02**  

Composto por: <br>
⭐César Augusto<br>
⭐Eduardo Carvalho<br>
⭐Iago Mansur<br>
⭐Leonardo Henrrique<br>
⭐Myrna Martinelli<br>
⭐Ruan Faria<br>


⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐

<center><h3>Projeto Vem Ser Tech 2023 - <DS> Turma 1105<h3></center>

**Objetivo**

O principal objetivo deste trabalho é explorar e analisar os dados disponíveis, buscando extrair insights relevantes e fornecer uma compreensão mais aprofundada sobre diversos aspectos relacionados à atividade parlamentar na Câmara dos Deputados.<br>


**Representantes do Povo**

Os representantes do povo são os principais agentes da Câmara dos Deputados, atuando como autores de proposições, membros de órgãos, entre outras funções. A quantidade de votos recebidos nas eleições determina se eles serão titulares ou suplentes no exercício dos mandatos, que são as vagas que um partido obtém para cada legislatura. No conjunto de dados disponibilizado, cada deputado que exerceu mandato, mesmo que por um único dia, recebe um número identificador exclusivo.<br>


**Sobre o Projeto**

O projeto Dados Abertos tem como objetivo oferecer, pela internet, um conjunto cada vez mais amplo de dados públicos sobre a Câmara dos Deputados. Esses dados são disponibilizados em formatos padronizados que os tornam mais adequados ao processamento por softwares de diversos tipos. Com isso, cidadãos e entidades da sociedade civil podem acessar e utilizar esses dados para desenvolver aplicações inteligentes sobre a atuação dos parlamentares, as votações da Casa, os gastos reembolsados com dinheiro público, entre outros aspectos relacionados à atividade legislativa.<br>

**Sobre os Dados**

Os arquivos disponibilizados contém informações sobre a Despesa pela Cota para Exercício da Atividade Parlamentar, que abrange os gastos individuais de cada deputado desde o ano de 2008 até o ano atual, 2024. Esses dados são fundamentais para entender como os recursos públicos são utilizados pelos parlamentares no exercício de suas atividades.

<a href="https://dadosabertos.camara.leg.br/swagger/api.html#staticfile" class="btn" target="_blank">Link para a Fonte de Dados</a>


**txNomeParlamentar:** Nome adotado pelo parlamentar no início de seu mandato na legislatura. Pode incluir também o título identificador de uma liderança partidária.<br>
**ideCadastro:** Identificador numérico exclusivo de cada parlamentar da Câmara dos Deputados.<br>
**sgUF:** Sigla da unidade da federação (estados e Distrito Federal) pela qual o parlamentar foi eleito.<br>
**sgPartido:** Sigla do partido ao qual o parlamentar é ou era filiado.<br>
**codLegislatura:** Número identificador da legislatura na qual ocorreu a despesa.<br>
**numSubCota:** Código numérico de uma categoria de despesa à qual o registro seja pertinente.<br>
**txtDescricao:** Título da categoria de despesa à qual o registro é pertinente, correspondente ao campo numSubCota.<br>
**vlrDocumento:** Valor de face do documento comprobatório da despesa. Pode ser negativo em alguns tipos de despesas, como passagens aéreas, quando são emitidos bilhetes de compensação pela não-utilização de uma passagem.<br>
**vlrGlosa:** Valor retido, ou seja, não coberto pela CEAP (Cota para o Exercício da Atividade Parlamentar), por qualquer motivo (impedimento legal, insuficiência de comprovação, etc).<br>
**vlrLiquido:** Valor da despesa efetivamente debitado da Cota Parlamentar, correspondente ao vlrDocumento menos o vlrGlosa. Em despesas de Telefonia, por exemplo, pode ser registrado como 0, indicando que a despesa foi coberta pela franquia do contrato.<br>

<a href="https://dadosabertos.camara.leg.br/howtouse/2023-12-26-dados-ceap.html" class="btn" target="_blank">Informações adicionais sobre os campos podem ser encontradas aqui</a>
<br>

**Análises Realizadas**

**Análise Exploratória:** Exploramos os dados para entender sua estrutura, identificar padrões e tendências, além de investigar possíveis relações entre as variáveis.<br>
**Análise Estatística:** Aplicamos técnicas estatísticas para investigar distribuições, calcular medidas de centralidade e dispersão, realizar testes de hipóteses, entre outros.<br>


**Ferramentas Utilizadas**

**Linguagem de programação:** Python<br>
**Bibliotecas principais:** Pandas, Numpy, Matplotlib, Seaborn, Scipy e Sklearn<br>
**Ambiente de desenvolvimento:** Jupyter Notebook<br>


⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐

**Como Usar**

Para utilizar este projeto, siga estes passos:

Clone o repositório em seu ambiente local.<br>
Certifique-se de ter Python instalado.<br>
Execute os notebooks Jupyter correspondentes a cada análise para interagir com os dados.<br>


**Requisitos**

Python 3.x<br>
Bibliotecas principais: Pandas, Numpy, Matplotlib, Seaborn, Scipy, Sklearn, entre outras utilizadas nos notebooks.<br>


**Contribuições e Feedback**

Contribuições são bem-vindas! Se encontrar erros ou tiver sugestões para melhorar o projeto, fique à vontade para criar issues ou enviar pull requests.<br>


**Licença**

Este projeto é licenciado sob a Licença MIT - veja o arquivo LICENSE para mais detalhes.