# Playing with Build 10 Applications from Talk Python Training.  This is a support file for App 4 from that course
# Program is a journaling app, and this is the journal module handling journal i/o
# Tested in Python 3.7

"""
This is the journal module
"""

import os


def get_full_pathname(name: object) -> object:
    """
    :rtype: object
    """
    filename = os.path.abspath(os.path.join('.', 'journals', name + '.jrl'))
    return filename


def load(name):
    """
    Method to create and load new journal
    :param name: base of the journal to load
    :return: a new journal data structure with file data

	data = []
	filename = get_full_pathname(name)


if os.path.exists(filename):
	with open(filename) as fin:
		for entry in fin.readlines():
			print("loading: " + entry.rstrip())

	return data
	"""
    return []


def save(name, journal_data):
	filename = os.path.abspath(os.path.join('./journals/', name+ '.jrl'))
	print("saving to......... {}".format(filename))

	fout = open(filename, 'w')
	# with open(filename) as fout:
	for entry in journal_data:
		fout.write(entry + '\n')


def add_entry(text, journal_data):
	journal_data.append(text)
