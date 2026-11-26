"""Make the app and Chronoa's shared library importable from a source checkout.

The skills that live here were moved out of Chronoa. They are still written
against Chronoa's plugin contract and still call Chronoa's shared library
modules (``files``, ``config``, ``sysfs``, ``sense_reading``, ``egress``,
``netprovision`` and ``skills.Skill``). Those modules deliberately stay in
Chronoa - they are not sysadmin-only, and moving them would fork the app.

So this module puts two directories on ``sys.path``:

* this app's root, so ``import shani_sysadmin`` works;
* Chronoa's library (a checkout beside this repo, or the installed
  ``/usr/lib/shani-chronoa``), so ``import shani_chronoa`` works.

When the app is installed as a package, Chronoa is expected to be installed
too; the fallback is for running straight from a checkout, which is how the
tests and the CLI in this repository are used.
"""

from __future__ import annotations

import os
import sys
from pathlib import Path

#: shani_sysadmin/bootstrap.py -> shani_sysadmin/ -> the repo root
APP_ROOT = Path(__file__).resolve().parents[1]


def _chronoa_root() -> Path | None:
    """A Chronoa checkout: $SHANI_CHRONOA_ROOT, else ../shani-chronoa beside this repo."""
    named = os.environ.get("SHANI_CHRONOA_ROOT", "").strip()
    if named:
        return Path(named).expanduser().resolve()
    sibling = APP_ROOT.parent / "shani-chronoa"
    return sibling if (sibling / "usr" / "lib" / "shani-chronoa").is_dir() else None


#: Chronoa's source tree when one is checked out (tests, tools/eval_cases.json,
#: the gsettings schema); None on an installed system.
CHRONOA_ROOT = _chronoa_root()
#: where `import shani_chronoa` comes from: $SHANI_CHRONOA_LIB, the checkout's
#: library, else the installed package.
CHRONOA_LIB = Path(
    os.environ.get("SHANI_CHRONOA_LIB", "").strip()
    or (CHRONOA_ROOT / "usr" / "lib" / "shani-chronoa" if CHRONOA_ROOT else "/usr/lib/shani-chronoa")
)
#: scratch space for model work (merges, distillation): Chronoa's cache/ in a
#: checkout, the user's cache dir otherwise
CACHE_DIR = (CHRONOA_ROOT / "cache") if CHRONOA_ROOT else Path(
    os.environ.get("XDG_CACHE_HOME", "") or Path.home() / ".cache") / "shani-chronoa-extras"


def install() -> tuple[Path, Path]:
    """Add both roots to sys.path, newest first, and return them."""
    for path in (CHRONOA_LIB, APP_ROOT):
        text = str(path)
        if path.is_dir() and text not in sys.path:
            sys.path.insert(0, text)
    return CHRONOA_LIB, APP_ROOT


install()
