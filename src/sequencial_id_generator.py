import time
import boto3


class SequentialIdGenerator:
    def __init__(self, root: int = 0):
        self.root = root
        self.curr = self.root

    def __next__(self):
        return_me = self.curr
        self.curr += 1
        return return_me


def alternate_sequence_id_gen(num_to_generate: int, root: int = 0):
    curr = root
    for i in range(num_to_generate):
        temp = curr
        curr += 1
        yield temp


class KSortableSequenceIdGenerator:
    # returns 64 bit sequence, the first is the sign (0 for positive),
    # second comes the datetime as this keeps it k-sortable within a second
    # third is the machine id so that it can be scaled to other machines
    # fourth is the local sequence which loops when it reaches its max locally

    SEQ_BITS: int = 12  # 4096 max
    MACHINE_ID_BITS: int = 10  # 1024 max
    DATETIME_BITS: int = 41  # 69.7 years till overflow
    SIGN_BIS: int = 1  # keep it positive

    def __init__(self, base_epoch: int = 0):
        self.base_epoch = base_epoch
        self.curr_seq = 0

    def __get_current_epoch(self) -> int:
        # This has to be a number less than or equal to 2 ** self.DATETIME_BITS
        return_me: int = 0
        curr_epoch: int = int(time.time())  # seconds since 1/1/1970
        return_me = curr_epoch - self.base_epoch
        if return_me <= (2**self.DATETIME_BITS):
            return return_me
        else:
            raise Exception(
                f"epoch: {return_me} exceeds {self.DATETIME_BITS} bit maximum"
            )

    def __get_machine_id(self) -> int:
        # this has to be a number less than or equal to 2 ** self.MACHINE_ID_BITS
        # this should read from a config variable for this deployed instance
        return 1

    def __next__(self):
        return_me: int = 0
        epoch_part = self.__get_current_epoch() << (
            self.SEQ_BITS + self.MACHINE_ID_BITS
        )
        machine_id_part = self.__get_machine_id() << self.SEQ_BITS
        return_me = epoch_part | machine_id_part | self.curr_seq

        if self.curr_seq < (2**self.SEQ_BITS):
            self.curr_seq += 1
        else:
            self.curr_seq = 0

        return return_me


class KSortableSequenceIdGenerator_WithAtomicDynamoDb:
    # returns 64 bit sequence, the first is the sign (0 for positive),
    # second comes the datetime as this keeps it k-sortable within a second
    # third is the atomic dynamodb sequence which is based off the epoch, so that many ids per second is supported

    SEQ_BITS: int = 22  # 4194304 max
    DATETIME_BITS: int = 41  # 69.7 years till overflow
    SIGN_BIS: int = 1  # keep it positive

    def __init__(self, base_epoch: int = 0):
        self.base_epoch = base_epoch
        self.curr_seq = 0

    def __get_current_epoch(self) -> int:
        # This has to be a number less than or equal to 2 ** self.DATETIME_BITS
        return_me: int = 0
        curr_epoch: int = int(time.time())  # seconds since 1/1/1970
        return_me = curr_epoch - self.base_epoch
        if return_me <= (2**self.DATETIME_BITS):
            return return_me
        else:
            raise Exception(
                f"epoch: {return_me} exceeds {self.DATETIME_BITS} bit maximum"
            )

    def __get_curr_seq(self, current_epoch) -> int:
        return_me: int = 0
        id_table = boto3.resource("dynamodb").Table("atomic_ids")

        resp = id_table.update_item(
            Key={"timestamp": current_epoch},
            UpdateExpression="ADD id_counter :inc SET expiry=:exp",
            ExpressionAttributeValues={":inc": 1, ":exp": current_epoch + 20},
            ReturnValues="UPDATED_NEW",
        )
        return_me = int(resp["Attributes"]["id_counter"])
        return return_me

    def __next__(self):
        return_me: int = 0
        epoch_part = self.__get_current_epoch() << self.SEQ_BITS
        current_seq_part = self.__get_curr_seq(current_epoch=epoch_part)
        return_me = epoch_part | current_seq_part

        return return_me
