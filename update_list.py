import os
import json

# 音频文件夹路径
audio_dir = './audio'
# 输出的 json 文件名
output_file = 'list.json'

def update_json():
    audio_files = []
    # 扫描文件夹
    if os.path.exists(audio_dir):
        # 排序确保列表顺序稳定
        files = sorted(os.listdir(audio_dir))
        for filename in files:
            if filename.endswith('.mp3'):
                # 名字去掉后缀作为显示名称
                name = os.path.splitext(filename)[0]
                audio_files.append({
                    "name": name,
                    "file": filename
                })
    
    # 写入文件
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(audio_files, f, ensure_ascii=False, indent=2)
    print(f"成功更新 {output_file}，共包含 {len(audio_files)} 个音频。")

if __name__ == "__main__":
    update_json()
