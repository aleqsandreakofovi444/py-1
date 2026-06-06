import unittest
from functions import get_allowed_users, register_user


class TestUserFunctions(unittest.TestCase):
    
    def test_register_user_in_allowed_users(self):
        """ტესტი 1: register_user("John") შედეგი უნდა იყოს get_allowed_users() სიაში"""
        result = register_user("John")
        allowed_users = get_allowed_users()
        self.assertIn(result, allowed_users)
    
    def test_users_in_list(self):
        """ტესტი 2: "john" და "alice" უნდა იყვნენ სიაში"""
        allowed_users = get_allowed_users()
        self.assertIn("john", allowed_users)
        self.assertIn("alice", allowed_users)
    
    def test_user_not_in_list(self):
        """ტესტი 2: "dato" არ უნდა იყოს სიაში"""
        allowed_users = get_allowed_users()
        self.assertNotIn("dato", allowed_users)


if __name__ == '__main__':
    unittest.main()
