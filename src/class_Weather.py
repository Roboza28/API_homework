# -*- coding: utf-8 -*-
from dataclasses import dataclass
import datetime


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

    def info_to_dict(self):
        report = {'Текущее время': self.time,
                  'Название города': self.place,
                  'Погодные условия': self.weather,
                  'Текущая температура': self.real_temperature,
                  'Ощущается как': self.feels_like_temperature,
                  'Скорость ветра': self.wind_speed}
        return report

    # def __str__(self) -> str:
    #     """
    #     Генерирует отчет для пользователя о погоде,
    #     основываясь на записанных в поля сведениях
    #     """
    #
    #     report = f"Текущее время: {self.time}\n" \
    #              f"Название города: {self.place}\n" \
    #              f"Погодные условия: {self.weather}\n" \
    #              f"Текущая температура: {self.real_temperature} градусов по цельсию\n" \
    #              f"Ощущается как: {self.feels_like_temperature} градусов по цельсию\n" \
    #              f"Скорость ветра: {self.wind_speed} м/c"
    #     return report

    # def to_dict(self):
    #     return dataclasses.asdict(self)
