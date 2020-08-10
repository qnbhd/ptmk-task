# This is a ptmk test task
# author: Templin Konstantin (qnbhd)
# 10 aug, 2020
import sys
from ptmkworker import PtmkWorker

CASE_MIN_ARGS_COUNT = 2
CASE_MAX_ARGS_COUNT = 7

if __name__ == '__main__':
    if len(sys.argv) < CASE_MIN_ARGS_COUNT or len(sys.argv) > CASE_MAX_ARGS_COUNT:
        raise TypeError('Incorrect input arguments set')

    choosed_word_id = int(sys.argv[1]) - 1

    worker = PtmkWorker()
    handlers = [
        worker.create_bd_handler,
        worker.create_record_handler,
        worker.out_unique_records_handler,
        worker.random_creator_handler,
        worker.sample_handler,
        worker.out_first_records,
    ]

    args = sys.argv[2:]
    kwargs = {}

    if len(args) > 0:
        # create user case
        kwargs = {
            'fullname': args[0:3],
            'born_date': args[3],
            'gender': args[4]
        }

    try:
        current_handler = handlers[choosed_word_id]
        current_handler(**kwargs)
    except IndexError:
        print('Incorrect work id')
    except TypeError:
        print('Incorrect input arguments set')
