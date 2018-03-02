#the program read a big file with a certain number of lines and produce output.
import pandas as pd
import argparse
import logging

def get_parser():
    """Get parser for command line arguments."""
    parser = argparse.ArgumentParser(description="Extract a part of file for testing purpose")
    parser.add_argument("-i",
                        "--inputfile",
                        dest="input",
                        help="File name of the input csv file",
                        default=None)

    parser.add_argument("-o",
                        "--outputfile",
                        dest="output",
                        help="Output csv file",
                        default="output.csv")

    parser.add_argument("-c",
                        "--count",
                        dest="count",
                        help="Line count to be extracted",
                        default="2000")

    return parser


if __name__ == '__main__':
    parser = get_parser()
    args = parser.parse_args()

    fileInput = args.input
    fileOutput = args.output
    count = int(args.count)

    fp = pd.read_csv(fileInput, sep=',', header=None, chunksize=count)

    if ".csv" not in fileOutput:
        fileOutput = fileOutput + '.csv'

    for line in fp:
        # f.write(line)  # python will convert \n to os.linesep
        line.to_csv(fileOutput, index=False, header=None)
        break

    logging.warning("Done")
