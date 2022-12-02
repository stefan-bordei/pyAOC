import sys, subprocess

if __name__ == '__main__':
    subprocess.call(f'python ./src/{sys.argv[1]}.py', shell=True)

