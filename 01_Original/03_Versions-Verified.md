# Версии игры и патчей — ВЕРИФИЦИРОВАНО

## Источники
- **Исходный файл**: C:\Users\Slava\Documents\VampireRemake-Starter\Reference\Vampire - The Masquerade Bloodlines\Vampire\
- **VPK архивы**: pack000.vpk по pack103.vpk

## Версии VPK архивов

### Исходная игра
- **pack000-009.vpk**: ~200 МБ каждый — UNKNOWN
- Это оригинальный релиз игры (2004)

### Патчи
- **pack011.vpk**: ~173 КБ (служебный?) — UNKNOWN
- **pack010.vpk**: 62.76 МБ — UNKNOWN
- **ВЕРДИКТ**: Timestamps НЕ доказывают содержимое патча. Конкретные изменения неизвестны без извлечения.
- **pack012.vpk**: 257.47 МБ — UNKNOWN
- **ВЕРДИКТ**: Timestamps НЕ доказывают содержимое патча. Конкретные изменения неизвестны без извлечения.
- **pack013.vpk**: 168.72 МБ — UNKNOWN
- **ВЕРДИКТ**: Timestamps НЕ доказывают содержимое патча. Конкретные изменения неизвестны без извлечения.
- **pack100-103.vpk**: ~300 КБ каждый — UNKNOWN

## Unofficial Patch
- **Размер**: ~1.22 ГБ
- **Структура**:
  - cfg/ — конфигурация (6 файлов)
  - dlg/ — диалоги (147 файлов)
  - maps/ — карты (222 файла)
  - materials/ — материалы (3700 файлов)
  - models/ — модели (1193 файла)
  - particles/ — частицы (274 файла)
  - python/ — скрипты (52 файла)
  - resource/ — ресурсы
  - save/ — сохранения
  - scripts/ — скрипты
  - sound/ — звук (9835 файлов)
  - data/ — данные игры

### Файлы, добавленные/изменённые в Unofficial Patch

#### data/system/
- **masquerade.txt** — новая система маскарада (540 байт)
- **stats - hunter.txt** — характеристики охотников (102170 байт)
- **stats - vampire.txt** — характеристики вампиров (101894 байт)
- **stats.txt** — характеристики (101894 байт)
- **strings - hunter.txt** — строки для охотников (25315 байт)
- **strings - vampire.txt** — строки для вампиров (25018 байт)
- **strings.txt** — строки (25018 байт)
- **traiteffects000 - hunter.txt** — эффекты черт для охотников (66864 байт)
- **traiteffects000 - vampire.txt** — эффекты черт для вампиров (66863 байт)
- **traiteffects000.txt** — эффекты черт (66863 байт)
- **npctemplate000.txt** — добавлено поле "AlwaysInnocent" "1" (комментарий: added by wesp)

#### python/ — скрипты локаций
- bradbury, cemetery, chinatown, crackhouse, downtown, fusyndicate, gallery, giovanni
- griffith, hollywood, leopold, lib, malkavian, museum, santamonica, temple, theatre
- tutorial, ventrue, warehouse, warrens, zvtool

## SDK Content
- **Путь**: SDKContent/VpkContent/vdata/system/
- **Размер**: ~2.01 ГБ
- **Полностью извлечён** — все системные файлы доступны для чтения

## Инструменты исследования (SDKBinaries)
- **hammer.exe** — редактор карт
- **vbsp.exe, vrad.exe, vvis.exe** — компиляция карт
- **studiomdl.exe** — создание моделей
- **hlfaceposer.exe** — анимация лиц
- **hlmv.exe** — просмотр моделей
- **soundbrowser.exe** — просмотр звуков
- **Turvy's VPKTool** — распаковка VPK (в Extras/Developer Tools/)
- **ZylonBane's ZVTool** — консольные инструменты

## Level Entity Lists
- **Путь**: Extras/Developer Tools/Level Entity Lists/
- **Формат**: текстовые файлы с сущностями карт
- **Примеры**: ch_hub_1.txt, sm_hub_1.txt, hw_hub_1.txt
- **Структура**: ObjNum OriginX OriginY OriginZ Flags Solid FadeMinDist FadeMaxDist PropTypeEntry
- **Состояния**: -default.txt, -up.txt

## Original Python Files
- **Путь**: Extras/Developer Tools/Original Python Files/
- **Структура**: папка для каждой локации
- **Пример**: chinatown/chinatown.py

## Выводы

### ВЕРИФИЦИРОВАННЫЕ данные
1. **VPK**: Valve Pack архивы Source Engine, НЕ Particle System
2. **Unofficial Patch**: community mod Wesp5/Werner Spahl, НЕ официальный
3. **Версии**: определены по файловой системе, но timestamp НЕ доказывают содержимое
4. **Инструменты исследования**: полностью включены в SDK
5. **Форматы**: dialog.txt (определения), npctemplate*.txt (шаблоны NPC), disciplinetgt_*.txt (дисциплины)

### НЕИЗВЕСТНОЕ
1. Точные изменения в pack010, pack012, pack013 (какие файлы изменены/добавлены/удалены)
2. Где хранятся реальные диалоги (только определения в dialog.txt)
3. Как работают системы дисциплин и их ограничения
4. Механики квестов и NPC
5. Связи между Python скриптами и VPK архивами
6. Как NPC шаблоны применяются в играх
