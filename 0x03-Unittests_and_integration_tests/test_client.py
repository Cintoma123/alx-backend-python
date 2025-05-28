#!/usr/bin/env python3 
import unittest
from unittest.mock import patch, Mock, PropertyMock
from parameterized import parameterized
from client import GithubOrgClient

class TestGithubOrgClient(unittest.TestCase):
    '''TestGithubOrgClient class tests the GithubOrgClient class'''
    @parameterized.expand([
        ("abc", {"login": "google"})
    ])
    @patch('client.get_json')
    def test_org(self, org_name, expected, mock_getjson) -> None:
        '''Test the GithubOrgClient org method'''
        mock_getjson.return_value = expected
        client = GithubOrgClient(org_name)
        result = client.org
        self.assertEqual(result, expected)


    @patch('client.get_json')
    def test_public_repos_url(self, mock_getjson) -> None:
        '''Test _public_repos_url method'''
        mock_getjson.return_value = {'repos_url': 'https://api.github.com/orgs/test/repos'}
        client = GithubOrgClient('client_test')
        result = client._public_repos_url
        self.assertEqual(result, 'https://api.github.com/orgs/test/repos')


    @patch('client.get_json')
    def test_public_repos(self, mock_getjson):
        '''Test the public_repos method'''
        result_payload = [{'name': 'repo1'}, {'name': 'repo2'}]
        with patch('client.GithubOrgClient._public_repos_url', new_callable=PropertyMock) as mock_url:
            mock_getjson.return_value = result_payload
            client = GithubOrgClient('client_test')
            mock_url.return_value = 'https://api.github.com/orgs/test/repos'
            result = client.public_repos()
            self.assertEqual(result, ['repo1', 'repo2'])
            mock_getjson.assert_called_once_with('https://api.github.com/orgs/test/repos')
            

        @parameterized.expand([
            ('valid_license', {'key': 'mit'}, True),
            ('invalid_license', {'key': 'nonexistent'}, False)
        ])

        def test_has_license(self, _, license_data, expected):
            client = GithubOrgClient('client_test')
            result = client.has_license(license_data, expected)
            self.assertEqual(result, expected)

          
            
            
          
       



