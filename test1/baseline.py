import sys
import pathlib
from argparse import ArgumentParser

def copy_file(source: pathlib.Path, dest: pathlib.Path) -> None:
    with open(source, "r", encoding = 'utf8') as fp_1:
        with open(dest, "w", encoding = 'utf8') as fp_2:
            for line in fp_1:
                fp_2.write(line)

def main() -> None:
    parser = ArgumentParser()
    parser.add_argument('-source', type = pathlib.Path)
    parser.add_argument('-dest', type = pathlib.Path)
    args = parser.parse_args()
    copy_file(args.source, args.dest)

if __name__ == "__main__":    
    sys.exit(main())
