import unittest, yaml
from YAMLMerger import YAMLMerger

input_one = open('./yaml/input_one.yaml', 'r').read()
input_two = open('./yaml/input_two.yaml', 'r').read()
input_three = open('./yaml/input_three.yaml', 'r').read()
output_one_two = yaml.safe_load(open('./yaml/output_one_two.yaml', 'r'))
output_all = yaml.safe_load(open('./yaml/output_all.yaml', 'r'))

class TestMergerMethods(unittest.TestCase):
            
    def test_merge_yaml_with_two_yamls(self):
        self.assertEqual(YAMLMerger().merge_yaml([input_one, input_two]), output_one_two)

    def test_merge_yaml_with_three_yamls(self):
        self.assertEqual(YAMLMerger().merge_yaml([input_one, input_two, input_three]), output_all)

if __name__ == '__main__':
    unittest.main()