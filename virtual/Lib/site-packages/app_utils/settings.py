import logging
import json
import configparser
import os
from pathlib import Path
from typing import Union


class SettingsJSON:
    """
    This class provides an easy to use abstraction layer for creating and working with
    application settings files in a JSON format.

    One limitation of this class is that the set functions for individual settings to not
    cascade down, you are only able to access key in the top level dictionary. You are however
    able to directly modify the dictionary that will be used to store the settings, so should
    you need to access a dictionary within a the top level dictionary, you are still free to do so.
    """

    def __init__(self, default_settings: dict, app_name: str, file_name: str = "settings",
                 folder_path: str = str(Path.home())) -> None:
        """
        Default constructor for working with JSON config files. Either finds or creates the settings file.
        When creating the file, the default settings provided will be used.
        If new keys in the first level of the dictionary are added, they will
        be added to any existing settings file.

        Upon first run of your application, a settings file is generated in a hidden file
        named after your application.

        :param default_settings: Default application settings
        :type default_settings: dict
        :param app_name: Name of your application, this will be the settings folder name.
        :type app_name: str
        :param file_name: Optional name for the settings file, defaults to settings.
        :type file_name: str
        :param folder_path: Optional path to the folder containing the application settings folder.
                            This defaults to the user's home directory.
        :type folder_path: str
        """
        self.path = folder_path + "/." + app_name
        self.default_settings = default_settings
        logging.debug("Config Path: {}".format(self.path))
        if not os.path.exists(self.path):  # check to see if the settings folder exists, if not create it.
            logging.debug("Config directory not found, creating config directory")
            os.mkdir(self.path)
        self.path += "/{}.json".format(file_name)
        try:
            with open(self.path, 'r') as settings_file:
                self.settings = json.load(settings_file)
                logging.debug("Loading settings")
                settings_file.close()
        except FileNotFoundError:
            with open(self.path, "w+") as settings_file:
                logging.debug("Settings not found, applying default settings")
                settings_file.write(json.dumps(self.default_settings))
                settings_file.close()
                settings_file = open(self.path, "r+")
                self.settings = json.load(settings_file)
                settings_file.close()

        # check for new default settings key
        changed = False
        for key in self.default_settings:
            if key not in self.settings:  # add any new keys
                logging.debug("New default setting found: {}".format(key))
                self.settings[key] = self.default_settings[key]
                changed = True
        if changed:  # if there are any new default settings keys added
            logging.debug("Adding new default config entries")
            with open(self.path, 'r+') as settings_file:
                settings_file.write(json.dumps(self.settings))
                settings_file.close()

    def get_json_dict(self) -> dict:
        """
        Gets the current settings dictionary.

        :return: JSON settings dictionary
        :rtype: dict
        """
        return self.settings

    def get_setting(self, key: str) -> Union[str, int, float, list, dict, set]:
        """
        Gets an individual setting entry from the top level of the dictionary.

        :param key: Setting
        :type key: str

        :return: Value of key
        """
        return self.settings[key]

    def set_setting(self, key: str, value: Union[str, int, float, list, dict, set]) -> None:
        """
        Set an individual setting at the top level.

        :param key: Setting key
        :type key: str
        :param value: Value of key

        :return: None
        """
        logging.debug("Updated setting {} with value: {}".format(key, str(value)))
        self.settings[key] = value
        with open(self.path, "w+") as settings_file:
            settings_file.write(json.dumps(self.settings))
            settings_file.close()

    def set_all(self, settings: dict) -> None:
        """
        Replace the current setting dictionary with a new one.

        :param settings: Settings dictionary to be used.
        :type settings: dict

        :return: None
        """
        logging.debug("Updating all settings")
        self.settings = settings
        with open(self.path, "w+") as settings_file:
            settings_file.write(json.dumps(self.settings))
            settings_file.close()

    def reset_setting(self, key: str) -> None:
        """
        Resets a specified setting to its default value.

        :param key: Setting key
        :type key: str

        :return: None
        """
        self.settings[key] = self.default_settings[key]
        with open(self.path, "w+") as settings_file:
            settings_file.write(json.dumps(self.settings))
            settings_file.close()

    def reset_all(self) -> None:
        """
        Resets all settings to their defaults.

        :return: None
        """
        self.settings = self.default_settings
        with open(self.path, "w+") as settings_file:
            settings_file.write(json.dumps(self.settings))
            settings_file.close()


class SettingsINI:
    """
    This class provides an easy to use abstraction layer for creating and working with
    application settings files in a .ini format.

    This class serves as an easy way to create the config file and manage any new default setting
    additions that may occur without over writing the user's existing settings
    """

    def __init__(self, default_settings: dict, app_name: str, file_name: str = "settings",
                 folder_path: str = str(Path.home())) -> None:
        """
        Default constructor for working with JSON config files. Either finds or creates the settings file.
        When creating the file, the default settings provided will be used.
        If new keys in the first level of the dictionary are added, they will
        be added to any existing settings file.

        Upon first run of your application, a settings file is generated in a hidden file
        named after your application.

        :param default_settings: Default application settings
        :type default_settings: dict
        :param app_name: Name of your application, this will be the settings folder name.
        :type app_name: str
        :param file_name: Optional name for the settings file, defaults to settings.
        :type file_name: str
        :param folder_path: Optional path to the folder containing the application settings folder.
                            This defaults to the user's home directory.
        :type folder_path: str
        """
        self.path = folder_path + "/." + app_name
        self.default_settings = default_settings
        self.settings = configparser.ConfigParser()
        logging.debug("Config Path: {}".format(self.path))
        if not os.path.exists(self.path):  # check to see if the settings folder exists, if not create it.
            logging.debug("Config directory not found, creating config directory")
            os.mkdir(self.path)
        self.path += "/{}.ini".format(file_name)
        try:
            if not os.path.exists(self.path):  # check to see if the file exists, ConfigParser.read does not check
                raise FileNotFoundError
            self.settings.read(self.path)
            logging.debug("Loading settings")
        except FileNotFoundError:
            logging.debug("Settings not found, applying default settings")
            for section in self.default_settings:
                if not isinstance(self.default_settings[section], dict):  # .ini format validation
                    logging.critical("Malformed ini file, section contains no keys: {}".format(section))
                    raise TypeError("Each section of an ini file must of a type dict.")
                self.settings[section] = self.default_settings[section]

            # if we passed all validation checks, go ahead and write the file
            with open(self.path, "w+") as settings_file:
                self.settings.write(settings_file)
                settings_file.close()
                settings_file = open(self.path, "r+")
                self.settings.read(settings_file)
                settings_file.close()

        # check for new default settings key
        changed = False
        for section in self.default_settings:  # looking for new sections
            if section not in self.settings.sections():  # add any new keys
                logging.debug("New default setting found: {}".format(section))
                self.settings[section] = self.default_settings[section]
                changed = True
            for key in self.default_settings[section]:  # looking for new keys in any section
                if key not in self.settings[section]:
                    logging.debug("New key found: {} in section: {}".format(key, section))
                    self.settings[section][key] = str(self.default_settings[section][key])
                    changed = True
        if changed:  # if there are any new default settings keys added
            logging.debug("Adding new default config entries")
            with open(self.path, 'r+') as settings_file:
                self.settings.write(settings_file)
                settings_file.close()

    def reset_all(self) -> None:
        """
        Resets all settings back to their defaults.

        :return: None
        """
        self.settings.read_dict(self.default_settings)
        with open(self.path, 'r+') as settings_file:
            self.settings.write(settings_file)
            settings_file.close()

    def reset_section(self, section: str) -> None:
        """
        Reset an entire section of the settings back to its defaults.

        :param section: section to reset.
        :type section: str
        :return: None
        """
        self.settings[section] = self.default_settings[section]
        with open(self.path, 'r+') as settings_file:
            self.settings.write(settings_file)
            settings_file.close()

    def reset_setting(self, section: str, key: str) -> None:
        """
        Reset an individual setting in a specified section.

        :param section: section of setting.
        :type section: str
        :param key: setting key
        :type key: str

        :return: None
        """
        self.settings[section][key] = str(self.default_settings[section][key])
        with open(self.path, 'r+') as settings_file:
            self.settings.write(settings_file)
            settings_file.close()

    def set_setting(self, section: str, key: str, value: Union[int, float, str]) -> None:
        """
        Updates an individual setting.

        :param section: section key.
        :type section: str
        :param key: setting key.
        :type key: str
        :param value: value to be applied.
        :type value: int, float, str

        :return: None
        """
        self.settings[section][key] = str(value)
        with open(self.path, 'r+') as settings_file:
            self.settings.write(settings_file)
            settings_file.close()

    def get_setting(self, section: str, key: str, cast_type: object = str()) -> Union[str, int, float]:
        """
        Gets the value of the specified setting and returns it cast as the specified data type.
        The supported data types are:
        1. str
        2. int
        3. float

        :param section: section key.
        :type section: str
        :param key: setting key.
        :type key: str
        :param cast_type: optional, defaults to str.
        :type cast_type: object

        :return: setting
        :rtype: str, int, float
        """
        if isinstance(cast_type, str):
            return str(self.settings[section][key])
        elif isinstance(cast_type, int):
            return int(self.settings[section][key])
        elif isinstance(cast_type, float):
            return float(self.settings[section][key])
        else:
            raise TypeError("Unsupported type: {}".format(str(cast_type)))
