# ♻️ TrashSort AI

A lightweight AI-based simulation environment for intelligent trash classification, built using a clean OpenEnv-style structure.

---

## 🚀 Live Demo

👉 https://rutiikal-trashsort-ai.hf.space

---

## 🧠 About the Project

TrashSort AI is a simple yet structured environment where an AI model learns to classify waste into four categories:

- Plastic  
- Paper  
- Metal  
- Organic  

The system evaluates the model across different difficulty levels and returns performance scores.

---

## ⚙️ How It Works

1. The environment generates a random trash type  
2. The model predicts the category  
3. Reward is assigned based on correctness  
4. Performance is evaluated across multiple tasks:
   - Easy  
   - Medium  
   - Hard  

---

## 📂 Project Structure
```
environment/
env.py
models.py

tasks/
easy.py
medium.py
hard.py

inference.py
openenv.yaml
Dockerfile
requirements.txt
```
---

## ▶️ Run Locally

```bash
pip install -r requirements.txt
python inference.py
```
---

## 🐳 Run with Docker
```
docker build -t trashsort-ai .
docker run trashsort-ai
```
---

## 📊 Sample Output
```
Easy Score: 0.6  
Medium Score: 0.64  
Hard Score: 0.5  
Final Score: 0.58
```

---

## ✨ Features
- Clean and modular environment design
- Multi-level evaluation (Easy, Medium, Hard)
- Simple AI prediction model
- Reproducible setup
- Docker support
- Live demo available

---

## ⭐ Support

If you like this project, please consider giving it a ⭐ on GitHub!

---
