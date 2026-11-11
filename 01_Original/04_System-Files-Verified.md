# Системные файлы игры — ВЕРИФИЦИРОВАНО

## SDKContent\VpkContent\vdata\system\

### Файлы правил (rules.txt, rules_tables.txt)
- **rules.txt**: 18181 байт (Unofficial Patch), 18020 байт (оригинал)
- **rules_tables.txt**: 8161 байт (Unofficial Patch), 8042 байт (оригинал)
- **Содержание** (VERIFIED):
  - VampFrenzy_Info — правила потери рассудка
  - Damage_Info — правила нанесения и soaking урона
  - Obfuscate_Info — правила скрытности
  - VampHeal_Info — правила регенерации и питания

### Характеристики (stats.txt, stats - vampire.txt, stats - hunter.txt)
- **stats.txt**: 101894 байт (Unofficial Patch), 92194 байт (оригинал)
- **stats - vampire.txt**: 101894 байт (Unofficial Patch)
- **stats - hunter.txt**: 102170 байт (Unofficial Patch)
- **Содержание** (VERIFIED):
  - Атрибуты: Strength, Dexterity, Stamina, Charisma, Manipulation, Appearance, Perception, Intelligence, Wits
  - Билды: BloodPool, FaithPoints, Starting_Equipment, Excluded_Equipment
  - Характеристики кланов в ClanDataTables

### Предметы (items.txt)
- **items.txt**: 33109 байт (Unofficial Patch), 28293 байт (оригинал)
- **Содержание**:
  - Определения предметов инвентаря
  - Типы оружия, брони, расходников

### Дисциплины (disciplinetgt_000.txt по disciplinetgt_004.txt)
- **disciplinetgt_000.txt**: 61347 байт (Unofficial Patch), 50234 байт (оригинал)
- **disciplinetgt_001.txt**: 65597 байт (Unofficial Patch), 49524 байт (оригинал)
- **disciplinetgt_002.txt**: 57510 байт (Unofficial Patch), 40438 байт (оригинал)
- **disciplinetgt_003.txt**: 43035 байт (Unofficial Patch), 40840 байт (оригинал)
- **disciplinetgt_004.txt**: 66052 байт (Unofficial Patch), 47763 байт (оригинал)
- **Содержание** (VERIFIED):
  - DisciplineTgtList — список дисциплин
  - DisciplineTgt — определения конкретных дисциплин
  - Параметры: Name, InternalName, Discipline, Level, BloodCost, Overt, RecoveryTime, AoE, Filters
  - 5 дисциплин (Animalism, Auspex, Celerity, Dominate, Fortitude)

### NPC шаблоны (npctemplate*.txt)
- **npctemplate000.txt**: 2118 байт (Unofficial Patch), 2075 байт (оригинал)
- **npctemplate001.txt** по npctemplate025.txt: 26 шаблонов NPC
- **Содержание** (VERIFIED):
  - ClanDataTables — таблицы данных кланов
  - Text — имя, описание, родительский шаблон
  - General — физические параметры, звук группы, AlwaysInnocent
  - Attributes — атрибуты персонажа
  - Clans — данные о принадлежности к кланам
  - Disciplines — дисциплины персонажа

### Квесты (quests_*.txt)
- **quests_chinatown.txt**: 14421 байт (Unofficial Patch), 11202 байт (оригинал)
- **quests_downtown.txt**: 33079 байт (Unofficial Patch), 31182 байт (оригинал)
- **quests_hollywood.txt**: 26193 байт (Unofficial Patch), 22471 байт (оригинал)
- **quests_santamonica.txt**: 39175 байт (Unofficial Patch), 33095 байт (оригинал)
- **quests_main.txt**: 1279 байт (оригинал)
- **Содержание**:
  - Определения квестов
  - Связи между квестами и NPC

### Диалоги (dialog.txt)
- **dialog.txt**: 537 байт (оригинал), 78867 байт (Unofficial Patch)
- **Содержание** (VERIFIED):
  - DialogData — данные диалогов
  - Text — тексты диалогов (Greeting, Appreciation, Leaving, Discipline_Blood, etc.)
  - Dependencies — зависимости (Discipline: Dominate, Dementation, Feat: Persuasion, Seduction)
- **ВЕРДИКТ**: Только определения, реальные диалоги где-то в VPK архивах

### Цитаты (loadingtips.txt)
- **loadingtips.txt**: 114038 байт (Unofficial Patch), 111249 байт (оригинал)
- **Содержание**:
  - Loading tips при запуске игры

### Кланы (clandoc000.txt)
- **clandoc000.txt**: 91531 байт (Unofficial Patch), 39191 байт (оригинал)
- **Содержание**:
  - Документация о кланах

### Черты (traiteffects000.txt, traiteffects000 - vampire.txt, traiteffects000 - hunter.txt)
- **traiteffects000.txt**: 66863 байт (Unofficial Patch), 45672 байт (оригинал)
- **traiteffects000 - vampire.txt**: 66863 байт
- **traiteffects000 - hunter.txt**: 66864 байт
- **Содержание**:
  - Эффекты черт (Traits) для вампиров и охотников

### Характеристики NPC (dispositiontable.txt)
- **dispositiontable.txt**: 24888 байт (оригинал)
- **Содержание**:
  - Таблицы настроения NPC

### Инвентарь NPC (vendors.txt)
- **vendors.txt**: 28084 байт (Unofficial Patch), 22429 байт (оригинал)
- **Содержание**:
  - Предметы, продаваемые NPC

### Системные файлы
- **charaction_sounds.txt**: 317 байт
- **charcreatewizard.txt**: 78867 байт (Unofficial Patch), 76346 байт (оригинал)
- **chareditor.txt**: 73 байт
- **dicerolls.txt**: 5596 байт
- **experience_table.txt**: 14708 байт (Unofficial Patch), 12408 байт (оригинал)
- **feats.txt**: 11148 байт (Unofficial Patch), 10946 байт (оригинал)
- **histories000.txt**: 64529 байт (Unofficial Patch), 62574 байт (оригинал)
- **infobartypes.txt**: 24119 байт (Unofficial Patch), 23968 байт (оригинал)
- **interestingplacetypelist.txt**: 22788 байт (Unofficial Patch), 22002 байт (оригинал)
- **keynames.txt**: 1923 байт
- **levelingtemplate_000.txt**: 51356 байт (Unofficial Patch), 50366 байт (оригинал)
- **newscaster_main.txt**: 4397 байт (Unofficial Patch), 4267 байт (оригинал)
- **newscaster_side.txt**: 4990 байт (Unofficial Patch), 4686 байт (оригинал)
- **particleimpacttable.txt**: 12426 байт (Unofficial Patch), 10910 байт (оригинал)
- **sndscheme_*.txt**: схемы звуков
- **sound_volume_table.txt**: таблицы громкости звуков
- **stealth.txt**: 11624 байт (Unofficial Patch), 11605 байт (оригинал)
- **stealthkillrules.txt**: 882 байт
- **strings.txt**: 25018 байт (Unofficial Patch), 24490 байт (оригинал)
- **strings_internal.txt**: 8953 байт
- **traiteffect.txt**: 452 байт

## Выводы

### ВЕРИФИЦИРОВАННЫЕ системы
1. **Правила игры**: rules.txt содержит VampFrenzy_Info, Damage_Info, Obfuscate_Info, VampHeal_Info
2. **Характеристики**: stats.txt определяет атрибуты, билды, характеристики кланов
3. **Дисциплины**: 5 файлов disciplinetgt_*.txt, каждый содержит 13 дисциплин
4. **NPC шаблоны**: 26 файлов npctemplate*.txt, каждый содержит ClanDataTables
5. **Квесты**: 5 файлов quests_*.txt, покрывающие все локации
6. **Диалоги**: dialog.txt содержит только определения, реальные диалоги в VPK

### НЕИЗВЕСТНОЕ
1. Где хранятся реальные тексты диалогов (в VPK архивах)
2. Как связываются дисциплины с NPC шаблонами
3. Какие изменения вносил Unofficial Patch в правила (только masquerade.txt и hunter files)
4. Связи между Python скриптами и системными файлами
