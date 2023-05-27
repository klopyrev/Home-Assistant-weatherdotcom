from __future__ import annotations

from dataclasses import dataclass
from typing import Callable, Any, cast

from .const import (
    FIELD_CONDITION_HUMIDITY,
    FIELD_CONDITION_PRESSURE,
    FIELD_CONDITION_TEMP,
    FIELD_CONDITION_WINDDIR,
    FIELD_CONDITION_WINDGUST,
    FIELD_CONDITION_WINDSPEED,
    FIELD_FORECAST_WINDDIRECTIONCARDINAL,
    ICON_THERMOMETER,
    ICON_UMBRELLA,
    ICON_WIND
)
from homeassistant.components.sensor import SensorEntityDescription, SensorDeviceClass, SensorStateClass
from homeassistant.const import PERCENTAGE, UnitOfIrradiance, UV_INDEX, DEGREE, UnitOfLength, UnitOfTemperature, \
    UnitOfVolumetricFlux, UnitOfPressure, UnitOfSpeed
from homeassistant.helpers.typing import StateType


@dataclass
class WeatherRequiredKeysMixin:
    """Mixin for required keys."""
    value_fn: Callable[[dict[str, Any], str], StateType]
    feature: str


@dataclass
class WeatherSensorEntityDescription(
    SensorEntityDescription, WeatherRequiredKeysMixin
):
    attr_fn: Callable[[dict[str, Any]], dict[str, StateType]] = lambda _: {}
    unit_fn: Callable[[bool], str | None] = lambda _: None
    """Describes Weather.com Sensor entity."""


current_condition_sensor_descriptions = [
    WeatherSensorEntityDescription(
        key="validTimeLocal",
        name="Local Observation Time",
        icon="mdi:clock",
        value_fn=lambda data, _: cast(str, data),
    ),
    WeatherSensorEntityDescription(
        key=FIELD_CONDITION_HUMIDITY,
        name="Relative Humidity",
        icon="mdi:water-percent",
        device_class=SensorDeviceClass.HUMIDITY,
        state_class=SensorStateClass.MEASUREMENT,
        unit_fn=lambda _: PERCENTAGE,
        value_fn=lambda data, _: cast(int, data) or 0,
    ),
    WeatherSensorEntityDescription(
        key="uvIndex",
        name="UV Index",
        icon="mdi:sunglasses",
        state_class=SensorStateClass.MEASUREMENT,
        unit_fn=lambda _: UV_INDEX,
        value_fn=lambda data, _: cast(int, data) or 0,
    ),
    WeatherSensorEntityDescription(
        key=FIELD_CONDITION_WINDDIR,
        name="Wind Direction - Degrees",
        icon=ICON_WIND,
        state_class=SensorStateClass.MEASUREMENT,
        unit_fn=lambda _: DEGREE,
        value_fn=lambda data, _: cast(int, data) or 0,
    ),
    WeatherSensorEntityDescription(
        key=FIELD_FORECAST_WINDDIRECTIONCARDINAL,
        name="Wind Direction - Cardinal",
        icon=ICON_WIND,
        unit_fn=lambda _: None,
        value_fn=lambda data, _: cast(str, data) or "",
    ),
    WeatherSensorEntityDescription(
        key="temperatureDewPoint",
        name="Dewpoint",
        icon="mdi:water",
        state_class=SensorStateClass.MEASUREMENT,
        device_class=SensorDeviceClass.TEMPERATURE,
        unit_fn=lambda metric: UnitOfTemperature.CELSIUS if metric else UnitOfTemperature.FAHRENHEIT,
        value_fn=lambda data, _: cast(float, data),
    ),
    WeatherSensorEntityDescription(
        key="temperatureFeelsLike",
        name="Temperature - Feels Like",
        icon=ICON_THERMOMETER,
        state_class=SensorStateClass.MEASUREMENT,
        device_class=SensorDeviceClass.TEMPERATURE,
        unit_fn=lambda metric: UnitOfTemperature.CELSIUS if metric else UnitOfTemperature.FAHRENHEIT,
        value_fn=lambda data, _: cast(float, data),
    ),
    WeatherSensorEntityDescription(
        key=FIELD_CONDITION_TEMP,
        name="Temperature",
        icon=ICON_THERMOMETER,
        state_class=SensorStateClass.MEASUREMENT,
        device_class=SensorDeviceClass.TEMPERATURE,
        unit_fn=lambda metric: UnitOfTemperature.CELSIUS if metric else UnitOfTemperature.FAHRENHEIT,
        value_fn=lambda data, _: cast(float, data),
    ),
    WeatherSensorEntityDescription(
        key="temperatureHeatIndex",
        name="Heat Index",
        icon=ICON_THERMOMETER,
        state_class=SensorStateClass.MEASUREMENT,
        device_class=SensorDeviceClass.TEMPERATURE,
        unit_fn=lambda metric: UnitOfTemperature.CELSIUS if metric else UnitOfTemperature.FAHRENHEIT,
        value_fn=lambda data, _: cast(float, data),
    ),
    WeatherSensorEntityDescription(
        key="temperatureWindChill",
        name="Wind Chill",
        icon=ICON_THERMOMETER,
        state_class=SensorStateClass.MEASUREMENT,
        device_class=SensorDeviceClass.TEMPERATURE,
        unit_fn=lambda metric: UnitOfTemperature.CELSIUS if metric else UnitOfTemperature.FAHRENHEIT,
        value_fn=lambda data, _: cast(float, data),
    ),
    WeatherSensorEntityDescription(
        key="precip1Hour",
        name="Precipitation - Last hour",
        icon=ICON_UMBRELLA,
        state_class=SensorStateClass.TOTAL_INCREASING,
        device_class=SensorDeviceClass.PRECIPITATION,
        unit_fn=lambda metric: UnitOfLength.MILLIMETERS if metric else UnitOfLength.INCHES,
        value_fn=lambda data, _: cast(float, data),
    ),
    WeatherSensorEntityDescription(
        key="precip6Hour",
        name="Precipitation - Last 6 hours",
        icon=ICON_UMBRELLA,
        state_class=SensorStateClass.TOTAL_INCREASING,
        device_class=SensorDeviceClass.PRECIPITATION,
        unit_fn=lambda metric: UnitOfLength.MILLIMETERS if metric else UnitOfLength.INCHES,
        value_fn=lambda data, _: cast(float, data),
    ),
    WeatherSensorEntityDescription(
        key="precip24Hour",
        name="Precipitation - Last 24 hours",
        icon=ICON_UMBRELLA,
        state_class=SensorStateClass.TOTAL_INCREASING,
        device_class=SensorDeviceClass.PRECIPITATION,
        unit_fn=lambda metric: UnitOfLength.MILLIMETERS if metric else UnitOfLength.INCHES,
        value_fn=lambda data, _: cast(float, data),
    ),
    WeatherSensorEntityDescription(
        key=FIELD_CONDITION_PRESSURE,
        name="Pressure",
        icon="mdi:gauge",
        state_class=SensorStateClass.MEASUREMENT,
        device_class=SensorDeviceClass.PRESSURE,
        unit_fn=lambda metric: UnitOfPressure.MBAR if metric else UnitOfPressure.INHG,
        value_fn=lambda data, _: cast(float, data),
    ),
    WeatherSensorEntityDescription(
        key=FIELD_CONDITION_WINDGUST,
        name="Wind Gust",
        icon=ICON_WIND,
        state_class=SensorStateClass.MEASUREMENT,
        device_class=SensorDeviceClass.WIND_SPEED,
        unit_fn=lambda metric: UnitOfSpeed.KILOMETERS_PER_HOUR if metric else UnitOfSpeed.MILES_PER_HOUR,
        value_fn=lambda data, _: cast(float, data),
    ),
    WeatherSensorEntityDescription(
        key=FIELD_CONDITION_WINDSPEED,
        name="Wind Speed",
        icon=ICON_WIND,
        state_class=SensorStateClass.MEASUREMENT,
        device_class=SensorDeviceClass.WIND_SPEED,
        unit_fn=lambda metric: UnitOfSpeed.KILOMETERS_PER_HOUR if metric else UnitOfSpeed.MILES_PER_HOUR,
        value_fn=lambda data, _: cast(float, data),
    ),
]
