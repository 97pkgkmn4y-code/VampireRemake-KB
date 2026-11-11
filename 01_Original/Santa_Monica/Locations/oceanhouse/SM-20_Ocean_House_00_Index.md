---
id: SM-20
maps: [sm_oceanhouse_1, sm_oceanhouse_2]
reference: Unofficial Patch Plus 12.0
status: VERIFIED_STATIC / RUNTIME_PENDING
---
# SM-20 — Ocean House

Исследованы внешний участок `sm_oceanhouse_1` и интерьер `sm_oceanhouse_2` по SDK VMF, entity lump установленных BSP, Python и Therese DLG. Для ключевых связей ниже совпадение VMF/BSP проверено выборочно. Геометрия, коллизия, последовательность посещения комнат и фактическое срабатывание событий в игре **UNVERIFIED**.

- [[SM-20_Ocean_House_01_Spatial|01 — карты, маршруты и переходы]]
- [[SM-20_Ocean_House_02_Systems|02 — предметы, I/O, квесты и постановка]]
- [[SM-20_Ocean_House_03_Analysis|03 — причинная модель и открытые проверки]]
- [[../../Space/Sewers|SM-12 — подход через канализацию]]
- [[../../Characters/SM-13_Asylum_07_Therese_Dialogue|Therese — подробный диалоговый разбор]]

## Паспорт источников

Пути ниже отсчитываются от `C:/Users/Slava/Documents/Bloodlines-GLM/Reference/Vampire - The Masquerade Bloodlines/`.

| Источник | SHA-256 | Роль |
| --- | --- | --- |
| `SDKContent/MapSrc/up sources/sm_oceanhouse_1_d.vmf` | `aafde93abe49b1f3b20e911778992dae8a9aeb0cac615c79ef0afe2b24518d6f` | Декомпилированные entities и геометрические данные наружной карты |
| `SDKContent/MapSrc/up sources/sm_oceanhouse_2_d.vmf` | `ea27603f7a070b397f2be905dcaa9d3f89c78b525b4422bce153c465ac598b5d` | Entities и геометрические данные интерьера |
| `Unofficial_Patch/maps/sm_oceanhouse_1.bsp` | `56ba7367f354ed7497ac08cb4508a22d0f64fa51f8b3bcc169ce5ee7935e4c31` | Установленная наружная карта, VBSP v17 |
| `Unofficial_Patch/maps/sm_oceanhouse_2.bsp` | `ed742545b3bc5508758fb9dd51644aaee4bfc4d93345ea16840d54d60fe4daa3` | Установленный интерьер, VBSP v17 |
| `Unofficial_Patch/python/santamonica/santamonica.py` | `634c5a2e97566d709157f4cd43424509689199302a6433708f3d2ced53f13fff` | Записи журнала и `Therese_Quest` |
| `Unofficial_Patch/dlg/santa monica/therese.dlg` | `5c19156f82bb64eaec03c569ad2b6fe25823f7a9baad9347c55955f06da98cdc` | Выдача задания и варианты сдачи предметов |
| `Unofficial_Patch/vdata/system/quests_santamonica.txt` | `d1f4cc18f44d4f231d0764a1d49da314fe4fb383ca70cddae8ef23db28b02f38` | Тексты журнальных стадий Hotel и Release the Spirit |

Оба VMF маркированы `Decompiled by BSPSource v1.2.1`; исходная BSP этой декомпиляции не установлена. Установленные UP BSP и базовые `Vampire/maps` BSP различаются. Выборочное совпадение entities не доказывает совпадение геометрии/коллизии или всех I/O. `VERIFIED_STATIC` далее относится только к указанным файлам и связям. Запуска игры не было.
