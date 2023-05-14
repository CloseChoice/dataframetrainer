from abc import ABC, abstractmethod
import pandas as pd

class BaseChallenge(ABC):

    @staticmethod
    @abstractmethod
    def initial() -> pd.DataFrame | pd.Series:
        pass

    @staticmethod
    @abstractmethod
    def transform(df: pd.DataFrame) -> pd.DataFrame | pd.Series:
        pass