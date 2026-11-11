# Инструменты исследования и доступ к ресурсам — ВЕРИФИЦИРОВАНО

## Инструменты в SDKBinaries (Source SDK)
- **hammer.exe** — редактор карт (.vmf)
  - Путь: SDKBinaries/hammer.exe
  - Использование: редактирование карт, создание новых локаций

- **vbsp.exe / vbspinfo.exe / vrad.exe / vvis.exe** — компиляция карт
  - Путь: SDKBinaries/
  - Использование:
    - vbsp.exe: BSP compilation
    - vbspinfo.exe: информация о BSP
    - vrad.exe: Radiosity (освещение)
    - vvis.exe: Visibility (видимость)

- **studiomdl.exe / studiomdl-sw.exe / studiomdl-fix.exe** — создание моделей
  - Путь: SDKBinaries/
  - Использование: генерация .mdl файлов из .smd

- **hlfaceposer.exe / hlfaceposer.tools.exe** — анимация лиц
  - Путь: SDKBinaries/
  - Использование: редактирование анимаций лиц персонажей

- **hlmv.exe / hlmv.shell.exe** — просмотр моделей
  - Путь: SDKBinaries/
  - Использование: просмотр .mdl и .vtx файлов

- **soundbrowser.exe** — просмотр звуков
  - Путь: SDKBinaries/
  - Использование: просмотр и выбор звуковых файлов

- **vbspzip.exe** — архивация BSP
  - Путь: SDKBinaries/
  - Использование: упаковка карт в .bsp

- **glview.exe** — просмотр OpenGL
  - Путь: SDKBinaries/
  - Использование: OpenGL preview

- **sdklauncher.exe** — запуск SDK
  - Путь: SDKBinaries/
  - Использование: запуск Hammer и других инструментов

- **studiovtmb49k.exe** — специальный редактор VTMB
  - Путь: SDKBinaries/
  - Использование: специализированный инструмент для VTMB

- **vtex.exe / vtf2tga.exe** — обработка текстур
  - Путь: SDKBinaries/
  - Использование: конвертация текстур

## Инструменты в Extras/Developer Tools

### Level Entity Lists
- **Путь**: Extras/Developer Tools/Level Entity Lists/
- **Количество**: 200+ файлов
- **Формат**: текстовые файлы
- **Примеры**:
  - ch_hub_1.txt — Chinatown hub
  - sm_hub_1.txt — Santa Monica hub
  - hw_hub_1.txt — Hollywood hub
  - ch_*.txt, sm_*.txt, hw_*.txt — локации
  - sp_*.txt — специальные последовательности
  - *-default.txt, *-up.txt — состояния
- **Структура** (VERIFIED):
  `
  ObjNum OriginX OriginY OriginZ Flags Solid FadeMinDist FadeMaxDist PropTypeEntry
  `
- **Использование**:
  - Понимание сущностей на картах
  - Анализ связей между объектами
  - Разбор уровней без запуска игры

### Original Python Files
- **Путь**: Extras/Developer Tools/Original Python Files/
- **Структура**: папка для каждой локации
- **Пример**:
  `
  chinatown/chinatown.py
  `
- **Содержимое** (VERIFIED):
  `python
  print "loading chinatown level script"
  import __main__
  from __main__ import G
  Find = __main__.FindEntityByName
  Finds = __main__.FindEntitiesByName
  RandomLine = __main__.RandomLine
  `
- **Использование**:
  - Понимание логики локаций
  - Квесты, события, NPC
  - Связи с Level Entity Lists

### Turvy's VPKTool
- **Путь**: Extras/Developer Tools/Turvy's VPKTool/
- **Использование**:
  - Распаковка VPK архивов
  - Извлечение содержимого без модификации оригинальных файлов

### ZylonBane's ZVTool
- **Путь**: Extras/Developer Tools/ZylonBane's ZVTool/
- **Использование**:
  - Консольные инструменты для анализа
  - Дополнительные утилиты

### Документация
- **ModDev Guide.txt** — руководство по моддингу
- **Dlg Template.dlg** — шаблоны диалогов
- **VTMB Transcripts.txt** — транскрипты диалогов
- **VTMB Walkthrough.txt** — руководство по версии 1.5

## Доступ к ресурсам без модификации

### SDKContent (извлечённые файлы)
- **Путь**: SDKContent/VpkContent/
- **Преимущества**:
  - Все файлы доступны для чтения без распаковки
  - Нет необходимости модифицировать оригинальные файлы
  - Можно анализировать структуру данных

### Unofficial Patch (копия)
- **Путь**: Unofficial_Patch/
- **Преимущества**:
  - Весь контент патча в одном месте
  - Можно сравнивать с оригиналом
  - Не влияет на оригинальную игру

### Python скрипты
- **Путь**: Original Python Files/
- **Преимущества**:
  - Исходный код логики локаций
  - Понятная структура
  - Не требует запуска игры

## Выводы

### ВЕРИФИЦИРОВАННЫЕ инструменты
1. **Hammer и компиляторы**: vbsp, vrad, vvis — для работы с картами
2. **Моделирование**: studiomdl, hlfaceposer, hlmv — для работы с моделями
3. **Звуки**: soundbrowser — для работы со звуками
4. **Текстуры**: vtex, vtf2tga — для работы с текстурами
5. **Level Entity Lists**: детальная информация о сущностях карт
6. **Python скрипты**: логика локаций в исходном коде
7. **VPKTool**: безопасная распаковка архивов

### Доступ к ресурсам
- **Без модификаций**: SDKContent, Original Python Files, Level Entity Lists
- **С безопасным анализом**: VPKTool для чтения содержимого
- **Безопасность**: все инструменты работают только с копиями файлов

### НЕИЗВЕСТНОЕ
1. Как связываются Python скрипты с VPK архивами
2. Где на самом деле хранятся тексты диалогов
3. Какие форматы используются для карт (.bsp, .bspzip)
4. Как работают специальные инструменты VTMB (studiovtmb49k)
