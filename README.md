README 

Requirements:
 - python 2.7 (3 may work too)

To run, download one of the electionware txt files into this directory (we already have the Apache.txt file here to demonstrate)
Run:
> ./electionware_2_csv.py -s county_formats.csv -t <County text file name> -c "<County name>" -o <output_csv_file.csv>

For example:
> ./electionware_2_csv.py -s county_formats.csv -t Apache.txt -c "Apache" -o apache.csv

The result will be in apache.csv