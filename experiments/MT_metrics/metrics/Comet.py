import logging
from typing import List, Optional

from comet import download_model, load_from_checkpoint
import numpy as np

from metrics.base import NeuralMetric, MetricOutput


class Comet(NeuralMetric):

    def __init__(self, name: str, **kwargs):
        init_name = name.split("/")[1]
        super().__init__(init_name)
        model_path = download_model(name)
        self._model = load_from_checkpoint(model_path)
        self.batch_size = kwargs.get("batch_size", 32)
        self.set_device(kwargs.get("device", "cuda:0"))

    @property
    def model(self):
        return self._model

    def set_device(self, device: str):
        self._device = device
        self._model = self._model.to(device)
        self.comet_devices = [int(device.split(":")[-1])]

    def evaluate(
        self,
        src: Optional[List[str]] = None,
        mt: Optional[List[str]] = None,
        tgt: Optional[List[str]] = None,
        **kwargs,
    ) -> MetricOutput:

        if mt is None:
            raise ValueError("mt is None!")

        if src is None:
            logging.warning("src is None! Creating a list of empty strings!")
            src = [""] * len(mt)

        if tgt is None:
            assert len(src) == len(mt)
            print(f"tgt is None. {self.name} will work in a reference-less fashion.")
            inputs = [{"src": src[i], "mt": mt[i]} for i in range(len(mt))]
        else:
            assert len(src) == len(mt) == len(tgt)
            inputs = [
                {"src": src[i], "mt": mt[i], "ref": tgt[i]} for i in range(len(mt))
            ]

        output = self.model.predict(
            inputs,
            batch_size=self.batch_size,
            gpus=1,
            devices=self.comet_devices,
            progress_bar=True,
        )
        
        self._model.to(self._device)

        return MetricOutput(
            scores=output.scores, corpus_score=np.mean(output.scores).item()
        )
