# Jarvis AI

Jarvis is an autonomous assistant entrypoint in `jarvis.py`.

## Running Jarvis

From the repository root:

```bash
source .venv/bin/activate
export PYTHONPATH=.
python jarvis.py
```

## Automated mode

Use a task list file with one command per line:

```bash
python jarvis.py --tasks sample_tasks.txt
```

## Running the web UI

Start the bundled web UI server:

```bash
bash runtime/start_ui.sh
```

Then open the printed localhost URL in your browser. The startup script will attempt port 8080 first and fall back to 8081, 8082, or 8083 if that port is already in use.

The backend uses the configured `MODEL` (default `qwen2.5:3b`) and requires the corresponding Ollama model or another supported provider to be available.

## Smart memory mode

Jarvis retrieves relevant memories before each task by default. To disable that behavior:

```bash
python jarvis.py --no-smart
```

## Sample tasks

A sample task file is provided at `sample_tasks.txt`.
