#log読み込み関数
def load_logs(file_path):
    logs = []
    with open(file_path,"r",encoding="utf-8") as file:
        for log in file:
            logs.append(log.strip())
    return logs

#エラー行特定関数
def get_error_logs(logs):
    error_logs = []
    for log in logs:
        if "ERROR" in log:
            error_logs.append(log)
    return error_logs

def get_warning_logs(logs):
    warning_logs = []
    for log in logs:
        if "WARNING" in log:
            warning_logs.append(log)
    return warning_logs

#logファイル出力
logs = load_logs("sample/app.log")
error_logs = get_error_logs(logs)
warning_logs = get_warning_logs(logs)

for log in error_logs:
    print(log)

for log in warning_logs:
    print(log)

print(f"ERROR件数: {len(error_logs)}")
print(f"WARNING件数: {len(warning_logs)}")