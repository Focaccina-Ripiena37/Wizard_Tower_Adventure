import os
import shutil
import zipfile
from pathlib import Path

def create_release(version: str):
    """Create a release package"""
    # Define paths
    release_name = f"WizardTower-v{version}"
    release_dir = Path(release_name)
    
    # Clean old release if exists
    if release_dir.exists():
        shutil.rmtree(release_dir)
    
    # Create directory structure
    os.makedirs(release_dir)
    os.makedirs(release_dir / "assets")
    os.makedirs(release_dir / "instances")
    os.makedirs(release_dir / "logs")
    
    # Copy executable and assets
    shutil.copy2("dist/WizardTower/WizardTower.exe", release_dir)
    shutil.copytree("assets", release_dir / "assets", dirs_exist_ok=True)
    shutil.copytree("instances", release_dir / "instances", dirs_exist_ok=True)
    
    # Copy documentation
    shutil.copy2("README.md", release_dir)
    shutil.copy2("LICENSE.md", release_dir)
    
    # Create ZIP archive
    with zipfile.ZipFile(f"{release_name}.zip", 'w', zipfile.ZIP_DEFLATED) as zipf:
        for root, _, files in os.walk(release_dir):
            for file in files:
                file_path = os.path.join(root, file)
                arcname = os.path.relpath(file_path, release_dir)
                zipf.write(file_path, arcname)
    
    print(f"Release package created: {release_name}.zip")

if __name__ == "__main__":
    create_release("1.0.0")
