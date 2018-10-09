
# Playing with Build 10 Applications from Talk Python Training.  This is App 4 from that course
# Program is a journaling app.
# Tested in Python 3.7

import random
import sys
import journal

version = sys.version
print(version)

def main():
	program_header()
	run_event_loop()

def program_header():
	print('--------------------------------------------')
	print('           JOURNAL MANAGER                  ')
	print('--------------------------------------------')
	print()


def list_entries(data):
	print('Listing. . .')


def add_entry(data):
	print('Adding ...')
	text = input('Type your entry, <enter> to exit')
	# data.append(text)
	journal.add_entry(text)


def run_event_loop():

	print('What are you doing today?')
	cmd = 'EMPTY'
	journal_name = 'default'
	journal_data = journal.load(journal_name)    # List of journal entries

	while cmd != 'x' and cmd:
		cmd = input('[L]ist entries, [A]dd entry, E[x]it: ')
		cmd = cmd.lower().strip()

		if cmd == 'l':
			list_entries(journal_data)
		elif cmd =='a':
			add_entry(journal_data)
		elif cmd != 'x':
			print("Sorry, command '{}' is not a valid command".format(cmd))

	print('Done. Goodbye.')



if __name__ == "__main__":
	main()
