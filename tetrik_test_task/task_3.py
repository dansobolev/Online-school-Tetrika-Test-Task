def appearance(intervals):
    lesson_time = intervals['lesson']
    lesson_start, lesson_end = lesson_time[0], lesson_time[1]
    lesson_time = list(range(lesson_start, lesson_end))

    pupil = intervals['pupil']
    pupil_list = [pupil[x:x + 2] for x in range(0, len(pupil), 2)]
    pupil_all_range = set()
    for pupil_range in pupil_list:
        start, end = pupil_range[0], pupil_range[1]
        pupil_all_range.update(list(range(start, end)))

    tutor = intervals['tutor']
    tutor_list = [tutor[x:x + 2] for x in range(0, len(tutor), 2)]
    tutor_all_range = set()
    for tutor_range in tutor_list:
        start, end = tutor_range[0], tutor_range[1]
        tutor_all_range.update(list(range(start, end)))

    return len(tutor_all_range.intersection(pupil_all_range).intersection(lesson_time))


tests = [
    {'data': {'lesson': [1594663200, 1594666800],
             'pupil': [1594663340, 1594663389, 1594663390, 1594663395, 1594663396, 1594666472],
             'tutor': [1594663290, 1594663430, 1594663443, 1594666473]},
     'answer': 3117
    },
    {'data': {'lesson': [1594702800, 1594706400],
             'pupil': [1594702789, 1594704500, 1594702807, 1594704542, 1594704512, 1594704513, 1594704564, 1594705150, 1594704581, 1594704582, 1594704734, 1594705009, 1594705095, 1594705096, 1594705106, 1594706480, 1594705158, 1594705773, 1594705849, 1594706480, 1594706500, 1594706875, 1594706502, 1594706503, 1594706524, 1594706524, 1594706579, 1594706641],
             'tutor': [1594700035, 1594700364, 1594702749, 1594705148, 1594705149, 1594706463]},
    'answer': 3577
    },
    {'data': {'lesson': [1594692000, 1594695600],
             'pupil': [1594692033, 1594696347],
             'tutor': [1594692017, 1594692066, 1594692068, 1594696341]},
    'answer': 3565
    },
]


if __name__ == '__main__':
    for i, test in enumerate(tests):
        test_answer = appearance(test['data'])
        assert test_answer == test['answer'], f'Error on test case {i}, got {test_answer}, expected {test["answer"]}'
