import os
import shutil

def organize_folder():
    current_dir = os.getcwd()
    # List of files the script should NEVER touch
    protected_files = ['weather.py', 'organizer.py', 'LICENSE', '.gitignore', '.git']
    
    for filename in os.listdir(current_dir):
        # Skip protected files and folders
        if filename in protected_files or os.path.isdir(filename):
            continue
            
        file_ext = filename.split('.')[-1].lower()
        
        if not os.path.exists(file_ext):
            os.makedirs(file_ext)
            
        try:
            shutil.move(filename, os.path.join(file_ext, filename))
            print(f"✅ Moved: {filename} -> {file_ext}/")
        except Exception as e:
            print(f"❌ Could not move {filename}: {e}")

if __name__ == "__main__":
    print("🚀 Starting safe file organization...")
    organize_folder()
    print("✨ Done!")