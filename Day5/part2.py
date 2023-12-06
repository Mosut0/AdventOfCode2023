import re
import sys

with open(sys.argv[1]) as lines:
    DATA = lines.read()

PATTERNS = [
    r'seeds:([\s\d]+)',
    r'seed-to-soil map:\n([\s\d]+)',
    r'soil-to-fertilizer map:\n([\s\d]+)',
    r'fertilizer-to-water map:\n([\s\d]+)',
    r'water-to-light map:\n([\s\d]+)',
    r'light-to-temperature map:\n([\s\d]+)',
    r'temperature-to-humidity map:\n([\s\d]+)',
    r'humidity-to-location map:\n([\s\d]+)'
]

def split_list_into_subarrays(lst, n):
    return [lst[i:i + n] for i in range(0, len(lst), n)]

SEEDS = [int(num) for num in re.search(PATTERNS[0], DATA).group(1).split()]
SS = [int(num) for num in re.search(PATTERNS[1], DATA).group(1).split()]
SF = [int(num) for num in re.search(PATTERNS[2], DATA).group(1).split()]
FW = [int(num) for num in re.search(PATTERNS[3], DATA).group(1).split()]
WL = [int(num) for num in re.search(PATTERNS[4], DATA).group(1).split()]
LT = [int(num) for num in re.search(PATTERNS[5], DATA).group(1).split()]
TH = [int(num) for num in re.search(PATTERNS[6], DATA).group(1).split()]
HL = [int(num) for num in re.search(PATTERNS[7], DATA).group(1).split()]

SEEDS = split_list_into_subarrays(SEEDS, 2)
SS = split_list_into_subarrays(SS, 3)
SF = split_list_into_subarrays(SF, 3)
FW = split_list_into_subarrays(FW, 3)
WL = split_list_into_subarrays(WL, 3)
LT = split_list_into_subarrays(LT, 3)
TH = split_list_into_subarrays(TH, 3)
HL = split_list_into_subarrays(HL, 3)

def seed_to_location():
    min_location = -1
    for seed in SEEDS:
        curr_seeds = []
        for i in range(seed[1]):
            curr_seeds.append(seed[0] + i)
        for inner_seed in curr_seeds:
            print(inner_seed)
            soil = None
            for map in SS:
                if inner_seed <= map[1] + map[2] - 1 and inner_seed >= map[1]:
                    soil = inner_seed - map[1] + map[0]
            if not soil:
                soil = inner_seed
            fertilizer = None
            for map in SF:
                if soil <= map[1] + map[2] - 1 and soil >= map[1]:
                    fertilizer = soil - map[1] + map[0]
            if not fertilizer:
                fertilizer = soil
            water = None
            for map in FW:
                if fertilizer <= map[1] + map[2] - 1 and fertilizer >= map[1]:
                    water = fertilizer - map[1] + map[0]
            if not water:
                water = fertilizer
            light = None
            for map in WL:
                if water <= map[1] + map[2] - 1 and water >= map[1]:
                    light = water - map[1] + map[0]
            if not light:
                light = water
            temperature = 0
            for map in LT:
                if light <= map[1] + map[2] - 1 and light >= map[1]:
                    temperature = light - map[1] + map[0]
            if not temperature:
                temperature = light
            humidity = None
            for map in TH:
                if temperature <= map[1] + map[2] - 1 and temperature >= map[1]:
                    humidity = temperature - map[1] + map[0]
            if not humidity:
                humidity = temperature
            location = None
            for map in HL:
                if humidity <= map[1] + map[2] - 1 and humidity >= map[1]:
                    location = humidity - map[1] + map[0]
            if not location:
                location = humidity
            min_location = location if min_location < 0 else min(location, min_location)
    return min_location

print(seed_to_location())