#!/usr/bin/env python3
import string

def main():
    return render_template('main.html')

def search():
    return render_template('main.html', error='haha, you think I have any function here?!')

if __name__ == '__main__':
    print string.printable.index('}')
