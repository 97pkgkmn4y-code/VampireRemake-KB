# Bloodlines Research - Индекс

## Категории заметок

### 📦 Core
- [01_Game-Structure.md](./01_Game-Structure.md) — Структура игры, VPK архивы, Unofficial Patch
- [02_Verification-Report.md](./02_Verification-Report.md) — Отчёт о верификации
- [02_VPK-Tools.md](./02_VPK-Tools.md) — Инструменты работы с VPK

### 🔍 Versions & Systems
- [03_Versions-Verified.md](./03_Versions-Verified.md) — Версии игры и патчей
- [04_System-Files-Verified.md](./04_System-Files-Verified.md) — Системные файлы
- [05_Research-Tools-Verified.md](./05_Research-Tools-Verified.md) — Инструменты исследования

### 🎯 Initial Research
- [06_Initial-Orientations-Verified.md](./06_Initial-Orientations-Verified.md) — Первичная ориентация и верификация

## Нерешённые вопросы

### НЕИЗВЕСТНОЕ (требует дальнейшего исследования)

1. **Точные изменения в pack010, pack012, pack013**
   - Какие файлы изменены/добавлены/удалены
   - Разница размеров Unofficial Patch vs pack010

2. **Где хранятся реальные диалоги**
   - dialog.txt содержит только определения
   - Текстовые диалоги где-то в VPK архивах

3. **Как работают системы дисциплин**
   - Связи между disciplinetgt_*.txt и NPC шаблонами
   - Ограничения и правила использования

4. **Механики квестов и NPC**
   - Как работают quests_*.txt
   - Связи между Python скриптами и VPK архивами
   - Как NPC шаблоны применяются в играх

5. **Взаимосвязи между источниками**
   - Связи между Python скриптами и Level Entity Lists
   - Как данные в VPK архивах связаны с SDKContent
   - Как Unofficial Patch модифицирует оригинальные файлы
   - Связи между pack010, pack012, pack013

## Следующие шаги исследования

### Приоритет 1: Понимание систем дисциплин
1. Изучить disciplinetgt_000.txt — Animalism
2. Изучить disciplinetgt_001.txt — Dementation
3. Изучить дисциплины в NPC шаблонах
4. Понять, как дисциплины применяются к NPC

### Приоритет 2: Понимание NPC и квестов
5. Проанализировать npctemplate001.txt — шаблон "пустышки"
6. Изучить quests_main.txt
7. Связать Python скрипты с NPC и квестами

### Приоритет 3: Понимание диалогов
8. Найти реальные диалоги в VPK архивах
9. Изучить структуру dialog.txt более подробно
10. Связать диалоги с NPC шаблонами

### Приоритет 4: Маппинг ресурсов
11. Связи между Python скриптами и Level Entity Lists
12. Как Unofficial Patch модифицирует файлы
13. Структура VPK архивов (какие файлы где)

## Критерии верификации

### Валидация данных
- **VERIFIED** требует прямого наблюдения (командная строка, содержимое файла, результат выполнения)
- **UNKNOWN предпочтительнее неподтверждённых утверждений**
- **НЕ claim source "completely extracted"** без фактического подсчёта
- **НЕ claim note "updated"** без чтения обратно
- Использовать Version.inf, gameinfo.txt, README файлы для версионирования

### Структура базы знаний
- Исходные файлы игры — primary evidence
- Obsidian vault — persistent research memory (не замена файлов)
- Различать оригинальную игру, патчи, SDK источники и производные материалы
- Не путать файлы из разных версий
- Не выдумывать отсутствующие связи или поведение
