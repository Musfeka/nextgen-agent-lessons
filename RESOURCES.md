# Agent Skills Resources

Primary sources only. Everything taught in `./lessons/` should be traceable to something here.

## Knowledge

### The spec (authoritative — treat as source of truth)

- [Agent Skills — Overview (Claude Platform Docs)](https://platform.claude.com/docs/en/agents-and-tools/agent-skills/overview)
  The canonical definition. Progressive disclosure levels, `SKILL.md` structure, `name`/`description`
  field constraints, directory layout, where Skills work (API / Claude Code / claude.ai), sharing
  scope, runtime limits, security guidance.
  **Use for:** Units 5, 6 — anything where exact format or field rules matter.

- [Skill authoring best practices (Claude Platform Docs)](https://platform.claude.com/docs/en/agents-and-tools/agent-skills/best-practices)
  The single densest document in this list. Concision, degrees of freedom, naming (gerund form),
  writing descriptions, progressive-disclosure patterns, workflow/checklist patterns, feedback loops,
  anti-patterns, evaluation-driven development, the final authoring checklist.
  **Use for:** Units 5, 6, 8, 10. This is the backbone of the build-and-evaluate half of the course.

- [Equipping agents for the real world with Agent Skills (Anthropic Engineering)](https://www.anthropic.com/engineering/equipping-agents-for-the-real-world-with-agent-skills)
  The *why* behind the format. Source of the "onboarding guide for a new hire" framing and the
  "effectively unbounded" scope argument.
  **Use for:** Unit 5 — motivating why Skills exist at all.

- [Introducing Agent Skills (Anthropic News)](https://www.anthropic.com/news/skills)
  Announcement-level framing, good for a non-technical audience.
  **Use for:** Unit 1 orientation, and slides for the team session.

- [Use Skills in Claude Code](https://code.claude.com/docs/en/skills)
  Filesystem-based Skills: `~/.claude/skills/` (personal) vs `.claude/skills/` (project).
  **Use for:** Unit 6 and Unit 10 — where learners actually put the file.

- [The Complete Guide to Building Skills for Claude (PDF)](https://resources.anthropic.com/hubfs/The-Complete-Guide-to-Building-Skill-for-Claude.pdf)
  Long-form companion. Good handout for the team.
  **Use for:** Unit 10 capstone reference.

- [Agent Skills Cookbook](https://platform.claude.com/cookbook/skills-notebooks-01-skills-introduction)
  Worked, runnable examples of custom Skills.
  **Use for:** Unit 6 — showing a complete real Skill.

- [anthropics/skills (GitHub)](https://github.com/anthropics/skills)
  Open-source Skills published by Anthropic. Reading real Skills is the fastest way to calibrate.
  **Use for:** Unit 5 and Unit 6 — "read three real Skills before writing your own."

### The mental model (agent fundamentals)

- [Building Effective AI Agents (Anthropic Engineering)](https://www.anthropic.com/engineering/building-effective-agents)
  The workflow-vs-agent distinction, the augmented LLM, and the five workflow patterns (prompt
  chaining, routing, parallelization, orchestrator-workers, evaluator-optimizer). Also the strongest
  available statement that simplicity beats complexity.
  **Use for:** Units 1, 2, 7. This is the single best citation for "what is an agent, really."

- [Effective context engineering for AI agents (Anthropic Engineering)](https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents)
  Context as a finite resource, context rot, the attention budget, the "right altitude" for
  instructions, and long-horizon techniques (compaction, note-taking, sub-agents, just-in-time
  retrieval).
  **Use for:** Unit 3 — the whole unit is built on this.

- [Writing effective tools for AI agents (Anthropic Engineering)](https://www.anthropic.com/engineering/writing-tools-for-agents)
  What makes a tool good, and why bloated tool sets degrade agent behaviour.
  **Use for:** Unit 4.

- [How we built our multi-agent research system (Anthropic Engineering)](https://www.anthropic.com/engineering/multi-agent-research-system)
  Real production account of orchestrator-worker at scale, including what went wrong.
  **Use for:** Unit 7 — grounding SkillGraph ideas in something that actually shipped.

- [Effective harnesses for long-running agents (Anthropic Engineering)](https://www.anthropic.com/engineering/effective-harnesses-for-long-running-agents)
  Consistency across multiple context windows.
  **Use for:** Unit 7 / Unit 8 stretch material.

## Wisdom (Communities)

Not yet discussed with the user — proposed, pending their preference. Ask before leaning on these.

- [r/ClaudeAI](https://reddit.com/r/ClaudeAI) — active, high volume. Use for: seeing how other people
  structure Skills, and what breaks in practice.
- [Anthropic Discord](https://www.anthropic.com/discord) — closest thing to talking to the people who
  build the thing. Use for: spec-level questions the docs don't answer.
- [anthropics/skills GitHub issues + PRs](https://github.com/anthropics/skills) — reading review
  comments on other people's Skills is unusually high-signal. Use for: calibrating quality.

## Gaps

- **No authoritative source on Skill *composition*.** The docs describe single Skills well; the
  "SkillGraph" idea in the user's outline is their own synthesis. Unit 7 must be built by mapping the
  workflow patterns from *Building Effective AI Agents* onto Skills, and labelled clearly as
  synthesis rather than spec.
- **No official evaluation harness.** The best-practices doc explicitly states: *"There is not
  currently a built-in way to run these evaluations."* Unit 8 therefore teaches a manual rubric.
- **Nothing role-specific.** No primary source covers BA/SQA/UX/PM/BD Skill patterns. Unit 9 is
  original work grounded in the general authoring principles.
