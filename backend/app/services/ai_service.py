# backend/app/services/ai_service.py
from transformers import pipeline

class AIService:
    def __init__(self):
        self.sentiment_analyzer = pipeline("sentiment-analysis")
        self.classifier = pipeline(
            "zero-shot-classification",
            model="facebook/bart-large-mnli"
        )
    
    def analyze_text(self, text: str):
        sentiment = self.sentiment_analyzer(text)[0]
        categories = ["work", "personal", "urgent", "leisure"]
        classification = self.classifier(
            text,
            candidate_labels=categories,
            multi_label=False
        )
        
        return {
            "sentiment": sentiment["label"],
            "category": classification["labels"][0]
        }