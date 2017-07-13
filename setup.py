import os

from setuptools import setup, find_packages

here = os.path.abspath(os.path.dirname(__file__))
README = open(os.path.join(here, "README.md")).read()
CHANGES = open(os.path.join(here, "CHANGES.txt")).read()

requires = [
    "apscheduler",
    "Babel",
    "bumpversion",
    "circus",
    "chaussette",
    "decorator",
    "docopt",
    "dogpile.cache",
    "GitPython",
    "gsutil",
    "jinja2",
    "markdown2",
    "pyramid>=1.5",
    "pyramid_jinja2>=2.0",
    "pyramid_beaker",
    "pyramid_debugtoolbar",
    "pyramid_tm",
    "pyScss",
    "pystalkd",
    "pyyaml",
    "raven",
    "requests",
    "transaction",
    "unicodecsv",
    "vcrpy",
    "waitress",
    "zope.component",
]

test_requires = [
    "webtest",
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
    tests_require=test_requires,
    entry_points="""\
        [paste.app_factory]
        main = avionvilleray:main
        [console_scripts]
        avion-scheduler = avionvilleray.scripts.scheduler:main
        avion-collector = avionvilleray.scripts.collector:main
    """,
    message_extractors={".": [
        ("**.py", "lingua_python", None),
        ("**.jinja2", "jinja2", None)
    ]},
)
