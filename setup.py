import setuptools 

setuptools.setup(
    name = "checks",
    packages = setuptools.find_packages(exclude = ("server.", "server")),       # Does this even work?
    author = "Kristian Olesen Larsen",
    author_email = "kristianuruplarsen@gmail.com",
    url = "https://github.com/Kristianuruplarsen/checks"   
)