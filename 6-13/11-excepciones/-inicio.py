#!/usr/bin/env python3

try:
    10/0
except Exception as e:
    print(f'Ocurrio un error: {e}')
