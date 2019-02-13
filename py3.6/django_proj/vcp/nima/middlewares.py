#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.utils.deprecation import MiddlewareMixin

class ResponsePhaser(MiddlewareMixin):
    """
    该模块仅用于本地测试
    通过设置响应头来允许跨域请求
    """
    def process_response(self,request,response):
        response['Access-Control-Allow-Origin'] = '*'
        return response
