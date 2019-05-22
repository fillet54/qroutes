# -*- coding: utf-8 -*-

from context import qroutes
from qroutes import wrap_config

import unittest

class MiddlewareTestSuite(unittest.TestCase):
    '''Middleware test cases
    
    ''' 

    def test_wrap_config(self):
        config = dict(config_item='my-config')
        def stub_handler(r):
            return r['config']

        middleware = wrap_config(stub_handler, config)

        self.assertEqual(middleware({}), config)


if __name__ == '__main__':
    unittest.main()