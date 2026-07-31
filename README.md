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

## Smart memory mode

Jarvis retrieves relevant memories before each task by default. To disable that behavior:

```bash
python jarvis.py --no-smart
```

## Sample tasks

A sample task file is provided at `sample_tasks.txt`.
