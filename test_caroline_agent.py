#!/usr/bin/env python3
"""
Test script for Caroline's Personal CrewAI Agent
Verifies all functionality works correctly before submission.
"""

from main import create_caroline_agent, create_introduction_task, create_background_task
import os

def test_caroline_agent():
    """Test Caroline's CrewAI agent functionality."""
    print("🧪 Testing Caroline's Personal CrewAI Agent...")
    print("=" * 50)
    
    try:
        # Test 1: Agent Creation
        print("\n📝 Test 1: Creating Caroline's agent...")
        agent = create_caroline_agent()
        print(f"✅ Agent created successfully")
        print(f"   Role: {agent.role}")
        print(f"   Goal: {agent.goal[:100]}...")
        
        # Test 2: Task Creation
        print("\n📝 Test 2: Creating tasks...")
        intro_task = create_introduction_task(agent)
        background_task = create_background_task(agent)
        print("✅ Tasks created successfully")
        print(f"   Introduction task: {intro_task.description[:80]}...")
        print(f"   Background task: {background_task.description[:80]}...")
        
        # Test 3: Agent Properties
        print("\n📝 Test 3: Verifying agent properties...")
        assert agent.role == 'Biostatistics AI Researcher & Healthcare Innovation Specialist'
        assert 'Caroline' in agent.backstory
        assert 'Harvard' in agent.backstory
        assert 'biostatistics' in agent.backstory.lower()
        print("✅ Agent properties verified")
        
        # Test 4: Task Properties  
        print("\n📝 Test 4: Verifying task properties...")
        assert 'Caroline' in intro_task.description
        assert 'MIT AI Studio' in intro_task.description
        assert '3 sentences' in background_task.description
        print("✅ Task properties verified")
        
        # Test 5: File System Check
        print("\n📝 Test 5: Checking file system permissions...")
        test_file = "test_write_permissions.txt"
        with open(test_file, 'w') as f:
            f.write("Test file for Caroline's agent")
        if os.path.exists(test_file):
            os.remove(test_file)
            print("✅ File writing permissions verified")
        
        print("\n🎉 All tests passed! Caroline's agent is ready for submission.")
        print("\n📋 Summary:")
        print("   ✅ Agent creation successful")
        print("   ✅ Tasks properly configured")
        print("   ✅ Properties correctly set")
        print("   ✅ File operations working")
        print("   ✅ Ready for main.py execution")
        
        print(f"\n🚀 To run Caroline's agent: python main.py")
        
    except Exception as e:
        print(f"\n❌ Error during testing: {str(e)}")
        print("\nTroubleshooting:")
        print("1. Make sure all dependencies are installed: pip install -r requirements.txt")
        print("2. Check that you're in the correct directory")
        print("3. Verify Python version is 3.8+")
        return False
        
    return True

def verify_homework_requirements():
    """Verify that all homework requirements are met."""
    print("\n📚 Verifying Homework Requirements...")
    print("=" * 50)
    
    requirements_met = []
    
    # Check 1: CrewAI Installation
    try:
        import crewai
        requirements_met.append("✅ CrewAI installed and importable")
    except ImportError:
        requirements_met.append("❌ CrewAI not installed - run: pip install crewai")
    
    # Check 2: Agent Definition
    try:
        agent = create_caroline_agent()
        requirements_met.append("✅ Agent defined with role, goal, and backstory")
    except:
        requirements_met.append("❌ Agent definition issue")
    
    # Check 3: Personal Representation
    agent = create_caroline_agent()
    if 'Caroline' in agent.backstory and 'Harvard' in agent.backstory:
        requirements_met.append("✅ Agent represents Caroline's personal background")
    else:
        requirements_met.append("❌ Agent doesn't properly represent Caroline")
    
    # Check 4: Test Prompts
    try:
        intro_task = create_introduction_task(agent)
        bg_task = create_background_task(agent)
        requirements_met.append("✅ Test prompts created (introduction, background)")
    except:
        requirements_met.append("❌ Test prompt creation failed")
    
    # Check 5: Code Organization
    files_needed = ['main.py', 'requirements.txt', 'README.md']
    existing_files = [f for f in files_needed if os.path.exists(f)]
    if len(existing_files) == len(files_needed):
        requirements_met.append("✅ All required files present for GitHub repo")
    else:
        missing = [f for f in files_needed if f not in existing_files]
        requirements_met.append(f"⚠️ Missing files: {missing}")
    
    print("\nRequirement Check Results:")
    for req in requirements_met:
        print(f"  {req}")
    
    all_good = all("✅" in req for req in requirements_met)
    if all_good:
        print("\n🎯 All homework requirements satisfied!")
        print("Ready for GitHub upload and zip file creation!")
    else:
        print("\n⚠️ Some requirements need attention before submission.")
    
    return all_good

if __name__ == "__main__":
    print("🔍 Caroline's CrewAI Agent Testing Suite")
    print("=" * 60)
    
    # Run agent tests
    agent_test_passed = test_caroline_agent()
    
    # Verify homework requirements
    hw_requirements_met = verify_homework_requirements()
    
    print("\n" + "=" * 60)
    if agent_test_passed and hw_requirements_met:
        print("🎊 ALL TESTS PASSED - READY FOR SUBMISSION! 🎊")
        print("\nNext steps:")
        print("1. Run 'python main.py' to see your agent in action")
        print("2. Create GitHub repository and upload code")
        print("3. Create zip file for submission")
    else:
        print("⚠️ Some issues need to be resolved before submission")
        print("Please address the failed tests above.")