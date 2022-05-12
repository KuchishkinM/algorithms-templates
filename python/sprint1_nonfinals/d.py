from typing import List


def get_weather_randomness(temperatures: List[int]) -> int:
    day_counter = 0
    if len(temperatures) == 1:
        day_counter += 1
    if len(temperatures) > 1 and temperatures[0] > temperatures[1]:
        day_counter += 1
    if len(temperatures) > 1 and temperatures[-1] > temperatures[-2]:
        day_counter += 1
    if len(temperatures) > 1:
        for i in range(1, len(temperatures) - 1):
            if (temperatures[i] > temperatures[i - 1]
                    and temperatures[i] > temperatures[i + 1]):
                day_counter += 1
    return day_counter


def read_input() -> List[int]:
    n = int(input())
    temperatures = list(map(int, input().strip().split()))
    return temperatures


temperatures = read_input()
print(get_weather_randomness(temperatures))
