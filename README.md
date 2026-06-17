#  Sistema de Recomendação de Filmes com Inteligência Artificial

Este projeto foi desenvolvido em Python com o objetivo de demonstrar conceitos básicos de Inteligência Artificial utilizando uma Árvore de Decisão.

O sistema permite que o usuário cadastre exemplos de pessoas informando suas preferências de consumo de filmes. A partir desses exemplos, o modelo é treinado para identificar padrões e prever o gênero favorito de novas pessoas.

##  Tecnologias Utilizadas

* Python 3
* Tkinter
* Scikit-Learn

##  Como a Inteligência Artificial Funciona

O sistema utiliza o algoritmo **DecisionTreeClassifier** da biblioteca Scikit-Learn.

Durante o treinamento, o usuário cadastra pessoas informando:

* Idade
* Quantidade de filmes assistidos por semana
* Se assiste filmes sozinho ou acompanhado
* Gênero favorito (Ação, Comédia ou Drama)

Como algoritmos de Machine Learning trabalham apenas com valores numéricos, algumas informações são convertidas para números:

| Informação  | Valor |
| ----------- | ----- |
| Sozinho     | 0     |
| Acompanhado | 1     |

Os gêneros favoritos são convertidos automaticamente para números utilizando a classe `LabelEncoder`.

Após o treinamento, a Árvore de Decisão analisa os padrões encontrados nos exemplos fornecidos e cria regras internas para realizar previsões.

Ao informar os dados de uma nova pessoa, o modelo percorre essas regras e retorna o gênero favorito mais provável.

##  Interface Gráfica

A interface foi desenvolvida utilizando a biblioteca Tkinter.

A aplicação possui duas etapas:

### Cadastro de dados para treinamento

O usuário informa os dados de várias pessoas e adiciona cada uma ao conjunto de treinamento.

### Teste da Inteligência Artificial

Após treinar o modelo, o usuário pode informar os dados de uma nova pessoa e solicitar uma previsão.

O resultado é exibido diretamente na janela da aplicação.

##  Como executar

Instale as dependências:

```bash
pip install scikit-learn
```

Execute o programa:

```bash
python filmes_ia.py
```

##  Observações

Este projeto possui finalidade educacional e utiliza um conjunto pequeno de exemplos para treinamento.

Quanto maior a quantidade de dados cadastrados, melhores tendem a ser as previsões realizadas pelo modelo.

##  Autor

Victor Manoel Brito, Marlon Reis, Erick Felipe
Acadêmico de Sistemas de Informação
