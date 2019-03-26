def day2_eval1(array):
    assert array.size == 100
    assert array.dtype == int
    print('Good Job!!')

def day2_eval2(array):
    assert array.size == 120
    assert array.shape[0] == 3
    assert array.shape[1] == 10
    assert array.shape[2] == 4
    print('Good Job!!')

def day3_eval1(array):
    assert array.size == 3
    assert '%3.f'%array[0] == '%3.f'%0.8597599607509335
    assert '%3.f'%array[1] == '%3.f'%0.26231767425972424
    assert '%3.f'%array[2] == '%3.f'%0.32748134
    print('Good Job!!')

def day3_eval2(array):
    assert array.size == 3
    assert '%3.f'%array[0] == '%3.f'%-13.867192
    assert '%3.f'%array[1] == '%3.f'%1.185539
    assert '%3.f'%array[2] == '%3.f'%10.226000
    print('Good Job!!')

