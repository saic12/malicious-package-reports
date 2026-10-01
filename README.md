# malicious-package-reports

Malicious npm and PyPI packages found by the smiling-hyena analysis pipeline.
Every report here was read and confirmed by a person before it was added;
an automated verdict on its own is never published.

Reports are [OSV](https://ossf.github.io/osv-schema/) JSON, one file per package:

```
pypi/malicious/osv/<package>.json
pypi/pentest/osv/<package>.json    security tests, proofs of concept, CTF probes
npm/malicious/osv/<package>.json   (scoped names: npm/malicious/osv/@scope/<name>.json)
npm/pentest/osv/<package>.json
withdrawn/                          reports we got wrong, kept with a note
```

`pentest` holds packages that still take data or run code they should not, but read
as testing rather than an attack (named as a test, a PoC exfiltrating CTF flags, a
callback-only probe). They are kept apart so they can be weighed separately.

Each report says what the package does, where the code is and when it runs,
which versions were checked, and any indicators (domains, URLs, IPs) found in it.

## Wrong report?

Open an issue or email smilinghyena4@gmail.com. We check it again and, if we
were wrong, move the file to `withdrawn/` with a short note on why.

## Contact

smilinghyena4@gmail.com
