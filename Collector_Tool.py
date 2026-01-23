import os
import shutil

def levanti_asset_collector():
    # قائمة المسارات اللي حددناها من صورك
    sources = [
        r"C:\DFTPRO\data",
        r"C:\Hydra Tool\Files",
        r"C:\Hydra Tool\Bin",
        r"C:\Program Files (x86)\Chimera"
    ]
    
    # مجلد مشروعنا الجديد
    destination = r"C:\Users\king\Desktop\MobileTool\KING_ASSETS"
    if not os.path.exists(destination):
        os.makedirs(destination)

    print("--- 👑 LEVANTI ASSET COLLECTOR START 👑 ---")
    
    extensions = ('.bin', '.da', '.auth', '.der', '.lib')
    
    for folder in sources:
        if os.path.exists(folder):
            print(f"🔍 Searching in: {folder}")
            for root, dirs, files in os.walk(folder):
                for file in files:
                    if file.lower().endswith(extensions):
                        try:
                            full_path = os.path.join(root, file)
                            shutil.copy(full_path, destination)
                            print(f"✅ Copied: {file}")
                        except:
                            pass
    print(f"\n🔥 Done! All files are now in: {destination}")

if __name__ == "__main__":
    levanti_asset_collector()