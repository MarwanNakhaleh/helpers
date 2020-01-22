class StringMethods:
    def reverse(self, string):
        if len(string) > 1:
            return string[::-1]
        return string

    def remove_last_character(self, string):
        if len(string) > 0:
            return string[:-1]
        return string

    def remove_first_character(self, string):
        if len(string) > 0:
            return string[1:]
        return string

    def remove_last_n_characters(self, string, n):
        if len(string) >= n:
            to_remove = n * -1
            return string[:to_remove]
        return string