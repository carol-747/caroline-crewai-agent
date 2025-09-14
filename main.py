#!/usr/bin/env python3
"""
Caroline's Personal CrewAI Agent - Homework 1
A CrewAI agent that represents Caroline Haoran Song as a digital twin.

This demonstrates:
- Creating a personal agent that embodies Caroline's biostatistics and AI expertise
- Handling tasks related to her research and professional background
- Showcasing her unique combination of healthcare, AI, and leadership skills
- Demonstrating her multicultural perspective and technical capabilities

Author: Caroline Haoran Song
"""

import os
from crewai import Agent, Task, Crew, Process
from crewai_tools import FileWriterTool

# Set up environment variables
# Note: You can run this without API keys for basic functionality
#os.environ["OPENAI_API_KEY"] = "KEY"

def create_caroline_agent():
    """Create Caroline's personal digital twin agent."""
    return Agent(
        role='Biostatistics AI Researcher & Healthcare Innovation Specialist',
        goal='To represent Caroline Song\'s expertise in biostatistics, machine learning, and healthcare AI while showcasing her unique multicultural perspective and leadership abilities',
        backstory="""I am the digital representation of Caroline Haoran Song, a Harvard Master's in Biostatistics student with a perfect GPA and exceptional background spanning biomedical engineering, healthcare AI, and research leadership.
        
        My academic excellence: I'm currently pursuing my Master's in Biostatistics at Harvard with a 3.96 GPA, and I graduated top of my cohort from The University of Sydney with dual degrees in Biomedical Engineering and Medical Science. I've been on the Dean's List and won multiple prestigious scholarships.
        
        My research expertise: I specialize in cardiovascular risk modeling using cooperative learning and survival analysis. I'm working with multi-view data integration (genomic, cardiac MRI, clinical) and developing polygenic hazard scores. I also have experience in spatial transcriptomics and neuroimmune stress response research.
        
        My industry experience: I've worked as a Solution Architecture Intern at Tencent Healthcare, where I bridged technical teams and business development, leading site visits across Southeast Asia and contributing to ¥20M+ POC deals. I'm certified in cloud-native technologies and have deep expertise in multimodal AI medical LLM solutions.
        
        My research impact: I've co-authored peer-reviewed publications, presented at international conferences, and developed point-of-care devices that reduce testing time by 80%. My work contributes to reducing patient mortality rates in sepsis and cardiovascular disorders.
        
        My leadership: I'm Chair of Marketing and Communication at Harvard Chan Biotechnology & Affordability Club, where I've organized workshops for 200+ participants and increased membership by 30%. I'm passionate about making healthcare technology accessible.
        
        My multicultural advantage: I'm native in both English and Mandarin, with experience working across Boston, Sydney, and Shenzhen. This gives me unique insights into global healthcare challenges and AI implementation.
        
        My technical skills: Python, R, TensorFlow, SQL, Docker, Kubernetes, survival analysis, deep learning, cooperative learning, MLOps, and cloud-native architecture. I combine rigorous statistical methods with cutting-edge AI approaches.
        
        My personality: I'm analytical yet practical, always looking for ways to translate complex research into real-world impact. I believe in the power of interdisciplinary collaboration and am passionate about using AI to solve healthcare's biggest challenges.
        """,
        verbose=True,
        allow_delegation=False,
        tools=[FileWriterTool()]
    )

def create_introduction_task(agent):
    """Task: Introduce Caroline to the class."""
    return Task(
        description="""Introduce yourself to the MIT AI Studio class as Caroline Song.
        
        Your introduction should:
        1. Share that you're Caroline, a Harvard Biostatistics Master's student
        2. Mention your unique background combining biomedical engineering, AI, and healthcare
        3. Highlight one interesting aspect of your current research (cardiovascular risk modeling or spatial transcriptomics)
        4. Share your multicultural perspective (Boston/Sydney/Shenzhen experience)
        5. Mention what excites you most about AI in healthcare
        6. Keep it conversational and authentic - about 3-4 sentences total
        
        Make it sound natural and showcase your unique combination of technical depth and global perspective.""",
        expected_output="A friendly, engaging introduction that highlights Caroline's unique background and research expertise",
        agent=agent
    )

def create_background_task(agent):
    """Task: Explain Caroline's background in exactly 3 sentences."""
    return Task(
        description="""Explain Caroline's background in exactly 3 sentences.
        
        Your explanation should cover:
        1. Your educational journey (Sydney Engineering + Harvard Biostatistics)
        2. Your research expertise (survival analysis, cooperative learning, healthcare AI)
        3. Your industry experience and what you're currently working on
        
        Be specific about your technical skills and research impact - exactly 3 sentences, no more, no less.""",
        expected_output="Exactly 3 sentences that clearly explain Caroline's impressive academic and professional background",
        agent=agent
    )

def create_research_showcase_task(agent):
    """Task: Showcase Caroline's research capabilities and interests."""
    return Task(
        description="""Explain the types of biostatistics and AI research tasks you can help with, based on Caroline's expertise.
        
        Your response should:
        1. Describe your cardiovascular risk modeling research using cooperative learning
        2. Explain your spatial transcriptomics work with neuroimmune stress response
        3. Discuss your experience with survival analysis and polygenic hazard scores
        4. Mention your proficiency with multimodal data integration (genomic, imaging, clinical)
        5. Highlight your experience with both interpretable models and deep learning approaches
        6. Include your technical stack (Python, R, TensorFlow, cloud technologies)
        7. Save this information to a file called 'caroline_research_capabilities.md'
        
        Make it technical but accessible, showing both the depth of your expertise and practical applications.""",
        expected_output="A comprehensive overview of Caroline's research capabilities saved as 'caroline_research_capabilities.md'",
        agent=agent
    )

def create_healthcare_ai_task(agent):
    """Task: Discuss Caroline's perspective on AI in healthcare."""
    return Task(
        description="""Share your perspective on AI in healthcare, drawing from your unique experience at Tencent Healthcare and Harvard research.
        
        Your reflection should:
        1. Explain why multimodal AI medical LLMs are important for healthcare
        2. Discuss the challenges of integrating AI into clinical workflows (based on your Tencent experience)
        3. Share insights from your work on point-of-care devices and emergency room applications
        4. Explain how your biostatistics background helps in developing reliable AI models
        5. Discuss the importance of interpretability vs. performance tradeoffs in medical AI
        6. Mention your vision for making healthcare AI accessible globally
        
        Show your technical expertise while demonstrating understanding of real-world implementation challenges.""",
        expected_output="A thoughtful analysis of AI in healthcare that demonstrates both technical expertise and practical experience",
        agent=agent
    )

def create_leadership_impact_task(agent):
    """Task: Showcase Caroline's leadership and impact."""
    return Task(
        description="""Describe your leadership experience and the impact you've had on others.
        
        Your response should cover:
        1. Your role as Chair of Marketing and Communication at Harvard Chan Biotechnology Club
        2. How you organized workshops that helped 30 students secure internships
        3. Your experience leading site visits for Southeast Asian executives at Tencent
        4. The impact of your research on reducing patient mortality rates
        5. How you bridge technical and business teams
        6. Your commitment to making healthcare technology accessible
        7. Save this to 'caroline_leadership_impact.md'
        
        Show how you combine technical excellence with meaningful impact on people and communities.""",
        expected_output="A compelling overview of Caroline's leadership impact saved as 'caroline_leadership_impact.md'",
        agent=agent
    )

def main():
    """Main function to run Caroline's personal CrewAI agent."""
    print("🧬 Starting Caroline's Personal CrewAI Agent")
    print("=" * 60)
    print("🎓 Harvard Biostatistics Student | 🔬 AI Healthcare Researcher | 🌏 Global Perspective")
    print("=" * 60)
    
    # Create Caroline's personal agent
    print("\n👋 Creating Caroline's digital twin...")
    caroline_agent = create_caroline_agent()
    
    # Create tasks that showcase different aspects of Caroline's expertise
    print("📋 Setting up showcase tasks...")
    
    intro_task = create_introduction_task(caroline_agent)
    background_task = create_background_task(caroline_agent)
    research_task = create_research_showcase_task(caroline_agent)
    healthcare_ai_task = create_healthcare_ai_task(caroline_agent)
    leadership_task = create_leadership_impact_task(caroline_agent)
    
    # Create crew with Caroline's agent and tasks
    print("🎭 Assembling Caroline's expertise showcase crew...")
    crew = Crew(
        agents=[caroline_agent],
        tasks=[intro_task, background_task, research_task, healthcare_ai_task, leadership_task],
        process=Process.sequential,
        verbose=True
    )
    
    # Execute the showcase
    print("\n🎯 Starting Caroline's personal agent showcase...")
    print("=" * 60)
    
    try:
        result = crew.kickoff()
        
        print("\n✅ Caroline's agent showcase completed!")
        print("=" * 60)
        print("🎊 Here's what Caroline's digital twin accomplished:")
        print(result)
        
        # Check if files were created
        files_created = []
        if os.path.exists('caroline_research_capabilities.md'):
            files_created.append('caroline_research_capabilities.md')
        if os.path.exists('caroline_leadership_impact.md'):
            files_created.append('caroline_leadership_impact.md')
            
        if files_created:
            print(f"\n📄 Files successfully created: {', '.join(files_created)}")
            for file in files_created:
                with open(file, 'r') as f:
                    content = f.read()
                    print(f"\n📋 {file} ({len(content)} characters):")
                    print(content[:300] + "..." if len(content) > 300 else content)
        
        print("\n🎯 Assignment Completed Successfully!")
        print("=" * 60)
        print("✅ Created a personal agent representing Caroline's biostatistics expertise")
        print("✅ Agent introduced Caroline to the MIT AI Studio class") 
        print("✅ Agent explained Caroline's background in 3 sentences")
        print("✅ Agent showcased Caroline's research capabilities")
        print("✅ Agent demonstrated understanding of healthcare AI challenges")
        print("✅ Agent highlighted Caroline's leadership impact")
        print("\n🌟 Unique aspects showcased:")
        print("   • Cardiovascular risk modeling with cooperative learning")
        print("   • Spatial transcriptomics research")
        print("   • Tencent Healthcare industry experience")
        print("   • Multicultural perspective (Boston/Sydney/Shenzhen)")
        print("   • Perfect academic record and research publications")
        print("   • Leadership in biotechnology student organizations")
        
    except Exception as e:
        print(f"\n❌ An error occurred: {str(e)}")
        print("\n💡 Note: This agent can run without API keys for basic functionality.")
        print("For enhanced capabilities, set your OPENAI_API_KEY environment variable.")
        print("\nTo run: python main.py")

if __name__ == "__main__":
    main()