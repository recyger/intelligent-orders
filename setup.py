#!/usr/bin/env python3
# -*- coding: utf-8 -*-
__author__ = 'VLADISLAV'

import importlib
import pip


def install_modules(modules):
    """
        Установка необходимых модулей
    :param modules:
    """
    for module in modules:
        if importlib.util.find_spec(module) is None:
            pip.main(['install', module])

if __name__ == '__main__':
    install_modules(('bottle', 'pony'))