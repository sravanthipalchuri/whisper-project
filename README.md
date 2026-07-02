# Whisper Speech Recognition using Hugging Face

## Project Overview

This project demonstrates how to use OpenAI's Whisper model from Hugging Face for Automatic Speech Recognition (ASR). The model converts speech audio into text and is evaluated using the Word Error Rate (WER) metric.

---

## Objectives

- Download a pretrained Whisper model from Hugging Face.
- Download the corresponding processor/tokenizer.
- Load a public speech dataset.
- Perform speech-to-text inference on 20 audio samples.
- Save the predicted transcriptions to a CSV file.
- Evaluate the model using Word Error Rate (WER).

---

## Model Used

- **Model:** `openai/whisper-small`
- **Framework:** Hugging Face Transformers
- **Task:** Automatic Speech Recognition (ASR)

---

## Dataset Used

- **Dataset:** LibriSpeech ASR
- **Samples Used:** 20
- **Source:** Hugging Face Datasets

---

## Technologies Used

- Python
- Google Colab
- Hugging Face Transformers
- Hugging Face Datasets
- PyTorch
- Pandas
- JiWER

---

## Project Structure

```
Whisper_Project/
│
├── Whisper_Project.ipynb
├── predictions.csv
├── README.md
├── requirements.txt
└── documentation.pdf
```

---

## Installation

Install the required libraries:

```bash
pip install transformers datasets torch librosa soundfile jiwer accelerate pandas
```

---

## Steps Performed

1. Loaded the pretrained Whisper model.
2. Loaded the Whisper processor.
3. Loaded the LibriSpeech dataset.
4. Performed inference on 20 speech samples.
5. Stored predictions in a CSV file.
6. Calculated the Word Error Rate (WER).

---

## Evaluation Metric

Word Error Rate (WER) was used to evaluate the model.

**Formula:**

```
WER = (Substitutions + Deletions + Insertions) / Total Words
```

---

## Results

| Metric | Value |
|---------|------:|
| Number of Samples | 20 |
| Model | Whisper Small |
| Overall WER | **0.0227 (2.27%)** |

The Whisper model achieved a **Word Error Rate (WER) of 2.27%**, indicating excellent transcription performance on the selected speech samples.

---

## Output

The generated predictions are saved in:

```
predictions.csv
```

Example:

| Ground Truth | Prediction |
|--------------|------------|
| CONCORD RETURNED TO ITS PLACE AMIDST THE TENTS | Concord returned to its place amidst the tents. |

---

## Future Improvements

- Evaluate on larger datasets.
- Compare Whisper with Wav2Vec2 and HuBERT.
- Test multilingual speech recognition.
- Deploy the model using Flask or FastAPI.

---

## References

1. OpenAI Whisper Research Paper
2. Hugging Face Transformers Documentation
3. Hugging Face Datasets Documentation
4. JiWER Documentation

---

## Author

**Name:** Khyathi Charitha Potnuru

**Project:** Whisper Speech Recognition using Hugging Face

