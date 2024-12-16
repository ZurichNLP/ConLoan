from metrics.Comet import Comet
from metrics.bleu import Bleu
from metrics.base import Metric
from metrics.length import Length
from metrics.metricx import MetricX24


class MetricProvider:

    bleu = "bleu"
    wmt22_comet_da = "Unbabel/wmt22-comet-da"
    xcometxl = "Unbabel/XCOMET-XL"
    cometkiwi = "Unbabel/wmt22-cometkiwi-da"
    cometkiwixl = "Unbabel/wmt23-cometkiwi-da-xl"
    metricx24large = "google/metricx-24-hybrid-large-v2p6"
    metricx24xl = "google/metricx-24-hybrid-xl-v2p6"
    metricx24xxl = "google/metricx-24-hybrid-xxl-v2p6"

    @classmethod
    def provide(cls, metric_name: str, **kwargs) -> Metric:
        if metric_name == cls.bleu:
            tgt_lang = kwargs.get("tgt_lang", None)

            if tgt_lang == "zh":
                metric = Bleu(tokenize="zh")
            else:
                metric = Bleu()

            return metric
        elif metric_name in {
            cls.wmt22_comet_da,
            cls.cometkiwi,
            cls.cometkiwixl,
            cls.xcometxl,
        }:
            return Comet(metric_name, **kwargs)
        elif metric_name in {cls.metricx24large, cls.metricx24xl, cls.metricx24xxl}:
            return MetricX24(metric_name, **kwargs)
        elif metric_name == cls.length:
            return Length()

        raise ValueError(f"Unknown metric: {metric_name}")
