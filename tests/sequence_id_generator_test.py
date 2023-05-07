import src.sequencial_id_generator as sequence_id_generator
import time
import datetime


def test_sequencialIdGenerator():
    seq_id_gen = sequence_id_generator.SequentialIdGenerator(10)

    result = 0
    for i in range(10):
        result = next(seq_id_gen)
        print(f"{i}: {result}")
    assert result == 19


def test_sequence_id_gen():
    result = 0
    for id_x, val in enumerate(
        sequence_id_generator.alternate_sequence_id_gen(num_to_generate=10, root=10)
    ):
        result = val
        print(f"{id_x}: {val}")
    assert result == 19


def test_sequence_k_sortable():
    base_epoch = int(datetime.datetime(2023, 1, 1).timestamp())
    k_sortable_generator = sequence_id_generator.KSortableSequenceIdGenerator(
        base_epoch=base_epoch
    )
    results = set()
    for i in range(10):
        if i == 5:
            time.sleep(1)
        result = next(k_sortable_generator)
        results.add(result)
        print(f"{i}: {result}")
    assert len(results) == 10
