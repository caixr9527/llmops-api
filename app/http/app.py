#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Time   : 2024/6/28 20:41
@Author : rxccai@gmail.com
@File   : app.py
"""
import dotenv
from injector import Injector

from config import Config
from internal.router import Router
from internal.server.http import Http

# 将env加载到环境变量中
dotenv.load_dotenv()
injector = Injector()
conf = Config()
app = Http(__name__, conf=conf, router=injector.get(Router))
if __name__ == "__main__":
    app.run(debug=True)