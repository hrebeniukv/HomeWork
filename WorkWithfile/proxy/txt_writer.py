from writer import Writer


class TxtWriter(Writer):

    def __init__(self, file_path):
        self.file_path = file_path

    def write(self, new_data, write_mode):
        if write_mode in ("w", "a"):
            with open(self.file_path, write_mode) as file:
                file.write(new_data)
        else:
            raise ValueError(
                "Something was wrong, be sure that write data is string and write mode match to requirement "
                "it should be 'w' or 'a'")
