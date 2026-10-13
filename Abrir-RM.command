#!/bin/zsh
task_root="$(cd -- "$(dirname -- "$0")" && pwd)"
exec python3 "$task_root/serve.py"
