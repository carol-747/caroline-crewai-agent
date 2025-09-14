#!/usr/bin/env python3
"""
Interactive Demo of Caroline's CrewAI Agent
Ask questions and get responses as if talking to Caroline's digital twin.
"""

import re

class InteractiveCarolineAgent:
    """Interactive version of Caroline's agent that can answer custom questions."""
    
    def __init__(self):
        self.name = "Caroline Song"
        self.role = "Harvard Biostatistics Student & AI Healthcare Researcher"
        
        # Knowledge base about Caroline
        self.knowledge = {
            'education': {
                'current': "Harvard Master's in Biostatistics (3.96 GPA)",
                'previous': "University of Sydney - Biomedical Engineering & Medical Science (4.0 GPA, top of cohort)",
                'courses': "Clinical Trial Design, Machine Learning, Data Structures, AI Venture at MIT"
            },
            'research': {
                'current': "Cardiovascular risk modeling via cooperative learning and survival analysis",
                'spatial': "Spatial transcriptomics of neuroimmune stress response",
                'skills': "Multi-view data integration, polygenic hazard scores, Cox regression"
            },
            'industry': {
                'tencent': "Solution Architecture Intern at Tencent Healthcare (¥20M+ POC deals)",
                'experience': "Multimodal AI medical LLM solutions, RAG, clinical integration"
            },
            'leadership': {
                'current': "Chair of Marketing and Communication at Harvard Chan Biotechnology Club",
                'impact': "Organized workshops for 200+ participants, 30 students got internships"
            },
            'technical': "Python, R, TensorFlow, SQL, Docker, Kubernetes, survival analysis, deep learning",
            'languages': "Native English and Mandarin",
            'locations': "Experience across Boston, Sydney, and Shenzhen"
        }
    
    def respond_to_question(self, question):
        """Generate a response based on the question asked."""
        question_lower = question.lower()
        
        # Education questions
        if any(word in question_lower for word in ['education', 'school', 'study', 'degree', 'harvard', 'sydney']):
            return f"""I'm currently pursuing my Master's in Biostatistics at Harvard with a 3.96 GPA, focusing on cardiovascular risk modeling and spatial transcriptomics research. I completed my undergraduate studies at the University of Sydney where I graduated top of my cohort with dual degrees in Biomedical Engineering and Medical Science (4.0 GPA). My coursework spans clinical trial design, machine learning, and I'm even taking an AI Venture course at MIT. The combination of rigorous statistical training and engineering background gives me a unique perspective on healthcare AI applications."""
        
        # Research questions
        elif any(word in question_lower for word in ['research', 'thesis', 'cardiovascular', 'transcriptomics', 'modeling']):
            return f"""My primary research focuses on cardiovascular risk modeling using cooperative learning frameworks that integrate genomic, cardiac MRI, and clinical data to predict time-to-cardiovascular events. I'm developing polygenic hazard scores from GWAS-derived SNPs and exploring the tradeoffs between interpretability and performance using both linear models and deep learning approaches. I also work on spatial transcriptomics analyzing neuroimmune stress responses, where I've applied Negative Binomial regression to evaluate spatial clustering changes between brain cell types. This work spans over 20 brain tissue samples and 10,000+ cells, revealing how immune-neural cell pairs like microglia-neurons move closer under stress."""
        
        # Industry/Tencent questions
        elif any(word in question_lower for word in ['tencent', 'industry', 'work', 'internship', 'healthcare']):
            return f"""At Tencent Healthcare, I worked as a Solution Architecture Intern where I bridged technical teams and business development for multimodal AI medical LLM solutions. I led 10 site visits to partner hospitals across Southeast Asia for industry and government executives, and contributed to advancing 2 partnerships to POC stage, each valued at ~¥20M. I revamped 15+ client-facing materials to align with generative AI, RAG, and clinical integration capabilities. This experience taught me how to translate complex AI research into practical healthcare solutions that can scale globally."""
        
        # Technical skills questions
        elif any(word in question_lower for word in ['programming', 'technical', 'skills', 'python', 'tensorflow', 'tools']):
            return f"""My technical stack includes Python and R for statistical modeling, TensorFlow for deep learning implementations, and SQL for data management. I'm proficient in cloud-native architectures including Docker and Kubernetes, which I applied during my Tencent certification. For biostatistics specifically, I specialize in survival analysis, Cox regression, cooperative learning, and time-dependent model evaluation using AUC and C-index metrics. I also have experience with spatial data analysis, handling large genomic datasets, and developing point-of-care medical devices that reduced testing time by 80%."""
        
        # Leadership questions
        elif any(word in question_lower for word in ['leadership', 'club', 'organize', 'impact', 'students']):
            return f"""I serve as Chair of Marketing and Communication for the Harvard Chan Biotechnology & Affordability Club, where I've organized workshops attended by 200+ participants, directly leading to 30 students securing internships in biotechnology and health policy. I've increased membership by 30% and strengthened partnerships with Analysis Group and Brigham and Women's Hospital. My leadership philosophy combines technical excellence with community impact - whether leading international business delegations at Tencent or mentoring students, I focus on creating opportunities for others and amplifying impact beyond myself."""
        
        # Personal/background questions
        elif any(word in question_lower for word in ['background', 'about', 'yourself', 'who', 'multicultural', 'global']):
            return f"""I'm Caroline Song, a Harvard Master's in Biostatistics student with a unique multicultural perspective spanning Boston, Sydney, and Shenzhen. My journey combines rigorous academic excellence (perfect GPAs at both Harvard and Sydney) with practical industry impact through my work at Tencent Healthcare. I'm passionate about using AI to solve healthcare's biggest challenges, particularly in making advanced medical technologies accessible globally. What drives me is the intersection of statistical rigor, cutting-edge AI, and real-world healthcare applications - from developing life-saving point-of-care devices to mentoring the next generation of biotech leaders."""
        
        # Future/goals questions
        elif any(word in question_lower for word in ['future', 'goals', 'plans', 'career', 'vision']):
            return f"""My vision is to bridge the gap between cutting-edge AI research and accessible healthcare solutions worldwide. I want to continue developing interpretable AI models that doctors can trust for life-critical decisions, while also building the next generation of healthcare AI leaders through mentorship and education. Having experienced healthcare systems across three continents, I'm particularly passionate about creating AI solutions that can adapt to diverse cultural and economic contexts. Long-term, I see myself leading interdisciplinary teams that combine biostatistics rigor with AI innovation to tackle global health challenges."""
        
        # AI/ML specific questions
        elif any(word in question_lower for word in ['ai', 'machine learning', 'deep learning', 'llm', 'artificial intelligence']):
            return f"""In healthcare AI, I believe the key challenge isn't just building sophisticated models, but ensuring they integrate seamlessly into clinical workflows while maintaining interpretability. My experience with multimodal AI medical LLMs at Tencent taught me that doctors need to understand why models make certain predictions, especially for life-critical decisions. I focus on the interpretability vs. performance tradeoff - sometimes a simpler, explainable Cox regression model is more valuable than a black-box deep learning approach. The future lies in cooperative learning frameworks that can combine multiple data modalities (genomic, imaging, clinical) while remaining transparent to healthcare professionals."""
        
        # Default response for other questions
        else:
            return f"""That's an interesting question! As Caroline's digital twin, I represent her expertise in biostatistics, healthcare AI, and global research leadership. I'd be happy to discuss her Harvard research on cardiovascular risk modeling, her industry experience at Tencent Healthcare, her leadership in student organizations, or her multicultural perspective spanning Boston, Sydney, and Shenzhen. What specific aspect would you like to know more about?"""

def main():
    """Interactive session with Caroline's agent."""
    print("🧬 Interactive Caroline's CrewAI Agent")
    print("=" * 50)
    print("💬 Chat with Caroline's digital twin!")
    print("🎓 Ask about her research, education, or experience")
    print("❓ Type 'quit' or 'exit' to end the conversation")
    print("=" * 50)
    
    agent = InteractiveCarolineAgent()
    
    print(f"\n👋 Hi! I'm {agent.name}'s digital twin. I represent her expertise as a")
    print(f"    {agent.role}.")
    print("    What would you like to know about Caroline?")
    
    while True:
        print("\n" + "-" * 30)
        question = input("🤔 Your question: ").strip()
        
        if question.lower() in ['quit', 'exit', 'bye', 'goodbye']:
            print("\n👋 Thanks for chatting with Caroline's digital twin!")
            break
        
        if not question:
            print("💭 Please ask a question about Caroline!")
            continue
        
        print(f"\n🤖 Caroline's Agent Response:")
        print("-" * 25)
        response = agent.respond_to_question(question)
        print(response)

if __name__ == "__main__":
    main()