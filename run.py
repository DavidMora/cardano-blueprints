#!/usr/bin/env python

# model import is required to set up database correctly
from app import create_app
from config import base


app = create_app(base)


if __name__ == '__main__':
    app.run(host=base.HOST)
