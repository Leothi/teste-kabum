from loguru import logger


class CalculadorFrete():
    cfg_frete = {
        'ninja': {
            'nome': 'Entrega Ninja',
            'cte_frete': 0.3,
            'altura_min': 10,
            'altura_max': 200,
            'largura_min': 6,
            'largura_max': 140,
            'prazo_dias': 6,
        },

        'kabum': {
            'nome': 'Entrega KaBuM',
            'cte_frete': 0.2,
            'altura_min': 5,
            'altura_max': 140,
            'largura_min': 13,
            'largura_max': 125,
            'prazo_dias': 4,
        },
    }

    @classmethod
    def validar(cls, dimensao: dict, peso: int) -> list:
        """Valida o produto através de suas características.

        :param dimensao: Dimensões do produto.
        :type dimensao: dict
        :param peso: Peso do produto.
        :type peso: int
        :return: Lista de fretes válidos para o produto.
        :rtype: list
        """
        logger.info("Validando dimensões do produto.")
        tipos_validos = []
        cfg_dict = cls.cfg_frete

        # Validação de peso
        if not peso <= 0:

            for key, value in cfg_dict.items():

                # Validação de altura e largura
                altura_valida = cfg_dict[key]['altura_min'] <= dimensao['altura'] <= cfg_dict[key]['altura_max']
                largura_valida = cfg_dict[key]['largura_min'] <= dimensao['largura'] <= cfg_dict[key]['largura_max']

                if altura_valida and largura_valida:
                    tipos_validos.append(key)

        logger.debug('Validação concluída.')
        return tipos_validos

    @classmethod
    def criar_lista_fretes(cls, body: dict) -> list:
        """Cria a lista de fretes disponíveis para o produto.

        :param body: Dicionário da requisição contendo informações do produto.
        :type body: dict
        :return: Lista de dicionários contendo os resultados dos cálculos de frete.
        :rtype: list
        """
        tipos_validos = cls.validar(**body)
        lista_fretes = []

        if tipos_validos:

            logger.info("Criando lista de fretes.")
            for tipo in tipos_validos:
                cfg_dict = cls.cfg_frete

                # Calculando frete
                cte_frete = cfg_dict[tipo]['cte_frete']
                frete = cte_frete * body['peso'] / 10

                # Dicionário final
                dict_frete = {
                    'nome': cfg_dict[tipo]['nome'],
                    'valor_frete': frete,
                    'prazo_dias': cfg_dict[tipo]['prazo_dias']
                }

                # Lista com os dicionários finais
                lista_fretes.append(dict_frete)

            logger.success("Lista criada.")
        else:
            logger.success("Dimensões inválidas para os fretes atuais.")
        return lista_fretes
