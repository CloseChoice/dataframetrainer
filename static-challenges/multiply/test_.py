import unittest
from solution import solution
# from hypothesis import example, given, strategies as st
import pytest


def test_moped():
    assert solution(2, 5) == 10
# class TestEncoding(unittest.TestCase):
#     # @given(text())
#     def test_multiply(self):
#         self.assertEqual(solution(4, 5), 20 )

#     def test_multiply2(self):
#         self.assertEqual(solution(4, 5), 22 )

# def test_multiply():
#     assertEqual(solution(4, 5), 20 )


# def test():
#     testProgramInstance = unittest.main()
#     print(testProgramInstance)
#     return testProgramInstance.result
    
# if __name__ == "__main__":
#     print('sheeeeeeeeeeeeeeeeeesh')
#     pytest.main()
    # testProgramInstance = unittest.main()
    
    # print(testProgramInstance.result)
    # testProgramInstance.result