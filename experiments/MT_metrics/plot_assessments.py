import argparse
from pathlib import Path
import json

import numpy as np
import matplotlib as mpl
from matplotlib import pyplot as plt

from metrics.base import MetricOutput

conloan_dir = Path(__file__).resolve().parents[2]

print(f"The root directory is {conloan_dir}")
datasets_dir = conloan_dir / "datasets"
assessments_dir = conloan_dir / "experiments" / "MT_metrics" / "assessments"
plots_dir = conloan_dir / "experiments" / "MT_metrics" / "plots"


metric2latex = {
    'wmt22-cometkiwi-da': 'CometKiwi',
    'wmt23-cometkiwi-da-xl': 'CometKiwi-XL',
    'metricx-24-hybrid-xl-v2p6': 'MetricX-24-XL',
    'XCOMET-XL': 'XCOMET-QE-XL'
}

def load_scores(metric_name: str, discard_identical=False):

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
    def build_evaluation_sets(data):
        native_eval, loan_eval = [], []

        # native_eval contains the sentences where native alternatives have been replaced to loanwords
        # loan_eval contains the sentences with loanwords
        for item in data:
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


    langs = [
        "Chinese",
        "French",
        "German",
        "Greek",
        "Icelandic",
        "Italian",
        "Northern-Kurdish",
        "Portuguese",
        "Russian",
        "Spanish",
    ]
    scores = {}
    for filepath in datasets_dir.glob("*.json"):

        language = filepath.stem
        language_assessments_dir = assessments_dir / language
        language_assessments_dir.mkdir(parents=True, exist_ok=True)
        language_metric_output = language_assessments_dir / f"{metric_name}.json" if not discard_identical else language_assessments_dir / f"{metric_name}-filtered.json"

        if language_metric_output.exists():
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
           raise ValueError(f"File {language_metric_output} does not exist.")

        scores[language] = {
            'native_eval': native_evaluation.corpus_score,
            'loan_eval': loan_evaluation.corpus_score
        }

    return scores


def plot_metric_assessments(metric: str, scores, discard_identical=False):
    languages = list(scores.keys())

    # Compute the differences
    differences = [scores[lang]['loan_eval'] - scores[lang]['native_eval'] for lang in languages]

    # Bar plot for differences
    fig, ax = plt.subplots(figsize=(12, 6))
    bars = ax.bar(languages, differences, color=['darkgreen' if diff >= 0 else 'darkred' for diff in differences])

    # Adding labels, title, and formatting
    #ax.set_xlabel('Languages')
    ax.set_ylabel('Score Difference: Original - Annotated')
    ax.set_title(f'{metric2latex[metric]}: Original vs Annotated')
    ax.axhline(0, color='black', linewidth=0.8, linestyle='--')  # Add a baseline at 0
    ax.set_xticks(range(len(languages)))
    ax.set_xticklabels(languages, rotation=45, ha="right")

    fig_path = plots_dir / f"{metric}" if not discard_identical else plots_dir / f"{metric}-filtered"

    # Display the plot
    plt.tight_layout()

    plt.savefig(fig_path.with_suffix('.png'))
    plt.savefig(fig_path.with_suffix('.pdf'))


def print_scores_per_language(scores):
    languages = scores['wmt22-cometkiwi-da'].keys()

    for lang in languages:
        print(f"{lang}:")
        for metric, metric_scores in scores.items():
            print(f"\t{metric2latex[metric]}: Annotated: {metric_scores[lang]['native_eval']:.2f}\tOriginal: {metric_scores[lang]['loan_eval']:.2f}")
        

def print_scores_differences(scores):
    languages = scores['wmt22-cometkiwi-da'].keys()

    for lang in languages:
        print(f"{lang}:")
        for metric, metric_scores in scores.items():
            print(f"\t{metric2latex[metric]}: {metric_scores[lang]['loan_eval'] - metric_scores[lang]['native_eval']:.2f}")


def plot_assessments(args):

    metrics = {
        'wmt22-cometkiwi-da',
        'wmt23-cometkiwi-da-xl',
        'metricx-24-hybrid-xl-v2p6',
        'XCOMET-XL'
    }

    scores = {}
    for metric in metrics:
        scores[metric] = load_scores(metric, discard_identical=args.discard_identical_pairs)
    
    print_scores_per_language(scores)
    print_scores_differences(scores)

    for metric, metric_scores in scores.items():
        plot_metric_assessments(metric, metric_scores, discard_identical=args.discard_identical_pairs)    


if __name__ == "__main__":
    parser = argparse.ArgumentParser()

    parser.add_argument(
        "--discard-identical-pairs",
        action="store_true",
        help="Whether to discard pairs where source and translation are identical",
    )

    args = parser.parse_args()
    plot_assessments(args)