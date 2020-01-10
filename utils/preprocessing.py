from utils import data_properties


def get_inputs(data):
    return data[data_properties.columns[:-1]].values


def get_classes(data):
    return data[data_properties.columns[-1]].values