import sys
from typing import List, Type, Dict

from test import ValidTest, InvalidInitTest, InvalidUpdateTest


TestMapperType = Dict[str, Type[ValidTest | InvalidUpdateTest | InvalidInitTest]]


class RunTest:

    def __init__(self) -> None:
        self.valid_test_types: List[str] = ["valid", "invalid_init", "invalid_update"]

        self.test_mapper: TestMapperType = {"valid": ValidTest,
                                            "invalid_init": InvalidInitTest,
                                            "invalid_update": InvalidUpdateTest}

    @staticmethod
    def invalid_run() -> None:
        print("Please pass one of the valid arguments.")
        sys.exit(1)


if __name__ == "__main__":
    """        
        In order to run this tests please execute on command line
        1. Valid Test:
            python3 run_test.py valid 
            
        2. Invalid attrs on init Test:
            python3 run_test.py invalid_init
            
        3. Invalid attrs on update Test:
            python3 run_test.py invalid_update 
    """
    sys_argv: List[str] = sys.argv
    run_test = RunTest()

    if len(sys_argv) != 2:
        run_test.invalid_run()

    test_type = sys_argv[1]
    if test_type not in run_test.valid_test_types:
        print("Please pass one of the valid arguments.")
        sys.exit(1)

    print(f"START TEST: {test_type}")
    run_test.test_mapper[test_type]()
