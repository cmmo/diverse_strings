# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")
def lastc_count(string, c):
    if len(string) >= 2 and string[-1] == c and string[-2] == c:
        return 2
    elif len(string) >= 1 and string[-1] == c:
        return 1
    else:
        return 0

def appendc(countc, string, c):
    if countc >= 2:
        if lastc_count(string, c) == 0:
            string += c
            countc -= 1
            string += c
            countc -= 1
        elif lastc_count(string, c) == 1:
            string += c
            countc -= 1
    elif countc == 1:
        if lastc_count(string, c) < 2:
            string += c
            countc -= 1
    return countc, string

def solution(A, B, C):
    string = ""
    elements = {
        "a":A,
        "b":B,
        "c":C
    }
    
    sorted_c = sorted(elements, key=elements.get)
    maxc = sorted_c[2]
    centerc = sorted_c[1]
    minc = sorted_c[0]

    count_maxc = elements[maxc]
    count_minc = elements[minc]
    count_centerc = elements[centerc]

    temp_count = [count_maxc, count_centerc, count_minc]
    while (count_maxc > 0 or count_minc > 0 or count_centerc > 0):
        if(count_maxc > 0):
            count_maxc,string = appendc(count_maxc, string, maxc)
        if(count_centerc > 0):
            count_centerc,string = appendc(count_centerc, string, centerc)
        if(count_maxc > 0):
            count_maxc,string = appendc(count_maxc, string, maxc)
        if(count_minc > 0):
            count_minc,string = appendc(count_minc, string, minc)

        if [count_maxc, count_centerc, count_minc] == temp_count:
            break
        else:
            temp_count = [count_maxc, count_centerc, count_minc]

    return string

if __name__ == '__main__':
    print("Start tests..")
    # assert solution(6, 1, 1) == "aabaacaa" or solution(6, 1, 1) == "aacaabaa"
    print( solution(6, 1, 1))
