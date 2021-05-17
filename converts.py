import sys
"""
Converts one minute timeframe to 5 min, 15 min, 1 hour, 1 day
python converts.py fileSource fileResult timeFrame
fileSource - one minutes time frame
timeFrame - M5 M15 H1 D1
"""


def natural_min(a :str) -> int:
    """converts a time string to an absolute number of minutes
    105200 HHMMSS  -> (10 * 60 + 52) = 652"""
    return int(a[0:2]) * 60 + int(a[2:4])

def main():

    print("Input name file -", sys.argv[1])
    print("Output name file -", sys.argv[2])
    cat = sys.argv[3]
    print("Time frame -", cat)

    if   cat ==  "M5" : cp = 5
    elif cat == "M15" : cp = 15
    elif cat ==  "H1" : cp = 60
    elif cat ==  "D1" : cp = 1440
    else:
        print("Invalid time")
        raise SystemExit(1)

    print ("Time ", cp)

    file_source = open(sys.argv[1],'r')
    file_fesult = open(sys.argv[2],'w')

    y = "0000"

    for s in file_source:

        arg = s.split(',')

        #write header
        if arg[0] == """<TICKER>""":
            file_fesult.write(s)
            continue

        t = natural_min(arg[3])
        if (t%cp == 0) :
            rec_start = "{0},{1},{2},{3},{4}".format(*arg)
            p_max   = arg[5]
            p_min   = arg[6]
            p_vol   = int (arg[8])
        else:
            if float(p_max) < float(arg[5]): p_max = arg[5]
            if float(p_min) > float(arg[6]): p_min = arg[6]
            p_vol += int (arg[8])

            if (t%cp == cp-1) :
                file_fesult.write(f"{rec_start},{p_max},{p_min},{arg[7]},{p_vol}\n")

        #report year
        a = arg[2][0:4]
        if (y != a):
            y = a
            print(y)


    file_fesult.close()
    file_source.close()

if __name__ == '__main__': main()
