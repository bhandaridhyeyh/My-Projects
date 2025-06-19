# Backend/models/predict_wrapper.py

import sys
import io
import torch
import pickle
from model_def import LSTM_NER  # Make sure this exists and is correct

# Fix encoding issue
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

# Setup device
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

# Load mappings
base_path = "D:/22000810/Artificial Intelligence/AI_Hackathon/Backend/models/model/"
with open(base_path + "word2idx.pkl", "rb") as f:
    word2idx = pickle.load(f)
with open(base_path + "idx2tag.pkl", "rb") as f:
    idx2tag = pickle.load(f)
with open(base_path + "tag_id_to_name.pkl", "rb") as f:
    tag_id_to_name = pickle.load(f)

# Load model
model = LSTM_NER(len(word2idx), len(idx2tag))
model.load_state_dict(torch.load(base_path + "lstm_ner_model.pt", map_location=device))
model.to(device)
model.eval()

# Prediction function
def predict(sentence):
    words = sentence.strip().split()
    ids = torch.tensor([[word2idx.get(w, word2idx["<UNK>"]) for w in words]]).to(device)

    with torch.no_grad():
        logits = model(ids)
        preds = torch.argmax(logits, dim=-1).cpu().numpy()[0]

    # Join tagged entities in desired format
    tagged = [f"{w} ({tag_id_to_name.get(idx2tag.get(p, -1), 'UNKNOWN')})" for w, p in zip(words, preds)]
    return " ".join(tagged)

# For command-line testing
if __name__ == "__main__":
    sentence = sys.argv[1]
    print(predict(sentence))
