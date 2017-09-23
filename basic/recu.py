#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def fact(n):
	return fact_iter(n, 1)

def fact_iter(num, porduct):
	if num == 1:
		return porduct
	return fact_iter(num-1, num * porduct)


print(fact_iter(1000,1))