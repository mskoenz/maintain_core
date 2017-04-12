#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Author:  Mario S. Könz <mskoenz@gmx.net>
# Date:    11.04.2017 06:58:10 CEST
# File:    spez_instances_sql.py

import os
from addon import core


def sql_setup(tbl):
    return """ALTER TABLE {0} ADD input INT;
              ALTER TABLE {0} ADD output INT;
           """.format(tbl)


def sql_to_dict(path, js):
    param = js.cmd_param

    res = dict(tag=param.input)

    with open(path + "/out.txt", "r") as f:
        l = f.readlines()

    for e in l:
        k, v = e.strip().split(" ", 1)
        res[k] = core.to_number(v)

    return res


def sql_dupl_case(tbl):
    return """UPDATE {} SET tag=tag || ', ' || :tag WHERE m5c=:m5c AND tag NOT LIKE '%'||:tag||'%'""".format(
        tbl)
