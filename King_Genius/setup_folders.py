import os

class LavenderAIEngine:
    def __init__(self):
        self.base_db = "./database"

    def find_exploit(self, brand, model):
        # التأكد من المسار الصحيح
        path = os.path.join(self.base_db, brand)
        if not os.path.exists(path):
            return f"Error: Directory for {brand} not found."

        # البحث عن ملفات
        files = [f for f in os.listdir(path) if model.lower() in f.lower()]
        
        if files:
            best_match = sorted(files)[-1]
            return f"AI_MATCH_FOUND: {best_match}"
        else:
            return "NO_LOCAL_MATCH: AI is switching to Cloud Search..."

    def cloud_sync(self):
        return "Syncing with Lavender Global Server... Done."