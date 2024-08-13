import pandas as pd

from quartz_solar_forecast.inverters.inverter import AbstractInverter


class MockInverter(AbstractInverter):

    def get_data(self, ts: pd.Timestamp) -> pd.DataFrame:
        return pd.DataFrame(columns=['timestamp', 'power_kw'])