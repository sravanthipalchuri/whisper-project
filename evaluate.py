import json

from jiwer import wer, Compose, ToLowerCase, RemovePunctuation, Strip

def evaluate(df):

    transform = Compose([
        ToLowerCase(),
        RemovePunctuation(),
        Strip()
    ])

    ground_truth = [
        transform(x)
        for x in df["Ground Truth"]
    ]

    predictions = [
        transform(x)
        for x in df["Prediction"]
    ]

    score = wer(ground_truth, predictions)

    metrics = {
        "model": "openai/whisper-small",
        "dataset": "LibriSpeech Dummy",
        "samples": len(df),
        "WER": score
    }

    with open("results/metrics.json","w") as f:
        json.dump(metrics,f,indent=4)

    with open("results/report.md","w") as f:

        f.write("# Whisper Evaluation Report\n\n")

        f.write(f"Model: openai/whisper-small\n\n")

        f.write(f"Dataset: LibriSpeech Dummy\n\n")

        f.write(f"Samples: {len(df)}\n\n")

        f.write(f"Word Error Rate: {score:.4f}\n")
