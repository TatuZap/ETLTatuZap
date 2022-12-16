from copy import deepcopy
import unittest
from src.turmas.turmas_model import find_codigos_turmas_by_ra, _get_collection_RA_TURMAS, find_materia_infos, populate_database, find_turmas_by_ra, insert_items_RA_TURMAS, insert_items_SALAS_HORARIOS, _get_collection_RA_TURMAS

class TestFretadoModel(unittest.TestCase):
    def test_insert_items_SALAS_HORARIOS_inserts(self):
        """
            A função de inserção de alguns elementos na tabela de SALAS_HORARIOS não deve retornar erros.
        """

        turmas_to_insert = [
            {
                'TURMA': 'CODIGO-TESTE-1',
                'Disciplina': 'Discilpina teste I',
                'teoria': 'segunda das 17:00 às 19:00, sala A1-S104-SB, semanal , quarta das 17:00 às 19:00, sala A1-S103-SB, semanal ',
                'prática': ' ',
                'TURNO': 'diurno'
            },
            {
                'TURMA': 'CODIGO-TESTE-2',
                'Disciplina': 'Discilpina teste II',
                'teoria': ' ',
                'prática': 'terça das 13:00 às 15:00, sala A2-S307-SB, semanal , sexta das 13:00 às 15:00, sala A2-S307-SB, semanal',
                'TURNO': 'noturno',
            }
        ]

        try:
            insert_items_SALAS_HORARIOS(turmas_to_insert)
        except Exception as e:
            self.fail("A inserção não deve retornar Erro")

    def test_insert_items_SALAS_HORARIOS_find(self):
        """
            Elementos inseridos na tabela de SALAS_HORARIOS devem ser recuperáveis sem retornar erros.
        """

        turmas_to_insert = [
            {
                'TURMA': 'CODIGO-TESTE-1',
                'Disciplina': 'Discilpina teste I',
                'teoria': 'segunda das 17:00 às 19:00, sala A1-S104-SB, semanal , quarta das 17:00 às 19:00, sala A1-S103-SB, semanal ',
                'prática': ' ',
                'TURNO': 'diurno'
            },
            {
                'TURMA': 'CODIGO-TESTE-2',
                'Disciplina': 'Discilpina teste II',
                'teoria': ' ',
                'prática': 'terça das 13:00 às 15:00, sala A2-S307-SB, semanal , sexta das 13:00 às 15:00, sala A2-S307-SB, semanal',
                'TURNO': 'noturno',
            }
        ]

        try:
            insert_items_SALAS_HORARIOS(turmas_to_insert)

            find_materia_infos(turmas_to_insert[0]["TURMA"])
            find_materia_infos(turmas_to_insert[1]["TURMA"])
        except Exception as e:
            self.fail("A inserção não deve retornar Erro")

    def test_insert_items_SALAS_HORARIOS_find_retrieve(self):
        """
            Elementos inseridos na tabela de SALAS_HORARIOS devem poder ser recuperados
        """

        turmas_to_insert = [
            {
                "TURMA": "CODIGO-TESTE-1",
                "Disciplina": "Discilpina teste I",
                "teoria": "segunda das 17:00 às 19:00, sala A1-S104-SB, semanal , quarta das 17:00 às 19:00, sala A1-S103-SB, semanal ",
                "prática": " ",
                "TURNO": "diurno"
            },
            {
                "TURMA": "CODIGO-TESTE-2",
                "Disciplina": "Discilpina teste II",
                "teoria": " ",
                "prática": "terça das 13:00 às 15:00, sala A2-S307-SB, semanal , sexta das 13:00 às 15:00, sala A2-S307-SB, semanal",
                "TURNO": "noturno",
            }
        ]

        turma_a = deepcopy(turmas_to_insert[0])
        turma_b = deepcopy(turmas_to_insert[1])

        insert_items_SALAS_HORARIOS(turmas_to_insert)

        turma_a_retrieved = find_materia_infos(turma_a["TURMA"])
        turma_b_retrieved = find_materia_infos(turma_b["TURMA"])

        del turma_a_retrieved['_id']
        del turma_b_retrieved['_id']

        self.assertEqual(
            sorted(turma_a.items()),
            sorted(turma_a_retrieved.items()),
            "O elemento turma_a inserido deve ser igual ao recuperado",
        )

        self.assertEqual(
            sorted(turma_b.items()),
            sorted(turma_b_retrieved.items()),
            "O elemento turma_b inserido deve ser igual ao recuperado",
        )

    def test_insert_items_RA_TURMAS_inserts(self):
        """
            A função de inserção de alguns elementos na tabela de RA_TURMAS não deve retornar erros.
        """

        turmas_to_insert = [
            { 'RA': 11202211111, 'TURMA': 'CODIGO-TESTE-1' },
            { 'RA': 11202222222, 'TURMA': 'CODIGO-TESTE-2' },
        ]

        try:
            insert_items_RA_TURMAS(turmas_to_insert)
        except Exception as e:
            self.fail("A inserção não deve retornar Erro")

    def test_insert_items_RA_TURMAS_find(self):
        """
            Elementos inseridos na tabela de RA_TURMAS devem ser recuperáveis sem retornar erros.
        """

        turmas_to_insert = [
            { 'RA': 11202211111, 'TURMA': 'CODIGO-TESTE-1' },
            { 'RA': 11202222222, 'TURMA': 'CODIGO-TESTE-2' },
        ]

        try:
            insert_items_RA_TURMAS(turmas_to_insert)

            _get_collection_RA_TURMAS().find_one({ 'TURMA': turmas_to_insert[0]["TURMA"] })
            _get_collection_RA_TURMAS().find_one({ 'TURMA': turmas_to_insert[1]["TURMA"] })
        except Exception as e:
            self.fail("A inserção não deve retornar Erro")

    def test_insert_items_RA_TURMAS_find_retrieve(self):
        """
            Elementos inseridos na tabela de RA_TURMAS devem poder ser recuperados
        """

        turmas_to_insert = [
            { 'RA': 11202211111, 'TURMA': 'CODIGO-TESTE-1' },
            { 'RA': 11202222222, 'TURMA': 'CODIGO-TESTE-2' },
        ]

        turma_a = deepcopy(turmas_to_insert[0])
        turma_b = deepcopy(turmas_to_insert[1])

        insert_items_RA_TURMAS(turmas_to_insert)

        turma_a_retrieved = _get_collection_RA_TURMAS().find_one({ 'TURMA': turmas_to_insert[0]["TURMA"] })
        turma_b_retrieved = _get_collection_RA_TURMAS().find_one({ 'TURMA': turmas_to_insert[1]["TURMA"] })

        del turma_a_retrieved['_id']
        del turma_b_retrieved['_id']

        self.assertEqual(
            sorted(turma_a.items()),
            sorted(turma_a_retrieved.items()),
            "O elemento turma_a inserido deve ser igual ao recuperado",
        )

        self.assertEqual(
            sorted(turma_b.items()),
            sorted(turma_b_retrieved.items()),
            "O elemento turma_b inserido deve ser igual ao recuperado",
        )

    def test_find_materia_infos(self):
        """
            Elementos inseridos na tabela de SALAS_HORARIOS devem poder ser recuperados pelo método find_materia_infos
        """

        turmas_to_insert = [
            {
                "TURMA": "CODIGO-TESTE-1",
                "Disciplina": "Discilpina teste I",
                "teoria": "segunda das 17:00 às 19:00, sala A1-S104-SB, semanal , quarta das 17:00 às 19:00, sala A1-S103-SB, semanal ",
                "prática": " ",
                "TURNO": "diurno"
            },
        ]

        turma = deepcopy(turmas_to_insert[0])

        insert_items_SALAS_HORARIOS(turmas_to_insert)

        turma_retrieved = find_materia_infos(turma["TURMA"])

        del turma_retrieved['_id']

        self.assertEqual(
            sorted(turma.items()),
            sorted(turma_retrieved.items()),
            "O elemento turma inserido deve ser igual ao recuperado",
        )

    def test_find_codigos_turmas_by_ra(self):
        """
            Deve ser possível achar elementos inseridos na tabela de RA_TURMAS correspondentes a um RA
        """

        """
            Elementos inseridos na tabela de RA_TURMAS devem poder ser recuperados
        """

        turmas_to_insert = [
            { 'RA': 123123123, 'TURMA': 'CODIGO-TESTE-1' },
            { 'RA': 123123123, 'TURMA': 'CODIGO-TESTE-2' },
        ]

        turma_a = deepcopy(turmas_to_insert[0])
        turma_b = deepcopy(turmas_to_insert[1])

        insert_items_RA_TURMAS(turmas_to_insert)

        turmas_retrieved = find_codigos_turmas_by_ra(123123123)

        del turmas_retrieved[0]['_id']
        del turmas_retrieved[1]['_id']

        self.assertEqual(
            [sorted(turma_a), sorted(turma_b)],
            [sorted(turmas_retrieved[0]), sorted(turmas_retrieved[1])],
            "Os codigos devem ser iguais aos inseridos para o aluno deste RA",
        )

    def test_find_turmas_by_ra(self):
        """
            OBS: TODO refatorar esse teste. Hoje ele depende do resultado de um quadrimestre especifico e que o banco esteja populado!

            Deve ser possível achar informações das turmas que estou matriculado
        """

        # populate_database()

        turmas_aluno = [
            {
                'Disciplina': 'Laboratório de Engenharia de Software',
                'horário_pratica': 'segunda das 10:00 às 12:00, sala 407-2, semanal , quarta das 08:00 às 10:00, sala 407-2, semanal ',
                'horário_teoria': ' ',
            },
            {
                'Disciplina': 'Programação Matemática',
                'horário_pratica': ' ',
                'horário_teoria': 'segunda das 08:00 às 10:00, sala S-301-2, semanal , quarta das 10:00 às 12:00, sala S-301-2, semanal '
            },
            {
                'Disciplina': 'Vida Artificial na Computação',
                'horário_pratica': ' ',
                'horário_teoria': 'sexta das 19:00 às 21:00, sala S-301-2, semanal ',
            }
        ]

        ra_aluno = '11201810247'

        retrieved_turmas = find_turmas_by_ra(ra_aluno)

        self.assertEqual(
            turmas_aluno,
            retrieved_turmas,
            "As turmas deste aluno devem ser iguais",
        )

if __name__ == '__main__':
    unittest.main()
