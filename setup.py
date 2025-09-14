#!/usr/bin/env python3
"""
Setup Helper for Caroline's CrewAI Agent
Handles installation and testing.
"""

import os
import subprocess
import zipfile
from datetime import datetime

def install_dependencies():
    """Install required dependencies."""
    print("📦 Installing dependencies...")
    try:
        subprocess.check_call(["pip", "install", "-r", "requirements.txt"])
        print("✅ Dependencies installed successfully")
        return True
    except subprocess.CalledProcessError as e:
        print(f"❌ Failed to install dependencies: {e}")
        return False

def test_installation():
    """Test if everything is installed correctly."""
    print("\n🧪 Testing installation...")
    try:
        import crewai
        from crewai import Agent, Task, Crew
        print("✅ CrewAI imported successfully")
        
        # Test our main module
        from main import create_caroline_agent
        agent = create_caroline_agent()
        print("✅ Caroline's agent created successfully")
        
        return True
    except ImportError as e:
        print(f"❌ Import error: {e}")
        return False
    except Exception as e:
        print(f"❌ Error running tests: {e}")
        return
    
    # Final summary
    print("\n" + "="*60)
    print("🎯 SETUP COMPLETE - READY FOR SUBMISSION!")
    print(f"\n🌟 Caroline's agent is ready to showcase:")
    print("   • Harvard Biostatistics expertise")
    print("   • Cardiovascular risk modeling research")
    print("   • Tencent Healthcare industry experience") 
    print("   • Multicultural perspective and leadership")
    print("   • Perfect academic record and research impact")

if __name__ == "__main__":
    main() e:
        print(f"❌ Error: {e}")
        return False


def main():
    """Main setup and submission preparation function."""
    print("🚀 Caroline's CrewAI Agent - Setup Helper")
    print("="*60)
    print("🎓 Harvard Biostatistics Student | 🔬 AI Healthcare Researcher")
    print("="*60)
    
    # Step 1: Install dependencies
    if not install_dependencies():
        print("❌ Setup failed at dependency installation")
        return
    
    # Step 2: Test installation
    if not test_installation():
        print("❌ Setup failed at testing")
        return
    
    # Step 3: Run agent test
    print("\n🧪 Running comprehensive agent test...")
    try:
        from test_caroline_agent import test_caroline_agent, verify_homework_requirements
        agent_ok = test_caroline_agent()
        hw_ok = verify_homework_requirements()
        
        if not (agent_ok and hw_ok):
            print("❌ Agent or homework requirements test failed")
            return
    except Exception as
