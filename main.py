#log読み込み関数
def load_logs(file_path):
    logs = []
    levels = []
    try:
        with open(file_path,"r",encoding="utf-8") as file:
            for log in file:
                logs.append(log.strip())
                levels.append(get_level(log))
    except FileNotFoundError as e:
        print(f"ファイルがありません{e}")
        return None, None
    else:
        unique_level = []
        for level in levels:
            if level not in unique_level:
                unique_level.append(level)

        return logs,unique_level

# ログレベル抽出関数
def get_level_logs(logs, level):
    matched_logs = []

    for log in logs:
        if get_level(log) == level:
            matched_logs.append(log)

    return matched_logs

def get_level(log):
    parts = log.split()
    level = parts[2]
    return level

#logファイル出力
logs,unique_level = load_logs("sample/app.log")

if logs is None:
    print("エラーのため終了します")
else:
    for level in unique_level:
        level_logs = get_level_logs(logs,level)
        print(f"{level}件数: {len(level_logs)}")
        for log in level_logs:
            print(log)        