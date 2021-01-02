#LXDB MediaSorter - A program to sort media files.
#Copyright (C) 2019-2020 LXDB Team

#This program is free software: you can redistribute it and/or modify
#it under the terms of the GNU General Public License as published by
#the Free Software Foundation, either version 3 of the License, or
#any later version.

#This program is distributed in the hope that it will be useful,
#but WITHOUT ANY WARRANTY; without even the implied warranty of
#MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#GNU General Public License for more details.

#You should have received a copy of the GNU General Public License
#along with this program.  If not, see <https://www.gnu.org/licenses/>.

#LXDB MediaSorter,  Copyright (C) 2019-2021  LXDB Team
#This program comes with ABSOLUTELY NO WARRANTY
#This is free software, and you are welcome to redistribute it
#under certain conditions.

from setuptools import setup

setup(name='lms',
      version='1.0',
      description='LXDB MediaSorter, a program to sort files after metadata.',
      long_description='LXDB MediaSorter, a program to sort files fast and easy.',
      url='https://github.com/lxdb-team/lms',
      author='LXDB Team',
      author_email='service@lxdb.de',
      license='GPLv3.0',
      packages=['lms'],
      install_requires=['PyQt5'],
      zip_safe=False,
      scripts=['data/bin/lms', 'data/bin/lms-cli'],
      include_package_data=True,
      data_files=[("share/applications", ["data/de.lxdb.lms.desktop"]), ("share/icons/hicolor/symbolic/apps/", ["data/icons/symbolic/de.lxdb.lms-symbolic.svg"]), ("share/icons/hicolor/scalable/apps/", ["data/icons/normal/de.lxdb.lms.svg"]), ("share/metainfo", ["data/de.lxdb.lms.appdata.xml"])])
