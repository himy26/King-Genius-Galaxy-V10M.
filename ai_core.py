import os
import google.generativeai as genai
import json

class LevantiAI:
    def __init__(self, api_key=None, model_name="gemini-pro"):
        self.api_key = api_key
        self.model_name = model_name
        self.chat_session = None
        
        if self.api_key:
            genai.configure(api_key=self.api_key)
            self.model = genai.GenerativeModel(self.model_name)
            self.start_new_session()
        else:
            print("⚠️ AI WARNING: No API Key provided.")

    def start_new_session(self):
        """Starts a new chat session with system instructions."""
        if hasattr(self, 'model'):
            self.chat_session = self.model.start_chat(history=[])
            # Prime the AI with context about the tool
            system_context = """
            You are 'Levanti AI', an intelligent assistant embedded in the 'Levanti Infinity Supreme' mobile repair tool.
            Your capabilities: 
            1. Analyze Android repair logs (ADB/Fastboot logs).
            2. Suggest solutions for FRP lock, obscure errors, and driver issues.
            3. You are helpful, concise, and technical.
            4. If the user asks for code, provide Python snippets compatible with the tool.
            
            Current Tool Features:
            - Force Wipe MTK (BROM)
            - FRP Kill (Samsung ADB)
            - Fastboot Erase
            """
            self.chat_session.send_message(system_context)

    def chat(self, user_input, context_logs=""):
        """
        Sends a message to the AI, optionally including recent logs for context.
        """
        if not self.chat_session:
            return "❌ AI Error: API Key missing or initialization failed."

        try:
            full_prompt = user_input
            if context_logs:
                full_prompt += f"\n\n[SYSTEM LOGS CONTEXT]:\n{context_logs}\n[END LOGS]"
            
            response = self.chat_session.send_message(full_prompt)
            return response.text
        except Exception as e:
            return f"❌ AI Connection Error: {str(e)}"

    def analyze_error(self, error_message):
        """Quick analysis of a specific error."""
        prompt = f"Analyze this error in an Android Repair Tool context and suggest a fix:\n{error_message}"
        return self.chat(prompt)

if __name__ == "__main__":
    # Test
    print("Testing LevantiAI...")
    # NOTE: You need a valid API key here to test
    # ai = LevantiAI("YOUR_API_KEY") 
    # print(ai.chat("Hello, who are you?"))
