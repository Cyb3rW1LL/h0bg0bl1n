import subprocess
import sys

def setup():
    print("Installing dependencies...")
    subprocess.check_call([sys.executable, "-m", "pip", "install", "-r", "requirements.txt"])
    
    print("Installing Playwright browser binaries...")
    subprocess.check_call([sys.executable, "-m", "playwright", "install"])
    
    print("\n--- SETUP COMPLETE ---")
    print("1. Rename '.env.example' to '.env'")
    print("2. Open '.env' and add your email/phone settings")
    print("3. Run 'python dealer_finder.py' to generate your dealer list")
    print("4. Run 'python zr2_tracker.py' to start tracking!")

if __name__ == "__main__":
    setup()