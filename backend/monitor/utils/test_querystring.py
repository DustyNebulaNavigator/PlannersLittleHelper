import unittest
from querystring import QueryString

class TestQueryString(unittest.TestCase):

    def setUp(self):
        self.qs = QueryString("")

    def test_no_query_parameters(self):
        self.assertEqual(self.qs.build_url("db_table"), "/en/001.1/api/v1/db_table")

    def test_select_one(self):
        self.assertEqual(self.qs.build_url("db_table", select_list=['Part']), "/en/001.1/api/v1/db_table?$select=Part")
    
    def test_select_three(self):
        self.assertEqual(self.qs.build_url("db_table", select_list=['Part', 'OperationRow', 'Id']), "/en/001.1/api/v1/db_table?$select=Part,OperationRow,Id")

    def test_expand_one(self):
        self.assertEqual(self.qs.build_url("db_table", expand_list=['Part']), "/en/001.1/api/v1/db_table?$expand=Part")
    
    def test_expand_three(self):
        self.assertEqual(self.qs.build_url("db_table", expand_list=['Part', 'OperationRow', 'Id']), "/en/001.1/api/v1/db_table?$expand=Part,OperationRow,Id")

    def test_filter_one(self):
        self.assertEqual(self.qs.build_url("db_table", filter_dict={'Id': ['101', '102', '103']}), "/en/001.1/api/v1/db_table?$filter=(Id eq '101') or (Id eq '102') or (Id eq '103')")
    
    def test_filter_three(self):
        self.assertEqual(self.qs.build_url("db_table", filter_dict={'Id': ['101', '102', '103'], 'Part': ['a', 'b'], 'Tool': ['g']}), "/en/001.1/api/v1/db_table?$filter=(Id eq '101') or (Id eq '102') or (Id eq '103') and (Part eq 'a') or (Part eq 'b') and (Tool eq 'g')")

    def test_expand_select_one(self):
        self.assertEqual(self.qs.build_url("db_table", expand_list=['Part'], select_list=['Part']), "/en/001.1/api/v1/db_table?$expand=Part&$select=Part")
    
    def test_expand_select_filter_one(self):
        self.assertEqual(self.qs.build_url("db_table", expand_list=['Part'], select_list=['Part'], filter_dict={'Id': ['101', '102', '103']}), "/en/001.1/api/v1/db_table?$expand=Part&$select=Part&$filter=(Id eq '101') or (Id eq '102') or (Id eq '103')")

if __name__ == "__main__":
    unittest.main()