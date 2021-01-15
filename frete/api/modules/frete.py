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
        logger.info("Validando dimensões do produto.")
        tipos_validos = []
        cfg_dict = cls.cfg_frete

        if not peso <= 0:

            for key, value in cfg_dict.items():

                altura_valida = cfg_dict[key]['altura_min'] <= dimensao['altura'] <= cfg_dict[key]['altura_max']
                largura_valida = cfg_dict[key]['largura_min'] <= dimensao['largura'] <= cfg_dict[key]['largura_max']

                if altura_valida and largura_valida:
                    tipos_validos.append(key)

        logger.debug('Validação concluída.')
        return tipos_validos

    @classmethod
    def criar_lista_fretes(cls, body: dict) -> list:
        tipos_validos = cls.validar(**body)
        lista_fretes = []

        if tipos_validos:

            logger.info("Criando lista de fretes.")
            for tipo in tipos_validos:
                cte_frete = cls.cfg_frete[tipo]['cte_frete']
                frete = cte_frete * body['peso'] / 10

                cfg_dict = cls.cfg_frete
                dict_frete = {
                    'nome': cfg_dict[tipo]['nome'],
                    'valor_frete': frete,
                    'prazo_dias': cfg_dict[tipo]['prazo_dias']
                }

                lista_fretes.append(dict_frete)

            logger.success("Lista criada.")
        else:
            logger.success("Dimensões inválidas para os fretes atuais.")
        return lista_fretes
