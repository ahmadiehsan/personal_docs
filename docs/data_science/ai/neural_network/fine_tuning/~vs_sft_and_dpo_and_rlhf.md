# Vs (SFT & DPO & RLHF)

## Description

- **SFT:** Trains on labeled input-output pairs, but does not directly optimize for human preferences.
- **RLHF:** Uses a reward model and reinforcement learning to align with preferences, but is complex and unstable.
- **DPO:** Directly optimizes for preference pairs, offering a simpler and more robust alternative to RLHF.

!!! info

    DPO is gaining popularity for instruction and alignment fine-tuning, especially when preference data is available.
