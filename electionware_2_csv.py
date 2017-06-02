#!/usr/bin/python

# electionware_2_csv.py
# convert electionware file to CSV

import argparse
import csv

parser = argparse.ArgumentParser(formatter_class=argparse.RawDescriptionHelpFormatter, description='Convert electionware file to CSV')
parser.add_argument('-s', '--format_spec_file', required=True, type=str, help="CSV file from CountyData_ElectionWare worksheet", action='store')
parser.add_argument('-t', '--text_file', required=True, type=str, help="electionware text file to be converted")
parser.add_argument('-c', '--county_name', required=True, type=str, help="name of county. Case sensitive, wrap in quotes if multiple words.")
parser.add_argument('-o', '--output_file', required=True, type=str, help="csv file for output")


class CountyParser:
    def __init__(self, format_specfilename, county_name):
        self.col_indices_map = dict()
        with open(format_specfilename, 'rb') as csvfile:
            format_reader = csv.reader(csvfile, delimiter=",", quotechar="\"")
            for row in format_reader:
                if row[0].strip().lower() == county_name.strip().lower():
                    # print "Adding row:{}".format(row[1])
                    self.col_indices_map[row[1]] = (int(row[2]), int(row[3]))

        if len(self.col_indices_map) == 0:
            raise Exception("County not specified in format specfile: {}".format(county_name))

    def parse_line(self, line):
        ans=dict()
        for k in self.col_indices_map:
            ans[k] = line[self.col_indices_map[k][0]-1: self.col_indices_map[k][1]].strip()
        return ans

    def convert_text_file(self, text_filename, csv_filename):
        cols = list(self.col_indices_map.keys())
        with open(csv_filename, 'wb') as csv_file:
            writer = csv.writer(csv_file, delimiter=",", quotechar="\"")
            writer.writerow(cols)
            with open(text_filename, 'rb') as tf:
                for line in tf:
                    parsed = self.parse_line(line)
                    writer.writerow(map(lambda x: parsed.get(x, ''), cols))

if __name__ == "__main__":
    args = parser.parse_args()
    parser = CountyParser(args.format_spec_file, args.county_name)
    parser.convert_text_file(args.text_file, args.output_file)
