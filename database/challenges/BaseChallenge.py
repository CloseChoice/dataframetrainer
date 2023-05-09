from abc import ABC, abstractmethod
import pandas as pd

class BaseChallenge(ABC):

    @staticmethod
    @abstractmethod
    def initial():
        pass

    @staticmethod
    @abstractmethod
    def transform(df: pd.DataFrame) -> pd.DataFrame:
        pass