import pickle
from athletelist import AthleteList


def get_coach_data(filename):
    try:
        with open(filename) as f:
            data = f.readline().strip().split(',')
        return AthleteList(data.pop(0), data.pop(0), data)
    except IOError as err:
        print('Error'+str(err))
        return None


def put_to_store(file_list):
    all_athlete = {}
    for each_file in file_list:
        ath = get_coach_data(each_file)
        all_athlete[ath.name] = ath
    try:
        with open('../file/athlete.pickle', 'wb') as ahf:
            pickle.dump(all_athlete, ahf)
    except IOError as ioerr:
        print('IoError'+str(ioerr))
    return all_athlete


def get_from_store():
    all_athlete = {}
    try:
        with open('../file/athlete.pickle', 'rb') as ahf:
            all_athlete = pickle.load(ahf)
    except IOError as ioerr:
        print('IoError'+str(ioerr))
    return all_athlete
