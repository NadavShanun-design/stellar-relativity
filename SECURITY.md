# Security Policy

This is a small, dependency-light scientific library with no network, file-write,
or credential handling in its core code paths. The main class of "security" issue
here is a **correctness** bug — a wrong physical value — which we treat seriously.

## Reporting

If you find an incorrect result, a crash on valid input, or any genuine security
concern, please open a [private security advisory](https://github.com/NadavShanun-design/stellar-relativity/security/advisories/new)
or a regular issue with a reproduction. Include the command/code, the output you
got, and the output you expected (with a source for physics values).

## Supported versions

The latest released version on the default branch is supported.
