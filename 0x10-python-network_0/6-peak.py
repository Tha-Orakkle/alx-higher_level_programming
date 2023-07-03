#!/usr/bin/python3
"""
COntains a function that finds the peak in a list of unsorted integers
"""


def find_peak(list_of_integers):
	"""Finds the peak"""
	if list_of_integers is None or list_of_integers == []:
		return None
	
