# LXDB MediaSorter
Release 1 Version 1.0.0

LXDB MediaSorter ist ein Programm zum Sortieren und Umbenennen von Mediendateien, d.h. Bildern und Videos.

Mit Hilfe des Kommandozeilen-Werkzeugs [ExifTool](https://exiftool.org/) werden Metadaten von den Dateien ausgelesen.

Nach einem frei bestimmbaren Namensschema werden die Dateien umbenannt und ggf. in passende Ordner verschoben.

### Beispiel:

#### Umbenennen

Schema: `%Y_%m_%d-%H_%M_%S`

Ergebnis: ```2019_12_31-23:59.jpg```

#### Sortieren

Schema: `%Y_%m_%d-%H_%M_%S` `%Y/%m`


Ergebnis:
```
> 2019
  > 12
    > 2019_12_31-23:59.jpg
```

## Funktionen

- Umbenennen und Sortieren von Dateien
- Anzeigen von Metadaten verschiedener Dateitypen
- Vorschau von verschiedenen Mediendateien(Bilder/Videos)
- Rekursive Durchsuchung von Ordnern
- Qt5-Interface
- Command Line Interface
- Python-Bibliothek zur Nutzung in anderen Anwendungen
- Tab-Interface

## Installation

Siehe [LXDB Website](https://lxdb.de/de/lms/linux) für Installationsanleitung Linux.

Windows 7+ amd64:

Siehe Releases/LXDB_MediaSorter_V2020.07_amd64.exe

## Lizenz

LXDB MediaSorter - A program to sort media files.  
Copyright (C) 2019-2021 LXDB Team  


This program is free software: you can redistribute it and/or modify  
it under the terms of the GNU General Public License as published by  
the Free Software Foundation, either version 3 of the License, or  
any later version.  

This program is distributed in the hope that it will be useful,  
but WITHOUT ANY WARRANTY; without even the implied warranty of  
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the  
GNU General Public License for more details.  

You should have received a copy of the GNU General Public License  
along with this program.  If not, see <https://www.gnu.org/licenses/>.  

LXDB MediaSorter,  Copyright (C) 2019-2021  LXDB Team  
This program comes with ABSOLUTELY NO WARRANTY  
This is free software, and you are welcome to redistribute it  
under certain conditions.  
