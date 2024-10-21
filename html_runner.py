import unittest
from HtmlTestRunner import HTMLTestRunner

test_suite = unittest.TestLoader().discover('tests')
runner = HTMLTestRunner(output = 'test-reports')
runner.run(test_suite)