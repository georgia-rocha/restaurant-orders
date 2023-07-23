# Boas-vindas ao Projeto Restaurant Orders! 🚀

 ## O que foi desenvolvido

Esta ferramenta foi desenvolvida para um Restaurante, com o objetivo de facilitar a criação de cardápios levando em consideração restrições alimentares e disponibilidade de ingredientes em estoque.

## Funcionalidades

- Geração automática de cardápios personalizados, considerando as preferências dos clientes e restrições alimentares.
- Gerenciamento eficiente de receitas e estoque de ingredientes.
- Consulta rápida para verificar disponibilidade de pratos e ingredientes.
- Adição, atualização e exclusão de pratos, receitas e ingredientes.
- Relatórios detalhados sobre o estoque de ingredientes para um controle preciso.

## Habilidades Exercitadas

- Prática do conceito de Hashmaps utilizando as estruturas de dados Dict e Set do Python.
- Utilização da ferramenta Pandas e sua estrutura de dados DataFrame.
- Testes de software para garantir a qualidade do código.
- Aplicação de conceitos de orientação a objetos.

<details><summary><strong>Para Clonar e Testar a Aplicação</strong></summary>
<br>

1. Para clonar a aplicação:

```
git clone git@github.com:georgia-rocha/restaurant-orders.git
```

2. Para entrar no diretório do projeto:
```
 cd restaurant-orders
```

3.  Para criar um ambiente virtual para o projeto:
```
python3 -m venv .venv && source .venv/bin/activate
```

4. Instale as dependências:
```
python3 -m pip install -r dev-requirements.txt
```

5. Executar os testes:
```
python3 -m pytest
```
O arquivo `pyproject.toml` já configura corretamente o pytest. Entretanto, caso você tenha problemas com isso e queira explicitamente uma saída completa, o comando é:

```bash
python3 -m pytest -s -vv
```

Caso precise executar apenas um arquivo de testes basta executar o comando:

```bash
python3 -m pytest tests/nome_do_arquivo.py
```

Caso precise executar apenas uma função de testes basta executar o comando:

```bash
python3 -m pytest -k nome_da_func_de_tests
```

Se desejar rodar os testes de um arquivo específico, execute com `-x nome_do_arquivo`

```bash
python -m pytest -x tests/test_jobs.py
```

Para executar um teste específico de um arquivo, basta executar o comando:

```bash
python -m pytest -x tests/nome_do_arquivo.py::test_nome_do_teste
```

Se quiser saber mais sobre a instalação de dependências com `pip`, veja esse [artigo](https://medium.com/python-pandemonium/better-python-dependency-and-package-management-b5d8ea29dff1).
</details>

## Requisitos 100%

- [x] 1 - Teste da classe Ingredient
- [x] 2 - Teste da classe Dish
- [x] 3 - Mapeando Pratos(Implementei a classe MenuData)
- [x] 4 - Gerando Cardápio(Implementei o método get_main_manu dentro da classe MenuBuilder)
- [x] 5 - Estoque de ingredientes(Implementei os métodos check_recipe_availability e consume_recipe dentro da classe InventoryMapping)
- [x] 6 - Cardápios baseados no estoque(Fiz um update no requisito 4, usando a classe InventoryMapping para ter acesso as informações de estoque)
