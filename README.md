# Caroline's Personal CrewAI Agent

A CrewAI agent that represents Caroline Haoran Song as her "digital twin lite" for MIT AI Studio Homework 1.

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

## 🛠️ Technical Skills Represented

**Programming & ML**: Python, R, TensorFlow, SQL, Deep Learning, Survival Analysis
**Cloud & DevOps**: Docker, Kubernetes, MLOps, Cloud-Native Architecture  
**Statistics**: Cooperative Learning, Regression Modeling, Clinical Trial Design
**Languages**: Native English and Mandarin

## 📁 Project Structure

```
caroline-crewai-agent/
├── main.py                          # Full CrewAI agent (requires OpenAI API key)
├── demo_main.py                     # Demo version (no API key required)
├── interactive_demo.py              # Interactive Q&A with Caroline's agent
├── test_caroline_agent.py           # Comprehensive test suite
├── setup.py                         # Automated setup and submission helper
├── requirements.txt                 # Python dependencies
├── README.md                        # This documentation
├── .gitignore                       # Git ignore file
├── caroline_research_capabilities.md # Generated research overview
└── caroline_leadership_impact.md    # Generated leadership summary
```

## 🚀 How to Use

### Option 1: Demo Version (Recommended for Testing)
```bash
python demo_main.py
```
Shows exactly what the agent would produce without requiring API keys.

### Option 2: Interactive Chat
```bash
python interactive_demo.py
```
Ask custom questions and chat with Caroline's digital twin. Try questions like:
- "Tell me about your research"
- "What's your experience at Tencent?"
- "What are your technical skills?"
- "What are your leadership accomplishments?"

### Option 3: Full Agent (Requires OpenAI API Key)
```bash
export OPENAI_API_KEY="your-key-here"
python main.py
```

### Option 4: Run Tests
```bash
python test_caroline_agent.py
```

## 🛠️ Setup Instructions

### Prerequisites
- Python 3.8+
- Optional: OpenAI API key for full functionality

### Installation

1. **Clone/Download the code**
2. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```
3. **Optional: Set API key** (for enhanced functionality):
   ```bash
   export OPENAI_API_KEY="your-openai-api-key-here"
   ```

## 📊 Expected Output

### Demo Version Output:
```
🧬 Caroline's Personal CrewAI Agent - DEMO VERSION
============================================================
🎓 Harvard Biostatistics Student | 🔬 AI Healthcare Researcher | 🌏 Global Perspective

📝 TASK 1: Class Introduction
Hi everyone! I'm Caroline Song, a Harvard Master's in Biostatistics student with a perfect GPA...

📝 TASK 2: Background Summary (3 sentences)
I graduated top of my cohort from the University of Sydney...

[Additional tasks and outputs...]

✅ CAROLINE'S AGENT SHOWCASE COMPLETED!
```

### Interactive Demo Output:
```
🧬 Interactive Caroline's CrewAI Agent
==================================================
💬 Chat with Caroline's digital twin!

🤔 Your question: What's your research about?

🤖 Caroline's Agent Response:
My primary research focuses on cardiovascular risk modeling using cooperative learning frameworks...
```

## 📋 Generated Files

The agent creates:
- `caroline_research_capabilities.md` - Detailed research expertise overview
- `caroline_leadership_impact.md` - Leadership experience and community impact

## 🎯 Three Ways to Experience the Agent

1. **Structured Demo** (`demo_main.py`) - See all capabilities in sequence
2. **Interactive Chat** (`interactive_demo.py`) - Ask specific questions
3. **Full Agent** (`main.py`) - Dynamic responses with OpenAI integration


## 🌟 Unique Value Proposition

This agent stands out because it represents:
- A true interdisciplinary expert (biostatistics + engineering + AI + business)
- Real-world industry impact (Tencent Healthcare, point-of-care devices)
- Academic excellence with practical application
- Global perspective and multicultural communication skills
- Leadership in student organizations and research mentorship
- Multiple interaction modes for different use cases

## 🚀 Running the Agent

**Primary**: `python demo_main.py` (Complete functionality demonstration)
**Interactive**: `python interactive_demo.py` (Custom Q&A capability)
**Testing**: `python test_caroline_agent.py` (Validates all requirements)

Perfect for showcasing how AI agents can represent complex, high-achieving professionals in the biostatistics and healthcare AI space!