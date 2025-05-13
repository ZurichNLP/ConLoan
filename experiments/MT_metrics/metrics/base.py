from abc import ABC
from typing import List
from dataclasses import dataclass


@dataclass
class MetricOutput:
    scores: List[float]
    corpus_score: float


class Metric(ABC):
    def __init__(self, name):
        self.name = name

    def evaluate(self, src=None, mt=None, tgt=None, **kwargs) -> MetricOutput:
        raise NotImplementedError("Subclasses must implement the evaluate() method.")

    def __str__(self):
        return self.name


class NeuralMetric(Metric, ABC):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    @property
    def model(self):
        raise NotImplementedError("Subclasses must implement the model property.")

    @property
    def device(self):
        return self.model.device

    def evaluate(self, src=None, mt=None, tgt=None, **kwargs) -> MetricOutput:
        raise NotImplementedError("Subclasses must implement the evaluate() method.")

    def to(self, device):
        self.model.to(device)
        return self
