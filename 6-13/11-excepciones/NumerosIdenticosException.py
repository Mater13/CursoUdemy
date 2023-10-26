#!/usr/bin/env python3
class NumerosIdenticosException(Exception):

    def __init__(self, mensaje):
        self.message = mensaje
