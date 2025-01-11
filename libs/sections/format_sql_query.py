import re


class FormatSqlQuery:
    def __init__(self, query: str):
        self.__query = query
        self.__left_space = 4
        self.__center_space = 4
        self.__right_space = 2
        self.__pretty_sql = ''

    def to_pretty_sql(self, left_space: str = None, center_space: str = None, right_space: str = None):
        raw_left_space = self.__get_raw_left_space()
        max_length_name_column = self.__get_max_length_name_column()
        max_length_type_data = self.__get_max_length_type_data()
        self.__left_space = int(left_space or (self.__left_space if raw_left_space == 0 else raw_left_space))
        self.__center_space = int(center_space or self.__center_space)
        self.__right_space = int(right_space or self.__right_space)
        for row in self.__extract_column_type_constraint():
            left_space_and_column = self.__left_space * ' ' + row[0] + (max_length_name_column - len(row[0])) * ' '
            if len(row) >= 2:
                center_space_and_type = self.__center_space * ' ' + row[1] + (max_length_type_data - len(row[1])) * ' '
            else:
                center_space_and_type = ''

            constraint = self.__right_space * ' ' + row[2] if len(row) == 3 else ''
            temp_row = left_space_and_column + center_space_and_type + constraint
            temp_row = temp_row.rstrip() + ',' + '\n'
            self.__pretty_sql += temp_row
        return self.__pretty_sql.rstrip(' ,\n') + '\n'

    def __get_raw_left_space(self) -> int:
        max_space = 0
        for row in self.__query.splitlines():
            match = re.match(r'(^\s*)', row)
            count_space = len(match.group(0))
            if count_space > max_space:
                max_space = count_space
        return max_space

    def __get_max_length_name_column(self) -> int:
        max_length = 0
        for row in self.__query.splitlines():
            replaced = re.sub(r'\s+', ' ', row).strip()
            try:
                count_length = len(replaced.split()[0])
            except:
                count_length = 0
            if count_length > max_length:
                max_length = count_length
        return max_length

    def __get_max_length_type_data(self) -> int:
        max_length = 0
        for row in self.__query.splitlines():
            replaced = re.sub(r'\s+', ' ', row).strip(' ,')
            try:
                count_length = len(replaced.split()[1])
            except:
                count_length = 0
            if count_length > max_length:
                max_length = count_length
        return max_length

    def __extract_column_type_constraint(self):
        result = []
        for row in self.__query.splitlines():
            replaced = re.sub(r'\s+', ' ', row).strip(' ,')
            result.append(tuple(re.split(r'\s+', replaced, maxsplit=2)))
        return result
