from setuptools import setup, find_packages
import os

version = '1.0a1'

long_description = (
    open('README.rst').read()
    + '\n' +
    'Contributors\n'
    '============\n'
    + '\n' +
    open('CONTRIBUTORS.rst').read()
    + '\n' +
    open('CHANGES.rst').read()
    + '\n')

setup(name='collective.ploneboard',
      version=version,
      description="",
      long_description=long_description,
      # Get more strings from
      # http://pypi.python.org/pypi?%3Aaction=list_classifiers
      classifiers=[
          "Environment :: Web Environment",
          "Framework :: Plone",
          "Operating System :: OS Independent",
          "Programming Language :: Python",
          "Programming Language :: Python :: 2.6",
          "Topic :: Software Development :: Libraries :: Python Modules",
      ],
      keywords='',
      author='Timo Stollenwerk',
      author_email='contact@timostollenwerk.net',
      url='http://github.com/tisto/collective.ploneboard/',
      license='gpl',
      packages=find_packages('src'),
      package_dir={'': 'src'},
      namespace_packages=['collective', ],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'setuptools',
          'collective.autopermission',
          'plone.app.dexterity',
          'plone.directives.form',  # get rid of that dependency
          'plone.namedfile[blobs]',
          'z3c.jbot',
          # 'plone.browserlayer',
          'plone.formwidget.captcha',
          'plone.formwidget.recaptcha',
          'collective.captcha',
          'collective.akismet',
          'collective.z3cform.norobots',
      ],
      extras_require={'test': ['plone.app.testing[robot]']},
      entry_points="""
      # -*- Entry points: -*-
      [z3c.autoinclude.plugin]
      target = plone
      """,
      setup_requires=["PasteScript"],
      paster_plugins=["templer.localcommands"],
      )
