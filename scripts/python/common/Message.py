#!/usr/bin/env python3
# @file      Message.py
# @author    Sergey Baigudin, sergey@baigudin.software
# @copyright 2023, Sergey Baigudin, Baigudin Software

import sys
from common.System import System

class Message:

    OK = 1
    ERR = 2
    INF = 3
    NOR = 4

    @staticmethod
    def out(string, status=None, is_block=None):
        color_bgn = Message.__COLOR_END
        color_end = Message.__COLOR_END

        if status == Message.OK:
            color_bgn = Message.__COLOR_OK
        elif  status == Message.ERR:
            color_bgn = Message.__COLOR_ERR
        elif status == Message.INF:
            color_bgn = Message.__COLOR_INF
        elif status == Message.NOR:
            color_bgn = Message.__COLOR_NOR
        else:
            color_bgn = Message.__COLOR_END

        if System.is_win32():
            color_bgn = ''
            color_end = ''            

        if is_block is not True:
            print(color_bgn + string + color_end, flush=True)
        else:
            print(color_bgn + '-------------------------------------------------------------------------------' + color_end, flush=True)
            print(color_bgn + ' ' + string + color_end, flush=True)
            print(color_bgn + '-------------------------------------------------------------------------------' + color_end, flush=True)
            

    __COLOR_OK  = '\033[32m'
    __COLOR_ERR = '\033[31m'
    __COLOR_INF = '\033[93m'    
    __COLOR_NOR = '\033[0m'
    __COLOR_END = '\033[0m'
