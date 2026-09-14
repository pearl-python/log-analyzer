from main import get_level, load_logs, save_results

def test_get_level_normal_log():
    log = "2026-09-11 10:01:00 ERROR Failed to connect database"

    level = get_level(log)

    assert level == "ERROR"

def test_get_level_invalid_log():
    log = "broken log"

    level = get_level(log)

    assert level is None

def test_load_logs_normal():
    logs, unique_levels, invalid_logs = load_logs("sample/app.log")

    assert logs is not None
    assert len(logs) == 5
    assert "INFO" in unique_levels
    assert "ERROR" in unique_levels
    assert "WARNING" in unique_levels
    assert invalid_logs == []

def test_load_logs_invalid():
    logs, unique_levels, invalid_logs = load_logs("sample/app_invalid.log")

    assert logs is not None
    assert len(logs) == 5
    assert len(invalid_logs) == 3

    assert "INFO" in unique_levels
    assert "ERROR" in unique_levels
    assert "WARNING" in unique_levels
    assert "DEBUG" in unique_levels

def test_load_logs_file_not_found():
    logs, unique_levels, invalid_logs = load_logs("sample/not_found.log")

    assert logs is None
    assert unique_levels is None
    assert invalid_logs is None

def test_save_results(tmp_path):
    output_file = tmp_path / "analysis.csv"

    logs = [
        "2026-09-11 10:00:00 INFO Application started",
        "2026-09-11 10:01:00 ERROR Database failed"
    ]
    invalid_logs = [
        "broken log"
    ]

    save_results(output_file, logs, invalid_logs)

    content = output_file.read_text(encoding="utf-8")

    assert "level,log" in content
    assert "INFO" in content
    assert "ERROR" in content
    assert "invalid" in content
    assert "broken log" in content