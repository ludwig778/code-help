from logging import getLogger
import json
import configparser
import csv

logger = getLogger(__name__)


class File:
    @classmethod
    def from_json(self, filename):
        logger.debug(f"FileConverter from json {filename}")

        with open(filename) as fd:
            data = json.load(fd)

        return data

    @classmethod
    def to_json(self, filename, data):
        logger.debug(f"FileConverter to json {filename} {data}")

        with open(filename, "w") as fd:
            json.dump(data, fd)

    @classmethod
    def from_ini(self, filename):
        logger.debug(f"FileConverter from ini {filename}")

        data = {}

        config = configparser.ConfigParser()
        config.read(filename)

        for section in config.sections():
            data[section] = {}
            for option in config.options(section):
                data[section][option] = config.get(section, option)

        return data

    @classmethod
    def to_ini(self, filename, data):
        logger.debug(f"FileConverter to ini {filename} {data}")

        with open(filename, "w") as fd:
            writer = configparser.ConfigParser()

            for section, values in data.items():
                if section.lower() == "default":
                    section = section.upper()
                else:
                    writer.add_section(section)

                for option, value in values.items():
                    writer.set(section, option, str(value))

            writer.write(fd)

    @classmethod
    def from_csv(self, filename):
        logger.debug(f"FileConverter from csv {filename}")

        with open(filename) as fd:
            reader = csv.reader(fd)
            data = []
            for line_index, row in enumerate(reader):
                if line_index == 0:
                    keys = row
                else:
                    data.append(dict(zip(keys, row)))

        return data

    @classmethod
    def to_csv(self, filename, data, headers=None):
        logger.debug(f"FileConverter to csv {filename} {data}")

        with open(filename, "w") as fd:
            if isinstance(data, dict):
                writer = csv.DictWriter(fd, fieldnames=headers or data.keys())

                writer.writeheader()
                writer.writerow(data)

            elif isinstance(data, list):
                writer = csv.DictWriter(
                    fd,
                    fieldnames=headers or isinstance(data[0], dict) and data[0].keys()
                )

                writer.writeheader()

                for item in data:
                    writer.writerow(item)

            else:
                logger.error("Input datas type not supported")

    @classmethod
    def from_yaml(self, filename):
        import yaml
        logger.debug(f"FileConverter from yaml {filename}")

        with open(filename) as fd:
            data = yaml.full_load(fd)

        return data

    @classmethod
    def to_yaml(self, filename, data):
        import yaml
        logger.debug(f"FileConverter to yaml {filename} {data}")

        with open(filename, "w") as fd:
            yaml.dump(data, fd)
