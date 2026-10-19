# Environment probe history

## First, `--internal` network attempt

The original successful bridge-probe `result.json` replaced the first blocked run's JSON at the same path. The raw first-run JSON is no longer available, so this note records only the observed facts and does not reconstruct or claim to preserve that file.

The synthetic server container was running on a user-defined Docker network created with `--internal`. `docker inspect` showed a requested host binding on `127.0.0.1` (first fixed port attempt: host port `63167` to container port `8000`), while `NetworkSettings.Ports` was `{ "8000/tcp": [] }`. `docker port <container> 8000/tcp` reported that no public port was published. Chromium navigation was therefore not attempted in that run. The probe was blocked by Docker port publication behavior, not by product behavior.

## Controlled bridge fallback

A later run succeeded on a dedicated user-defined bridge (`Internal=false`) with app and fixture ports effectively bound only to `127.0.0.1`. Its full machine-readable evidence is in `result.json`. The browser request route allowed the two local origins and aborted the deliberate `https://example.com/` check. Bridge egress was not enforced; this is not `network-none` or egress-blocked evidence.
