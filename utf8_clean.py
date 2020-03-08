from os import listdir, mkdir
from os.path import dirname, isdir, join, realpath

def main():
    program_path = dirname(realpath(__file__))
    for file in listdir(join(program_path, "raw_data")):
        if not isdir(join(program_path, "clean_data")):
            mkdir(join(program_path, "clean_data"))
        raw_path = join(join(program_path, "raw_data"), file)
        if file.endswith("videos.csv"):
            with open(raw_path, 'rb') as raw_file, \
                open(raw_path.replace(".csv", "_utf8.csv").replace("raw_data", "clean_data"), 'wb') as processed_file:
                for line in raw_file:
                    processed_file.write(line.decode('utf-8', 'replace').encode('utf-8'))

if __name__ == "__main__":
    main()