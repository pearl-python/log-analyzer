# Log Analyzer

A small Python command-line log analysis tool that reads a structured log file, automatically detects log levels, separates invalid log lines, and exports the analysis results to CSV.

This project was created as part of practical Python training focused on file handling, string processing, error handling, function decomposition, testing, and Git/GitHub workflow.

## Features

* Reads a text log file line by line
* Automatically detects log levels from each log entry
* Groups and displays logs by detected level
* Supports previously unknown levels such as `DEBUG`
* Separates malformed log lines from valid logs
* Handles missing input files
* Exports valid and invalid logs to CSV
* Includes automated tests with `pytest`

## Expected Log Format

The analyzer expects each valid log line to follow this format:

```text
YYYY-MM-DD HH:MM:SS LEVEL message
```

Example:

```text
2026-09-11 10:00:00 INFO Application started
2026-09-11 10:01:00 ERROR Failed to connect database
2026-09-11 10:02:00 WARNING Response is slow
```

The third whitespace-separated element is treated as the log level.

For example:

```text
2026-09-11 10:03:00 ERROR Failed to read INFO config
```

is classified as `ERROR`, even though the message itself contains the word `INFO`.

## Invalid Log Handling

A line is treated as invalid when it does not contain enough elements to extract a log level.

Example:

```text
broken log
```

Invalid lines are excluded from normal log analysis but are preserved separately and included in the CSV output.

This allows valid log entries to continue being analyzed even when malformed lines are present.

## Project Structure

```text
log-analyzer/
├─ main.py
├─ sample/
│  ├─ app.log
│  └─ app_invalid.log
├─ tests/
│  └─ test_main.py
├─ .gitignore
└─ README.md
```

`analysis.csv` is generated when the program runs and is excluded from Git tracking.

## Usage

Run the program from the project root:

```powershell
python main.py
```

The current version reads:

```text
sample/app.log
```

and prints detected log levels, counts, and matching log lines.

Example output:

```text
INFO件数: 1
2026-09-11 10:00:00 INFO Application started

ERROR件数: 2
2026-09-11 10:01:00 ERROR Failed to connect database
2026-09-11 10:03:00 ERROR Failed to read INFO config

WARNING件数: 1
2026-09-11 10:02:00 WARNING Response is slow

DEBUG件数: 1
2026-09-11 10:04:00 DEBUG Cache refreshed

不正ログ件数：3
```

## CSV Output

The program writes analysis results to:

```text
analysis.csv
```

Example:

```csv
level,log
INFO,2026-09-11 10:00:00 INFO Application started
ERROR,2026-09-11 10:01:00 ERROR Failed to connect database
WARNING,2026-09-11 10:02:00 WARNING Response is slow
invalid,broken log
```

The log level is extracted again from each valid log line when the CSV is generated.

## Main Functions

### `load_logs(file_path)`

Reads a log file and separates valid and invalid log entries.

Returns:

```python
logs, unique_levels, invalid_logs
```

If the input file does not exist:

```python
None, None, None
```

is returned.

### `get_level(log)`

Extracts the log level from a log line.

Example:

```python
get_level(
    "2026-09-11 10:01:00 ERROR Failed to connect database"
)
```

returns:

```text
ERROR
```

Malformed lines return:

```python
None
```

### `get_level_logs(logs, level)`

Returns only the log entries whose actual log-level field matches the requested level.

### `save_results(file_path, logs, invalid_logs)`

Exports valid logs and invalid lines to CSV.

## Testing

The project uses `pytest`.

Run all tests with:

```powershell
python -m pytest
```

Current tests cover:

* Normal log-level extraction
* Invalid log-level extraction
* Normal log-file loading
* Mixed valid and invalid log lines
* Missing input files
* CSV result output

Current result:

```text
6 passed
```

## Design Decisions

### Automatic log-level detection

Log levels such as `INFO`, `ERROR`, `WARNING`, or `DEBUG` are not hard-coded.

Instead, the analyzer extracts the third element of each valid log line.

This allows new log levels to be handled without modifying the filtering logic.

### Invalid lines do not stop the entire analysis

A missing input file prevents analysis completely, so processing stops.

A malformed individual line affects only that line, so it is recorded as invalid while analysis continues for the remaining valid entries.

### Exact log-level field matching

The analyzer checks the actual level field rather than searching the entire log string.

This prevents a line such as:

```text
2026-09-11 10:03:00 ERROR Failed to read INFO config
```

from being incorrectly classified as both `ERROR` and `INFO`.

## Current Limitations

* The log format must follow the expected positional structure.
* Timestamp validation is not currently performed.
* Multi-line log entries and stack traces are not parsed.
* The input file path is currently defined in `main.py`.
* The tool does not currently accept command-line arguments.

## Possible Future Improvements

* Accept input and output paths through command-line arguments
* Add stricter timestamp and log-format validation
* Support additional log formats
* Add summary-only reporting
* Add JSON output
* Refactor internal data structures if additional reporting requirements make it useful

## Technologies

* Python 3
* Standard library `csv`
* `pytest`
* Git / GitHub
