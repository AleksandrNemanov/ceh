from enum import Enum

import yaml

from libs.sections.format_sql_query import FormatSqlQuery
from libs.static.yaml import bound


class Params(Enum):
    LENGTH = 'length'
    PRECISION = 'precision'
    NULL = 'null'
    NOT_NULL = 'not null'


class FormatYamlSqlConverter:
    def __init__(self, query):
        self.query = query
        self.table_name = 'НаименованиеТаблицы'
        self.layer_name = None
        self.footer = None
        self.body = None
        self.header = None

    def to_sql(self, table_name, layer):
        self.layer_name = layer
        self.table_name = table_name or self.table_name
        self.header = bound['header_dapp'].format(self.table_name) if self.layer_name == 'DAPP' else bound[
            'header_rdv'].format(self.table_name)
        self.footer = bound['footer_dapp'] if self.layer_name == 'DAPP' else bound['footer_rdv']
        raw_body = self.__extract_sql()
        self.body = FormatSqlQuery(raw_body).to_pretty_sql()
        return self.header + self.body + self.footer

    def __extract_sql(self):
        full_column = ''
        data = yaml.safe_load(self.query)
        for column in data:
            column_name = self.__get_column_name(column)
            name_type_data = self.__get_name_type_data(column)
            length_data, precision_data = self.__get_type_data_size(column)
            constraint = self.__get_constraint(column)
            if length_data:
                type_data = f'{name_type_data}({length_data}{f',{precision_data})' if precision_data else ')'}'
            else:
                type_data = name_type_data
            full_column += f'{column_name} {type_data} {constraint},\n'

        return full_column.rstrip(',\n')

    @staticmethod
    def __get_column_name(column):
        return column['name'].lower()

    def __get_name_type_data(self, column):
        if self.layer_name == 'DAPP':
            if column['type'].lower() == 'text':
                return 'string'
        return column['type'].lower()

    @staticmethod
    def __get_type_data_size(column):
        if 'params' in column:
            if Params.LENGTH.value in column['params']:
                length_name = Params.LENGTH.value
            elif Params.PRECISION.value in column['params']:
                length_name = Params.PRECISION.value
            else:
                length_name = ''
            length = column['params'][length_name]
        else:
            length = 0

        if 'params' in column and 'scale' in column['params']:
            precision = column['params']['scale']
        else:
            precision = 0

        return length, precision

    def __get_constraint(self, column):
        if 'nullable' in column:
            if self.layer_name == 'RDV':
                return Params.NULL.value if column['nullable'] else Params.NOT_NULL.value
            else:
                return ''
        else:
            if self.layer_name == 'DAPP':
                return ''

            return Params.NULL.value
