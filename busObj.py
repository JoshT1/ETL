class Bus:

# An object used to store the business data temporarily until inserted into a database
    def __init__(self, **kwargs):
        default_values = {'companyName': 'Null', 'address': 'Null', 'execName': 'Null', 'city': 'Null',
                          'state': 'Null', 'zip': 'Null', 'cs': 'Null', 'execTit': 'Null', 'fax': 'Null',
                          'iusa': 'Null', 'empMin': 'Null', 'empMax': 'Null', 'phone': 'Null', 'sic': 'Null',
                          'recordType': 'Null', 'recordId': 'Null', 'naics': 'Null'}
        for key in default_values:
            if key in kwargs:
                default_values[key] = kwargs[key]
        self.__dict__.update(default_values)
