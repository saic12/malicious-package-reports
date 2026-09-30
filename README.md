# malicious-package-reports

Malicious npm and PyPI packages found by the smiling-hyena analysis pipeline.
Every report here was read and confirmed by a person before it was added;
an automated verdict on its own is never published.

Reports are [OSV](https://ossf.github.io/osv-schema/) JSON, one file per package:

```
pypi/malicious/osv/<package>.json
npm/malicious/osv/<package>.json   (scoped names: npm/malicious/osv/@scope/<name>.json)
withdrawn/                          reports we got wrong, kept with a note
```

Each report says what the package does, where the code is and when it runs,
which versions were checked, and any indicators (domains, URLs, IPs) found in it.

## Wrong report?

Open an issue or email smilinghyena4@gmail.com. We check it again and, if we
were wrong, move the file to `withdrawn/` with a short note on why.

## Contact

smilinghyena4@gmail.com
