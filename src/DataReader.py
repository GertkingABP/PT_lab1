# -*- coding: utf-8 -*-
from Types import DataType
from abc import ABC, abstractmethod


class DataReader(ABC):
    def __init__(self, file_path):
        self.file_path = file_path

    @abstractmethod
    def read(self) -> DataType:
        pass
