#log読み込み関数
def load_logs(file_path):
    logs = []
    try:
        with open(file_path,"r",encoding="utf-8") as file:
            for log in file:
                logs.append(log.strip())
    except FileNotFoundError as e:
        print(f"ファイルがありません{e}")
        return None
    else:
        return logs

#エラー行特定関数
def get_level_logs(logs, level):
    matched_logs = []

    for log in logs:
        if level in log:
            matched_logs.append(log)

    return matched_logs

#logファイル出力
logs = load_logs("sample/app.log")
if logs is None:
    print("エラーのため終了します")
else:
    error_logs = get_level_logs(logs,"ERROR")
    warning_logs = get_level_logs(logs,"WARNING")

    for log in error_logs:
        print(log)

    for log in warning_logs:
        print(log)

    print(f"ERROR件数: {len(error_logs)}")
    print(f"WARNING件数: {len(warning_logs)}")