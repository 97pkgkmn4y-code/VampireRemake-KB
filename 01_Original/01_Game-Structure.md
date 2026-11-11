# Структура игры Vampire: The Masquerade — Bloodlines

## Верифицированные данные

### Исходные файлы игры
- **Путь**: C:\Users\Slava\Documents\VampireRemake-Starter\Reference\Vampire - The Masquerade Bloodlines\Vampire\
- **VPK архивы**: pack000.vpk по pack103.vpk
  - pack000-009: 
  - pack010: 
  - pack011: 
  - pack012: 
  - pack013: 
  - pack100-103: 2004-10-06 (служебные файлы)

### Каталог Unofficial Patch (VTMBup)
- **Путь**: C:\Users\Slava\Documents\VampireRemake-Starter\Reference\Vampire - The Masquerade Bloodlines\Unofficial_Patch\
- **Размер**: ~1.22 ГБ
- **Структура каталогов**:
  - cfg — конфигурация (6 файлов)
  - dlg — диалоги (147 файлов, 5.06 МБ)
  - maps — карты (222 файла, 612.57 МБ)
  - materials — материалы (3700 файлов, 82.77 МБ)
  - models — модели (1193 файла, 219.06 МБ)
  - particles — частицы (274 файла, 0.89 МБ)
  - python — скрипты (52 файла, 1.13 МБ)
  - 
esource — ресурсы (8 файлов, 0.10 МБ)
  - save — сохранения (11 файлов, 3.03 МБ)
  - scripts — скрипты (6 файлов, 0.04 МБ)
  - sound — звук (9835 файлов, 317.42 МБ)
  - data — данные игры (549 файлов, 2.70 МБ)

### SDK (Source SDK)
- **Путь**: C:\Users\Slava\Documents\VampireRemake-Starter\Reference\Vampire - The Masquerade Bloodlines\SDKContent\
- **Размер**: ~2.01 ГБ
- **Структура**:
  - MapSrc — исходные карты
  - MaterialSrc — исходные материалы
  - ModelSrc — исходные модели
  - VpkContent — извлечённое содержимое VPK архивов
    - data\system\ — системные файлы:
      - 
ules.txt — правила игры
      - stats.txt — характеристики
      - items.txt — предметы
      - dialog.txt — диалоги
      - disciplinetgt_*.txt — дисциплины
      - 
pctemplate*.txt — шаблоны NPC
      - quests*.txt — квесты
      - data\quotes.txt — цитаты
  - SDKBinaries — инструменты Source Engine:
    - hammer.exe — редактор карт
    - bsp.exe / rad.exe — компиляция карт
    - studiomdl.exe — создание моделей
    - tex.exe — обработка текстур

### Инструменты в Extras/Developer Tools
- **Level Entity Lists** — текстовые файлы с сущностями карт:
  - ch_hub_1.txt, sm_hub_1.txt, hw_hub_1.txt — хабы
  - ch_*.txt, sm_*.txt, hw_*.txt — локации
  - sp_*.txt — специальные последовательности
  - Формат: ObjNum OriginX OriginY OriginZ Flags Solid FadeMinDist FadeMaxDist PropTypeEntry
- **Original Python Files** — скрипты для каждой локации:
  - chinatown.py, sm_hub_1.py и т.д.
  - Управляют событиями, квестами, NPC
- **Turvy's VPKTool** — распаковка VPK архивов
- **ZylonBane's ZVTool** — консольные инструменты
- **Hammer Files** — исходные карты в формате .vmf

### Документация
- Docs/License.txt — лицензия Activision
- Extras/VTMB Transcripts.txt — транскрипты диалогов (Манчкианская Башня, Радио)
- Extras/VTMB Walkthrough.txt — руководство по версии 1.5
- Unofficial_Patch/VTMBup-readme.txt — документация патча Wesp5

## Инферированные данные

### Версия игры
- **Исходная версия**: 1.0 (2004-10-14, pack000-009)
- **Официальный патч**: v1.2 (включён в VTMBup)
- **Unofficial Patch**: накопительный патч Wesp5/Werner Spahl
  - Базовый патч (Basic Patch) — исправляет баги
  - Плюс-патч (+) — добавляет контент
  - Extras — инструменты и дополнительные материалы

### VPK формат
- Valve Pack архивы Source Engine
- Не Valve Particle System
- Содержат: модели, материалы, звуки, текстуры, скрипты, карты
- Загружаются в числовом порядке (pack000, pack001, ...)
- Более новые версии могут быть в более поздних архивах

## Неизвестное

- Точные изменения в pack010, pack012, pack013
- Взаимосвязи между Python скриптами и VPK архивами
- Где хранятся данные о дисциплинах (Disciplines)
- Как работают механики квестов и NPC
- Структура диалогов в dialog.txt
- Детали патча 1.2 от Activision

## Источники

- **Primary**: Файловая система игры
- **Secondary**: Документация в Extras и SDK
- **External**: VTMBup-readme.txt (Wesp5)

## Следующие шаги

1. Изучить структуру диалогов в dialog.txt
2. Проанализировать NPC шаблоны в 
pctemplate*.txt
3. Исследовать правила в 
ules.txt
4. Понять структуру дисциплин в disciplinetgt_*.txt
5. Изучить Python скрипты локаций

## Ошибки в предыдущем отчёте

- ❌ Unofficial Patch описан как официальный — это **неправда**, это community mod
- ❌ Версия 11.5 взята из walkthrough — **неправда**, walkthrough версия 1.5
- ❌ VPK — Valve Particle System — **неправда**, это Valve Pack архивы Source Engine
- ❌ Содержимое VPK описано частично — **неправда**, структура не изучена полностью

