#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author:    xurongzhong#126.com 
# 技术支持qq群： 144081101 591302926 567351477 钉钉免费群：21745728 
# 作者博客：https://www.jianshu.com/u/9bc194fde100
# CreateDate: 2018-1-29
# from https://pymotw.com/3/pathlib/index.html
# pathlib_resolve.py

import pathlib

usr_local = pathlib.Path('/usr/local')
share = usr_local / '..' / 'share'
print(type(share.resolve()))
print(share.resolve())
