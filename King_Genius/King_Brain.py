import json
import os

class NeuralBrain:
    def __init__(self):
        self.memory_path = "king_neural_memory.json"
        self.knowledge = self.load_memory()

    def load_memory(self):
        """تحميل الذاكرة العصبية من الملف"""
        if os.path.exists(self.memory_path):
            try:
                with open(self.memory_path, 'r') as f:
                    return json.load(f)
            except:
                return {}
        return {}

    def save_memory(self):
        """تخزين الخبرات الجديدة"""
        with open(self.memory_path, 'w') as f:
            json.dump(self.knowledge, f, indent=4)

    def analyze_device(self, model):
        """تحليل الجهاز واقتراح الحل الأمثل بناءً على الخبرة السابقة"""
        if model in self.knowledge:
            strategies = self.knowledge[model]
            # البحث عن الاستراتيجية ذات أعلى نسبة نجاح
            best_strategy = max(strategies, key=strategies.get)
            confidence = strategies[best_strategy]
            return best_strategy, confidence
        else:
            # جهاز جديد تماماً
            return "UNKNOWN", 0

    def train(self, model, strategy, success):
        """عملية التعلم (Training Step)"""
        if model not in self.knowledge:
            self.knowledge[model] = {"ROOT_METHOD": 50, "AT_METHOD": 50, "FRP_EXPLOIT": 50}
        
        current_score = self.knowledge[model].get(strategy, 50)
        
        # خوارزمية التعلم التعزيزي (Reinforcement Logic)
        if success:
            # مكافأة: زيادة الثقة
            new_score = min(current_score + 15, 99)
        else:
            # عقاب: تقليل الثقة لتجنب الخطأ مستقبلاً
            new_score = max(current_score - 10, 5)
            
        self.knowledge[model][strategy] = new_score
        self.save_memory()
        return new_score