#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

def read_settings_file(file= "settings.json"):
    """Function to read the configuration file, settings.jsonself.

    Parameters:
    file (str): name of file.

    Returns:
    dict: Data from the json object.
    """
    with open(file) as f:
        data = json.load(f)

        # 'Default' value for parameter: try to find it in settings
        # file, otherwise default it
        try:
            data['time_step']
        except Exception as e:
            data['time_step'] = 5
        try:
            data['max_steps']
        except Exception as e:
            data['max_steps'] = 200
        try:
            data['temperature']
        except Exception as e:
            data['temperature'] = 300
        try:
            data['ensemble']
        except Exception as e:
            data['ensemble'] = "NVE"
        try:
            data['friction']
        except Exception as e:
            data['friction'] = 0.001
        try:
            data['decimals']
        except Exception as e:
            data['decimals'] = 5
        return data

if __name__ == "__main__":
    settings = read_settings_file()
    print(settings)
