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

Packages that share infrastructure or code are grouped in `campaigns/`, and each
member report names its campaign under `database_specific.campaign`.

This repository holds descriptions and indicators only. It does not and will not
contain the code of any reported package.

## Wrong report?

Open an issue or email smilinghyena4@gmail.com with the package, version and
what you think is wrong. We read the code again and, if we were wrong, move the
file to `withdrawn/` with a short note on why. Please do not send a pull request
that edits a report directly: reports are exported from our review records, and
the next export would overwrite the change.

## Disclaimer

Reports are published as they are, without warranty. Each one reflects a manual
review of the code at the version listed; other versions were not checked unless
they are listed too. Mistakes are possible, which is why the process above exists.

## License

The reports and campaign files are licensed under
[CC BY 4.0](https://creativecommons.org/licenses/by/4.0/): you may use them for
any purpose as long as you credit smiling-hyena as the source.

## Contact

smilinghyena4@gmail.com
