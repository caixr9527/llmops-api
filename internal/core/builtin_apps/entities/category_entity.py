#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Time    : 2025/01/02 22:02
@Author  : rxccai@gmail.com
@File    : category_entity.py
"""
from pydantic import BaseModel, Field


class CategoryEntity(BaseModel):
    """内置工具分类实体"""
    category: str = Field(default="")  # 分类唯一标识
    name: str = Field(default="")  # 分类对应的名称