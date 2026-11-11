# SM-18 — причинность и границы вывода

## Нормальная ветка (`G.Gimble_Vandal=0`)

1. [DLG] Телефонная ветка Stan 12→51→52→61 либо 13→21→32→41 устанавливает `G.Gimble_Buzzer=1`; ID 71 ставит `Arthur Knox=6`. Это два способа получить приглашение, а не два обязательных события.
2. [VMF] `logic_auto` ID 1133 пытается начать разговор в подвале. [DLG] Инициализация 282–285 выбирает реплики по состояниям телефона/клана; разговор 111 или 251 ставит `G.Gimble_Leave=1`. [VMF] Независимо от значения этой переменной OnDialogEnd Stan запускает `gimble_leave_check` ID 1169. Прямого VMF-чтения `G.Gimble_Leave` в этой цепи не найдено.
3. [VMF] True запускает последовательности `gimble_leave` ID 63609 → `gimble_leave_end` ID 995 → `gimble_teleport`, после чего Stan перемещён к нижней зоне. [HYP] Успешное завершение анимации в установленной игре не наблюдалось.
4. [VMF] OnDeath Stan запускает `gimble_dead_relay` ID 1139 и `gimbleDeath()`; [PY] последний ставит `Arthur Knox=3`, `G.Gimble_Dead=1`. Relay отпирает `gimbledoor1/2`, переносит игрока и запускает освобождение Carson. [VMF] `player_release_carson` деактивирует `carson_switch`, что отпирает/открывает `celldoor4`, а `_2` запускает диалог Carson.
5. [DLG] После `G.Gimble_Dead=1` Carson начинает с ID 21 (или Nosferatu ID 61); они ставят `G.Carson_Rescued=1`. [VMF] OnDialogEnd запускает `carson_free_relay` и `gimble_attack_check`; True ветка последнего задаёт Stan враждебность `D_HT 5` и отпирает `gimbledoor3`. [INF] Это карта задаёт нападение при проверке, но его фактическое воспроизведение требует наблюдения.

## Plus ветка с Vandal

- [DLG] При `G.Patch_Plus=1`, `G.Vandal_Quest=1` и Persuasion 5 Stan ID 162/193→255→256/257 ставит `G.Gimble_Vandal=1`, `Danielle=7`; Humanity ≥4 даёт временное −1 и `G.Gimble_Humanity=1`. Это условная ветка, не гарантированная часть прохождения.
- [VMF] `gimble_leave_check` False запускает `gimble_leave2`, через 4 c отпирает `gimbledoor3` и посылает `Stan_Gimble.Kill`. Позднее `gimble_attack_check` False снова посылает Stan `Kill` и **явно** `gimble_dead_relay.Trigger` (L23727–28). Следовательно, relay в Plus ветке не зависит только от события OnDeath. [HYP] Будет ли `Kill` вызывать `gimbleDeath()` и когда именно установится `G.Gimble_Dead`, исходный текст I/O не доказывает.
- [DLG] Carson IDs 13/14 при `G.Gimble_Vandal>0` ставят `G.Gimble_Dead=1`, `Arthur Knox=3`; ID 13 при `G.Gimble_Humanity=1` возвращает Humanity +1. [INF] При достижении диалога эти действия задают ключевой квестовый результат независимо от непроверенного OnDeath Stan; [VMF] OnDialogEnd Carson в этой ветке явно запускает `gimble_dead_relay` через `gimble_attack_check` False. Момент срабатывания `Kill → OnDeath` и то, проходит ли игрок к Carson до диалога, остаются runtime-вопросами, а не пробелом в статической причинности.

## Внешние зависимости и возможные расхождения

- [PY] `santamonica.py:1938–1945` `gimbleQuestDone()` запирает `intercom_button`, если `G.Gimble_Dead=1` **или** `G.Gimble_Vandal=1`; при `G.Patch_Plus=0` дополнительно закрывает `basementdr`. Вызов этой функции на другой карте нужно доказать отдельно; здесь известна лишь её логика.
- [PY] `santamonica.py:44–49` при Plus и `G.Carson_Rescued=1` удаляет в квартире `Carson_Computer`, `Carson_Poster`, `tape_player`; это межкартовый эффект, зависящий от запуска соответствующей функции квартиры. См. [[SM-16_Apartment_00_Index]].
- [PY] `vamputil.py:595–597` при `G.Gimble_Dead=1` скрывает `stumpy`, если объект существует. Это не доказывает немедленное обновление в подвале.
- [VMF] `Carson_free_relay` запускает последовательность, конец которой посылает `Carson.Kill` (L23319). [PY] `carsonDeath()` установил бы `Arthur Knox=8` и открыл switch, **если** вызван OnDeath; автоматическую связь `Kill`→OnDeath в доступных исходниках не подтверждаем. Нельзя писать, что спасённый Carson неизбежно «умирает» по квестовой логике.

## Открытая проверка

[HYP] Проверить в установленной UP Plus: от двери `stairdoor` до нижнего пола и клетки, поведение обеих веток `G.Gimble_Vandal`, порядок OnDeath/`Kill`, наличие диалога после переносов, фактическое сохранение `Carson_Rescued`. До этого геометрическая связность лестницы и итоговые runtime-события остаются открытыми.
