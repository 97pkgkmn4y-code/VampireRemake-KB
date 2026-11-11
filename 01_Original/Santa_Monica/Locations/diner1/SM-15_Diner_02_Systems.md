---
id: SM-15-SYSTEMS
map: sm_diner_1
---
# SM-15.02 — Засада и персонажи

## Развилка состояниями

| Условие при загрузке | Действие | Доказательство |
| --- | --- | --- |
| `G.Therese_Quest==3` | `dinerAttack()` прячет Doris и посетителей, включает `trigger_attack`, `spawner_relay` показывает четырёх assassin. При `Patch_Plus==0` дополнительно `assassin_s.WillTalk(0)`. | [PY] `santamonica.py` L1085–1106; [VMF] `logic_auto` ID 280, `spawner_relay` ID 283 |
| Иное состояние | Doris и посетители показаны, четыре assassin скрыты, `post_robbery_cop_call` скрыт, `world.SetCopGrace(0.0)`. | [PY] L1107–1129 |
| `Therese_Quest<3 && Story_State<4 && Killer_Angry==0` | `Killer` показан; при `Patch_Plus==1 && Killer_Phoned==0` запускается сцена телефона, временно `SetSafeArea(2)`, затем через 20 секунд планируется `SetSafeArea(1)`. | [PY] `killerInDiner()` L1144–1175; [VMF] `logic_auto` ID 280 |
| Условие Killer ложно | `Killer.Kill()`; наличие шаблона NPC в VMF не доказывает его присутствие в данном состоянии. | [PY] L1159–1162 |

## Охрана пространства и исход засады

[VMF] `trigger_attack` ID 266 `OnStartTouch → go_attack.Trigger`; `go_attack` ID 274 устанавливает `world.SetSafeArea(0)`, запирает `dindoora`, запускает `assassins_attack` и делает `assassin_*` враждебными. Разговорный `assassin_s` также может вызвать этот relay через `OnFoundPlayer`. У четырёх NPC `OnDeath → thug_counter.Subtract 1`; `thug_counter` ID 286 стартует с 4, минимум 0, а `OnHitMin` вызывает `thugsAllDead()` и включает `post_robbery_cop_call`. Это цепь сущностей, **не** доказательство, что игрок обязан убить четырёх противников.

[DLG/PY] `thug.dlg` стартовые условия: ID 43 `Patch_Plus==1 → 1`, ID 44 `Patch_Plus==0 → 41`. ID 11/31 пишут `G.Thugs_Peace=1`; ID 22 — `G.Thugs_Attack=1`. [VMF] `assassin_s.OnDialogEnd` вызывает `thugState()` (ID 235); [PY] `vamputil.py:1037–1054` при `Thugs_Attack==1` делает четырёх NPC враждебными, а при `Thugs_Peace==1` выключает `trigger_attack` и `go_attack`, отключает разговор `assassin_s` и вызывает `thugsAllDead()`. Таким образом в статическом UP Plus есть **мирная причинная ветка к тому же состоянию квеста**; её достижимость игроком в конкретном состоянии требует проверки DLG/движка.

[PY] `thugsAllDead()` (`santamonica.py` L1212–1231) не повторяет действие при `Therese_Quest==4`; иначе устанавливает `Therese_Quest=4`, квест `Diner=2`, `world.SetSafeArea(1)`, запускает звонок `phone_ring` и `SMphone.WillTalk(1)`. [VMF] `SMphone.OnDialogEnd` открывает `dindoora` (ID 238). Здесь телефон служит условным связующим звеном между завершением засады и выходом.

## Doris, Killer и предмет Lily

[VMF/PY/DLG] `Doris.OnDialogEnd → dorisDialog()` (ID 252). `doris.dlg` ID 81 увеличивает `G.Doris_Scare`; при 1–3 `dorisDialog()` запускает `Doris_Faint`, при >3 наносит Doris 100 урона (`santamonica.py` L1131–1141). DLG ID 51 ставит `Doris_Lily=1`, ID 62/63 ставят `Doris_Purse=1` и вызывают `playerGotPurse()`; ID 121/131/141/151 записывают отдельные сведения. Стартовые узлы ID 184 (Nosferatu) и 185 (первый разговор); порядок оценки при пересечении условий не проверен.

[PY/VMF] `lillyStuff()` показывает `lilly_purse` только при `E_Quest==1` и (Nosferatu **или** мёртвой Doris). `lilly_purse.OnPlayerPickup → playerGotPurse()` (ID 303). Функция устанавливает стадию Lily 11 или 7 в зависимости от `RolfTotenKnowledge` при исключении состояний 10/5/6 и выдаёт фото, bailbond receipt, ключ; саму purse дополнительно выдаёт не-Nosferatu. Это межлокационная линия, а не просто декоративная сумка (`santamonica.py` L1186–1209).

[DLG/PY] `killer.dlg` имеет 218 нумерованных строк; стартовые условия ID 213–218 зависят от `Story_State`, `times_talked`, `Killer_Lucky`, `Killer_Freed`. ID 137/138 и 152/153 устанавливают `Killer_Freed=1` и разные стадии `Serial`; ID 135/136 имеют дополнительный эффект Humanity при `Patch_Plus==1`. [VMF] `Killer.OnFoundPlayer → killerInDinerAngry()` меняет модель на Beastform и ставит `Killer_Angry=1` [PY L1179–1184]. Наличие DLG-ветки не доказывает, что она доступна при встрече в Diner.
