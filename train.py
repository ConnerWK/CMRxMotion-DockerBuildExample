import os
import argparse


def main():
    """
    The main function of your running scripts. 
    """
    parser = argparse.ArgumentParser()
    parser.add_argument('--input', type=str, nargs='?', default='/input', help='input directory')
    parser.add_argument('--output', type=str, nargs='?', default='/output', help='output directory')
    args = parser.parse_args()

    ## functions read and write are not real python functions, but are examples here.

    ## You can put your training scripts here
    

if __name__ == "__main__":
	main()
