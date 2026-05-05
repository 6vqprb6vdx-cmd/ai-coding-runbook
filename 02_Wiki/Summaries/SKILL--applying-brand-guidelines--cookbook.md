---
type: summary
source: 01_Raw/github/anthropics/claude-cookbooks/skills/custom_skills/applying-brand-guidelines/SKILL.md
source_url: https://github.com/anthropics/claude-cookbooks/blob/main/skills/custom_skills/applying-brand-guidelines/SKILL.md
title: "Claude Cookbooks — applying-brand-guidelines custom SKILL"
summarized_at: 2026-05-05
entities_referenced: [Skill]
concepts_referenced: []
---

Custom skill demonstrating how to enforce consistent corporate branding and styling across all generated documents.

**Frontmatter.** `name: applying-brand-guidelines`, `description: This skill applies consistent corporate branding and styling to all generated documents including colors, fonts, layouts, and messaging`.

**Brand identity (sample).** Company "Acme Corporation"; tagline "Innovation Through Excellence"; industry Technology Solutions.

**Visual standards.**

- **Color palette.** Primary: Acme Blue `#0066CC`, Acme Navy `#003366`, White `#FFFFFF`. Secondary: Success Green `#28A745` (positive metrics), Warning Amber `#FFC107` (cautions), Error Red `#DC3545` (negative values), Neutral Gray `#6C757D` (secondary text).
- **Typography.** Primary font family: Segoe UI, system-ui, -apple-system, sans-serif. Hierarchy: H1 32pt Bold Acme Blue; H2 24pt Semibold Acme Navy; H3 18pt Semibold Acme Navy; Body 11pt Regular Acme Navy; Caption 9pt Regular Neutral Gray.
- **Logo usage.** Top-left corner on first page/slide; 120px width; minimum 20px clear-space padding on all sides. Never distort, rotate, or apply effects.

**Document standards.**

- **PowerPoint slide templates.** Title Slide (logo + presentation title + date + presenter); Section Divider (section title with blue background); Content Slide (title bar with blue background, white content area); Data Slide (charts/graphs maintaining the palette).
- **Layout rules.** 0.5-inch margins on all sides (file continues with additional layout, table, chart, voice/messaging, and accessibility rules).

The skill exists as a worked example in the Skills cookbook for **Notebook 3: Custom Skills Development**, demonstrating how to encode an organization's brand standards as a reusable skill that downstream document-generation skills (xlsx, pptx, pdf, docx) can compose with.
