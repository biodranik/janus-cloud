import os
from setuptools import setup, find_packages
import januscloud

here = os.path.abspath(os.path.dirname(__file__))
README = open(os.path.join(here, 'README.md')).read()
CHANGES = open(os.path.join(here, 'CHANGES.md')).read()

requires = [
    'gevent==1.4.0',
    'ws4py==0.5.1',
    'PyYAML==5.1',
    'pyramid==1.10.4',
    'requests>=2.18.4',
    'python-daemon==2.2.3'
]

setup(name='janus-cloud',
      version=januscloud.__version__,
      license='AGPLv3',
      url='https://github.com/OpenSight/janus-cloud',
      description='Janus-cloud is an JANUS API proxy to implement the Janus WebRTC server cluster',
      long_description=README + '\n\n' + CHANGES,
      classifiers=[
          "Development Status :: 3 - Alpha",
          "Framework :: Pyramid",
          "Intended Audience :: System Administrators",
          "Intended Audience :: Developers",
          "Intended Audience :: Janus user",
          "License :: OSI Approved :: GNU Affero General Public License v3",
          "Operating System :: POSIX :: Linux",
          "Programming Language :: Python",
          "Programming Language :: Python :: 3.5",
          "Programming Language :: Python :: 3.6",
          "Programming Language :: Python :: 3.7",
          "Topic :: Internet :: WWW/HTTP",
          "Topic :: Internet :: WWW/HTTP :: WSGI :: Application",
          "Topic :: System :: Monitoring",
          "Topic :: System :: Networking :: Monitoring",
          "Topic :: System :: Systems Administration",
      ],
      author='OpenSight',
      author_email='public@opensight.cn',
      keywords='Janus cloud WebRTC',
      packages=find_packages(),
      include_package_data=True,
      zip_safe=False,
      install_requires=requires,
      tests_require=requires,
      entry_points="""
      [console_scripts]
      janus-proxy = januscloud.proxy.main:main
      janus-sentinel = januscloud.sentinel.main:main
      janus-install-conf = januscloud.console:install_conf
      """,
      )
