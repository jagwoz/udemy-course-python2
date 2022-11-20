import os


class ini_file_cm:
    def __init__(self, path):
        self.path = path
        self.parameters = {}

        if os.path.isfile(path):
            with open(path) as file:
                for line in file:
                    param = line.replace('\n', '').split('=')
                    self.write_param(param[0], param[1])

    def write_param(self, key, value):
        self.parameters[key] = value

    def read_param(self, key):
        return self.parameters[key]

    def save_file(self):
        with open(self.path, 'w') as file:
            for key, value in self.parameters.items():
                line = "{}={}\n".format(key, value)
                file.writelines(line)

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.save_file()
        return True if exc_type == OSError else False


if __name__ == "__main__":
    with ini_file_cm("ini_file.ini") as ini:
        ini.write_param("key", "value")
    with ini_file_cm("ini_file.ini") as ini:
        ini.write_param("key2", "value2")
        print(ini.read_param("key"))
        print(ini.read_param("key2"))
