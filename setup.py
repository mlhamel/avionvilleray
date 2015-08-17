import os

from setuptools import setup, find_packages

here = os.path.abspath(os.path.dirname(__file__))
README = open(os.path.join(here, "README.md")).read()
CHANGES = open(os.path.join(here, "CHANGES.txt")).read()

requires = [
    "alembic",
    "ansible",
    "Babel",
    "bumpversion",
    "circus",
    "chaussette",
    "decorator",
    "docopt",
    "dogpile.cache",
    "GitPython",
    "jinja2",
    "markdown2",
    "pyramid>=1.5",
    "pyramid_jinja2>=2.0",
    "pyramid_beaker",
    "pyramid_debugtoolbar",
    "pyramid_tm",
    "pyScss",
    "raven",
    "transaction",
    "unicodecsv",
    "waitress",
    "webhelpers",
    "zope.sqlalchemy",
]

setup(
    name="avionvilleray",
    version="0.3.0",
    description="Des avions dans Villeray",
    long_description=README + "\n\n" + CHANGES,
    classifiers=[
        "Programming Language :: Python",
        "Framework :: Pyramid",
        "Topic :: Internet :: WWW/HTTP",
        "Topic :: Internet :: WWW/HTTP :: WSGI :: Application",
    ],
    author="",
    author_email="",
    url="",
    keywords="web wsgi bfg pylons pyramid",
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    test_suite="avionvilleray",
    install_requires=requires,
    entry_points="""\
        [paste.app_factory]
        main = avionvilleray:main
    """,
    message_extractors={".": [
        ("**.py", "lingua_python", None),
        ("**.jinja2", "jinja2", None)
    ]},
)
