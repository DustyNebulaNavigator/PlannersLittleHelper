from typing import Dict, List

class QueryString:
    """
    self.host : should be https://localhost:8001
    """
    def __init__(self, host):
        self.host = host + "/en/001.1/api/v1/"
        
    def build_url(self, endpoint:str, expand_list: List[str]=None, select_list: List[str]=None, filter_dict: Dict[str,List[str]]=None):
        """
        Params
        ------
            db_table: str
                Manufacturing/ManufacturingOrderOperations
            expand_list: List[str]
                ['OperationRow','Part']
            select_list: List[str]
                ['Part','OperationRow','Id','WorkCenterId']
            filter_dict: Dict[str,List[str]]
                {
                'Id': ['1055163819848163782', '1054024718258726891'],
                'OrderId': ['1055163819848163782', '1054024718258726891']
                }
        Returns
        -------
            str
        """
        query_str = self.host + endpoint
        
        if expand_list or select_list or filter_dict:
            # Query must starts with '?'
            query_str += "?"
        
            if  expand_list:
                query_str += self.add_expand(expand_list)
            if select_list:
                if expand_list:
                    # Between different queries there must be 
                    query_str += "&"
                query_str += self.add_select(select_list)
                
            if filter_dict:
                if expand_list or select_list:
                    query_str += "&"
                query_str += self.add_filter(filter_dict)
                
        
        return query_str
        
 
    def add_select(self, select_list:List[str]):
        select_str = '$select='
        select_str += ",".join(select_list)
        return select_str
    
    def add_expand(self, expand_list: List[str]):
        expand_str = "$expand="
        expand_str += ",".join(expand_list)
        return expand_str
    

    def add_filter(self, filter_dict:Dict[str, List[str]]):
        """Create filter string"""
        filter_str = "$filter="

        for i, (column, values) in enumerate(filter_dict.items()):
            if len(values) == 1:
                filter_str += f"({column} eq '{values[0]}')"
            else:
                for value in values[:-1]:
                    filter_str += f"({column} eq '{value}') or "
                filter_str += f"({column} eq '{values[-1]}')"
            if i < len(filter_dict) - 1:
                filter_str += ' and '
        return filter_str
