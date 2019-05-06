# coding: utf-8

r"""Custom exceptions definition"""


class GeneralException(Exception):
    r"""Base class for custom exceptions"""
    pass


class ConnectError(GeneralException):
    r"""Custom exception : connection error"""
    pass


class ProcessingBreak(GeneralException):
    r"""Custom exception : processing break"""
    pass


class ProcessingError(GeneralException):
    r"""Custom exception : processing error"""
    pass
