import os
import pickle
import pandas as pd
import torch
import torch.nn as nn
from torch.utils.data import Dataset, DataLoader
from sklearn.model_selection import train_test_split

# Device setup
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

# Create model folder if not exists
os.makedirs("model", exist_ok=True)

# Load Excel sheets
df = pd.read_excel("D:/22000810/Artificial Intelligence/AI_Hackathon/Backend/models/HindiNER.xlsx", sheet_name=0)
tag_map_df = pd.read_excel("D:/22000810/Artificial Intelligence/AI_Hackathon/Backend/models/HindiNER.xlsx", sheet_name=1, header=None)
tag_id_to_name = dict(tag_map_df.values.tolist())

# Preprocess
df.columns = ["id", "tokens", "ner_tags"]
df["tokens"] = df["tokens"].apply(lambda x: str(x).split())
df["ner_tags"] = df["ner_tags"].apply(lambda x: list(map(int, str(x).split())))

# Build vocab and tag mapping
all_words = set(word for row in df["tokens"] for word in row)
all_tags = set(tag for row in df["ner_tags"] for tag in row)

word2idx = {w: i + 2 for i, w in enumerate(sorted(all_words))}
word2idx["<PAD>"] = 0
word2idx["<UNK>"] = 1
tag2idx = {t: i for i, t in enumerate(sorted(all_tags))}
idx2tag = {i: t for t, i in tag2idx.items()}

# Dataset class
class NERDataset(Dataset):
    def __init__(self, tokens, tags):
        self.tokens = tokens
        self.tags = tags

    def __len__(self):
        return len(self.tokens)

    def __getitem__(self, idx):
        word_ids = [word2idx.get(w, word2idx["<UNK>"]) for w in self.tokens[idx]]
        tag_ids = self.tags[idx]
        return torch.tensor(word_ids), torch.tensor(tag_ids)

# Padding function
def pad_collate(batch):
    inputs, targets = zip(*batch)
    max_len = max(len(x) for x in inputs)
    padded_inputs = [torch.cat([x, torch.zeros(max_len - len(x), dtype=torch.long)]) for x in inputs]
    padded_targets = [torch.cat([y, torch.zeros(max_len - len(y), dtype=torch.long)]) for y in targets]
    return torch.stack(padded_inputs), torch.stack(padded_targets)

# Train/test split
X_train, X_test, y_train, y_test = train_test_split(df["tokens"], df["ner_tags"], test_size=0.1)
train_data = NERDataset(X_train.tolist(), y_train.tolist())
test_data = NERDataset(X_test.tolist(), y_test.tolist())
train_loader = DataLoader(train_data, batch_size=16, shuffle=True, collate_fn=pad_collate)
test_loader = DataLoader(test_data, batch_size=16, collate_fn=pad_collate)

# LSTM Model
class LSTM_NER(nn.Module):
    def __init__(self, vocab_size, tagset_size, embedding_dim=64, hidden_dim=128):
        super(LSTM_NER, self).__init__()
        self.embedding = nn.Embedding(vocab_size, embedding_dim, padding_idx=0)
        self.lstm = nn.LSTM(embedding_dim, hidden_dim, batch_first=True)
        self.fc = nn.Linear(hidden_dim, tagset_size)

    def forward(self, x):
        emb = self.embedding(x)
        out, _ = self.lstm(emb)
        logits = self.fc(out)
        return logits

# Initialize
model = LSTM_NER(len(word2idx), len(tag2idx)).to(device)
criterion = nn.CrossEntropyLoss(ignore_index=0)
optimizer = torch.optim.Adam(model.parameters(), lr=0.001)

# Train
for epoch in range(10):
    model.train()
    total_loss = 0
    for inputs, targets in train_loader:
        inputs, targets = inputs.to(device), targets.to(device)
        outputs = model(inputs)
        outputs = outputs.view(-1, outputs.shape[-1])
        targets = targets.view(-1)
        loss = criterion(outputs, targets)
        optimizer.zero_grad()
        loss.backward()
        optimizer.step()
        total_loss += loss.item()
    print(f"Epoch {epoch+1}, Loss: {total_loss:.4f}")

# Accuracy
def evaluate_accuracy(model, loader):
    model.eval()
    total, correct = 0, 0
    with torch.no_grad():
        for inputs, targets in loader:
            inputs, targets = inputs.to(device), targets.to(device)
            outputs = model(inputs)
            predictions = torch.argmax(outputs, dim=-1)
            mask = targets != 0
            correct += (predictions[mask] == targets[mask]).sum().item()
            total += mask.sum().item()
    print(f"Accuracy: {100 * correct / total:.2f}%")

evaluate_accuracy(model, test_loader)

# Save Model and Mappings
torch.save(model.state_dict(), "model/lstm_ner_model.pt")
with open("model/word2idx.pkl", "wb") as f:
    pickle.dump(word2idx, f)
with open("model/idx2tag.pkl", "wb") as f:
    pickle.dump(idx2tag, f)
with open("model/tag_id_to_name.pkl", "wb") as f:
    pickle.dump(tag_id_to_name, f)

print("✅ Model and mappings saved successfully!")