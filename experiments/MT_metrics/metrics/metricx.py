import subprocess
import json
import os

from metrics.base import NeuralMetric
from metrics.base import MetricOutput


class MetricX24(NeuralMetric):
    def __init__(self, name: str, **kwargs):
        init_name = name.split("/")[1]
        super().__init__(init_name)
        self.model_name_or_path = kwargs.get("model_name_or_path", None)
        self.predict_path = kwargs.get("predict_path", None)
        self.tokenizer = kwargs.get("tokenizer", None)
        self.max_input_length = kwargs.get("max_input_length", 1536)
        self.input_file = kwargs.get("input_file", "input.jsonl")
        self.output_file = kwargs.get("output_file", None)
        self.batch_size = kwargs.get("batch_size", 16)
        self.qe = kwargs.get("qe", False)

    def evaluate(self, src=None, mt=None, tgt=None, **kwargs) -> MetricOutput:

        os.environ["PROTOCOL_BUFFERS_PYTHON_IMPLEMENTATION"] = "python"

        # first, arrange inputs in a jsonl input file that the bash script will take as input
        inputs = []
        if not self.qe:
            assert len(src) == len(mt) == len(tgt)
            for source, hypothesis, reference in zip(src, mt, tgt):
                inputs.append(
                    {"source": source, "hypothesis": hypothesis, "reference": reference}
                )
        else:
            assert len(src) == len(mt)
            for source, hypothesis in zip(src, mt):
                inputs.append({"source": source, "hypothesis": hypothesis})

        with open(self.input_file, "w") as f:
            for input in inputs:
                json.dump(input, f)
                f.write("\n")

        # run the bash script
        bash_command = f"python {self.predict_path} --tokenizer {self.tokenizer} --model_name_or_path {self.model_name_or_path} --max_input_length {self.max_input_length} --batch_size {self.batch_size} --input_file {self.input_file} --output_file {self.output_file}"
        if self.qe:
            bash_command += " --qe"

        process = subprocess.Popen(
            bash_command.split(),
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
        )

        stdout, stderr = process.communicate()
        print("Output: ", stdout)
        print("Error: ", stderr)

        # read the output file to collect scores
        # reverse each score to have negative values between -25 and 0
        with open(self.output_file, "r") as f:
            scores = [-json.loads(line)["prediction"] for line in f]

        return MetricOutput(scores=scores, corpus_score=sum(scores) / len(scores))
