
# Value Investing BR

O projeto consiste em calcular um ranking de ações seguindo a filosofia de value investing. 

O value investing é uma estratégia de investimento de longo prazo que visa encontrar bons ativos que sejam intrinsecamente valiosos, mas estão sendo negociados abaixo do seu valor intrínseco. Em outras palavras, o **preço importa** e estamos em busca das ações mais descontadas.

Neste projeto foram implementados os métodos: 
1. Clube do Valor (Deep Value Investing) - [https://www.youtube.com/watch?v=ZyVOPdhQO_s](https://www.youtube.com/watch?v=ZyVOPdhQO_s)
2. A Fórmula Mágica de Joel Greenblatt - [https://www.youtube.com/watch?v=Kxv6OwWwS8g](https://www.youtube.com/watch?v=Kxv6OwWwS8g)
2. A Fórmula Mágica de Joel Greenblatt Modificada (baseado em P/L e ROE) - [https://www.youtube.com/watch?v=Kxv6OwWwS8g](https://www.youtube.com/watch?v=Kxv6OwWwS8g)
3. A Fórmula de Benjamin Grahan - [https://www.youtube.com/watch?v=HLfuMUTlRxA](https://www.youtube.com/watch?v=HLfuMUTlRxA)
4. Lobo Alfa - [https://www.youtube.com/watch?v=EpukfkCCIhQ&t=2445s](https://www.youtube.com/watch?v=EpukfkCCIhQ&t=2445s)
5. Décio Bazin - [https://www.youtube.com/watch?v=P5012s7sMio](https://www.youtube.com/watch?v=P5012s7sMio)
6. Descontadas (baseado em menor P/L e menor P/VP)

# Considerações
1. **ISSO NÃO É UMA RECOMENDAÇÃO DE INVESTIMENTO!  PROJETO FEITO APENAS PARA FINS DE ESTUDO.**
2. Este projeto é apenas um facilitador ao gerar os rankings de forma automática, a seleção dos ativos deverá ser **feita manualmente**.
3. O script não leva em consideração os diferentes tickers de uma mesma empresa, como ações ON, PN/PNB e Units (Ex: SANB3, SANB4 e SANB11).
Se um usuário quiser montar uma carteira com 20 ativos, por exemplo, no momento da escolha será preciso remover os tickers repetidos e empresas com não-recorrentes ou em recuperação judicial.
Para a eliminação de tickers repetidos, você pode optar por escolher aqueles com maior liquidez ou com maior Dividend Yield.

4. O método de Décio Bazin requer uma verificação complementar. Por ser uma estratégia focada em dividendos, recomenda-se olhar o dividendo médio pago pela empresa nos últimos 2, 3 ou 5 anos, e escolher aquelas que pagam pelo menos 6% ao ano.

5. Caso o arquivo utilizado for do site Fundamentus, não será gerado o ranking de Graham, pois na tabela deles não contém as colunas de VPA e LPA.

6. Por enquanto o projeto suporta apenas as tabelas geradas na busca avançada do Status Invest e Fundamentus.

7. Para uma escolha mais segura, recomenda-se usar alguns filtros no momento da busca, por exemplo:

## Pré-requisitos
- Python 3.8+ **(obrigatório)**
- Pip3 **(obrigatório)**
- Git **(obrigatório)**
- Poetry (opcional)

## Instalação
1. Abra o terminal e clone o repositório:
```bash
git clone https://github.com/georgenv/value-investing-br.git
```

2. Acesse a pasta do projeto:
```bash
cd value-investing-br
```

3. Crie um ambiente virtual e o ative:
```bash
python3 -m venv env
source env/bin/activate
```

4. Instale as dependências do projeto:
```bash
poetry install
```
Caso não tenha o poetry instalado, execute:
```bash
pip3 install pandas openpyxl
```

## Execução

1. Após aplicar os filtros de sua escolha na área de busca avançada do Status Invest ou Fundamentus, salve o resultado numa planilha ou baixe o csv.

2. Execute o projeto a partir do `main.py` informando o caminho do arquivo e o nome do site de onde foi baixado:
```bash
python3 main.py -f "caminho_do_arquivo.xlsx" -s "fundamentus"
```
Alternativamente:
```bash
python3 main.py --file "caminho_do_arquivo.csv" --source "status_invest"
```

3. Os arquivos resultado da execução do script estarão na pasta `result`, localizada na raíz do projeto.

## Licença
Apache 2.0