#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Time   : 2024/11/3 16:51
@Author : rxccai@gmail.com
@File   : segment_handler.py
"""
from dataclasses import dataclass
from uuid import UUID

from flask import request
from injector import inject

from internal.schema.segment_schema import (
    GetSegmentsWithPageReq,
    GetSegmentsWithPageResp,
    GetSegmentResp,
    UpdateSegmentEnabledReq,
    CreateSegmentReq,
    UpdateSegmentReq
)
from internal.service import SegmentService
from pkg.paginator import PageModel
from pkg.response import validate_error_json, success_json, success_message


@inject
@dataclass
class SegmentHandler:
    segment_service: SegmentService

    def create_segment(self, dataset_id: UUID, document_id: UUID):
        """创建知识库文档片段"""
        req = CreateSegmentReq()
        if not req.validate():
            return validate_error_json(req.errors)
        self.segment_service.create_segment(dataset_id, document_id, req)
        return success_message("新增知识库文档片段成功")

    def get_segment_with_page(self, dataset_id: UUID, document_id: UUID):
        req = GetSegmentsWithPageReq(request.args)
        if not req.validate():
            return validate_error_json(req.errors)
        segments, paginator = self.segment_service.get_segment_with_page(dataset_id, document_id, req)
        resp = GetSegmentsWithPageResp(many=True)
        return success_json(PageModel(list=resp.dump(segments), paginator=paginator))

    def get_segment(self, dataset_id: UUID, document_id: UUID, segment_id: UUID):
        segment = self.segment_service.get_segment(dataset_id, document_id, segment_id)
        resp = GetSegmentResp()
        return success_json(resp.dump(segment))

    def update_segment_enabled(self, dataset_id: UUID, document_id: UUID, segment_id: UUID):
        req = UpdateSegmentEnabledReq()
        if not req.validate():
            return validate_error_json(req.errors)
        self.segment_service.update_segment_enabled(dataset_id, document_id, segment_id, req.enabled.data)
        return success_message("修改片段状态成功")

    def update_segment(self, dataset_id: UUID, document_id: UUID, segment_id: UUID):
        """根据传递的信息更新文档片段信息"""
        # 1.提取请求并校验
        req = UpdateSegmentReq()
        if not req.validate():
            return validate_error_json(req.errors)

        # 2.调用服务更新文档片段信息
        self.segment_service.update_segment(dataset_id, document_id, segment_id, req)

        return success_message("更新文档片段成功")

    def delete_segment(self, dataset_id: UUID, document_id: UUID, segment_id: UUID):
        self.segment_service.delete_segment(dataset_id, document_id, segment_id)
        return success_message("删除文档片段成功")