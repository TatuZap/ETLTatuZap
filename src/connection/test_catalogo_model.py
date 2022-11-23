import unittest
import catalogo_model
import json

class TestCatalogoModel(unittest.TestCase):
  """
      Todos os casos de testes devem ser escritos como funções
      que começam com test.
  """

  def test_list_all(self):
    """
        O list_all após população deve retornar ao menos 1 elemento
    """
    catalogo_model.populate_database() # garante que o database foi populado
    all_classes = catalogo_model.list_all() # lista todos

    self.assertGreater(len(list(all_classes)), 0,"A lista deve ser não nula")

  def test_find_by_apelido(self):
    """
        O método find_by_apelido deve achar a disciplina com o apelido indicado
    """
    catalogo_model.populate_database() # garante que o database foi populado
    apelido = "bm"
    find_by_apelido = catalogo_model.find_by_apelido(apelido)

    self.assertEqual(list(find_by_apelido)[0]['disciplina'], 'Bases Matematicas', "Deveria ter achado a matéria pelo apelido")

  def test_find_by_sigla(self):
    """
        O método find_by_sigla deve achar a sigla com o apelido indicado
    """
    catalogo_model.populate_database() # garante que o database foi populado
    sigla = "BIS0003-15"
    find_by_sigla = catalogo_model.find_by_sigla(sigla)

    self.assertEqual(list(find_by_sigla)[0]['disciplina'], 'Bases Matematicas', "Deveria ter achado a matéria pela sigla")

  def test_insert_item_inserts(self):
    """
        A função de inserção de um único elemento não deve retornar erros.
    """
    disciplina = {
        "sigla": "Sigla teste",
        "disciplina": "Disciplina teste",
        "TPI": "TPI teste",
        "recomendacoes": "Recomendações teste",
        "objetivos": "Objetivos teste",
        "ementa":"Ementa teste",
        "apelido": "Apelido teste"
    }
    try:
        catalogo_model.insert_item(json.loads(json.dumps(disciplina)))
    except Exception as e:
        self.fail("A inserção não deve retornar Erro")

  def test_insert_item_find(self):
    """
        Um elemento inserido deve ser recuperável sem retornar erros.
    """
    disciplina = {
      "sigla": "Sigla teste",
      "disciplina": "Disciplina teste",
      "TPI": "TPI teste",
      "recomendacoes": "Recomendações teste",
      "objetivos": "Objetivos teste",
      "ementa":"Ementa teste",
      "apelido": "Apelido teste"
    }
    try:
      catalogo_model.insert_item(json.loads(json.dumps(disciplina)))
      catalogo_model.find_by_sigla(disciplina['sigla'])
      catalogo_model.find_by_apelido(disciplina['apelido'])
    except Exception as e:
      self.fail("Um elemento inserido deve ser recuperado sem erro")


  def test_insert_item_find_retrieve(self):
    """
        Um elemento inserido deve ser recuperado.
    """

    disciplina = {
      "sigla": "Sigla teste",
      "disciplina": "Disciplina teste",
      "TPI": "TPI teste",
      "recomendacoes": "Recomendações teste",
      "objetivos": "Objetivos teste",
      "ementa":"Ementa teste",
      "apelido": "Apelido teste"
    }

    catalogo_model.insert_item(json.loads(json.dumps(disciplina)))
    searched_class = catalogo_model.find_by_sigla(disciplina['sigla'])

    class_retrieved = list(searched_class)[0]
    del class_retrieved["_id"] # deleta o atributo "_id" que vem do banco de dados e não usamos para nada
    self.assertEqual(
      sorted(json.loads(json.dumps(class_retrieved)).items()),
      sorted(json.loads(json.dumps(disciplina)).items()),
      "O elemento inserido deve ser igual ao recuperado",
    )

  def test_insert_items_inserts(self):
    """
        A função de inserção de multiplos elementos não deve retornar erros.
    """
    disciplina_1 = {
      "sigla": "Sigla teste 1",
      "disciplina": "Disciplina teste 1",
      "TPI": "TPI teste 1",
      "recomendacoes": "Recomendações teste 1",
      "objetivos": "Objetivos teste 1",
      "ementa":"Ementa teste 1",
      "apelido": "Apelido teste 1"
    }
    disciplina_2 = {
      "sigla": "Sigla teste 2",
      "disciplina": "Disciplina teste 2",
      "TPI": "TPI teste 2",
      "recomendacoes": "Recomendações teste 2",
      "objetivos": "Objetivos teste 2",
      "ementa":"Ementa teste 2",
      "apelido": "Apelido teste 2"
    }

    disciplinas = [ json.loads(json.dumps(disciplina)) for disciplina in [disciplina_1, disciplina_2] ]

    try:
      catalogo_model.insert_items(disciplinas)
    except Exception as e:
      self.fail("A inserção de multiplos elementos não deve retornar Erro")

  def test_delete_all(self):
    """
        A função de delecao de todos os elementos deve deixar o banco vazio.
    """
    catalogo_model.delete_all()

    self.assertEqual(catalogo_model.find_all(), [], "Ao deletar tudo deve ficar vazio")

    catalogo_model.populate_database()
    return

  def test_populate_database(self):
    """
        A função de popular o banco deixar o banco com todos os elementos.
    """
    catalogo_model.delete_all()

    catalogo_model.populate_database()

    self.assertGreater(len(list(catalogo_model.list_all())), 0, "A lista deve ser não nula")
    return

if __name__ == '__main__':
  unittest.main()
