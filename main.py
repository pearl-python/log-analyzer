#log読み込み関数
def load_logs(file_path):
    logs = []
    levels = []
    invalid_logs = []
    try:
        with open(file_path,"r",encoding="utf-8") as file:
            for log in file:
                log = log.strip()
                level = get_level(log)

                if level is None:
                    invalid_logs.append(log)
                    continue
                logs.append(log)
                levels.append(level)
    except FileNotFoundError as e:
        print(f"ファイルがありません{e}")
        return None, None, None
    else:
        unique_level = []
        for level in levels:
            if level not in unique_level:
                unique_level.append(level)

        return logs,unique_level,invalid_logs

# ログレベル抽出関数
def get_level_logs(logs, level):
    matched_logs = []

    for log in logs:
        if get_level(log) == level:
            matched_logs.append(log)

    return matched_logs

#エラーレベル取得関数
def get_level(log):
    parts = log.split()
    if len(parts) < 3:
        return None
    else:    
        return parts[2] 

#logファイル出力
logs,unique_level,invalid_logs = load_logs("sample/app.log")

if logs is None:
    print("エラーのため終了します")
else:
    for level in unique_level:
        level_logs = get_level_logs(logs,level)
        print(f"{level}件数: {len(level_logs)}")
        for log in level_logs:
            print(log)
    print(f"不正ログ件数：{len(invalid_logs)}")
    for log in invalid_logs:
        print(log)