
def configuration(parent_package="", top_path=None):
    from numpy.distutils.misc_util import Configuration
    config = Configuration('externals', parent_package, top_path)
    config.add_subpackage('joblib')
    config.add_subpackage('iced')

    return config
