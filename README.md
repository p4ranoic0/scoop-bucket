# Scoop bucket for AI·mana

```powershell
scoop bucket add aimana https://github.com/p4ranoic0/scoop-bucket
scoop install usage-relay
usage-relay setup
```

`usage-relay` publishes your Claude Code and Codex usage to a file that the
[AI·mana](https://github.com/p4ranoic0/AI-mana) app reads on iPhone, iPad and Apple Watch. `setup` finds your
Claude Code and Codex data, installs the Claude statusline capture and a hidden scheduled task, and tells you which
file to choose on the iPhone. `usage-relay doctor` checks everything; `usage-relay uninstall` removes the task and
restores your statusline.

The manifest installs the Windows x86_64 ZIP from the
[AI·mana releases](https://github.com/p4ranoic0/AI-mana/releases). A daily workflow points it at the newest
release, installs it with Scoop on Windows and commits the change. Run `update` from the Actions tab right after a
release to skip the wait.
