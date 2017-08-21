import sys

def write_data_file(filename, data):
    with open(filename, 'a') as f:
        for line in data:
            f.write(line + '\n')

def read_and_segregate(filename, l1, l2):
    lang1_list = []
    lang2_list = []

    with open(filename) as f:
        for line in f.readlines():
            if '<tuv xml:lang="'+ str(l1) +'">' in line:
                t1 = line.split('<seg>')[-1]
                t2 = t1.split('</seg></tuv>')[0]
                lang1_list.append(t2)
            if '<tuv xml:lang="'+ str(l2) +'">' in line:
                t1 = line.split('<seg>')[-1]
                t2 = t1.split('</seg></tuv>')[0]
                lang2_list.append(t2)

    if len(lang1_list) == len(lang2_list):
        write_data_file('data.' + str(l1), lang1_list)
        write_data_file('data.' + str(l2), lang2_list)

if __name__ == '__main__':
    if len(sys.argv) == 4:
        read_and_segregate(sys.argv[1], sys.argv[2], sys.argv[3])
    else:
        print "usage: python tmx_convertor.py <tmx_file_name> <language1> <language2>"
        sys.exit()