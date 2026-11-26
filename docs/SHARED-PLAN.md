# shani-chronoa-extras: its part of the shared architecture

The plan for all repos is `../shani-shell/docs/SHARED-ARCHITECTURE.md` (https://github.com/shani8dev/shani-shell/blob/master/docs/SHARED-ARCHITECTURE.md). Read it first; its rules apply
here. This file is only this repo's part; change the plan there, not here.

**Role:** specialist skills on Chronoa's contract (an add-on).

**Do as much of this as your task allows** (never breaking a consumer), and
add a line to the plan's Status section when you finish something:

- Do not add a copy of something the shell's bridges or Cassini already do: note it in `../shani-shell/docs/CAPABILITY-INVENTORY.md` instead; the registry will serve both.
- When a domain service exists, call it instead of re-reading the system.
- Keep the `shani_sysadmin` import name until Chronoa's shims move with it.
