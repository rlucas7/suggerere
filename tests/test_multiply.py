from collections2.multiply import multiply

import pytest

# uncomment if needed
#from unittest import TestCase


 # some comment here to commit
    # you can use the parametrize fixture for concise looping like so
    @pytest.mark.parametrize("a,b,expected", [(3,5,15), (2,4,8)])
    def test_multiply(self, a, b, expected):
        assert multiply(a, b) == expected

