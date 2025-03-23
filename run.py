import os
import subprocess
import sys

def run_pipeline():
    print("🚀 Starting ML-based Phishing Detection Pipeline")
    
    # Ensure we're in the correct directory
    project_dir = os.path.dirname(os.path.abspath(__file__))
    os.chdir(project_dir)
    
    try:
        # Step 1: Prepare dataset
        print("\n📊 Preparing dataset...")
        subprocess.run([sys.executable, "data/prepare_dataset.py"], check=True)
        
        # Step 2: Train model
        print("\n🧠 Training ML model...")
        subprocess.run([sys.executable, "ml/train_model.py"], check=True)
        
        # Step 3: Start Flask API
        print("\n🌐 Starting Flask API server...")
        print("API will be available at http://localhost:5000")
        subprocess.Popen([sys.executable, "api/app.py"])
        
        print("\n✅ Setup complete!")
        print("\nNext steps:")
        print("1. Open Chrome and go to chrome://extensions/")
        print("2. Enable Developer Mode")
        print("3. Click 'Load unpacked' and select the 'extension' folder")
        print("4. The extension icon should appear in your browser toolbar")
        print("\nPress Ctrl+C to stop the API server when done.")
        
    except subprocess.CalledProcessError as e:
        print(f"\n❌ Error: {str(e)}")
        sys.exit(1)

if __name__ == "__main__":
    run_pipeline()
