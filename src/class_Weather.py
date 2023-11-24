# -*- coding: utf-8 -*-
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

    def info_to_dict(self) -> dict[str, Any]:
        """
        Метод позволяющий перевести пользвательский тип данных Weather в словарь
        Returns:
            dict c информацией о погоде
        """
        report = {'Текущее время': self.time,
                  'Название города': self.place,
                  'Погодные условия': self.weather,
                  'Текущая температура': self.real_temperature,
                  'Ощущается как': self.feels_like_temperature,
                  'Скорость ветра': self.wind_speed}
        return report
