def solution(array, commands):
    answer = [sorted(array[x-1:y])[z-1] for x,y,z in commands]
    return answer