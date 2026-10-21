# Home Care Ledger acceptance probe

This probe is a standard-library HTTP client for the target described in the blueprint. It creates records with a unique suffix, never deletes, and is intended for a disposable data directory.

## Prerequisites
- Python 3.11 or newer.
- The target server running locally.
- A fresh disposable data directory. Do not point it at real household data.

## Start the target
```sh
HOMECARE_DATA_DIR=./probe-data python3 app.py --data-dir ./probe-data --host 127.0.0.1 --port 8765
```
The server stores `homecare.sqlite3` in the data directory and binds loopback only. There is no authentication.

## Run one case
```sh
python3 probe.py --base-url http://127.0.0.1:8765 --case A01
```
Cases:
- A01 home and equipment anchor, duplicate and invalid zero-write checks.
- A02 plan bounds, due statuses, and as_of and horizon edges.
- A03 completion, note, leap and month and year date edges, rollback checks.
- A04 home and equipment history ordering and filters.
- A05 accessible HTML shell, unknown route, and method errors.

Run cases one at a time or all five sequentially against the same disposable database. Each case creates unique records.

## Expected result
The script prints `PASS A0N` and exits 0 when every assertion passes. It prints `FAIL A0N: ...` or `ERROR A0N: ...` and exits 1 otherwise. A failure is evidence of a contract mismatch, not a reason to weaken the documented contract.

## Restart
Operator stop and start can be tested manually by stopping the server, starting it again with the same `--data-dir`, and re-reading the records. This is an operator step and was not automated here.

## Runtime status
not_run. The target and probe were authored, not executed. No upstream build or run was performed. No certification is claimed.
