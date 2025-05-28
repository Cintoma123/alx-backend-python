#!/usr/bin/env python3 
import unittest
from unittest.mock import patch, Mock
from utils import access_nested_map, get_json, memoize
from parameterized import parameterized



from typing import Any

class TestAccessNestedMap(unittest.TestCase):
    '''Test case for access_nested_map function'''
    @parameterized.expand([
        ({'a': '1'}, ('a',), '1'),
        ({'a': {'b': '2'}}, ('a',), {'b': '2'}),
        ({'a': {'b': '2'}}, ('a', 'b'), '2')
    ])
    def test_access_nested_map(self, nested_map: dict, path: tuple, expected_key: Any) -> None:
        result = access_nested_map(nested_map, path)
        self.assertEqual(result, expected_key, f'accessing {path} in {nested_map} should return {expected_key}')



    @parameterized.expand([
        ({}, ('a',), 'a'),
        ({'a': '1'}, ('b',), 'b'),
        ({'a': '1'}, ('a', 'b'), 'b')
    ])
    def test_access_nested_map_exception(self, nested_map: dict, path: tuple, expected_key: str) -> None:
        with self.assertRaises(KeyError) as cm:
            access_nested_map(nested_map, path)
        self.assertEqual(str(cm.exception), f"'{expected_key}'", f"KeyError for {path} should reference '{expected_key}'")

   

    class TestGetJson(unittest.TestCase):
            @parameterized.expand([
                ('example_com','https://example.com',{'payload' : True})
                ('app_com','https://app.com',{'payload' : True})
                ('example_com','https://exist.com',{'payload' : True})
                ('example_com','https://lagoon.com',{'payload' : True})
            ])
                
         
            def test_get_json(self , test_url , test_payload ,mock_get ):
              mock_get.return_value.json.return_value = test_payload 
              result = get_json(test_url)
              self.assertDictEqual(self,test_url,test_payload,mock_get) 
              mock_get.assert_called_once_with(test_url)



    
class TestMemoize(unittest.TestCase):
     def test_memoize(self):
          class TestClass:
            def a_method(self):
              return 42
          @property
          @memoize
          def a_property(self):
              return self.a_method()
          with patch.object(TestClass, 'a_method') as mock_method:
              mock_method.return_value = 42
              obj = TestClass()
              result1 = obj.a_property
              result2 = obj.a_property
              self.assertEqual(result1, 42)
              self.assertEqual(result2, 42)



         


     


        

