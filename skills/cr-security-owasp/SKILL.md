---
name: cr-security-owasp
description: Security review lens — injection, authentication/authorization, secrets, unsafe input handling, dependency risk, memory safety. Load when a change touches untrusted input, security boundaries, or credentials.
---

# Security Review (OWASP lens)

## When to use this skill
A change handles untrusted input, crosses a trust boundary, touches credentials/secrets, or the
review explicitly asks for a security pass.

## Scope
- **Covers:** A language-agnostic security review pass (OWASP-informed), with C/C++/Python notes.
- **Does not cover:** Full threat modeling, penetration testing, compliance audits.

## Core guidance
Follow data from every untrusted source to every sink. A security finding names the attack path:
what the attacker controls → what it reaches → what breaks.

## Steps / patterns
1. **Injection & input handling** — every external input validated/encoded before reaching a sink:
   SQL (parameterized queries only), OS commands (no shell interpolation; in Python no
   `shell=True` with user data), paths (no traversal — resolve and check prefixes), format strings.
2. **AuthN / AuthZ** — every new endpoint/operation checks identity *and* permission; no
   authorization decisions in the client; fail closed.
3. **Secrets** — no credentials, tokens, or keys in code, config defaults, or logs; loaded from
   the environment or a secret store; not echoed in error messages.
4. **Data exposure** — error messages and logs don't leak internals (stack traces, queries,
   PII); debug modes off by default.
5. **Deserialization & parsing** — no `pickle`/`eval`/unsafe YAML load on untrusted data; parsers
   given size limits and timeouts.
6. **Dependencies** — new dependencies pinned and justified; known-CVE check; no abandoned packages.
7. **Memory safety (C/C++)** — bounds, lifetimes, and integer overflow findings from
   `cr-checklist-c`/`cr-checklist-cpp` are security findings here: treat overflows near
   allocation sizes and parsing code as exploitable until shown otherwise.
8. **Concurrency & TOCTOU** — check-then-use on files or shared state inspected for races.

## Pitfalls & anti-patterns
- Blocklist validation where an allowlist is possible.
- "Internal only" as a reason to skip authorization — boundaries move.
- Rolling custom crypto or session management instead of platform primitives.
- Reporting "insecure" without an attack path — findings must be concrete and located.

## References
- [OWASP Top 10](https://owasp.org/www-project-top-ten/) · [CWE Top 25](https://cwe.mitre.org/top25/)
