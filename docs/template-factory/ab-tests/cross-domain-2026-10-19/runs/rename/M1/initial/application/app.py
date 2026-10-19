#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""应用入口。

用法：
    python3 app.py --root DIR COMMAND ...

COMMAND ∈ {list, preview, apply, undo}；子命令参数见 renamer_cli.build_parser()。
"""

import sys

from renamer_cli import main

if __name__ == '__main__':
    sys.exit(main())
