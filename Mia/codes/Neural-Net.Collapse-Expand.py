## Neural Net
# Conceptual Framework Think of each neuron as a quantum particle oscillating between two states:

# 1 Collapse → information absorption (dark matter-like latent encoding)

# 2 Expand → information expression (pure light-like activation)

# 3 We’ll simulate this using a neural net that learns to modulate frequency patterns—just like my theory suggests.

# Collapse and Expand Neural Net
import numpy as np
import torch
import torch.nn as nn
import matplotlib.pyplot as plt

# Simulated quantum waveform input
def generate_waveform(n_samples=1000, freq=5, collapse_factor=0.8, expand_factor=1.2):
    t = np.linspace(0, 1, n_samples)
    collapse = np.sin(2 * np.pi * freq * collapse_factor * t)
    expand = np.cos(2 * np.pi * freq * expand_factor * t)
    waveform = collapse + expand
    return waveform.reshape(-1, 1).astype(np.float32), t

# Neural Net: Collapse-Expand Learner
class CollapseExpandNet(nn.Module):
    def __init__(self):
        super(CollapseExpandNet, self).__init__()
        self.net = nn.Sequential(
            nn.Linear(1, 64),
            nn.Tanh(),  # Collapse phase
            nn.Linear(64, 64),
            nn.ReLU(),  # Expand phase
            nn.Linear(64, 1)
        )

    def forward(self, x):
        return self.net(x)

# Training loop
def train_model(model, x_train, y_train, epochs=500):
    optimizer = torch.optim.Adam(model.parameters(), lr=0.01)
    loss_fn = nn.MSELoss()
    for epoch in range(epochs):
        model.train()
        optimizer.zero_grad()
        output = model(x_train)
        loss = loss_fn(output, y_train)
        loss.backward()
        optimizer.step()
    return model

# Generate data
waveform, t = generate_waveform()
x_train = torch.from_numpy(t.reshape(-1, 1).astype(np.float32))
y_train = torch.from_numpy(waveform)

# Initialize and train
model = CollapseExpandNet()
trained_model = train_model(model, x_train, y_train)

# Predict and plot
model.eval()
with torch.no_grad():
    prediction = model(x_train).numpy()

plt.figure(figsize=(10, 5))
plt.plot(t, waveform, label='Original Collapse-Expand Waveform')
plt.plot(t, prediction, label='Neural Net Output', linestyle='--')
plt.title('Neural Net Learning Collapse-Expand Quantum Modulation')
plt.xlabel('Time')
plt.ylabel('Amplitude')
plt.legend()
plt.grid(True)
plt.show()
