---
id: SM-28
map: sm_junkyard_1
reference: Unofficial Patch Plus 12.0
status: PARTIAL / VERIFIED_STATIC / RUNTIME_PENDING
---
# SM-28 — Junkyard

Пакет рассматривает установленный BSP и связанный с ним квест Serial. `VERIFIED_STATIC` относится к указанным полям, а не к достижимости, всей геометрии или поведению в игре. Игра не запускалась.

- [[SM-28_Junkyard_01_Spatial|Пространство, объекты и переходы]]
- [[SM-28_Junkyard_02_Systems|I/O, Python, DLG и Serial]]
- [[SM-28_Junkyard_03_Analysis|Расхождения и открытые проверки]]
- [[../../Space/Transitions|Реестр переходов]]; [[../diner1/SM-15_Diner_02_Systems|ранняя встреча Killer в Diner]]

## Источники

Пути от `C:/Users/Slava/Documents/VampireRemake-Starter/Vampire - The Masquerade Bloodlines/`; SHA-256 вычислен для фактических файлов:

| Файл | SHA-256 |
|---|---|
| `Unofficial_Patch/maps/sm_junkyard_1.bsp` | `25c1e71bdab9190dbdf24f2a8ca9801fc4570499492d36fd8c8a06cb34e4bc00` |
| `Vampire/maps/sm_junkyard_1.bsp` | `614c7d8aded63bf96983985e70ce834ff6120df61901dc0e19b8284b98eaaa76` |
| `SDKContent/MapSrc/up sources/sm_junkyard_1_d.vmf` | `35edded23abee191499ec3221d77d8fe8b5d193f73f2a28be0044fafc44ef139` |
| `Unofficial_Patch/python/santamonica/santamonica.py` | `634c5a2e97566d709157f4cd43424509689199302a6433708f3d2ced53f13fff` |
| `Unofficial_Patch/python/vamputil.py` | `a2873d3a2a230c0ac9f38398e093910810f7ab3c51fa06bae71a7b004168e491` |
| `Unofficial_Patch/dlg/santa monica/killer.dlg` | `8ca7c5738d6bcafe59ab650844d559faad3b2c191af44a15aa7594762c947dda` |
| `Unofficial_Patch/vdata/system/quests_santamonica.txt` | `d1f4cc18f44d4f231d0764a1d49da314fe4fb383ca70cddae8ef23db28b02f38` |

UP BSP — `VBSP` v17, 530 entities в entity lump; базовый BSP — v17, 505 entities. VMF строка 20 указывает декомпиляцию BSPSource 1.2.1 из файла с тем же именем, но конкретные байты входной BSP и версия сборки не установлены. Разница количества и SHA сама по себе не объясняет различия карт. Приоритет для полей установленной карты — UP BSP; VMF используется как дополнительный геометрический источник.
