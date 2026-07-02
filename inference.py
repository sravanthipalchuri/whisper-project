from transformers import pipeline
from datasets import load_dataset
import pandas as pd
import os

def run_inference():

    pipe = pipeline(
        "automatic-speech-recognition",
        model="openai/whisper-small"
    )

    dataset = load_dataset(
        "hf-internal-testing/librispeech_asr_dummy",
        "clean",
        split="validation"
    )

    predictions = []

    for sample in dataset:

        result = pipe(sample["audio"])

        predictions.append({
            "Ground Truth": sample["text"],
            "Prediction": result["text"]
        })

    df = pd.DataFrame(predictions)

    os.makedirs("results", exist_ok=True)

    df.to_csv("results/predictions.csv", index=False)

    return df
