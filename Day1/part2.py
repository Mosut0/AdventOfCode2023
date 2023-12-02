import re
import sys

LETTER_TO_NUM = {
    "one" : 1,
    "two" : 2,
    "three" : 3,
    "four" : 4,
    "five": 5,
    "six" : 6,
    "seven" : 7,
    "eight" : 8,
    "nine" : 9
}

def calibration_value(file):
    sum = 0
    with open(file) as input:
        for line in input:
            nums = re.findall(r'(?=(one|two|three|four|five|six|seven|eight|nine|\d+))', line)
            if nums:
                temp = str(LETTER_TO_NUM.get(nums[0])) if nums[0] in LETTER_TO_NUM else nums[0][0]
                temp += str(LETTER_TO_NUM.get(nums[-1])) if nums[-1] in LETTER_TO_NUM else nums[-1][-1]
            sum += int(temp)
    return sum

print(calibration_value(sys.argv[1]))
