import sys

sys.stderr.write('This is stderr text\n')
sys.stderr.flush()
sys.stdout.write('This is stdout text\n')

print(sys.argv)

if len(sys.argv) > 1:
    print(sys.arv[1])

#how to use arguments
#python filename.py "this is an argument"
#sys.arv outputs a list of arguments 0th argument is filename
