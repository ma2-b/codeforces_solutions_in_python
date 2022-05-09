from sys import stdin, stdout
from sys import stdin, stdout
def main():
	a, b, c = tuple(map(int, stdin.read().split()))
	stdout.write(str(max(a+b+c, a+b*c, (a+b)*c, a*b+c, a*(b+c), a*b*c)) + '\n')
if __name__ == '__main__':
	main()