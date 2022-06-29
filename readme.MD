2 new classes that support UniqueValues.

**`UniqueValueDict()`**

* UniqueValueDict is `dict` that enforces uniques of values.
                                    
            ```
            unique_dict_value = UniqueValueDict()
            
            unique_dict_value['a'] = 0
            unique_dict_value['b'] = 3
            
            unique_dict_value.update({'a': 2})
            
            ======================================
            {'a': 2, 'b': 3}
            ```
            
* in case we use the same value it will raise `NotUniqueValueDictError`

            ```
            unique_dict_value = UniqueValueDict()
            
            unique_dict_value['a'] = 0
            unique_dict_value['b'] = 3
            
            unique_dict_value.update({'a': 3})
            
            ======================================
            NotUniqueValueDictError exception.
            ```
                  
**`UniqueAttrClass()`**

* UniqueAttrClass is a class that enforces uniques of attribute values that is based on `UniqueValueDict` class

            ```
            unique_attr_class = UniqueAttrClass()
            
            unique_attr_class.attr_1 = 0
            unique_attr_class.attr_2 = 3
            
            setattr(unique_attr_class, 'attr_1', '0')
            
            ======================================
            UniqueAttrClass(attr_1='0', attr_2=3)
            ```
            
* in case we use the same value it will raise `NotUniqueValueAttrError`

            ```
            unique_attr_class = UniqueAttrClass()
            
            unique_attr_class.attr_1 = 0
            unique_attr_class.attr_2 = 3
            
            setattr(unique_attr_class, 'attr_1', 3)
            
            ======================================
            NotUniqueValueAttrError exception.
            ```



In order to run this tests please execute on command line:


1. Valid Test: \
            `python3 run_test.py valid`


2. Invalid attrs on init Test: \
            `python3 run_test.py invalid_init` 


3. Invalid attrs on update Test: \
            `python3 run_test.py invalid_update` 

