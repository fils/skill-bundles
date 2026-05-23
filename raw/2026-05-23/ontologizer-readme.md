# Ontologizer

Ontologizer is an OpenClaw agent skill for building a clear product ontology: the named concepts in a product, their attributes, their relationships, their states, and the rules that hold them together.

The point is understanding. A good ontology gives the team and its AI agents the same model of the product. That model can then guide product work, documentation, support, automation, and agent behavior without re-teaching the same concepts every time.

## Why this matters

Products get messy because people use the same word for different things, or different words for the same thing. A "project" becomes a folder in one screen, a goal in another, and a billing container in a third. Humans can sometimes muddle through. AI agents usually cannot. They guess.

A product ontology reduces that guessing. It defines the important concepts and relationships directly enough that people can read them and agents can use them.

## What the skill helps you do

- Find the concepts already hiding in your product.
- Define attributes, states, relationships, and rules.
- Separate approved product meaning from guesses and proposals.
- Turn messy terminology into a shared model.
- Review new features against the model before they add confusion.
- Give AI agents a stable product map they can reason from.
- Improve the ontology over time as the product changes.

## Tiny example: fruit

Fruit is boring, which makes it useful.

A fruit can have attributes: color, variety, ripeness, sweetness, weight.

A fruit can have relationships: it grows on a plant, belongs to a category, appears in a recipe, ripens after it is picked.

That is ontology work in miniature. You name the concepts, describe their attributes, and show how they relate. The same move works for a real product.

## Product example: notetaking app

Before ontology work, a notetaking app might have notes, docs, pages, spaces, folders, tags, tasks, reminders, links, backlinks, and projects. The team uses the words loosely. The AI assistant guesses from context.

After ontology work, the model is clearer:

- A note captures an idea.
- A task is a commitment with a status.
- A project groups work toward an outcome.
- A tag describes a note without owning it.
- A backlink connects two notes.
- A reminder belongs to a task or note and has a trigger.

Now the team can improve the model instead of arguing with every interface, help article, and AI response separately.

## Structure

- `SKILL.md` defines the skill behavior.
- `references/` contains deeper guidance.
- `templates/` contains reusable output shapes.
- `examples/` contains sample outputs.
- `scripts/` contains helper tools for term extraction, drift checks, and visualization experiments.
