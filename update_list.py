import os
import json


audio_dir = './audio'
output_file = 'list.json'

def update_json():
    audio_files = []
    if os.path.exists(audio_dir):
        files = sorted(os.listdir(audio_dir))
        for filename in files:
            if filename.endswith('.mp3'):
                name = os.path.splitext(filename)[0]
                audio_files.append({
                    "name": name,
                    "file": filename
                })
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(audio_files, f, ensure_ascii=False, indent=2)
    print(f"成功更新 {output_file}，共包含 {len(audio_files)} 个音频。")

if __name__ == "__main__":
    update_json()
