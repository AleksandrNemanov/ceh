import json

import yaml


class FormatYamlJsonConverter:
    def __init__(self, query, is_primary, is_nullable):
        self.indent = None
        self.yaml_data = None
        self.query = query
        self.is_primary = is_primary
        self.is_nullable = is_nullable

    def to_json(self, indent):
        self.indent = int(indent or 8)
        self.__correct_yaml()
        json_data = json.dumps(self.yaml_data, indent=2)
        extended_left_space_json_data = "\n".join([self.indent * ' ' + line for line in json_data.splitlines()])
        body = self.__extract_body_json(extended_left_space_json_data)
        return body

    def __correct_yaml(self):
        self.yaml_data = yaml.safe_load(self.query)
        for field in self.yaml_data:
            field['type'] = field['type'].lower()
            if 'nullable' not in field and self.is_nullable:
                field['nullable'] = 'true'
            if self.is_primary:
                field['primary_key'] = 'false'
            if 'params' in field:
                del field['params']

    @staticmethod
    def __extract_body_json(json_data):
        min_lines = 2
        lines = json_data.splitlines()
        if len(lines) > min_lines:
            lines = lines[1:-1]
        body_json = "\n".join(lines)
        return body_json
