# Версии игры и происхождение источников

Проверка 11.11.2026 относится к установленному каталогу `C:/Users/Slava/Documents/Bloodlines-GLM/Reference/Vampire - The Masquerade Bloodlines`. Версия установленного патча зафиксирована в `Unofficial_Patch/gameinfo.txt:4` как 12.0. `cfg/user.cfg:2` выбирает `setPlus()`, который в `python/vamputil.py:305–308` задаёт `G.Patch_Plus=1`. Выполнение этой настройки в конкретном запуске не наблюдалось.

| Файл | SHA-256 | Роль |
|---|---|---|
| `Version.inf` | `b9c74f44d4b69c3153740c9605e990c9d4c0d3027e92424cfb7f00ae19b2db48` | Базовая версия 1.2. |
| `Unofficial_Patch/gameinfo.txt` | `f24c54baea8fc21d9c8b9e67280c3c4f2dddd70518b5a859a70851ad01e88a2f` | Каталог патча 12.0 и SearchPaths. |
| `Unofficial_Patch/cfg/user.cfg` | `7fab03f930daaf560de3e41244cef1aef23042756d78c9949d7210e7435442b6` | Выбор Plus. |
| `Unofficial_Patch/VTMBup-readme.txt` | `74f9a20a59577877b9a323e5403b86957e176ac88121e3c90f4ee00dbabeaaa5` | Запись v12.0 на строке 111. |
| `Docs/Readme-UP [Eng].txt` | `0bb89b14e449dad88a71e3fff2f2f54f6d1b6757e6e84a42339b45506ffc2abd` | Отдельный документ с записью v11.5. |

В `Vampire/` найдены 18 архивов `pack000`–`pack013` и `pack100`–`pack103`. Метки LastWriteTime и размеры не устанавливают редакцию каждого payload. `Unofficial_Patch/maps/*.bsp` являются установленными картами, а `SDKContent/MapSrc/up sources/*.vmf` являются исходниками SDK. Декомпиляция BSP требует отдельной идентификации входного файла и инструмента. Совпадение выбранных сущностей не подтверждает совпадение всей геометрии.

## Источники
- **Исходный файл**: C:\Users\Slava\Documents\Bloodlines-GLM\Reference\Vampire - The Masquerade Bloodlines\Vampire\
- **VPK архивы**: pack000.vpk по pack103.vpk

## Версии VPK архивов

### Исходная игра
- **pack000-009.vpk**: ~200 МБ каждый — UNKNOWN
- Происхождение всех payload здесь не проверялось.

### Патчи
- **pack011.vpk**: ~173 КБ (служебный?) — UNKNOWN
- **pack010.vpk**: 62.76 МБ — UNKNOWN
- **ВЕРДИКТ**: Timestamps НЕ доказывают содержимое патча. Конкретные изменения неизвестны без извлечения.
- **pack012.vpk**: 257.47 МБ — UNKNOWN
- **ВЕРДИКТ**: Timestamps НЕ доказывают содержимое патча. Конкретные изменения неизвестны без извлечения.
- **pack013.vpk**: 168.72 МБ — UNKNOWN
- **ВЕРДИКТ**: Timestamps НЕ доказывают содержимое патча. Конкретные изменения неизвестны без извлечения.
- **pack100.vpk** и **pack102.vpk**: по 9 байт; **pack101.vpk**: 25 575 811 байт; **pack103.vpk**: 355 209 байт. Назначение payload UNKNOWN.

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
  - vdata/ — данные игры

### Файлы, обнаруженные в Unofficial Patch

#### vdata/system/
- **masquerade.txt** — данные системы маскарада (540 байт)
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
- Выбранные системные файлы доступны для чтения. Полнота извлечения не установлена.

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
2. Полное распределение DLG между loose-файлами и архивами; проверенные диалоги Santa Monica находятся в `Unofficial_Patch/dlg/santa monica/`.
3. Как работают системы дисциплин и их ограничения
4. Механики квестов и NPC
5. Связи между Python скриптами и VPK архивами
6. Как NPC шаблоны применяются в играх
