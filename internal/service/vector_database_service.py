#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Time   : 2024/8/21 22:12
@Author : rxccai@gmail.com
@File   : vector_database_service.py
"""
import os

import weaviate
from injector import inject
from langchain_core.vectorstores import VectorStoreRetriever
from langchain_weaviate import WeaviateVectorStore
from weaviate import WeaviateClient
from weaviate.collections import Collection

from .embeddings_service import EmbeddingsService

COLLECTION_NAME = "Dataset"


@inject
class VectorDatabaseService:
    """向量数据库服务"""
    client: WeaviateClient
    vector_store: WeaviateVectorStore
    embeddings_service: EmbeddingsService

    def __init__(self, embeddings_service: EmbeddingsService):
        """构造函数，完成向量数据库服务客户端和LangChain向量数据库示例创建"""
        self.embeddings_service = embeddings_service
        # 1. 创建/连接weaviate向量数据库
        self.client = weaviate.connect_to_local(
            host=os.getenv("WEAVIATE_HOST"),
            port=int(os.getenv("WEAVIATE_PORT"))
        )
        # # todo 这里使用text-embedding-3-small
        # embedding = HuggingFaceEndpointEmbeddings(
        #     model="sentence-transformers/all-MiniLM-L12-v2",
        # )
        # 2. 创建LangChain向量数据库
        self.vector_store = WeaviateVectorStore(
            client=self.client,
            index_name=COLLECTION_NAME,
            text_key="text",
            embedding=self.embeddings_service.embeddings
        )

    def get_retriever(self) -> VectorStoreRetriever:
        """获取检索器"""
        return self.vector_store.as_retriever()

    @property
    def collection(self) -> Collection:
        return self.client.collections.get(COLLECTION_NAME)
