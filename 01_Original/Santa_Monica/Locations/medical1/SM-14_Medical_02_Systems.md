---
id: SM-14-SYSTEMS
map: sm_medical_1
---
# SM-14.02 — Доступ и интерактивные системы

## Верхний этаж

[VMF+BSP] Четыре `trigger_player_activity_level` имеют `targetname=restricted_section` (IDs 6175, 6183, 6191, 6708), `criminal_level=3`, `supernatural_level=−1`. `player_on_floor_two` (ID 6411, L74844) вызывает `guard_sees_player.CheckVisibility`; `guard_sees_player` (ID 6410, L74824) при обнаружении посылает два выхода: адресный `guard_warning-wesp.Trigger` и Python-вызов `sneakTest()`. Имя `guard_warning-wesp` отсутствует как `targetname` и в исходном VMF, и в entity lump установленной UP BSP; выполнение **этого** выхода не подтверждено.

[PY] `sneakTest()` находится в `Unofficial_Patch/python/vamputil.py:963`; `santamonica.py:21–22` содержит **условный** `from vamputil import *`. Только при `G.Patch_Plus==1`, низком центре игрока (`GetCenter()[2]−GetOrigin()[2] <= 18`), `CalcFeat("Sneaking")>4` и квадрате расстояния до охранника `>18000` функция возвращается без предупреждения. В остальных случаях она вызывает существующий `guard_warning.Trigger` (VMF ID 6409, L74807). Значит, реализация скриптовой ветки существует независимо от неразрешённого имени `guard_warning-wesp`; её фактическое связывание с пространством имён и выполнение в игре не проверялись наблюдением.

[VMF] Две `security_camera`: `camera_cs` (ID 5613, L62814) направляет обнаружение в `guard_to_cs.StartSchedule`, `camera_prescriptions` (ID 5615, L62863) — в `guard_to_prescriptions.StartSchedule`. Существование этих связей не доказывает, что игрок неизбежно попадает в поле зрения.

[PY] `guardDialog()` (L814) при `G.Guard_Dominated` или `G.Guard_Open` устанавливает `G.Clinic_Upstairs_Safe=1` (если было 0), убивает `restricted_section`, `guard_warning`, оба расписания охранника и `player_on_floor_two`. При `G.Guard_CS==1` или `G.Guard_Open==1` запускает отдельные маршруты сопровождения к CS или CIS и переводит флаги в 2. При `G.Guard_Warning>=3` без разрешения планирует враждебность через 5 секунд. [DLG] `clinic_guard.dlg` строки 2→121 и 121 дают `G.Guard_Open=1` при `G.Nurse_Persuade==1`; строки 3/5 дают ключ через Dominate/Dementation, строки 6/7 дополнительно ограничены `G.Patch_Plus==1`. Доступность реплики зависит от условий и порядка веток DLG.

[VMF] `controlledsubstancesdr` ID 5603 и `cisdr` ID 5626 вызывают `keycardCheck()` при открытии. [PY] Функция L912 удаляет `item_k_clinic_cs_key` только после увеличения `G.Clinic_Keycard_Used` до 2. Аналогично `stairsKeyCheck()` (L1024) удаляет лестничный ключ на втором открытии. Это логика расходования ключа, а не доказательство, что обе двери открыты с самого начала.

## Первый этаж и подвал

[VMF] Три `nurse_talk_trigger` (IDs 6272, 6326, 6342) присваивают `G.Nurse_Force=1` при касании. `Nurse.OnDialogEnd` вызывает `nurseDialog()` (ID 5298, L58571); `Nurse.OnFoundPlayer` отдельно вызывает `first_floor_guard.Spawn` (L58568). [PY] `nurseDialog()` (L959) переводит `G.Nurse_Force` в счётчик `G.Nurse_Warn`; на 3 вызывает `first_floor_guard.Spawn`, `SetCriminalLevel(2)` и враждебность охранника. Если `G.Nurse_Flag` или `G.Nurse_Persuade`, удаляет триггеры разговора. [DLG] Nurse ID 61 выдаёт `item_k_clinic_stairs_key`, устанавливает `G.Nurse_Persuade=1` и сбрасывает предупреждения. [INF] Система превращает нарушение пространственного правила в социальное предупреждение, затем в боевое последствие — при условии, что соответствующие события реально выполняются.

[VMF] `morgue_trunk` ID 6146 вызывает `gimbleItemPickup()`; три морфиновых предмета IDs 6510/6512/6514 вызывают `morphinePickup()`; `garou_blood` ID 6656 вызывает `werewolfBloodPickup()`. [PY] Выдача записи в журнале зависит от текущего состояния квеста и/или инвентаря (L806–812, 947–956, 1073–1084), поэтому физический предмет сам по себе не гарантирует квестовый исход.

## Терминалы и двери

| Терминал / предмет | Проверенное действие | Ограничение доказательства |
| --- | --- | --- |
| `smmc` ID 5297, `hack_file=clinic_security_computer.txt`, `difficulty=3`, `skilltype=2` [VMF/DATA] | Подменю Camera использует пароль `optometry`; `trigger 1` отключает CS-камеру и включает prescription, `trigger 0` делает обратное (VMF L58496–58503). | Указанная сложность относится к терминалу; реальный доступ к нему и ввод пароля не наблюдались. |
| `cis` ID 5636, `hack_file=clinic_cis_computer.txt`, `difficulty=3`, `skilltype=2` [VMF/DATA] | `CS Door` с паролем `dosage`: `trigger 0/1` запирает/отпирает `cs_doorknob`; `CS Cabinet` с паролем `paige`: `trigger 2/3` запирает/отпирает `left_door` и `hack_door`; одновременно переключаются камеры (VMF L63228–63237). | В terminal data две ветки Cabinet зависят от `G.Werewolf_Quest==0` или `==1`; состояния >1 не покрыты этими двумя ветками. |
| `employee_entrance` ID 5720 [VMF] | Это `prop_doorknob` с `parentname=halldr1`, `difficulty=9`, `skilltype=1`; `vandalDialog()` отпирает ручку при `G.Vandal_Permission`. | Ручка и дверь — разные сущности; значение `skilltype` требует движкового определения для точного названия навыка. |
| `clinic_administration_computer.txt` [DATA] | VMF-терминал ID 6160 у `(857,342,36)` имеет `difficulty=2`, `skilltype=2`; данные содержат записи персонала и email с зависимостями `G.Werewolf_Quest` / `G.PP`. | Email подтверждает сведения на экране, но не квестовое последствие чтения без отдельного выхода/скрипта. |
| `blood_bank_computer.txt` [DATA] | Терминал VMF ID 5950, `difficulty=3`; меню Freezers требует `ambrosia`. При `G.E_Quest<2` выдаёт ошибку; при `G.E_Quest==2` или `G.E_Quest>1 && G.PP==1` показывает код `1969` и вызывает `freezerCode()` (DATA L27–40). | Наличие записи не доказывает, что игрок может попасть к терминалу в любой момент. |
| `malcolm_computer.txt` [DATA] | Терминал VMF ID 6120, `difficulty=2`; меню Patients требует `hippocrates`; запись H. Poe зависит от `G.Story_State<10` (DATA L16–29). | Переписка служит информационным ресурсом; автоматический квестовый эффект чтения не показан. |
| `morgue_computer.txt` [DATA] | Терминал VMF ID 6143, `difficulty=3`; меню Cadavers требует `Cowbell`; отдельные записи зависят от `G.VirgilCrumbKnowledge`, `G.Heather_Drank`, `G.Story_State`, `G.PP` (DATA L18–85). | Условия меняют отображаемую информацию, а не подтверждают сами по себе сюжетный исход. |

Подтверждённые технические механизмы доступа: социальный маршрут Nurse→guard [DLG/PY], способности в диалоге guard [DLG], ключи и дверные проверки [VMF/PY], терминалы с I/O [VMF/DATA]. Их реальная доступность игроку при конкретном состоянии зависит от условий, расположения и движка. Проходимость вентканалов игровым тестом не установлена.
