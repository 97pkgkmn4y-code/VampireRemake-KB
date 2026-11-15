---
id: SM-30
map: sm_vamparena
reference: Unofficial Patch Plus 12.0
status: PARTIAL / VERIFIED_STATIC / RUNTIME_PENDING
---
# SM-30 — Foxy Boxes

Foxy Boxes — арена `sm_vamparena` из задания The Hunted Hunter. Имя локализации взято из `SDKContent/VpkContent/vdata/system/mapnames_localized.txt:103`. У обеих размещённых версий противника в UP BSP отсутствует `dialogname`; ветви задания принадлежат [[../../Quests/Knox_Quest|DLG Кнокса и Бертрама]].

## Источники

| Путь от установленной игры | SHA-256 |
|---|---|
| `Unofficial_Patch/maps/sm_vamparena.bsp` | `cbf8e78fc55f6dcd8df3123b8dff976aafcb8b0be57ba9c05d6d55fa8c19b97b` |
| `Vampire/maps/sm_vamparena.bsp` | `0e86a7c7e3ef90b55826d07537894d372bbb1c9ec09734f1420f8c18e5a0e754` |
| `SDKContent/MapSrc/up sources/sm_vamparena.vmf` | `461c5579cbc1bcf835b3d2dbc2e7b86b5bda915a20f4a094b962fe3a6dd1ec0b` |
| `Unofficial_Patch/maps/sm_hub_1.bsp` | `566aa6200c7a56b7892a3b42c855a1745382273ad4a0264c911c3c0ccdee8e29` |
| `Unofficial_Patch/python/santamonica/santamonica.py` | `634c5a2e97566d709157f4cd43424509689199302a6433708f3d2ced53f13fff` |
| `Unofficial_Patch/python/vamputil.py` | `a2873d3a2a230c0ac9f38398e093910810f7ab3c51fa06bae71a7b004168e491` |
| `Unofficial_Patch/vdata/system/quests_santamonica.txt` | `d1f4cc18f44d4f231d0764a1d49da314fe4fb383ca70cddae8ef23db28b02f38` |

UP BSP v17 содержит 128 entities, базовый BSP v17 — 109. SDK VMF содержит `OnDeath → asianVampDeath()` для двух NPC (строки 13192, 13253). Поведение ниже опирается на установленный BSP и Python.

## Пространство и доступ

- В `sm_hub_1` дверь `vamparenadoor` у `(-658,517.5,-58)` имеет электронную ручку с `key_name=item_k_gimble_key` и `difficulty=1`. `OnFullyOpen → vamparenatransition.ChangeNow`, landmark `vamparena`. Ключ Foxy Boxes связан с моргом: `santamonica.py:gimbleDead()` при `(Knox_Quest == 5 and Patch_Plus == 0) or VirgilCrumbKnowledge == 1` добавляет `gimble_key` и `gimble_ring` в `morgue_trunk`; `gimbleItemPickup()` при наличии ключа пишет Knox Asian=7. См. [[../medical1/SM-14_Medical_03_Quests|Clinic]].
- Внутри `info_player_start` = `(-111.874,-633.025,31.8837)`, landmark = `(-112,-633,9)`. `exitdoor` (`*3`) возвращает в Hub 1 тем же именем перехода. Вход и выход занимают южную часть карты, боковая дверь `officedoor` (`*2`) ведёт в сторону +X. `prop_hacking` у `(84,-517,43)` находится с той же стороны от входного коридора.
- К северу от входа `arenadoor` (`*1`, `(-137,-400.5,54)`) отделяет коридор от зоны боя. `player_in_room` (`*5`) расположен за дверью. Его локальный AABB из lump 14 после прибавления origin охватывает X [-420,256], Y [-304,-276], Z [0,128]. За ним `sVamp_entrance` у `(-129,151,0)` и NPC у `(-239,162,4)`.
- Выборка горизонтальных world faces UP BSP (lump 7) подтверждает пол Z=0 у старта и двери выхода (678), перед порогом арены (682–683), за порогом и в полосе триггера (684), в зоне противника (437) и у бокового офиса (685). Высоты относятся к полигонам карты. Динамические коллизии, перемещения на уступах и работа двери после боя открыты.

## Сцена и бой

По [[../../Space/Santa_Monica_BSP_Brush_Routes.csv|пробам]] ходовой объём достигает зоны поклона из входного коридора по world model (`arena-approach`, 68 точек) и доходит до офисной стороны (`arena-office`). С неподвижным брашем `arenadoor` `*1` у `(-137,-400.5,54)` путь в зону поклона не найден при тех же параметрах (`arena-closed`, 333 посещённых состояния). Это проверяет геометрическую роль створки. Время начала закрытия и блокировка после контакта относятся к I/O и сцене ниже.

| Шаг | Сохранённые связи UP BSP и Python |
|---|---|
| Загрузка | `logic_auto.OnMapLoad → unhidePlus()` запускает alias `patchtype`; текущий user.cfg выбирает `setPlus()`. Его блок Foxy Boxes при наличии `AsianVamp` и `Asian_Swap=0` скрывает исходного NPC и переименовывает его в `AsianVamp_basic`, показывает `AsianVamp_plus`, переименовывает его в `AsianVamp` и ставит `Asian_Swap=1`. При Basic перед заменой доступен NPC `AsianVamp` с `StartHidden=0`, `item_w_chang_blade`, `item_w_crossbow` и `cantdropweapons=1`. Plus-копия начинается скрытой и имеет `item_w_avamp_blade`, `item_w_crossbow`, `cantdropweapons=0`. |
| Вход на арену | `player_in_room.OnStartTouch → player_enter_arena.Trigger`. Записанный порядок выходов relay: очистка активных дисциплин (0, один раз), `focusa1.PlayAsCameraTarget` (0), `tracka1.PlayAsCameraPosition` (0), `sVamp_entrance.BeginSequence` (0.5), запись `asian_fade.Fade` с пустым ключом (0), `arenadoor.Lock` (0.1), `arenadoor.Close` (0). Пустой ключ присутствует и в базовом BSP. Его исполнение неизвестно. |
| Поклон и агрессия | `sVamp_entrance` назначает `pre_fight_bow` актёру с именем `AsianVamp`. `OnBeginSequence → SetRelationship("player D_HT 5")` задержан на 3 с. У обоих NPC `OnFoundPlayer → arenadoor.Lock` без задержки. |
| Смерть | Оба NPC имеют два `OnDeath`: `arenadoor.Unlock` и `asianVampDeath()` без задержки. Скрипт пишет `Kjspy_Dead=1`, журнал Knox Asian=3 (XP-ключ `Asian01`). В теле функции есть отдельная ветка создания меча, арбалета и подсветки при `Patch_Plus == 2`; обычный `setPlus()` устанавливает 1. Подбор оружия при активной Plus-копии требует проверки в игре. |
| Отчёт | `knox.dlg:292–297` и другие ветки проверяют `Knox_Quest == 6 or IsDead("AsianVamp")`. У вариантов Plus с лицензией Гимбла есть удаление лицензии при ответе. Пример основного исхода: ID 381 ставит `Knox_Quest=7`, `Knox_Done=1`, журнал Knox Asian=4. |

Базовый BSP содержит одного изначально скрытого NPC и раскрывает его при входе на арену. В базовом BSP враждебность привязана к `OnEndSequence` без задержки. Это различие между двумя файлами BSP. В установленном UP Basic и Plus используют описанный выше UP BSP с выбором актёра через конфигурацию.

## Расхождения и проверки

- В `knox.dlg:494` условие содержит буквальное `G.Knox_Quest == 6 and or IsDead("AsianVamp")`. Проверить обработку повреждённого условия и соседние ответы Plus, особенно после разоблачения Бертрама.
- Проверить доступ с ключом и без него, переключение актёра при первой загрузке и после загрузки сохранения, закрытие арены, кадр/поклон, отпирание, журнал, фактический набор оружия и выход. См. [[../../Space/Runtime_Verification|план runtime-проверок]].
