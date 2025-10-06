"""
Caroline's Interactive Demo with Speech Capabilities
Enhanced version using gTTS (more reliable alternative to Kokoro)
"""

import whisper
from gtts import gTTS
import soundfile as sf
import sounddevice as sd
import numpy as np
from datetime import datetime
import json
import os

class CarolineVoiceDemo:
    """
    Interactive demo of Caroline's agent with speech capabilities
    Works without API keys using pre-defined responses
    """
    
    def __init__(self):
        """Initialize speech models"""
        print("Initializing Caroline's Voice Agent...")
        
        # Load Whisper for STT
        print("Loading speech recognition (Whisper)...")
        self.whisper_model = whisper.load_model("base")
        
        # Caroline's knowledge base (from your demo_main.py)
        self.knowledge_base = {
            "research": """I focus on cardiovascular risk modeling using cooperative 
            learning and survival analysis. My thesis involves developing polygenic 
            hazard scores using multi-view data integration across genomic, cardiac MRI, 
            and clinical data. I'm also working on spatial transcriptomics to understand 
            neuroimmune stress response in the brain.""",
            
            "tencent": """As a Solution Architecture Intern at Tencent Healthcare, I 
            designed multimodal AI medical LLM solutions and contributed to POC deals 
            worth over 20 million yuan. I also developed point-of-care diagnostic devices 
            that reduced testing time by 80 percent, which taught me how to translate complex 
            AI into practical clinical workflows.""",
            
            "skills": """I'm proficient in Python, R, TensorFlow, and SQL for machine 
            learning. I specialize in survival analysis, cooperative learning, and 
            clinical trial design. I also have experience with Docker, Kubernetes, and 
            MLOps for deploying healthcare AI solutions.""",
            
            "leadership": """As Chair of the Harvard Chan Biotechnology Club, I organize 
            workshops and career panels for over 200 students. I also mentor undergraduates 
            in biostatistics research and help them navigate career paths in healthcare AI.""",
            
            "background": """I'm a Harvard Master's student in Biostatistics with a 
            perfect 4.0 GPA from University of Sydney. I bring a multicultural perspective 
            from my experiences in Boston, Sydney, and Shenzhen. This diversity helps me 
            bridge technical research with real-world healthcare needs."""
        }
        
        self.conversation_history = []
        print("✓ Caroline's voice agent ready!\n")
    
    def speech_to_text(self, audio_path: str) -> str:
        """Transcribe speech to text"""
        print("🎤 Transcribing your voice...")
        result = self.whisper_model.transcribe(audio_path, language="en")
        text = result["text"].strip()
        print(f"You said: {text}")
        return text
    
    def text_to_speech(self, text: str, output_path: str = "caroline_voice.mp3") -> str:
        """Generate speech from text using gTTS"""
        print("🔊 Generating Caroline's voice response...")
        tts = gTTS(text=text, lang='en', slow=False)
        tts.save(output_path)
        print(f"✓ Audio saved to {output_path}")
        return output_path
    
    def play_audio(self, audio_path: str):
        """Play audio file"""
        print("🔊 Playing response...")
        
        # For MP3 files, we need to convert or use a different player
        if audio_path.endswith('.mp3'):
            # Use system player for MP3
            import platform
            system = platform.system()
            
            if system == 'Darwin':  # macOS
                os.system(f'afplay "{audio_path}"')
            elif system == 'Linux':
                os.system(f'mpg123 "{audio_path}" 2>/dev/null || ffplay -nodisp -autoexit "{audio_path}" 2>/dev/null')
            elif system == 'Windows':
                os.system(f'start "" "{audio_path}"')
        else:
            # For WAV files
            data, sample_rate = sf.read(audio_path)
            sd.play(data, sample_rate)
            sd.wait()
    
    def get_response(self, user_input: str) -> str:
        """Generate Caroline's response based on keywords"""
        user_lower = user_input.lower()
        
        # Match keywords to responses
        if any(word in user_lower for word in ["research", "thesis", "cardiovascular", "genomic"]):
            return self.knowledge_base["research"]
        
        elif any(word in user_lower for word in ["tencent", "internship", "industry", "healthcare ai"]):
            return self.knowledge_base["tencent"]
        
        elif any(word in user_lower for word in ["skills", "technical", "programming", "python"]):
            return self.knowledge_base["skills"]
        
        elif any(word in user_lower for word in ["leadership", "club", "mentor", "harvard chan"]):
            return self.knowledge_base["leadership"]
        
        elif any(word in user_lower for word in ["background", "about", "who", "sydney", "boston"]):
            return self.knowledge_base["background"]
        
        elif any(word in user_lower for word in ["hello", "hi", "hey"]):
            return """Hi! I'm Caroline Song's AI assistant. I can tell you about my 
            research in cardiovascular modeling, my experience at Tencent Healthcare, 
            my technical skills, or my leadership at Harvard. What would you like to know?"""
        
        else:
            return """That's an interesting question! I specialize in biostatistics, 
            healthcare AI, and cardiovascular research. Feel free to ask me about my 
            research, industry experience at Tencent, technical skills, or leadership 
            activities at Harvard."""
    
    def record_audio(self, duration: int = 5, output_file: str = "user_input.wav") -> str:
        """Record audio from microphone"""
        print(f"\n🎤 Recording for {duration} seconds...")
        print("Speak now!")
        
        sample_rate = 16000
        recording = sd.rec(
            int(duration * sample_rate),
            samplerate=sample_rate,
            channels=1,
            dtype=np.float32
        )
        sd.wait()
        
        sf.write(output_file, recording, sample_rate)
        print(f"✓ Recording saved")
        return output_file
    
    def voice_interaction(self):
        """Complete voice interaction"""
        print("\n" + "="*70)
        print("CAROLINE'S VOICE INTERACTION")
        print("="*70)
        
        # Record user speech
        input("Press ENTER to start recording (you'll have 5 seconds to speak)...")
        audio_file = self.record_audio(duration=5)
        
        # Transcribe
        user_text = self.speech_to_text(audio_file)
        
        # Get response
        response = self.get_response(user_text)
        print(f"\n💭 Caroline: {response}\n")
        
        # Generate and play speech
        audio_output = "caroline_response.mp3"
        self.text_to_speech(response, audio_output)
        
        play = input("Play Caroline's voice response? (y/n): ").lower()
        if play == 'y':
            self.play_audio(audio_output)
        
        # Log conversation
        self.conversation_history.append({
            "timestamp": datetime.now().isoformat(),
            "user": user_text,
            "caroline": response,
            "user_audio": audio_file,
            "response_audio": audio_output
        })
        
        return {"user": user_text, "response": response}
    
    def text_interaction(self):
        """Text-based interaction with TTS output"""
        user_input = input("\n💬 You: ").strip()
        
        if not user_input:
            return None
        
        response = self.get_response(user_input)
        print(f"💭 Caroline: {response}")
        
        # Generate TTS
        audio_file = f"response_{len(self.conversation_history)}.mp3"
        self.text_to_speech(response, audio_file)
        
        play = input("\nPlay audio response? (y/n): ").lower()
        if play == 'y':
            self.play_audio(audio_file)
        
        self.conversation_history.append({
            "timestamp": datetime.now().isoformat(),
            "user": user_input,
            "caroline": response,
            "response_audio": audio_file
        })
        
        return {"user": user_input, "response": response}
    
    def save_conversation(self, filename: str = "caroline_conversation.json"):
        """Save conversation history"""
        with open(filename, 'w') as f:
            json.dump({
                "session_start": self.conversation_history[0]["timestamp"] if self.conversation_history else None,
                "total_interactions": len(self.conversation_history),
                "history": self.conversation_history
            }, f, indent=2)
        print(f"\n✓ Conversation saved to {filename}")


def main():
    """Run Caroline's interactive voice demo"""
    print("\n" + "="*70)
    print("CAROLINE SONG - AI VOICE ASSISTANT DEMO")
    print("="*70)
    print("\nHarvard Biostatistics | Healthcare AI | Research Innovation")
    print()
    
    demo = CarolineVoiceDemo()
    
    print("\nSelect interaction mode:")
    print("1. Voice Interaction (speak with Caroline)")
    print("2. Text Chat (type with TTS responses)")
    print("3. Run Demo Sequence")
    print("4. Exit")
    
    while True:
        choice = input("\nYour choice (1-4): ").strip()
        
        if choice == "1":
            demo.voice_interaction()
        
        elif choice == "2":
            result = demo.text_interaction()
            if result is None:
                continue
        
        elif choice == "3":
            # Demo sequence
            demo_questions = [
                "Tell me about your research",
                "What was your experience at Tencent?",
                "What are your leadership activities?"
            ]
            
            for question in demo_questions:
                print(f"\n💬 Demo Question: {question}")
                response = demo.get_response(question)
                print(f"💭 Caroline: {response}\n")
                
                audio_file = f"demo_{len(demo.conversation_history)}.mp3"
                demo.text_to_speech(response, audio_file)
                print("Playing audio...")
                demo.play_audio(audio_file)
                
                demo.conversation_history.append({
                    "timestamp": datetime.now().isoformat(),
                    "user": question,
                    "caroline": response,
                    "response_audio": audio_file
                })
                
                input("Press ENTER for next question...")
        
        elif choice == "4":
            demo.save_conversation()
            print("\nThank you for chatting with Caroline's AI!")
            break
        
        else:
            print("Invalid choice. Please select 1-4.")


if __name__ == "__main__":
    main()