from sys import stdin, stdout
from re import search
def main():
	# stdin = open('input.txt', 'r')
	stdout.write("#Color\n" if search('C|M|Y', stdin.read()) else "#Black&White\n")
main()