import yaml
from mergedeep import merge

class YAMLMerger:
    
    def __init__(self):
        None

    def merge_yaml(self, args, output=None):
        merged = {}

        if not isinstance(args, list):
            raise TypeError("Argument should be a list")

        for e in args:
            try:
                merged = merge({}, merged, yaml.safe_load(e))
            except Exception as e:
                raise Exception("Failed to merge yamls: " + e)

        if output is not None:
            try:
                with open(output, 'w') as output_file:
                    yaml.dump(merged, output_file, default_flow_style=False)
                return merged
            except Exception as e:
                raise Exception("Failed to save yamls in path " + output)
        return merged