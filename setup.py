from distutils.core import setup

setup(
    name="parser_app",
    description="Module for serializing or deserializing Json/Pickle/Toml/Yaml data",
    author="Potapchik Victoria",
    author_email="vika1super2014@gmail.com",
    packages=["jsonParser", "pickleParser", "tomlParser", "yamlParser",
              "Utilities", "ParserSerializer"],
    install_requires=["dill", "pytomlpp", "pyyaml"],
    scripts=["parser_app.py"]
)
