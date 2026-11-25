"""Install an isolated brain into a new/empty directory. Python standard library only."""
import argparse
import json
import shutil
import sys
from pathlib import Path

parser = argparse.ArgumentParser(description=__doc__)
parser.add_argument('destination', type=Path)
parser.add_argument('--enable-hooks', action='store_true')
args = parser.parse_args()
source = Path(__file__).resolve().parent / 'template-vault'
dest = args.destination.expanduser().resolve()
if dest.exists() and (not dest.is_dir() or any(dest.iterdir())):
    parser.error('Destination must be a new or empty directory; existing files are never overwritten.')
if dest == source or source in dest.parents:
    parser.error('Choose a destination outside the template.')
shutil.copytree(source, dest, dirs_exist_ok=True)
if args.enable_hooks:
    # Quote absolute interpreter and script paths for shells on Windows and POSIX.
    import shlex
    import subprocess
    def command(mode):
        parts = [sys.executable, str(dest / '.claude/hooks/memory.py'), mode]
        return subprocess.list2cmdline(parts) if sys.platform == 'win32' else shlex.join(parts)
    hooks = {event: [{'hooks': [{'type': 'command', 'command': command(mode)}]}]
             for event, mode in [('SessionStart', 'load'), ('UserPromptSubmit', 'context')]}
    (dest / '.claude/settings.json').write_text(json.dumps({'hooks': hooks}, indent=2) + '\n')
print(f'Installed at {dest}. Open this folder in your AI client and say: Set up my brain.')
