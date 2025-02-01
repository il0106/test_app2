import requests
import pandas as pd
import apimoex

def get_moex_data(engine: str, 
                  market: str, 
                  board: str, 
                  seccode: str,
                  end: str = '2100-01-01 00:00:00',
                  start: str = '2000-01-01 00:00:00',
                  interval: int = 24
                  ):
    """
    Функция для получения данных с Московской биржи через API iss.moex.

    Параметры:
    -----------
    engine : str
        Движок торговой системы. Возможные значения:
        - "stock" : Акции, облигации.
        - "currency" : Валютный рынок.
        - "futures" : Фьючерсы.
        - "options" : Опционы.

    market : str
        Рынок внутри движка. Возможные значения для некоторых движков:
        - Движок "stock":
            - "shares" : Акции.
            - "bonds" : Облигации.
        - Движок "currency":
            - "selt" : Валютные сделки.
        - Движок "futures":
            - "forts" : Фьючерсы.
            - "options" : Опционы.

    board : str
        Торговая доска. Возможные значения зависят от рынка и движка:
        - Для акций (движок "stock", рынок "shares"):
            - "TQBR" : Основной рынок акций.
        - Для облигаций (движок "stock", рынок "bonds"):
            - "TQCB" : Основной рынок корпоративных облигаций.
        - Для фьючерсов (движок "futures", рынок "forts"):
            - "RFUD" : Основной рынок фьючерсов.

    seccode : str
        Security code ценной бумаги или фьючерса на MOEX.

    end : str
        Дата, до которой выводить данные.
        Формат: ГГГГ-ММ-ДД ЧЧ:ММ:СС.
        Default: 2037-12-31

    start : str
        Дата, начиная с которой необходимо начать выводить данные.
        Формат: ГГГГ-ММ-ДД ЧЧ:ММ:СС.

    interval : int
        Интервал графика.
        1 - 1 минута
        10 - 10 минут
        60 - 1 час
        24 - 1 день
        7 - 1 неделя
        31 - 1 месяц
        4 - 1 квартал
        Default: 24
    
    Возвращает:
    ----------
    pd.DataFrame
        Таблица с рыночными данными.

    Примечание:
    Для получения более подробной информации о доступных параметрах, обратитесь к документации Московской биржи:
    https://iss.moex.com/iss/reference/
    """

    url = f'https://iss.moex.com/iss/engines/{engine}/markets/{market}/boards/{board}/securities/{seccode}/candles.json'
    request_url = (url)
    arguments = {
        'from':start,
        'till':end,
        'interval':interval
    }
    with requests.Session() as session:
        iss = apimoex.ISSClient(session, request_url, arguments)
        data_raw = iss.get_all()
    
    if data_raw and len(data_raw) > 0:
        quotes = pd.DataFrame(data_raw['candles'])
        return quotes
    else:
        print(f"Ошибка при запросе данных (функция: get_moex_data, параметры: {[seccode,interval,start,end,board,market,engine]}): \n{data}")
        return None
    

def get_correlations(date):
    """
    Аргументы:
        date - дата в формате ГГГГ-ММ-ДД
    """

    url = 'https://iss.moex.com/iss/statistics/engines/stock/markets/shares/correlations.json'

    request_url = (url)
    arguments = {'date': date}
    with requests.Session() as session:
        iss = apimoex.ISSClient(session, request_url, arguments)
        data = iss.get_all()
    return pd.DataFrame(data['coefficients'])