from src.inference import run_inference
from src.evaluate import evaluate

print("Running inference...")

df = run_inference()

print("Calculating WER...")

evaluate(df)

print("Done!")

print("Results saved in results/")
