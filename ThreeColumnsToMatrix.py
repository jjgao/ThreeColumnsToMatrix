#!/usr/bin/python
import sys

rows = []
cols = []
values = {}

file = open(sys.argv[1])
for line in file:
	if line.startswith("#"):
		continue
	parts = line.split("\t",3)
	if parts[0] not in rows:
		rows.append(parts[0])
	if parts[1] not in cols:
		cols.append(parts[1])
	if parts[0] not in values:
		values[parts[0]] = {}
	values[parts[0]][parts[1]] = parts[2].strip()
file.close()

# print column headers
for col in cols:
	print "\t"+col,
print

# print rows
for row in rows:
	print row,
	for col in cols:
		print "\t",
		if col in values[row]:
			print values[row][col],
	print
