# AI SDLC Demos

A collection of small, self-contained demos exploring different ways to bring AI
into the software development lifecycle (SDLC).

## Purpose

Each demo tries out one idea for using AI at a specific stage of the SDLC, so
different approaches can be compared on real (if small) examples. The goal is to
learn what works, what doesn't, and where AI adds the most value.

## Demos

| Demo | Description |
| --- | --- |
| [sdd-eshop](sdd-eshop/) | Spec-driven development with AI |

## Working on a demo

Every demo lives in its own top-level folder and is fully self-contained. It has
its own dependencies, lockfile, virtualenv/`node_modules`, and scripts. There is
no shared tooling at the root.

- **Open only the demo you're working on.** Run `code <demo-folder>` (or
  `cursor ...`). Search, the file tree and language servers then cover only that
  demo, and Source Control still works because the editor finds the parent
  `.git` on its own.
- **Run Claude Code from inside the demo folder** for the same reason.
- **Keep editor settings local to the demo** by putting them in
  `<demo>/.vscode/settings.json`.
- **Prefix commits with the demo name**, for example
  `sdd-eshop: add initial spec`. Run `git log -- <demo>/` to see one demo's
  history.

## Status

Early days. Demos will be added as they're built.
