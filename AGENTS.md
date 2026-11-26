# AGENTS.md - shani-chronoa-extras

Specialist tools split out of `../shani-chronoa` (history kept with `git
subtree split` of `apps/shani-sysadmin`). Read Chronoa's AGENTS.md too: its
rules (verify by execution, the shani-testbed harness, consent keys) apply here.

- **An add-on, not an app.** Every skill imports Chronoa's library through
  `shani_sysadmin/bootstrap.py`, which finds it (`$SHANI_CHRONOA_LIB`, a
  checkout at `$SHANI_CHRONOA_ROOT` or `../shani-chronoa`, then
  `/usr/lib/shani-chronoa`). Never copy Chronoa modules in here; fix them there.
- **Import name.** The package is still `shani_sysadmin`: Chronoa's shims
  (`model_registry`, `cultivation`, `merge`, `adapter`, `skills/run_command.py`,
  `skills/backup_status.py`) import it by that name. Renaming it means changing
  those shims in the same step.
- **Consent keys live in Chronoa's gsettings schema**, not here, so grants
  survive the move.
- **Tests** need a Chronoa checkout (they load its `tests/conftest.py` and
  schema): `python3 -m pytest -q tests`. GTK-free; never run anything that
  opens windows on the person's display.
- Never `git stash`. Commit messages end with the co-author line of whoever
  made the change.
