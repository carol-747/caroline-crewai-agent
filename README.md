# Caroline's Personal CrewAI Agent with Voice Interaction

A CrewAI agent that represents Caroline Haoran Song as her "digital twin lite" - now with **multimodal voice capabilities** using speech-to-text and text-to-speech!

## 🎓 About Caroline

This agent embodies Caroline Song, a Harvard Master's in Biostatistics student with:
- **Perfect Academic Record**: 3.96 GPA at Harvard, 4.0 GPA and top of cohort at University of Sydney
- **Research Excellence**: Cardiovascular risk modeling, spatial transcriptomics, cooperative learning
- **Industry Experience**: Solution Architecture Intern at Tencent Healthcare (¥20M+ POC deals)
- **Global Perspective**: Experience across Boston, Sydney, and Shenzhen
- **Leadership Impact**: Chair of Harvard Chan Biotechnology Club, organized workshops for 200+ students

## 🤖 What This Agent Does

The agent represents Caroline's unique combination of:

### 🔬 Research Expertise
- Cardiovascular risk modeling via cooperative learning and survival analysis
- Spatial transcriptomics of neuroimmune stress response
- Multi-view data integration (genomic, cardiac MRI, clinical data)
- Polygenic hazard score development

### 🏥 Healthcare AI Experience
- Multimodal AI medical LLM solutions
- Point-of-care device development (80% testing time reduction)
- Clinical workflow integration
- RAG and generative AI in healthcare

### 🌟 Leadership & Communication
- Cross-functional team collaboration
- Executive-facing presentations
- Student mentorship and career guidance
- Multicultural stakeholder engagement

## 🎙️ NEW: Voice Interaction Features

**HW4 Extension**: The agent now supports natural voice conversations!

- **Speech-to-Text**: Powered by OpenAI Whisper for accurate transcription
- **Text-to-Speech**: Natural voice responses using Google TTS
- **Real-time Interaction**: ~2 second response time for conversational feel
- **Offline Capable**: No API costs for voice features

### Voice Interaction Modes:
1. **Live Voice Chat**: Speak questions, hear Caroline's responses
2. **Text Chat with TTS**: Type questions, hear spoken answers
3. **Automated Demo**: Watch pre-programmed voice interactions

## 🛠️ Technical Skills Represented

**Programming & ML**: Python, R, TensorFlow, SQL, Deep Learning, Survival Analysis  
**Cloud & DevOps**: Docker, Kubernetes, MLOps, Cloud-Native Architecture  
**Statistics**: Cooperative Learning, Regression Modeling, Clinical Trial Design  
**Languages**: Native English and Mandarin  
**Multimodal AI**: Speech Recognition, Text-to-Speech, Voice Interface Design

## 📁 Project Structure

```
caroline-crewai-agent_speech/
├── caroline_interactive_with_speech.py  # ⭐ NEW - Voice interaction demo
├── main.py                              # Full CrewAI agent (requires OpenAI API key)
├── demo_main.py                         # Demo version (no API key required)
├── interactive_demo.py                  # Interactive Q&A with Caroline's agent
├── test_caroline_agent.py               # Comprehensive test suite
├── setup.py                             # Automated setup and submission helper
├── requirements.txt                     # Python dependencies (updated for speech)
├── README.md                            # This documentation
├── .gitignore                           # Git ignore file
├── caroline_research_capabilities.md    # Generated research overview
└── caroline_leadership_impact.md        # Generated leadership summary
```

## 🚀 How to Use

### ⭐ NEW: Voice Interaction (Recommended for HW4)
```bash
python caroline_interactive_with_speech.py
```

**Select from 3 modes:**
1. **Voice Interaction** - Speak to Caroline, hear her response
2. **Text Chat with TTS** - Type questions, hear spoken answers
3. **Auto Demo** - Watch automated voice interactions

**What to ask:**
- "Tell me about your cardiovascular research at Harvard"
- "What was your experience at Tencent Healthcare?"
- "What are your technical skills in machine learning?"

---

### Original Modes (Text-only):

#### Option 1: Demo Version
```bash
python demo_main.py
```
Shows exactly what the agent would produce without requiring API keys.

#### Option 2: Interactive Chat (Text)
```bash
python interactive_demo.py
```
Ask custom questions and chat with Caroline's digital twin via text.

#### Option 3: Full Agent (Requires OpenAI API Key)
```bash
export OPENAI_API_KEY="your-key-here"
python main.py
```

#### Option 4: Run Tests
```bash
python test_caroline_agent.py
```

## 🛠️ Setup Instructions

### Prerequisites
- Python 3.8+
- Microphone (for live voice interaction)
- Speakers/headphones (for TTS output)
- Optional: OpenAI API key for full text-based functionality

### Installation

1. **Clone/Download the code**

2. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```
   
   This includes:
   - CrewAI framework
   - OpenAI Whisper (speech-to-text)
   - Google TTS (text-to-speech)
   - Audio libraries (sounddevice, soundfile)

3. **For macOS users**: Install ffmpeg for audio processing
   ```bash
   brew install ffmpeg
   ```

4. **Optional: Set API key** (for enhanced text functionality):
   ```bash
   export OPENAI_API_KEY="your-openai-api-key-here"
   ```

### First Run

The first time you run the voice demo, Whisper will download a ~150MB model. This is normal and only happens once.

## 📊 Expected Output

### Voice Interaction Demo:
```
======================================================================
CAROLINE SONG - AI VOICE ASSISTANT DEMO
======================================================================

Harvard Biostatistics | Healthcare AI | Research Innovation

Initializing Caroline's Voice Agent...
Loading speech recognition (Whisper)...
✓ Caroline's voice agent ready!

Select interaction mode:
1. Voice Interaction (speak with Caroline)
2. Text Chat (type with TTS responses)
3. Run Demo Sequence
4. Exit

Your choice (1-4): 1

Press ENTER to start recording (you'll have 5 seconds to speak)...
🎤 Recording for 5 seconds...
Speak now!
✓ Recording saved
🎤 Transcribing your voice...
You said: Tell me about your cardiovascular research at Harvard

💭 Caroline: I focus on cardiovascular risk modeling using cooperative 
learning and survival analysis...

🔊 Generating Caroline's voice...
✓ Saved: caroline_response.mp3
🔊 Playing: caroline_response.mp3
[Audio plays Caroline's response]

✓ Interaction complete!
```

### Text Demo Output:
```
🧬 Caroline's Personal CrewAI Agent - DEMO VERSION
============================================================
🎓 Harvard Biostatistics Student | 🔬 AI Healthcare Researcher | 🌍 Global Perspective

📋 TASK 1: Class Introduction
Hi everyone! I'm Caroline Song, a Harvard Master's in Biostatistics student...
```

## 📋 Generated Files

The agent creates:
- `caroline_research_capabilities.md` - Detailed research expertise overview
- `caroline_leadership_impact.md` - Leadership experience and community impact
- `caroline_conversation_log.json` - Voice interaction history with timestamps
- Audio files (`.mp3`) - Generated questions and responses

## 🎯 Four Ways to Experience the Agent

1. **Voice Interaction** (`caroline_interactive_with_speech.py`) - ⭐ NEW! Natural voice conversations
2. **Structured Demo** (`demo_main.py`) - See all capabilities in sequence (text)
3. **Interactive Chat** (`interactive_demo.py`) - Ask specific questions (text)
4. **Full Agent** (`main.py`) - Dynamic responses with OpenAI integration

## 🎬 Demo Video & Write-up

- **Video Demo**: [YouTube Link - Unlisted]
- **Technical Write-up**: Available in repository
- **Shows**: Complete STT → Processing → TTS pipeline with real-time interaction

## 🌟 Unique Value Proposition

This agent stands out because it represents:
- **Multimodal Capabilities**: Text AND voice interaction
- True interdisciplinary expert (biostatistics + engineering + AI + business)
- Real-world industry impact (Tencent Healthcare, point-of-care devices)
- Academic excellence with practical application
- Global perspective and multicultural communication skills
- Leadership in student organizations and research mentorship
- Natural conversational AI using state-of-the-art speech models

## 🔧 Technologies Used

### Voice Features (NEW):
- **Whisper** (OpenAI): Speech-to-text transcription
- **gTTS** (Google): Text-to-speech synthesis
- **SoundDevice**: Audio capture and playback
- **SoundFile**: Audio file processing

### Original Agent:
- **CrewAI**: Agent framework
- **LangChain**: LLM orchestration
- **Python**: Core implementation

## 🚀 Quick Start

**For HW4 Voice Demo**:
```bash
pip install -r requirements.txt
python caroline_interactive_with_speech.py
# Choose option 3 for automated demo
```

**For Original Text Agent**:
```bash
python demo_main.py
```

Perfect for showcasing how AI agents can represent complex, high-achieving professionals in the biostatistics and healthcare AI space - now with natural voice interaction! 