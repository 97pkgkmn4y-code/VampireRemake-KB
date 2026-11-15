# Отчёт о верификации установки Vampire: The Masquerade — Bloodlines

> Установленные маркеры патча, архивы и SDK перечислены в [[03_Versions-Verified]]. Приведённые ниже размеры и числа файлов относятся к первоначальному инвентарю.

## 1. Что было верифицировано

### Версии игры и патчей
- **Исходная игра**: pack000-009.vpk (оригинальные файлы игры)
- **Unofficial Patch**: отдельный каталог `Unofficial_Patch\`
  - pack010.vpk (62.76 МБ)
  - pack012.vpk (257.47 МБ)
  - pack013.vpk (168.72 МБ)
- **Unofficial_Patch** содержит дополнительные данные:
  - `vdata\system\masquerade.txt` — новая система маскарада
  - `vdata\system\stats - hunter.txt` — характеристики охотников
  - `vdata\system\strings - hunter.txt` — строки для охотников
  - `vdata\system\traiteffects000 - hunter.txt` — эффекты черт для охотников
  - В `npctemplate000.txt` добавлена строка `"AlwaysInnocent" "1"` (mod для охотников)

### VPK архивы
- **Тип**: Valve Pack (Source Engine), НЕ Valve Particle System
- **Количество**: 18 архивов (pack000-013, pack100-103)
- **Содержимое**:
  - pack000-009: происхождение payload UNVERIFIED
  - pack010: происхождение payload UNVERIFIED
  - pack012, pack013: происхождение payload UNVERIFIED
  - pack100-103: назначение payload UNVERIFIED

### SDKContent
- **Путь**: `SDKContent\VpkContent\vdata\system\`
- **Содержимое**:
  - `rules.txt` — правила игры (frenzy, damage, etc.)
  - `stats.txt` — характеристики персонажа
  - `items.txt` — предметы инвентаря
  - `dialog.txt` — диалоги
  - `disciplinetgt_*.txt` — дисциплины (5 файлов)
  - `npctemplate*.txt` — 26 шаблонов NPC
  - `quests_*.txt` — квесты (5 файлов)
  - `clandoc000.txt` — документы кланов
  - `traiteffects000.txt` — эффекты черт

### Инструменты исследования
- **Hammer.exe** — редактор карт (.vmf)
- **vbsp.exe, vrad.exe, vvis.exe** — компиляция карт
- **studiomdl.exe** — создание моделей
- **hlfaceposer.exe** — анимация лиц
- **hlmv.exe** — просмотр моделей
- **soundbrowser.exe** — просмотр звуков
- **Turvy's VPKTool** — распаковка VPK (в Extras/Developer Tools/)
- **Original Python Files** — скрипты локаций (в Extras/)
- **Level Entity Lists** — текстовые файлы сущностей карт (в Extras/)

### Unofficial Patch структура
- **cfg**: 6 файлов (autoexec.cfg, config.cfg, default.cfg, multiplayer.cfg, skill1.cfg, user.cfg)
- **dlg**: 147 файлов диалогов
- **maps**: 222 файла карт
- **materials**: 3700 файлов материалов
- **models**: 1193 файла моделей
- **particles**: 274 файла частиц
- **python**: 52 файла скриптов
- **resource**: 8 файлов интерфейса
- **scripts**: 6 файлов
- **sound**: 9835 файлов звуков
- **vdata**: 549 файлов данных

### Original Python Files
- **Путь**: `Extras/Developer Tools/Original Python Files/`
- **Локации**: bradbury, cemetery, chinatown, crackhouse, downtown, fusyndicate, gallery, giovanni, griffith, hollywood, leopold, lib, malkavian, museum, santamonica, temple, theatre, tutorial, ventrue, warehouse, warrens

### Level Entity Lists
- **Путь**: `Extras/Developer Tools/Level Entity Lists/`
- **Формат**: текстовые файлы с сущностями карт
- **Примеры**: `ch_hub_1.txt`, `sm_hub_1.txt`, `hw_hub_1.txt`
- **Структура**: ObjNum OriginX OriginY OriginZ Flags Solid FadeMinDist FadeMaxDist PropTypeEntry

## 2. Что было неправильным в предыдущем отчёте

### Неправильные утверждения (все исправлены):
- ❌ Unofficial Patch описан как официальный — **исправлено**: это community mod Wesp5/Werner Spahl
- ❌ Версия 11.5 взята из walkthrough — **исправлено**: walkthrough указывает версию 1.5, фактические версии определены по файлам
- ❌ VPK — Valve Particle System — **исправлено**: это Valve Pack архивы Source Engine
- ❌ Содержимое VPK описано частично — **исправлено**: изучена структура pack000-013, Unofficial_Patch, SDKContent

### Что нужно было уточнить:
- Атрибуция pack010, pack012, pack013 по LastWriteTime снята; происхождение payload требует сравнения байтов.
- ✅ Unofficial_Patch содержит дополнительные файлы для охотников и маскарада
- ✅ Инструменты исследования полностью перечислены

## 3. Что было обнаружено

### Важные наблюдения:
1. **Unofficial Patch добавляет контент для охотников**:
   - Новые файлы в `vdata\system`: `masquerade.txt`, `stats - hunter.txt`, `strings - hunter.txt`, `traiteffects000 - hunter.txt`
   - Изменения в NPC шаблонах: `"AlwaysInnocent" "1"` для NPCGeneric

2. **Структура VPK архивов**:
   - pack000-009: оригинальные файлы (2004)
   - pack010: происхождение payload UNVERIFIED
   - pack012, pack013: происхождение payload UNVERIFIED
   - pack100-103: назначение payload UNVERIFIED

3. **SDKContent полностью извлечён**:
   - Все системные файлы доступны для чтения
   - Нет необходимости распаковывать VPK для анализа

4. **Инструменты исследования уже включены в SDK**:
   - Hammer, vbsp, vrad, vvis, studiomdl, hlfaceposer, hlmv, soundbrowser
   - Дополнительно: Turvy's VPKTool, ZVTool

5. **Python скрипты находятся в Extras/**:
   - Original Python Files — скрипты локаций
   - Unofficial_Patch/python/ — модифицированные скрипты

6. **Level Entity Lists содержат детальную информацию о картах**:
   - Формат: ObjNum OriginX OriginY OriginZ Flags Solid FadeMinDist FadeMaxDist PropTypeEntry
   - Поддерживаются различные состояния: -default.txt, -up.txt

## 4. Созданные/обновлённые Obsidian заметки

### Обновлённые заметки:
- `01_Original/01_Game-Structure.md` — структура игры, VPK, Unofficial Patch (уже содержала часть верифицированных данных)

### Новая заметка:
- `01_Original/02_Verification-Report.md` — этот отчёт о верификации

## 5. Что остаётся нерешённым

### Неизвестные:
1. **Точные изменения в pack010, pack012, pack013**:
   - Какие файлы изменены/добавлены
   - Какие файлы удалены

2. **Структура диалогов в dialog.txt**:
   - Формат и правила записи
   - Связи между диалогами и NPC

3. **Системы дисциплин**:
   - Количество дисциплин (5 файлов: disciplinetgt_000-004.txt)
   - Правила использования и ограничения

4. **Механики квестов и NPC**:
   - Как работают квесты в quests_*.txt
   - Связи между Python скриптами и VPK архивами
   - Как NPC шаблоны применяются в играх

5. **Взаимосвязи между источниками**:
   - Связи между Python скриптами и Level Entity Lists
   - Как данные в VPK архивах связаны с SDKContent
   - Как Unofficial Patch модифицирует оригинальные файлы

## 6. Планы на следующие исследования

### Приоритет 1: Понимание игровых систем (краткий обзор)
1. Изучить `dialog.txt` — формат диалогов и зависимости
2. Проанализировать `disciplinetgt_*.txt` — системы дисциплин
3. Исследовать `npctemplate*.txt` — NPC шаблоны и их применение
4. Изучить `rules.txt` — базовые правила (frenzy, damage, etc.)

### Приоритет 2: Картирование данных
5. Маппинг Python скриптов к локациям (через Original Python Files)
6. Связи между Entity Lists и VPK архивами
7. Структура квестов в `quests_*.txt`

### Приоритет 3: Инструменты и методы
8. Проверка Turvy's VPKTool и его возможностей
9. Создание скриптов для анализа больших файлов
10. Разработка стратегии для работы с VPK архивами

### Приоритет 4: Документация
11. Создание заметок о системах дисциплин
12. Создание заметок о NPC шаблонах и квестах
13. Создание заметок о Python скриптах

## Источники

### Верифицированные источники:
- Файловая система игры:
  - `C:\Users\Slava\Documents\Bloodlines-GLM\Reference\Vampire - The Masquerade Bloodlines\Vampire\`
  - `C:\Users\Slava\Documents\Bloodlines-GLM\Reference\Vampire - The Masquerade Bloodlines\Unofficial_Patch\`
  - `C:\Users\Slava\Documents\Bloodlines-GLM\Reference\Vampire - The Masquerade Bloodlines\SDKContent\`
  - `C:\Users\Slava\Documents\Bloodlines-GLM\Reference\Vampire - The Masquerade Bloodlines\Extras\`

- SDKContent\VpkContent\vdata\system\:
  - rules.txt, stats.txt, items.txt, dialog.txt
  - disciplinetgt_*.txt (5 файлов)
  - npctemplate*.txt (26 файлов)
  - quests_*.txt (5 файлов)
  - clandoc000.txt, traiteffects000.txt

- Extras/Developer Tools:
  - Original Python Files/ (22 локации)
  - Level Entity Lists/ (200+ файлов)
  - Turvy's VPKTool/ (VPKTool.exe, Readme.txt)

### Проверенные инструменты:
- Hammer.exe, vbsp.exe, vrad.exe, vvis.exe, studiomdl.exe, hlfaceposer.exe, hlmv.exe, soundbrowser.exe
- Turvy's VPKTool.exe, Readme.txt

### Неизвестное:
- Точные изменения в pack010, pack012, pack013 (требуется распаковка)
- Полное покрытие Python скриптов за пределами исследованных локаций
- Взаимосвязи между Python скриптами и VPK архивами (требуется анализ)

## Следующие шаги

1. **Начать с dialog.txt**: понять формат диалогов и зависимости
2. **Перейти к disciplinetgt_*.txt**: изучить системы дисциплин
3. **Проанализировать npctemplate*.txt**: понять NPC шаблоны
4. **Создать заметку о dialog.txt**: документировать формат и правила
5. **Создать заметку о дисциплинах**: документировать системы дисциплин






