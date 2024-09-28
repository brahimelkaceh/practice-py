import unittest
# assert 3 * 8 == 24 , 'should be equal to 24'

# def test_case_one() :
#     assert 2 + 2 == 4 , 'should be equal to 4'

# def test_case_two() :
#     assert 10 - 5 == 5 , 'should be equal to 5'

# if __name__ == '__main__':
#     test_case_one()
#     test_case_two()
#     print('All test cases passed')
    

# test_case_one()

# test_case_two() 

class TestCase(unittest.TestCase):
    def test_case_one(self):
        self.assertTrue(100 > 99 , 'should be true')
    
    def test_case_two(self):
        self.assertEqual(10 - 5, 5 , 'should be 5')

if __name__ == '__main__':
    unittest.main()