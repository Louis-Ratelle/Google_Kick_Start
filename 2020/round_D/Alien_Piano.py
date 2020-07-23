import math

def calc_runs(notes, nb_pitches = 4):
    seq_runs = []
    is_increasing = True
    run_length = 1
    for i in range(1, len(notes)):
        note = notes[i]
        prev_note = notes[i-1]
        if prev_note < note:
            if is_increasing:
                run_length += 1
            else:
                seq_runs.append(run_length)
                is_increasing = True
                run_length = 2
        elif prev_note > note:
            if is_increasing is False:
                run_length += 1
            else:
                seq_runs.append(run_length)
                is_increasing = False
                run_length = 2
    seq_runs.append(run_length)
    return seq_runs


if __name__ == '__main__':
    T = int(input())
    for t in range(1, T + 1):
        K = int(input())
        notes = list(map(int, input().split()))
        seq_runs = calc_runs(notes)
        sol = [((run-1)//4) for run in seq_runs if run]
        sol = sum(sol)
        print("Case #{}: ".format(t) + str(sol))


""" 
1
17 
0 1 2 3 4 3 2 1 0 1 2 3 4 3 2 1 0
"""