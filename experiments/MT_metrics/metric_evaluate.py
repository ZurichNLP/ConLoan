import argparse
from pathlib import Path
import json

from metrics.utils import MetricProvider
from metrics.base import MetricOutput

conloan_dir = Path(__file__).resolve().parents[2]

print(f"The root directory is {conloan_dir}")
datasets_dir = conloan_dir / "datasets"
assessments_dir = conloan_dir / "experiments" / "MT_metrics" / "assessments"


def load_data(filepath):
    with open(filepath, "r") as f:
        data = json.load(f)
    return data


def load_assessments(filepath):
    with open(filepath, "r") as f:
        assessments = json.load(f)
    return assessments


# I want to assess how reference-less metrics evaluate native alternatives compared to sentences containing loanwords.
# Therefore, I am reversing the order of source-translation, so that we consider as source the sentence
# in English, while the translation is the sentence in the annotated language.
def build_evaluation_sets(data, discard_identical=False):
    native_eval, loan_eval = [], []

    # native_eval contains the sentences where native alternatives have been replaced to loanwords
    # loan_eval contains the sentences with loanwords
    for item in data:
        
        if discard_identical and item["source_annotated_plain"] == item["source_plain"]:
            continue

        native_eval.append(
            {
                "src": item["target"],
                "mt": item["source_annotated_plain"],
            }
        )

        loan_eval.append(
            {
                "src": item["target"],
                "mt": item["source_plain"],
            }
        )

    return native_eval, loan_eval


def evaluate(args: argparse.Namespace) -> None:

    metric = None
    metric_name = args.metric.split("/")[1]

    for filepath in datasets_dir.glob("*.json"):
        print("Loading data from {}".format(filepath))
        data = load_data(filepath)
        native_eval, loan_eval = build_evaluation_sets(data, discard_identical=args.discard_identical_pairs)
        language = filepath.stem

        print(f"Language:{language}\tTotal: {len(data)}\tDiscarded: {len(data) - len(native_eval)}")

        language_assessments_dir = assessments_dir / language
        language_assessments_dir.mkdir(parents=True, exist_ok=True)
        language_metric_output = language_assessments_dir / f"{metric_name}.json" if not args.discard_identical_pairs else language_assessments_dir / f"{metric_name}-filtered.json"

        if language_metric_output.exists() and not args.override:
            metric_assessments = load_assessments(language_metric_output)
            native_evaluation: MetricOutput = MetricOutput(
                scores=metric_assessments["native_eval"],
                corpus_score=sum(metric_assessments["native_eval"])
                / len(metric_assessments["native_eval"]),
            )
            loan_evaluation: MetricOutput = MetricOutput(
                scores=metric_assessments["loan_eval"],
                corpus_score=sum(metric_assessments["loan_eval"])
                / len(metric_assessments["loan_eval"]),
            )

        else:

            if not metric:
                metric = MetricProvider.provide(
                    metric_name=args.metric,
                    model_name_or_path=args.metric,
                    batch_size=args.batch_size,
                    input_file=args.metricx_input_file,
                    output_file=args.metricx_output_file,
                    qe=args.qe_metricx,
                    tokenizer=args.metricx_tokenizer,
                    predict_path=args.metricx_predict_path,
                )

            native_evaluation: MetricOutput = metric.evaluate(
                src=[item["src"] for item in native_eval],
                mt=[item["mt"] for item in native_eval],
            )

            loan_evaluation: MetricOutput = metric.evaluate(
                src=[item["src"] for item in loan_eval],
                mt=[item["mt"] for item in loan_eval],
            )

            with open(language_metric_output, "w") as f:
                json.dump(
                    {
                        "native_eval": native_evaluation.scores,
                        "loan_eval": loan_evaluation.scores,
                    },
                    f,
                )

        print(
            f"Metric: {metric_name}\tLanguage: {language}\nNative evaluation: {native_evaluation.corpus_score}\nLoan evaluation: {loan_evaluation.corpus_score}\n"
        )


if __name__ == "__main__":

    parser = argparse.ArgumentParser()

    parser.add_argument(
        "--metric",
        type=str,
        help="Name of the metric to use for the evaluation",
        default=None,
        required=True,
    )

    parser.add_argument(
        "--batch-size",
        type=int,
        help="Batch size of the metric",
        default=8,
    )

    parser.add_argument(
        "--discard-identical-pairs",
        action="store_true",
        help="Whether to discard pairs where source and translation are identical",
    )

    parser.add_argument(
        "--metricx-input-file",
        type=str,
        help="Path to the input file to pass predictions to metricx",
        default="experiments/MT_metrics/metricx_tmp_data/input.jsonl",
    )

    parser.add_argument(
        "--metricx-output-file",
        type=str,
        help="Path to the output file to collect predictions from metricx",
        default="experiments/MT_metrics/metricx_tmp_data/output.jsonl",
    )

    parser.add_argument(
        "--metricx-tokenizer",
        type=str,
        help="Tokenizer used by metricx",
        default="google/mt5-xl",
    )

    parser.add_argument(
        "--qe-metricx",
        type=bool,
        help="If True, metricx will be used in QE mode",
        default=True,
    )

    parser.add_argument(
        "--metricx-predict-path",
        type=str,
        help="Path to predict.py for metricx",
        default="experiments/MT_metrics/metricx/metricx24/predict.py",
    )

    parser.add_argument(
        "--override",
        action="store_true",
        help="Whether to override existing predictions if they exist",
    )

    args = parser.parse_args()

    evaluate(args)
