# -*- coding: utf-8 -*-
import dataclasses
from dataclasses import dataclass
import datetime
from typing import Any


@dataclass
class Weather:
    """
    Датакласс содержит основную информацию о погоде:
    - Текущее время в населенном пункте, откуда идет запрос
    - Имя населенного пункта
    - Погода
    - Реальная температура воздуха
    - Ощущаемая температура воздуха
    - Скорость ветра
    """
    time: datetime.datetime
    place: str
    weather: str
    real_temperature: int
    feels_like_temperature: int
    wind_speed: int

    def to_dict(self):
        return dataclasses.asdict(self)
