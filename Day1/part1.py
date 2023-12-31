import re
import sys

def calibration_value(file):
    sum = 0
    with open(file) as input:
        for line in input:
            nums = re.findall(r'\d+', line)
            if nums:
                sum += int(nums[0][0] + nums[-1][-1])
    return sum

print(calibration_value(sys.argv[1]))
